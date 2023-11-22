

# $0 (o $zero): Siempre contiene el valor 0.
# $v0, $v1: Usados para devolver valores de funciones.
# $a0 a $a3: Usados para argumentos de funciones.
# $t0 a $t9: Registros temporales, no preservados a través de llamadas a funciones.
# $s0 a $s7: Registros salvados, preservados a través de llamadas a funciones.

# $gp: Puntero global, usado para acceder a datos globales.
# $sp: Puntero de pila, usado para gestión de la pila.
# $fp: Puntero de marco, usado para gestionar marcos de pila.
# $ra: Registro de retorno, almacena la dirección de retorno de funciones.


class MemoryManager:
    def __init__(self):
        # registros
        
        self.args_registers = {
            'a0': None,
            'a1': None,
            'a2': None,
            'a3': None,
        }
        
        self.return_value_registers = {
            'v0': None,
            'v1': None,
        }
        
        self.temporal_registers = {
            't0': None,
            't1': None,
            't2': None,
            't3': None,
            't4': None,
            't5': None,
            't6': None,
            't7': None,
            't8': None,
            't9': None,
        }
        
        self.saved_registers = {
            's0': None,
            's1': None,
            's2': None,
            's3': None,
            's4': None,
            's5': None,
            's6': None,
            's7': None,
        }

        self.stack = []
        pass
    