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
        self.classes_vars_map: Record[str, Record[str, str]] = {}
        self.actual_class = None
        self.actual_function = None

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
        if not self.classes_vars_map[self.actual_class].get(var_name):
            self.classes_vars_map[self.actual_class][var_name] = generateRandomVariable(
            )

        return self.classes_vars_map[self.actual_class][var_name]

    def add_instruction(self, instruction: str):
        self.functions[self.actual_function]['instructions'].append(
            instruction)

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

    def visitGlobalVarDeclaration(self, ctx: ThreeAddressCodeParser.GlobalVarDeclarationContext): # ✅  # ✅
        id_name = self.rename_vars(ctx.IDENTIFIER())
        exp = self.visit(ctx.expression())

        type_var = None

        if exp.type == IntermediateCodeTypeEnum.INTEGER:
            type_var = '.word'
        elif exp.type == IntermediateCodeTypeEnum.STRING:
            type_var = '.asciiz'
        elif exp.type == IntermediateCodeTypeEnum.BOOLEAN:
            type_var = '.word'
        else:
            raise Exception('Type not supported')

        # registrar variable
        self.variables[id_name] = {
            'name': id_name,
            'type': type_var,
            'value': exp.value,
        }

    def visitMethodDeclaration(self, ctx: ThreeAddressCodeParser.MethodDeclarationContext):  # ✅
        id_method = self.rename_vars(ctx.IDENTIFIER())

        self.actual_function = id_method

        self.functions[id_method] = {
            'name': id_method,
            'instructions': [],
        }

        for instruct in ctx.instruction():
            self.visit(instruct)

        self.actual_function = None

    def visitReturnInstr(self, ctx: ThreeAddressCodeParser.ReturnInstrContext):
        return self.visitChildren(ctx)

    def visitAssignInstr(self, ctx: ThreeAddressCodeParser.AssignInstrContext):
        return self.visitChildren(ctx)

    def visitEqualInstr(self, ctx: ThreeAddressCodeParser.EqualInstrContext):
        return self.visitChildren(ctx)

    def visitNegateInstr(self, ctx: ThreeAddressCodeParser.NegateInstrContext):
        return self.visitChildren(ctx)

    def visitLtInstr(self, ctx: ThreeAddressCodeParser.LtInstrContext):
        return self.visitChildren(ctx)

    def visitIfInstr(self, ctx: ThreeAddressCodeParser.IfInstrContext):
        return self.visitChildren(ctx)

    def visitGotoInstr(self, ctx: ThreeAddressCodeParser.GotoInstrContext):
        return self.visitChildren(ctx)

    def visitPushParamInstr(self, ctx: ThreeAddressCodeParser.PushParamInstrContext):
        return self.visitChildren(ctx)

    def visitPopParamInstr(self, ctx: ThreeAddressCodeParser.PopParamInstrContext):
        return self.visitChildren(ctx)

    def visitFCallInstr(self, ctx: ThreeAddressCodeParser.FCallInstrContext):
        return self.visitChildren(ctx)

    def visitLabelInstr(self, ctx: ThreeAddressCodeParser.LabelInstrContext):
        return self.visitChildren(ctx)

    def visitFCallStatement(self, ctx: ThreeAddressCodeParser.FCallStatementContext):
        return self.visitChildren(ctx)

    def visitSelfExpr(self, ctx: ThreeAddressCodeParser.SelfExprContext): # ✅
        return 'self'

    def visitIdExpr(self, ctx: ThreeAddressCodeParser.IdExprContext): # ✅
        return self.rename_vars(ctx.IDENTIFIER())

    def visitNumberExpr(self, ctx: ThreeAddressCodeParser.NumberExprContext): # ✅
        return IntermediateCodeType(
            value=ctx.NUMBER(),
            type=IntermediateCodeTypeEnum.INTEGER,
        )

    def visitStringExpr(self, ctx: ThreeAddressCodeParser.StringExprContext): # ✅
        return IntermediateCodeType(
            value=ctx.STRING(),
            type=IntermediateCodeTypeEnum.STRING,
        )

    def visitBoolExpr(self, ctx:ThreeAddressCodeParser.BoolExprContext): # ✅        
        return IntermediateCodeType(
            value= 1 if str(ctx.BOOLEAN()) == 'true' else 0,
            type=IntermediateCodeTypeEnum.BOOLEAN,
        )


    def visitLabelExpr(self, ctx: ThreeAddressCodeParser.LabelExprContext):
        return self.visitChildren(ctx)

    def visitOperatorExpr(self, ctx: ThreeAddressCodeParser.OperatorExprContext):
        return self.visitChildren(ctx)

    def visitNegateExpr(self, ctx: ThreeAddressCodeParser.NegateExprContext):
        return self.visitChildren(ctx)

    def visitGraterThanExpr(self, ctx: ThreeAddressCodeParser.GraterThanExprContext):
        return self.visitChildren(ctx)

    def visitGraterEqualExpr(self, ctx: ThreeAddressCodeParser.GraterEqualExprContext):
        return self.visitChildren(ctx)

    def visitComparateExpr(self, ctx: ThreeAddressCodeParser.ComparateExprContext):
        return self.visitChildren(ctx)
