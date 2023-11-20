from enum import Enum

class IntermediateCodeTypeEnum(Enum):
    STRING = 1
    INTEGER = 2
    BOOLEAN = 3

class IntermediateCodeType:
    def __init__(self, value: str | int, type: IntermediateCodeTypeEnum):
        self.value = value
        self.type = type
        
    def to_string(self):
        return f'{self.value}'
    
    def __str__(self):
        return self.to_string()
    
    def __repr__(self):
        return self.to_string()
        