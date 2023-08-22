from gramar_generated.YALPParserVisitor import YALPParserVisitor
from gramar_generated.YALPParser import YALPParser
from .models.compiler_types import PrimitiveType, CompilerType
from .models.symbol_table import SymbolTable, search_scope, SymbolTableValue, SymbolTableClass, SymbolTableMethod, SymbolTableProgram, PRIMITIVE_TYPES, SymbolTableLet
from .models.sematic_error import SemanticError


class CustomVisitor(YALPParserVisitor):
    def __init__(self):
        self.scope_context: list[SymbolTable] = []

    def add_to_last_scope(self, name: str, type_scope: SymbolTableClass | SymbolTableMethod | SymbolTableValue, is_method_param=False) -> None:
        self.scope_context[-1].add(name, type_scope, is_method_param=is_method_param)

    def add_scope(self, type_scope: SymbolTableClass | SymbolTableMethod | SymbolTableValue | SymbolTableLet) -> None:
        self.scope_context.append(
            SymbolTable(type_scope)
        )

    def remove_scope(self) -> None:
        self.scope_context.pop()

    def get_type(self, type_name) -> CompilerType:
        value: SymbolTableClass | SymbolTableMethod | SymbolTableValue = search_scope(type_name, self.scope_context)
        return value.type

    def get_type_definition(self, type_name, level_search=None) -> SymbolTableClass | SymbolTableMethod | SymbolTableValue:
        return search_scope(type_name, self.scope_context, level_search=level_search)

    def search_recursive_type_parents(self, type_name: str, inherit_classes=[]) -> list[SymbolTableClass]:
        type_definition: SymbolTableClass = self.get_type_definition(type_name)
        program_scope: SymbolTableProgram = self.scope_context[0].scope_context
        
        if type_definition.name not in inherit_classes:
            inherit_classes.append(type_definition.name)
        
        for class_type in program_scope.classes.values():
            if class_type.inherit and class_type.inherit.type.compare(type_definition.type) and class_type.name not in inherit_classes:
                return self.search_recursive_type_parents(class_type.name, inherit_classes)

        return inherit_classes

    def check_type_exists(self, type_name: str) -> bool:
        return search_scope(type_name, self.scope_context) is not None

    def check_type_exists_in_scope(self, type_name: str, search_in_parent=False) -> bool:
        return self.scope_context[-1].consult(type_name, search_in_parent=search_in_parent) is not None

    def check_operators(self, left, right, type_check: PrimitiveType, type_return: PrimitiveType, operator: str):
        left_type: CompilerType = self.visit(left)
        right_type: CompilerType = self.visit(right)

        if not left_type.check_type(type_check) or not right_type.check_type(type_check):
            if not left_type.check_type(type_check):
                line = left.start.line
                column = left.start.column

                self.report_error(SemanticError(
                    f'operator \'{operator}\' only works with Number. Got a {left_type}',
                    line, column,
                    left_type,
                ))

            if not right_type.check_type(type_check):
                line = right.start.line
                column = right.start.column

                self.report_error(SemanticError(
                    f'operator \{operator}\' only works with Number. Got a {right_type}',
                    line, column,
                    right_type,
                ))

        return CompilerType(type_return)

    def report_error(self, SemanticError):
        print(SemanticError)
        exit(1)

    def visitStringExpr(self, ctx: YALPParser.StringExprContext) -> CompilerType:
        return CompilerType(PrimitiveType.STRING)

    def visitEqualExpr(self, ctx: YALPParser.EqualExprContext) -> CompilerType:
        exprs = ctx.expr()
        return CompilerType(PrimitiveType.BOOLEAN)

    def visitTrueExpr(self, ctx: YALPParser.TrueExprContext) -> CompilerType:
        return CompilerType(PrimitiveType.BOOLEAN)

    def visitFalseExpr(self, ctx: YALPParser.FalseExprContext) -> CompilerType:
        return CompilerType(PrimitiveType.BOOLEAN)

    def visitIntExpr(self, ctx: YALPParser.IntExprContext) -> CompilerType:
        return CompilerType(PrimitiveType.INTEGER)

    def visitDivideExpr(self, ctx: YALPParser.DivideExprContext) -> CompilerType:
        left, right = ctx.expr()
        return self.check_operators(left, right, PrimitiveType.INTEGER,  PrimitiveType.INTEGER, '/')

    def visitLessEqualExpr(self, ctx: YALPParser.LessEqualExprContext):
        left, right = ctx.expr()
        return self.check_operators(left, right, PrimitiveType.INTEGER, PrimitiveType.BOOLEAN, '<=')

    def visitPlusExpr(self, ctx: YALPParser.PlusExprContext) -> CompilerType:
        left, right = ctx.expr()
        return self.check_operators(left, right, PrimitiveType.INTEGER, PrimitiveType.INTEGER, '+')

    def visitLessThanExpr(self, ctx: YALPParser.LessThanExprContext) -> CompilerType:
        left, right = ctx.expr()
        return self.check_operators(left, right, PrimitiveType.INTEGER, PrimitiveType.BOOLEAN, '<')

    def visitTimesExpr(self, ctx: YALPParser.TimesExprContext) -> CompilerType:
        left, right = ctx.expr()
        return self.check_operators(left, right, PrimitiveType.INTEGER, PrimitiveType.INTEGER, '*')

    def visitMinusExpr(self, ctx: YALPParser.MinusExprContext) -> CompilerType:
        left, right = ctx.expr()
        return self.check_operators(left, right, PrimitiveType.INTEGER, PrimitiveType.INTEGER, '-')
    
    def visitModExpr(self, ctx: YALPParser.ModExprContext):
        left, right = ctx.expr()
        return self.check_operators(left, right, PrimitiveType.INTEGER, PrimitiveType.INTEGER, '%')

    def visitMethodParam(self, ctx: YALPParser.MethodParamContext) -> CompilerType:
        object_id = str(ctx.OBJECT_ID())
        type_id = str(ctx.TYPE_ID())

        # add variable param to scope
        self.add_to_last_scope(
            object_id,
            SymbolTableValue(CompilerType(
                PrimitiveType.CUSTOM_TYPE, type_id), object_id),
            is_method_param=True,
        )

        # check if type exists
        if not self.check_type_exists(type_id):
            line = ctx.start.line
            column = ctx.start.column
            self.report_error(SemanticError(
                f'type {type_id} does not exist',
                line,
                column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, type_id),
            ))

        return CompilerType(PrimitiveType.CUSTOM_TYPE, type_id)

    def visitNotExpr(self, ctx: YALPParser.NotExprContext) -> CompilerType:
        expr = ctx.expr()
        child_type: CompilerType = self.visit(expr)

        if not child_type.check_type(PrimitiveType.BOOLEAN):
            line = expr.start.line
            column = expr.start.column
            self.report_error(SemanticError(
                'operator \'not\' only works Bool. Got a {}'.format(
                    child_type),
                line,
                column,
                child_type,
            ))

        return CompilerType(PrimitiveType.BOOLEAN)

    # Visit a parse tree produced by YALPParser#AssignExpr.
    def visitAssignExpr(self, ctx: YALPParser.AssignExprContext) -> CompilerType:
        object_id = str(ctx.OBJECT_ID())
        expr = ctx.expr()

        # consultar si variable existe en el contexto actual
        if not self.check_type_exists(object_id):
            line = ctx.start.line
            column = ctx.start.column

            self.report_error(SemanticError(
                f'Variable \'{object_id}\' don\'t exists',
                line,
                column
            ))

        expr_type: CompilerType = self.visit(expr)

        var_type: CompilerType = self.get_type(object_id)
        var_inherit_classes = self.search_recursive_type_parents(var_type.custom_type_name, [])

        if expr_type.custom_type_name not in var_inherit_classes:
            line = expr.start.line
            column = expr.start.column

            self.report_error(SemanticError(
                f'Given assign expression type didn\'t match with variable type or its parents',
                line,
                column,
                var_type,
            ))

        return expr_type

    def visitVariableFeature(self, ctx: YALPParser.VariableFeatureContext) -> CompilerType:
        object_id = str(ctx.OBJECT_ID())
        type_id = str(ctx.TYPE_ID())
        assign = ctx.ASSIGN()

        # Validar que el tipo de dato que se esta asignando si exista
        if not self.check_type_exists(type_id):
            line = ctx.start.line
            column = ctx.start.column
            self.report_error(SemanticError(
                'type {} does not exist'.format(type_id),
                line,
                column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, type_id),
            ))

        # verificar que variable no este especificada en la clase padre o en la clase que hereda
        if self.check_type_exists(object_id):
            line = ctx.start.line
            column = ctx.start.column
            self.report_error(SemanticError(
                f'Variable \'{object_id}\' already exists',
                line,
                column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, object_id),
            ))
            
        variable_definition = SymbolTableValue(CompilerType(PrimitiveType.CUSTOM_TYPE, type_id), object_id)

        # agregar variable en scope
        self.add_to_last_scope(
            object_id,
            variable_definition,
        )

        var_type: CompilerType = self.get_type(object_id)
        var_inherit_classes = self.search_recursive_type_parents(var_type.custom_type_name, [])

        if assign:
            expr = ctx.expr()
            expr_type: CompilerType = self.visit(expr)

            if expr_type.custom_type_name not in var_inherit_classes:
                line = expr.start.line
                column = expr.start.column

                self.report_error(SemanticError(
                    f'Given assign expression type didn\'t match with variable type or its parents',
                    line,
                    column,
                    var_type,
                ))
            
            variable_definition.var_value_type = expr_type

        return variable_definition.var_value_type

    def visitIdExpr(self, ctx: YALPParser.IdExprContext) -> CompilerType:
        object_id = str(ctx.OBJECT_ID())

        if not self.check_type_exists(object_id):
            line = ctx.start.line
            column = ctx.start.column

            self.report_error(SemanticError(
                f'Variable \'{object_id}\' don\'t exists',
                line,
                column
            ))

        variable: SymbolTableValue = self.get_type_definition(object_id)
        return variable.var_value_type
    
    
    def visitTypeExpr(self, ctx: YALPParser.TypeExprContext):
        type_id = str(ctx.TYPE_ID())
        
        if not self.check_type_exists(type_id):
            line = ctx.start.line
            column = ctx.start.column
            self.report_error(SemanticError(
                f'type {type_id} does not exist',
                line,
                column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, type_id),
            ))
            
        class_type: CompilerType = self.get_type(type_id)
        return class_type
    

    def visitClass(self, ctx: YALPParser.ClassContext) -> CompilerType:
        type_ids = list(map(str, ctx.TYPE_ID()))
        inherits = ctx.INHERITS()
        class_type = type_ids[0]

        # Verificar si existe el tipo
        if self.check_type_exists(type_ids[0]):
            self.report_error(
                SemanticError(
                    f'Class \'{type_ids[0]}\' already exists',
                    ctx.start.line,
                    ctx.start.column,
                    CompilerType(PrimitiveType.CUSTOM_TYPE, type_ids[0]),
                )
            )

        # verificar si tiene herencia y verificar si existe en el scope actual
        if inherits and len(type_ids) != 2:
            self.report_error(SemanticError(
                f'Class \'{type_ids[0]}\' must have a parent class',
                ctx.start.line,
                ctx.start.column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, type_ids[0]),
            ))

        # verificar que existe el tipo de la clase padre
        if inherits and not self.check_type_exists(type_ids[1]):
            self.report_error(SemanticError(
                f'Class \'{type_ids[1]}\' does not exists',
                ctx.start.line,
                ctx.start.column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, type_ids[1]),
            ))

        # verificar que no herede de un tipo primitivo
        if inherits and type_ids[1] in PRIMITIVE_TYPES.keys():
            self.report_error(SemanticError(
                f'Class \'{type_ids[0]}\' cannot inherit from primitive type \'{type_ids[1]}\'',
                ctx.start.line,
                ctx.start.column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, type_ids[1]),
            ))

        # verificar que no herede de si mismo
        if inherits and type_ids[0] == type_ids[1]:
            self.report_error(SemanticError(
                f'Class \'{type_ids[0]}\' cannot inherit from itself',
                ctx.start.line,
                ctx.start.column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, type_ids[1]),
            ))

        # crear definicion de la clase para agregar variables y metodos
        class_definition = SymbolTableClass(
            CompilerType(PrimitiveType.CUSTOM_TYPE, type_ids[0]),
            type_ids[0],
            None,
            {
                'self': SymbolTableValue(CompilerType(PrimitiveType.CUSTOM_TYPE, type_ids[0]), 'self'),
            },
            {},
        )

        if inherits:
            parent_class = self.get_type_definition(type_ids[1])
            class_definition.inherit = parent_class
            
        # agregar clase a scope
        self.add_to_last_scope(type_ids[0], class_definition)

        # iniciar nuevo contexto
        self.add_scope(class_definition)

        for feature in ctx.feature():
            self.visit(feature)

        # inish_context
        self.remove_scope()

        return CompilerType(PrimitiveType.CUSTOM_TYPE, class_type)

    def visitProgram(self, ctx: YALPParser.ProgramContext) -> CompilerType:
        classes = ctx.class_()

        self.add_scope(SymbolTableProgram())

        for class_program in classes:
            self.visit(class_program)
            
        main_defition: SymbolTableClass = self.get_type_definition('Main')
        
        if not main_defition:
            self.report_error(SemanticError(
                f'Main class must be defined',
                ctx.start.line,
                ctx.start.column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, 'Main'),
            ))
            
        if main_defition.inherit:
            self.report_error(SemanticError(
                f'Main class cannot inherit from another class',
                ctx.start.line,
                ctx.start.column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, 'Main'),
            ))
            
        if 'main' not in main_defition.methods:
            self.report_error(SemanticError(
                f'Main class must have a \'main\' method',
                ctx.start.line,
                ctx.start.column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, 'Main'),
            ))
            
        main_method: SymbolTableMethod = main_defition.methods['main']
                
        if len(main_method.params) != 0:
            self.report_error(SemanticError(
                f'Main class \'main\' method must have no parameters',
                ctx.start.line,
                ctx.start.column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, 'Main'),
            ))

        self.remove_scope()

    def visitMethodFeature(self, ctx: YALPParser.MethodFeatureContext) -> CompilerType:
        object_id = str(ctx.OBJECT_ID())
        type_id = str(ctx.TYPE_ID())
        expr = ctx.expr()
        params = ctx.formal()

        # verificar que el tipo exista
        if not self.check_type_exists(type_id):
            line = ctx.start.line
            column = ctx.start.column
            self.report_error(SemanticError(
                'type {} does not exist'.format(type_id),
                line,
                column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, type_id),
            ))

        # crear clase de metodo
        method_definition = SymbolTableMethod(
            CompilerType(PrimitiveType.CUSTOM_TYPE, type_id),
            object_id,
            [],
            {},
        )

        # comprobar que no haya una funcion o variables con el mismo nombre en la clase, si si reportar error
        if self.check_type_exists_in_scope(object_id):
            line = ctx.start.line
            column = ctx.start.column
            self.report_error(SemanticError(
                f'Method \'{object_id}\' already exists',
                line,
                column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, object_id),
            ))

        # add method to scope
        self.add_to_last_scope(object_id, method_definition)

        # iniciar un contexto
        self.add_scope(method_definition)

        # agregar parametros al contexto
        for param in params:
            self.visit(param)

        # comprobar que no haya una funcion con mismo nombre pero diferente firma en la clase padre, si si reportar error
        scope_parent_class = self.scope_context[-2].scope_context.inherit

        if scope_parent_class:
            methods = scope_parent_class.methods

            for method in methods.values():
                if method.name == method_definition.name and not method_definition.check_signiture(method):
                    line = ctx.start.line
                    column = ctx.start.column
                    self.report_error(SemanticError(
                        f'Method \'{object_id}\' must have the same signature as the parent class \'{scope_parent_class.name}\' method \'{method.name}\' to override it',
                        line,
                        column,
                        CompilerType(PrimitiveType.CUSTOM_TYPE, object_id),
                    ))

        # correr expresion de adentro y comprobar que el tipo de retorno sea el mismo que el tipo de la funcion
        expr_type = self.visit(expr)
        inherit_method_classes = self.search_recursive_type_parents(type_id, [])
        
        # verificar que el tipo que retorna la funcion sea el mismo que el tipo de la funcion
        if expr_type.custom_type_name not in inherit_method_classes:
            self.report_error(SemanticError(
                f'Function \'{object_id}\' must return a \'{method_definition.type}\' type, got a \'{expr_type}\' type',
                ctx.start.line,
                ctx.start.column,
                method_definition.type,
            ))

        # terminar contexto
        self.remove_scope()

        # returnar tipo de la funcion
        return CompilerType(PrimitiveType.CUSTOM_TYPE, type_id)

    def visitBlockExpr(self, ctx: YALPParser.BlockExprContext):
        exprs = ctx.expr()

        for index, expr in enumerate(exprs):
            return_type = self.visit(expr)

            if index == len(exprs) - 1:
                return return_type

        return None

    def visitIfExpr(self, ctx: YALPParser.IfExprContext):
        exprs = ctx.expr()

        predicate_type: CompilerType = self.visit(exprs[0])
        if_true_type = self.visit(exprs[1])
        if_false_type = self.visit(exprs[2])

        if not predicate_type.check_type(PrimitiveType.BOOLEAN):
            self.report_error(SemanticError(
                f'If predicate is not Boolean, found {predicate_type}',
                ctx.start.line,
                ctx.start.column,
                predicate_type,
            ))
            
        if not if_true_type.compare(if_false_type):
            
            # Buscar un super tipo en comun
            inherit_if_true = self.search_recursive_type_parents(if_true_type.custom_type_name, [])
            inherit_if_false = self.search_recursive_type_parents(if_false_type.custom_type_name, [])
            
            if if_false_type.custom_type_name in inherit_if_true:
                return if_true_type
            elif if_true_type.custom_type_name in inherit_if_false:
                return if_false_type
            else:
                self.report_error(SemanticError(
                    f'If true and false types must be the same, found \'{if_true_type}\' and \'{if_false_type}\'',
                    ctx.start.line,
                    ctx.start.column,
                    if_true_type,
                ))
            
        return if_true_type
    

    def visitWhileExpr(self, ctx: YALPParser.WhileExprContext):
        exprs = ctx.expr()
        
        predicate_type: CompilerType = self.visit(exprs[0])
        
        if not predicate_type.check_type(PrimitiveType.BOOLEAN):
            self.report_error(SemanticError(
                f'While predicate is not \'Boolean\', found \'{predicate_type}\'',
                ctx.start.line,
                ctx.start.column,
                predicate_type,
            ))
        
        return CompilerType(PrimitiveType.VOID)
    
    def visitParenExpr(self, ctx: YALPParser.ParenExprContext):
        expr_type = self.visit(ctx.expr())
        return expr_type
    
    def visitNegateExpr(self, ctx: YALPParser.NegateExprContext):
        expr_type = self.visit(ctx.expr())
        
        if not expr_type.check_type(PrimitiveType.INTEGER):
            self.report_error(SemanticError(
                f'Negate operator only works with \'Integer\', found \'{expr_type}\'',
                ctx.start.line,
                ctx.start.column,
                expr_type,
            ))
            
        return expr_type
        
    def visitIsvoidExpr(self, ctx: YALPParser.IsvoidExprContext):
        expr_type = self.visit(ctx.expr()) # TODO: PARA LUEGO AQUI SE PODRA VERIFICAR QUE SI SEA VOID        
        return CompilerType(PrimitiveType.BOOLEAN)
    
    # Visit a parse tree produced by YALPParser#LetExpr.
    def visitLetExpr(self, ctx: YALPParser.LetExprContext):
        features = ctx.feature()
        expr_let = ctx.expr()
                
        let_scope = SymbolTableLet(
            None,
            None,
            {},
        )
        
        self.add_scope(let_scope)
        
        for feature in features:
            object_id = str(feature.OBJECT_ID())
            type_id = str(feature.TYPE_ID())
            assign = feature.ASSIGN()
            
            # validar que el tipo de dato exista
            if not self.check_type_exists(type_id):
                line = feature.start.line
                column = feature.start.column
                self.report_error(SemanticError(
                    f'type {type_id} does not exist',
                    line,
                    column,
                    CompilerType(PrimitiveType.CUSTOM_TYPE, type_id),
                ))
            
            # verificar que variable no este especificada en el contexto actual de let o en scopes arriba
            if self.check_type_exists(object_id):
                line = feature.start.line
                column = feature.start.column
                self.report_error(SemanticError(
                    f'Variable \'{object_id}\' already exists',
                    line,
                    column,
                    CompilerType(PrimitiveType.CUSTOM_TYPE, object_id),
                ))
            
            # crear definicion de variable
            variable_definition = SymbolTableValue(CompilerType(PrimitiveType.CUSTOM_TYPE, type_id), object_id)
            
            # agregar variable en scope
            self.add_to_last_scope(
                object_id,
                variable_definition,
            )
            
            var_type: CompilerType = self.get_type(object_id)
            var_inherit_classes = self.search_recursive_type_parents(var_type.custom_type_name, [])
            
            if assign:
                expr = feature.expr()
                expr_type: CompilerType = self.visit(expr)
                
                if expr_type.custom_type_name not in var_inherit_classes:
                    line = expr.start.line
                    column = expr.start.column
                    
                    self.report_error(SemanticError(
                        f'Given assign expression type didn\'t match with variable type or its parents',
                        line,
                        column,
                        var_type,
                    ))
            
        expr_type = self.visit(expr_let)
        
        self.remove_scope()
            
        return expr_type
    
    def visitNewExpr(self, ctx: YALPParser.NewExprContext):
        type_id = str(ctx.TYPE_ID())
        
        # validar que el tipo de dato exista
        if not self.check_type_exists(type_id):
            line = ctx.start.line
            column = ctx.start.column
            self.report_error(SemanticError(
                f'type {type_id} does not exist',
                line,
                column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, type_id),
            ))
        
        return CompilerType(PrimitiveType.CUSTOM_TYPE, type_id)

    def visitCallExpr(self, ctx: YALPParser.CallExprContext):
        object_id = str(ctx.OBJECT_ID())
        exprs = ctx.expr()
                
        if not self.check_type_exists(object_id):
            line = ctx.start.line
            column = ctx.start.column
            self.report_error(SemanticError(
                f'Method \'{object_id}\' don\'t exists',
                line,
                column
            ))
            
        method_definition: SymbolTableMethod = self.get_type_definition(object_id)
        
        # Comprobar que las expresiones tengan el mismo tipo que los parametros o bien que sea tipos derivados implicitamente
        if len(exprs) != len(method_definition.params):
            self.report_error(SemanticError(
                f'Method \'{object_id}\' must have the same number of parameters, expected {len(method_definition.params)}, got {len(exprs)}',
                ctx.start.line,
                ctx.start.column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, object_id),
            ))
            
        for index, param in enumerate(method_definition.params):
            expr_type: CompilerType = self.visit(exprs[index])
            param_inherit_classes = self.search_recursive_type_parents(param.type.custom_type_name, [])
            
            is_implicit_cast = expr_type.compare(CompilerType(PrimitiveType.BOOLEAN)) and param.type.compare(CompilerType(PrimitiveType.INTEGER)) \
                or expr_type.compare(CompilerType(PrimitiveType.INTEGER)) and param.type.compare(CompilerType(PrimitiveType.BOOLEAN))
            
            if expr_type.custom_type_name not in param_inherit_classes and not is_implicit_cast:
                self.report_error(SemanticError(
                    f'Method \'{object_id}\' parameter \'{param.name}\' must be \'{param.type}\' type, got \'{expr_type}\' type',
                    ctx.start.line,
                    ctx.start.column,
                    CompilerType(PrimitiveType.CUSTOM_TYPE, object_id),
                ))
            
        return method_definition.type

    def visitDotExpr(self, ctx: YALPParser.DotExprContext):
        object_id = str(ctx.OBJECT_ID())
        exprs = ctx.expr()
        
        cast = ctx.SIGN()
        cast_type = str(ctx.TYPE_ID())
        
        begin_object_type: CompilerType = self.visit(exprs[0])
        class_definition: SymbolTableClass = self.get_type_definition(begin_object_type.custom_type_name)
        
        # si hay cast, intentar castear
        if cast:
            inherit_classes = self.search_recursive_type_parents(cast_type, [])
            
            if begin_object_type.custom_type_name not in inherit_classes:
                self.report_error(SemanticError(
                    f'Cannot cast \'{begin_object_type}\' to \'{cast_type}\'',
                    ctx.start.line,
                    ctx.start.column,
                    begin_object_type,
                ))
            
            begin_object_type = CompilerType(PrimitiveType.CUSTOM_TYPE, cast_type)
            class_definition: SymbolTableClass = self.get_type_definition(cast_type)
        
        return_type = None    
        
        # inicial scope de la clase
        self.add_scope(class_definition)
        
        method_definition: SymbolTableMethod = self.get_type_definition(object_id, level_search=1)
        
        if not method_definition:
            self.report_error(SemanticError(
                f'Method \'{object_id}\' don\'t exists in class \'{class_definition.name}\'',
                ctx.start.line,
                ctx.start.column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, object_id),
            ))
        
        current_method_params = exprs[1:]
        
        # Comprobar que las expresiones tengan el mismo tipo que los parametros o bien que sea tipos derivados implicitamente
        if len(current_method_params) != len(method_definition.params):
            self.report_error(SemanticError(
                f'Method \'{object_id}\' must have the same number of parameters, expected {len(method_definition.params)}, got {len(current_method_params)}',
                ctx.start.line,
                ctx.start.column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, object_id),
            ))
            
        for index, param in enumerate(method_definition.params):
            expr_type: CompilerType = self.visit(current_method_params[index])
            param_inherit_classes = self.search_recursive_type_parents(param.type.custom_type_name, [])
            
            is_implicit_cast = expr_type.compare(CompilerType(PrimitiveType.BOOLEAN)) and param.type.compare(CompilerType(PrimitiveType.INTEGER)) \
                or expr_type.compare(CompilerType(PrimitiveType.INTEGER)) and param.type.compare(CompilerType(PrimitiveType.BOOLEAN))
            
            if expr_type.custom_type_name not in param_inherit_classes and not is_implicit_cast:
                self.report_error(SemanticError(
                    f'Method \'{object_id}\' parameter \'{param.name}\' must be \'{param.type}\' type, got \'{expr_type}\' type',
                    ctx.start.line,
                    ctx.start.column,
                    CompilerType(PrimitiveType.CUSTOM_TYPE, object_id),
                ))
        
        return_type = method_definition.type
        
        self.remove_scope()
        
        return return_type
        
