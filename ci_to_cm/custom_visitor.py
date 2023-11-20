from ThreeAdress_parser.ThreeAddressCodeVisitor import ThreeAddressCodeVisitor
from ThreeAdress_parser.ThreeAddressCodeParser import ThreeAddressCodeParser
import jinja2

class CI2MPIPSVisitor(ThreeAddressCodeVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = []
    
    def fillTemplate(self):
        TEMPLATE_PATH = 'ci_to_cm/templates/mips_code_template.j2'
        template = jinja2.Template(open(TEMPLATE_PATH).read())

        data = {
            'data': [
                {
                    'name': 'number1',
                    'bytes': 4,
                },
                {
                    'name': 'number2',
                    'bytes': 10,
                }
            ],
            'text': {
                'functions': [
                    {
                        'name': 'main',
                        'instructions': [],
                    }    
                ],    
            },
        }

        output = template.render(data)

        with open('ci_to_cm/outputs/mips_code.asm', 'w', encoding='utf-8') as f:
            f.write(output)
    
    def visitProgram(self, ctx:ThreeAddressCodeParser.ProgramContext):
        self.fillTemplate()
        print('visitProgram')
        return self.visitChildren(ctx)


    def visitClassDeclaration(self, ctx:ThreeAddressCodeParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    def visitGlobalVarDeclaration(self, ctx:ThreeAddressCodeParser.GlobalVarDeclarationContext):
        return self.visitChildren(ctx)


    def visitMethodDeclaration(self, ctx:ThreeAddressCodeParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    def visitReturnInstr(self, ctx:ThreeAddressCodeParser.ReturnInstrContext):
        return self.visitChildren(ctx)


    def visitAssignInstr(self, ctx:ThreeAddressCodeParser.AssignInstrContext):
        return self.visitChildren(ctx)


    def visitEqualInstr(self, ctx:ThreeAddressCodeParser.EqualInstrContext):
        return self.visitChildren(ctx)


    def visitNegateInstr(self, ctx:ThreeAddressCodeParser.NegateInstrContext):
        return self.visitChildren(ctx)


    def visitLtInstr(self, ctx:ThreeAddressCodeParser.LtInstrContext):
        return self.visitChildren(ctx)


    def visitIfInstr(self, ctx:ThreeAddressCodeParser.IfInstrContext):
        return self.visitChildren(ctx)


    def visitGotoInstr(self, ctx:ThreeAddressCodeParser.GotoInstrContext):
        return self.visitChildren(ctx)


    def visitPushParamInstr(self, ctx:ThreeAddressCodeParser.PushParamInstrContext):
        return self.visitChildren(ctx)


    def visitPopParamInstr(self, ctx:ThreeAddressCodeParser.PopParamInstrContext):
        return self.visitChildren(ctx)


    def visitFCallInstr(self, ctx:ThreeAddressCodeParser.FCallInstrContext):
        return self.visitChildren(ctx)


    def visitLabelInstr(self, ctx:ThreeAddressCodeParser.LabelInstrContext):
        return self.visitChildren(ctx)


    def visitFCallStatement(self, ctx:ThreeAddressCodeParser.FCallStatementContext):
        return self.visitChildren(ctx)


    def visitExpression(self, ctx:ThreeAddressCodeParser.ExpressionContext):
        return self.visitChildren(ctx)