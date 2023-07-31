from gramar_generated.YALPParserVisitor import YALPParserVisitor
from gramar_generated.YALPParser import YALPParser
from .models.compiler_types import PrimitiveType, CompilerType
from .models.symbol_table import SymbolTable, search_scope
from .models.sematic_error import SemanticError


class CustomVisitor(YALPParserVisitor):
    def __init__(self):
        self.scope_context: list[SymbolTable] = []
        self.errors = []

    def add_to_last_scope(self, name: str, type_scope: CompilerType) -> None:
        self.scope_context[-1].add(name, type_scope)

    def add_scope(self) -> None:
        self.scope_context.append(SymbolTable())

    def remove_scope(self) -> None:
        self.scope_context.pop()

    def get_type(self, type_name) -> CompilerType:
        return search_scope(type_name, self.scope_context)

    def check_type_exists(self, type_name) -> bool:
        return search_scope(type_name, self.scope_context) is not None

    # Visit a parse tree produced by YALPParser#class.
    def visitClass(self, ctx: YALPParser.ClassContext) -> CompilerType:
        type_ids = ctx.TYPE_ID()
        inherits = ctx.INHERITS()

        # verificar si tiene herencia y verificar si existe en el scope actual
        if inherits:
            if len(type_ids) != 2:
                pass  # error
            else:
                # search_scope
                pass

        # TODO: iniciar nuevo contexto
        self.add_scope()

        # add class to context
        class_type = type_ids[0]

        self.add_to_last_scope(
            class_type,
            CompilerType(PrimitiveType.CUSTOM_TYPE, class_type)
        )

        for feature in ctx.feature():
            self.visit(feature)

        # TODO: finish_context
        self.remove_scope()

        return CompilerType(PrimitiveType.CUSTOM_TYPE, class_type)

    def visitMethodFeature(self, ctx: YALPParser.MethodFeatureContext):
        type_id = str(ctx.TYPE_ID())
        expr = ctx.expr()

        # TODO: init_context
        self.add_scope()

        # TODO: visit
        self.visit(expr)

        # TODO: finish_context
        self.remove_scope()
        return CompilerType(PrimitiveType.CUSTOM_TYPE, type_id)

    def visitVariableFeature(self, ctx: YALPParser.VariableFeatureContext) -> CompilerType:
        object_id = str(ctx.OBJECT_ID())
        type_id = str(ctx.TYPE_ID())
        assign = ctx.ASSIGN()
        expr = ctx.expr()

        if not self.check_type_exists(type_id):
            line = ctx.start.line
            column = ctx.start.column
            self.errors.append(SemanticError(
                'type {} does not exist'.format(type_id),
                line,
                column,
                CompilerType(PrimitiveType.CUSTOM_TYPE, type_id),
            ))

        # agregar variable en scope
        self.add_to_last_scope(
            object_id,
            CompilerType(PrimitiveType.CUSTOM_TYPE, type_id)
        )

        # verificar que se le este asignando un valor que corresponda al tipo
        if assign:
            child_type: CompilerType = self.visit(expr)

            if not child_type.check_type(PrimitiveType.CUSTOM_TYPE, type_id):
                line = expr.start.line
                column = expr.start.column
                self.errors.append(SemanticError(
                    'type {} does not match with {}'.format(
                        child_type,
                        type_id
                    ),
                    line,
                    column,
                    child_type,
                ))

        return CompilerType(PrimitiveType.CUSTOM_TYPE, type_id)

    def visitFormal(self, ctx: YALPParser.FormalContext):
        # TODO: init_context

        # TODO: finish_context
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#WhileExpr.
    def visitWhileExpr(self, ctx: YALPParser.WhileExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#StringExpr.
    def visitStringExpr(self, ctx: YALPParser.StringExprContext) -> CompilerType:
        return CompilerType(PrimitiveType.STRING)

    # Visit a parse tree produced by YALPParser#EqualExpr.
    def visitEqualExpr(self, ctx: YALPParser.EqualExprContext) -> CompilerType:
        return CompilerType(PrimitiveType.BOOLEAN)

    # Visit a parse tree produced by YALPParser#IfExpr.
    def visitIfExpr(self, ctx: YALPParser.IfExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#TrueExpr.
    def visitTrueExpr(self, ctx: YALPParser.TrueExprContext) -> CompilerType:
        return CompilerType(PrimitiveType.BOOLEAN)

    # Visit a parse tree produced by YALPParser#AssignExpr.
    def visitAssignExpr(self, ctx: YALPParser.AssignExprContext):
        object_id = str(ctx.OBJECT_ID())
        expr = ctx.expr()

        # consultar si variable existe en el contexto actual
        if not self.check_type_exists(object_id):
            line = ctx.start.line
            column = ctx.start.column

            self.errors.append(SemanticError(
                f'Variable \'{object_id}\' don\'t exists',
                line,
                column
            ))

        # verificar que el tipo de la expresion sea igual al tipo de la variable
        child_type: CompilerType = self.visit(expr)
        var_type = self.get_type(object_id)

        if var_type is not None and not child_type.compare(var_type):
            line = expr.start.line
            column = expr.start.column

            self.errors.append(SemanticError(
                f'Given assign expression type didn\'t match with variable type',
                line,
                column,
                var_type,
            ))

        return var_type

    # Visit a parse tree produced by YALPParser#FalseExpr.
    def visitFalseExpr(self, ctx: YALPParser.FalseExprContext) -> CompilerType:
        return CompilerType(PrimitiveType.BOOLEAN)

    # Visit a parse tree produced by YALPParser#DivideExpr.
    def visitDivideExpr(self, ctx: YALPParser.DivideExprContext) -> CompilerType:
        left, right = ctx.expr()

        left_type: CompilerType = self.visit(left)
        right_type: CompilerType = self.visit(right)

        if not left_type.check_type(PrimitiveType.INTEGER) or not right_type.check_type(PrimitiveType.INTEGER):
            if not left_type.check_type(PrimitiveType.INTEGER):
                line = left.start.line
                column = left.start.column

                self.errors.append(SemanticError(
                    'operator \'/\' only works with Number. Got a {}'.format(
                        left_type),
                    line, column,
                    left_type,
                ))

            if not right_type.check_type(PrimitiveType.INTEGER):
                line = right.start.line
                column = right.start.column

                self.errors.append(SemanticError(
                    'operator \'/\' only works with Number. Got a {}'.format(
                        right_type),
                    line, column,
                    right_type,
                ))

        return CompilerType(PrimitiveType.INTEGER)

    # Visit a parse tree produced by YALPParser#LessEqualExpr.
    def visitLessEqualExpr(self, ctx: YALPParser.LessEqualExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#PlusExpr.
    def visitPlusExpr(self, ctx: YALPParser.PlusExprContext) -> CompilerType:
        left, right = ctx.expr()

        left_type: CompilerType = self.visit(left)
        right_type: CompilerType = self.visit(right)

        if not left_type.check_type(PrimitiveType.INTEGER) or not right_type.check_type(PrimitiveType.INTEGER):
            if not left_type.check_type(PrimitiveType.INTEGER):
                line = left.start.line
                column = left.start.column

                self.errors.append(SemanticError(
                    'operator \'*\' only works with Number. Got a {}'.format(
                        left_type),
                    line, column,
                    left_type,
                ))

            if not right_type.check_type(PrimitiveType.INTEGER):
                line = right.start.line
                column = right.start.column

                self.errors.append(SemanticError(
                    f'operator \'*\' only works with Number. Got a {right_type}',
                    line, column,
                    right_type,
                ))

        return CompilerType(PrimitiveType.INTEGER)

    # Visit a parse tree produced by YALPParser#CallExpr.
    def visitCallExpr(self, ctx: YALPParser.CallExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#NotExpr.
    def visitNotExpr(self, ctx: YALPParser.NotExprContext) -> CompilerType:
        expr = ctx.expr()
        child_type: CompilerType = self.visit(expr)

        if not child_type.check_type(PrimitiveType.BOOLEAN):
            line = expr.start.line
            column = expr.start.column
            self.errors.append(SemanticError(
                'operator \'not\' only works Bool. Got a {}'.format(
                    child_type),
                line,
                column,
                child_type,
            ))

        return CompilerType(PrimitiveType.BOOLEAN)

    # Visit a parse tree produced by YALPParser#LessThanExpr.
    def visitLessThanExpr(self, ctx: YALPParser.LessThanExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#TimesExpr.
    def visitTimesExpr(self, ctx: YALPParser.TimesExprContext) -> CompilerType:
        left, right = ctx.expr()

        left_type: CompilerType = self.visit(left)
        right_type: CompilerType = self.visit(right)

        if not left_type.check_type(PrimitiveType.INTEGER) or not right_type.check_type(PrimitiveType.INTEGER):
            if not left_type.check_type(PrimitiveType.INTEGER):
                line = left.start.line
                column = left.start.column

                self.errors.append(SemanticError(
                    'operator \'*\' only works with Number. Got a {}'.format(
                        left_type),
                    line, column,
                    left_type,
                ))

            if not right_type.check_type(PrimitiveType.INTEGER):
                line = right.start.line
                column = right.start.column

                self.errors.append(SemanticError(
                    'operator \'*\' only works with Number. Got a {}'.format(
                        right_type),
                    line, column,
                    right_type,
                ))

        return CompilerType(PrimitiveType.INTEGER)

    # Visit a parse tree produced by YALPParser#MinusExpr.
    def visitMinusExpr(self, ctx: YALPParser.MinusExprContext) -> CompilerType:
        left, right = ctx.expr()

        left_type: CompilerType = self.visit(left)
        right_type: CompilerType = self.visit(right)

        if not left_type.check_type(PrimitiveType.INTEGER) or not right_type.check_type(PrimitiveType.INTEGER):
            if not left_type.check_type(PrimitiveType.INTEGER):
                line = left.start.line
                column = left.start.column

                self.errors.append(SemanticError(
                    'operator \'-\' only works with Number. Got a {}'.format(
                        left_type),
                    line, column,
                    left_type,
                ))

            if not right_type.check_type(PrimitiveType.INTEGER):
                line = right.start.line
                column = right.start.column

                self.errors.append(SemanticError(
                    'operator \'-\' only works with Number. Got a {}'.format(
                        right_type),
                    line, column,
                    right_type,
                ))

        return CompilerType(PrimitiveType.INTEGER)

    # Visit a parse tree produced by YALPParser#IdExpr.
    def visitIdExpr(self, ctx: YALPParser.IdExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#LetExpr.
    def visitLetExpr(self, ctx: YALPParser.LetExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#DotExpr.
    def visitDotExpr(self, ctx: YALPParser.DotExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#TypeExpr.
    def visitTypeExpr(self, ctx: YALPParser.TypeExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#BlockExpr.
    def visitBlockExpr(self, ctx: YALPParser.BlockExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#IsvoidExpr.
    def visitIsvoidExpr(self, ctx: YALPParser.IsvoidExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#NegateExpr.
    def visitNegateExpr(self, ctx: YALPParser.NegateExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#NewExpr.
    def visitNewExpr(self, ctx: YALPParser.NewExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#IntExpr.
    def visitIntExpr(self, ctx: YALPParser.IntExprContext) -> CompilerType:
        return CompilerType(PrimitiveType.INTEGER)

    # Visit a parse tree produced by YALPParser#ModExpr.
    def visitModExpr(self, ctx: YALPParser.ModExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YALPParser#ParenExpr.
    def visitParenExpr(self, ctx: YALPParser.ParenExprContext):
        return self.visit(ctx.expr())


# ----- Este lab debe tener -----

# - Reglas de Inferencia para Asignación de Expresiones.
# - Reglas de Inferencia para Operaciones Aritméticas.

# Tabla de Símbolos.
# a. Las operaciones mínimas sobre la tabla de símbolos deben ser las de agregar y consulta un símbolo dentro del ámbito actual.


# Implementación de las reglas de Inferencia para Operaciones Aritméticas de expresiones sintácticas simples [i.e. clases base: Integer, Boolean, String]
