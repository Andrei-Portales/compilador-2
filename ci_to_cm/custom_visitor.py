from ThreeAdress_parser.ThreeAddressCodeVisitor import ThreeAddressCodeVisitor
from ThreeAdress_parser.ThreeAddressCodeParser import ThreeAddressCodeParser
from .models.intermediate_code_type import IntermediateCodeType, IntermediateCodeTypeEnum
import jinja2
from util.functions import generateRandomVariable


class CI2MPIPSVisitor(ThreeAddressCodeVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}
        # {'class_name': {'var1': 'asdgdfg'}}
        # Record[str, Record[str, str]]Record[str, Record[str, str]]
        self.classes_vars_map = {}
        self.registers = {'$t0', '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7'}
        self.actual_class = None
        self.actual_function = None
        self.insertIOFunctions()

    def insertIOFunctions(self):
        class_name = 'IO'
        self.classes_vars_map[class_name] = {}
        self.actual_class = class_name
        # print(self.rename_vars('out_int'))
        self.functions['out_int'] = {
            'name': self.rename_vars('out_int'),
            'instructions': [
                {
                    'instruction': 'li $v0, 1',
                    'has_semicolon': False,
                },
                {
                    'instruction': 'syscall',
                    'has_semicolon': False,
                },
                {
                    'instruction': 'jr $ra',
                    'has_semicolon': False,
                },
            ],
        }
        self.functions['out_string'] = {
            'name': 'out_string',
            'instructions': [
                {
                    'instruction': 'li $v0, 4',
                    'has_semicolon': False,
                },
                {
                    'instruction': 'syscall',
                    'has_semicolon': False,
                },
                {
                    'instruction': 'jr $ra',
                    'has_semicolon': False,
                },
            ],
        }
        self.functions['in_int'] = {
            'name': 'in_int',
            'instructions': [
                {
                    'instruction': 'li $v0, 5',
                    'has_semicolon': False,
                },
                {
                    'instruction': 'syscall',
                    'has_semicolon': False,
                },
                {
                    'instruction': 'jr $ra',
                    'has_semicolon': False,
                },
            ],
        }
        # self.functions['in_string'] = {
        #     'name': 'in_string',
        #     'instructions': [
        #         {
        #             'instruction': 'li $v0, 8',
        #             'has_semicolon': False,
        #         },
        #         {
        #             'instruction': 'li $a1, 1024',
        #             'has_semicolon': False,
        #         },
        #         {
        #             'instruction': 'la $a0, buffer',
        #             'has_semicolon': False,
        #         },
        #         {
        #             'instruction': 'syscall',
        #             'has_semicolon': False,
        #         },
        #         {
        #             'instruction': 'jr $ra',
        #             'has_semicolon': False,
        #         },
        #     ],
        # }

    def fillTemplate(self):
        TEMPLATE_PATH = 'ci_to_cm/templates/mips_code_template.j2'
        template = jinja2.Template(open(TEMPLATE_PATH).read())

        data = {
            'data': self.variables.values(),
            'text': {
                'functions': self.functions.values(),
            },
        }

        output = template.render(data)

        with open('ci_to_cm/outputs/mips_code.asm', 'w', encoding='utf-8') as f:
            f.write(output)

    def rename_vars(self, var_name: str):
        if not self.classes_vars_map[self.actual_class].get('out_int'):
            self.classes_vars_map[self.actual_class]['out_int'] = 'out_int'

        var_name = str(var_name)
        if not self.classes_vars_map[self.actual_class].get(var_name):
            self.classes_vars_map[self.actual_class][var_name] = generateRandomVariable(
            )

        return self.classes_vars_map[self.actual_class][var_name]

    def add_instruction(self, instruction: str, has_semicolon: bool = False):
        self.functions[self.actual_function]['instructions'].append({
            'instruction': instruction,
            'has_semicolon': has_semicolon,
        })

    # ----------------------------------------------------------------------------------------

    def visitProgram(self, ctx: ThreeAddressCodeParser.ProgramContext):  # ✅
        for class_d in ctx.classDeclaration():
            self.visit(class_d)

        self.fillTemplate()
        return self.visitChildren(ctx)

    def visitClassDeclaration(self, ctx: ThreeAddressCodeParser.ClassDeclarationContext):  # ✅
        class_name = ctx.IDENTIFIER()

        self.classes_vars_map[class_name] = {}

        self.actual_class = class_name

        for var in ctx.globalVarDeclaration():
            self.visit(var)

        for method in ctx.methodDeclaration():
            self.visit(method)

        self.actual_class = None

    def visitGlobalVarDeclaration(self, ctx: ThreeAddressCodeParser.GlobalVarDeclarationContext):  # ✅  # ✅
        id_name = self.rename_vars(ctx.IDENTIFIER())
        exp = self.visit(ctx.expression())

        type_var = None

        if isinstance(exp, IntermediateCodeType):
            if exp.type == IntermediateCodeTypeEnum.INTEGER:
                type_var = '.word'
            elif exp.type == IntermediateCodeTypeEnum.STRING:
                type_var = '.asciiz'
            elif exp.type == IntermediateCodeTypeEnum.BOOLEAN:
                type_var = '.word'
            else:
                raise Exception('Type not supported')
        else:
            type_var = exp

        # registrar variable
        self.variables[id_name] = {
            'name': id_name,
            'type': type_var,
            'value': exp.value,
        }

    def visitMethodDeclaration(self, ctx: ThreeAddressCodeParser.MethodDeclarationContext):  # ✅
        # id_method = self.rename_vars(ctx.IDENTIFIER())
        id_method = ctx.IDENTIFIER()

        self.actual_function = id_method

        # if id_method == 'main' save it on the first position of the functions list
        if id_method.getText() == 'main':
            self.functions = {
                id_method: {
                    'name': id_method,
                    'instructions': [],
                },
                **self.functions,
            }
        else:

            self.functions[id_method] = {
                'name': id_method,
                'instructions': [],
            }

        for instruct in ctx.instruction():
            self.visit(instruct)

        self.actual_function = None

    def visitReturnInstr(self, ctx: ThreeAddressCodeParser.ReturnInstrContext):
        expr = self.visit(ctx.expression())
        # print(expr)
        
        # if expr value = Main, finish program with li $v0, 10 and syscall
        if expr == 'self':
            # get actual function name
            # function_name = self.actual_function
            # get actual class name
            class_name = self.actual_class.getText()
            if class_name == 'Main':
                self.add_instruction('li $v0, 10')
                self.add_instruction('syscall')
            else:
                self.add_instruction(f'jr $ra')
        if expr == 'Main':
            self.add_instruction('li $v0, 10')
            self.add_instruction('syscall')


        # if ctx.expression():
        #     expr = self.visit(ctx.expression())

        #     if type(expr) == str:
        #         self.add_instruction(f'la $v0, {expr}')
        #     elif isinstance(expr, IntermediateCodeType):
        #         if expr.type == IntermediateCodeTypeEnum.INTEGER:
        #             self.add_instruction(f'li $vo, {expr.value}')
        #         elif expr.type == IntermediateCodeTypeEnum.STRING:
        #             # No se como manejar en este caso cadenas
        #             pass

        # elif ctx.SELF():
        #     self.add_instruction('move $v0, $s0')

        # self.add_instruction('jr $ra')
        pass

    def visitEqualInstr(self, ctx: ThreeAddressCodeParser.EqualInstrContext):        
        expr = ctx.expression()

        left = self.visit(expr[0])
        right = self.visit(expr[1])

        id_name = self.rename_vars(left)

        print('left', left)
        print('right', right)

        type_var = None
        variable = False

        if right == 'OperatorExpr':
            self.add_instruction(f'sw $t0, {id_name}')
            return

        if isinstance(right, IntermediateCodeType):
            if right.type == IntermediateCodeTypeEnum.INTEGER:
                type_var = '.word'
            elif right.type == IntermediateCodeTypeEnum.STRING:
                type_var = '.asciiz'
            elif right.type == IntermediateCodeTypeEnum.BOOLEAN:
                type_var = '.word'
            else:
                raise Exception('Type not supported')
        else: # if right is a variable
            # buscar la variable en variables y obtener su tipo y valor
            # if self.variables.get(right):
            #     type_var = self.variables[right]['type']
            #     right = self.variables[right]['value']
            variable = True
            type_var = self.variables[self.rename_vars(right)]['type']

        # check if left exist in variables. If not, save it in variables, else, change the value of the variable
        if not self.variables.get(id_name):
            if variable:
                self.variables[id_name] = {
                    'name': id_name,
                    'type': type_var,
                    'value': '',
                }
            else:
                self.variables[id_name] = {
                    'name': id_name,
                    'type': type_var,
                    'value': right,
                }
        else:
            # print('id_name', id_name)
            # print('right', right)
            self.variables[id_name]['value'] = right
            # self.add_instruction(f'la $t0, {id_name}')
            # self.add_instruction(f'li $t1, {right}')
            # self.add_instruction(f'sw $t1, 0($t0)')


        # self.add_instruction(f'la $t0, {left}')
        # self.add_instruction(f'li $t1, {right}')
        # self.add_instruction(f'sw $t1, 0($t0)')

    def visitNegateInstr(self, ctx: ThreeAddressCodeParser.NegateInstrContext):
        return self.visitChildren(ctx)

    def visitLtInstr(self, ctx: ThreeAddressCodeParser.LtInstrContext):
        exprs = ctx.expression()
        print(exprs)
        return self.visitChildren(ctx)

    def visitIfInstr(self, ctx: ThreeAddressCodeParser.IfInstrContext):  # ✅
        predicate = self.rename_vars(ctx.expression())
        label = str(ctx.LABEL())
        
        self.add_instruction(f'lw $t0, {predicate}')
        self.add_instruction(f'beq $t0, $zero, {label}')
        
    def visitGotoInstr(self, ctx: ThreeAddressCodeParser.GotoInstrContext):  # ✅
        lable = str(ctx.LABEL())
        
        self.add_instruction(f'j {lable}')

    def visitPushParamInstr(self, ctx: ThreeAddressCodeParser.PushParamInstrContext):
        expr = self.visit(ctx.expression())
        id_name = self.rename_vars(expr)

        self.add_instruction(f'la $a0, {id_name}')

        # return self.visitChildren(ctx)

    def visitPopParamInstr(self, ctx: ThreeAddressCodeParser.PopParamInstrContext):
        return self.visitChildren(ctx)

    def visitFCallInstr(self, ctx: ThreeAddressCodeParser.FCallInstrContext):
        # expr = ctx.IDENTIFIER()

        # if expr has only one element, call that function, else, first identifier is the class name and the second is the function name
        # if len(expr) == 1:
        #     function_name = self.rename_vars(expr[0])
        #     self.add_instruction(f'jal {function_name}')
        # else:
        #     class_name = self.rename_vars(expr[0])
        #     function_name = self.rename_vars(expr[1])
        #     self.add_instruction(f'jal {class_name}_{function_name}')

        return self.visitChildren(ctx)

    def visitLabelInstr(self, ctx: ThreeAddressCodeParser.LabelInstrContext):  # ✅
        self.add_instruction(f'{ctx.LABEL()}:', has_semicolon=False)

    def visitFCallStatement(self, ctx: ThreeAddressCodeParser.FCallStatementContext):
        expr = ctx.IDENTIFIER()
        if len(expr) == 1:
            name = expr[0].getText()
            # print(name)
            if name == 'out_int':
                self.add_instruction('jal out_int')
            elif name == 'out_string':
                self.add_instruction('jal out_string')
            elif name == 'in_int':
                self.add_instruction('jal in_int')
            elif name == 'in_string':
                self.add_instruction('jal in_string')
            else:
                function_name = self.rename_vars(expr[0])
                self.add_instruction(f'jal {function_name}')
        else:
            class_name = self.rename_vars(expr[0])
            function_name = self.rename_vars(expr[1])
            self.add_instruction(f'jal {class_name}_{function_name}')
        return self.visitChildren(ctx)

    def visitSelfExpr(self, ctx: ThreeAddressCodeParser.SelfExprContext):  # ✅
        return 'self'
    
    def visitTempExpr(self, ctx:ThreeAddressCodeParser.TempExprContext): # ✅
        return str(ctx.TEMPORAL())

    def visitIdExpr(self, ctx: ThreeAddressCodeParser.IdExprContext):  # ✅
        # return self.rename_vars(ctx.IDENTIFIER())
        return str(ctx.IDENTIFIER())

    def visitNumberExpr(self, ctx: ThreeAddressCodeParser.NumberExprContext):  # ✅
        return IntermediateCodeType(
            value=ctx.NUMBER(),
            type=IntermediateCodeTypeEnum.INTEGER,
        )

    def visitStringExpr(self, ctx: ThreeAddressCodeParser.StringExprContext):  # ✅
        return IntermediateCodeType(
            value=ctx.STRING(),
            type=IntermediateCodeTypeEnum.STRING,
        )

    def visitBoolExpr(self, ctx: ThreeAddressCodeParser.BoolExprContext):  # ✅
        return IntermediateCodeType(
            value=1 if str(ctx.BOOLEAN()) == 'true' else 0,
            type=IntermediateCodeTypeEnum.BOOLEAN,
        )
        
    def visitNullExpr(self, ctx:ThreeAddressCodeParser.NullExprContext):
        return IntermediateCodeType(
            value=ctx.NUMBER(),
            type=IntermediateCodeTypeEnum.INTEGER,
        )

    def visitLabelExpr(self, ctx: ThreeAddressCodeParser.LabelExprContext):  # ✅
        return str(ctx.LABEL())

    def visitOperatorExpr(self, ctx: ThreeAddressCodeParser.OperatorExprContext):
        # validar que registros estan disponibles
        # registers = {'$t0': False, '$t1': False, '$t2': False, '$t3': False, '$t4': False, '$t5': False, '$t6': False, '$t7': False}
        # registro_actual = ''

        operator = str(ctx.OP())
        exprs = ctx.expression()
        
        left = self.visit(exprs[0])
        right = self.visit(exprs[1])

        left_register = ''
        right_register = ''

        if isinstance(left, IntermediateCodeType):
            # obtener registro disponible
            # for register in registers:
            #     if not registers[register]:
            #         registro_actual = register
            #         registers[register] = True
            #         break
            # mover el valor a ese registro
            self.add_instruction(f'li $t0, {left.value}')
            left_register = '$t0'
        else:
            # obtener registro disponible
            # for register in registers:
            #     if not registers[register]:
            #         registro_actual = register
            #         registers[register] = True
            #         break
            # buscar la variable en variables y obtener su valor
            if self.variables.get(self.rename_vars(left)):
                nombre = self.rename_vars(left)
                self.add_instruction(f'la $t0, {nombre}')
                # for register in registers:
                #     if not registers[register]:
                #         registro_actual = register
                #         registers[register] = True
                #         break
                self.add_instruction(f'lw $t1, 0($t0)')
                left_register = '$t1'

        if isinstance(right, IntermediateCodeType):
            self.add_instruction(f'li $t2, {right.value}')
            right_register = '$t2'
        else:
            # buscar la variable en variables y obtener su valor
            if self.variables.get(self.rename_vars(right)):
                nombre = self.rename_vars(right)
                self.add_instruction(f'la $t2, {nombre}')
                self.add_instruction(f'lw $t3, 0($t2)')
                right_register = '$t3'

        if operator == '+':
            self.add_instruction(f'add $t0, {left_register}, {right_register}')
        elif operator == '-':
            self.add_instruction(f'sub $t0, {left_register}, {right_register}')
        elif operator == '*':
            self.add_instruction(f'mul $t0, {left_register}, {right_register}')
        elif operator == '/':
            self.add_instruction(f'div $t0, {left_register}, {right_register}')

            

        # print(left, operator, right)
        
        # print(operator, exprs)
        return 'OperatorExpr'

    def visitNegateExpr(self, ctx: ThreeAddressCodeParser.NegateExprContext):
        return self.visitChildren(ctx)

    def visitGraterThanExpr(self, ctx: ThreeAddressCodeParser.GraterThanExprContext):
        return self.visitChildren(ctx)

    def visitGraterEqualExpr(self, ctx: ThreeAddressCodeParser.GraterEqualExprContext):
        return self.visitChildren(ctx)

    def visitComparateExpr(self, ctx: ThreeAddressCodeParser.ComparateExprContext):
        return self.visitChildren(ctx)
