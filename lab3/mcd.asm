.data
msg:    .asciiz "MCD: " 

.text
.globl main

main:
    # Inicializa los numeros
    li $t0, 97 # Primer numero a
    li $t1, 509 # Segundo numero b
    
    # Llama a la funcion gcd
    move $a0, $t0
    move $a1, $t1
    jal gcd
    
    # Guarda el resultado
    move $t2, $v0
    
    # Imprime el mensaje
    li $v0, 4     # syscall para imprimir string
    la $a0, msg
    syscall
    
    # Imprime el resultado
    move $a0, $t2 # mover el resultado para imprimirlo
    li $v0, 1     # syscall para imprimir int
    syscall
    
    # Salir del programa
    li $v0, 10    # syscall para salir
    syscall
    
gcd:
    # Verifica si b es 0
    beq $a1, $zero, done
    
    # Guarda el registro de retorno
    addiu $sp, $sp, -4  # reduce el puntero de pila
    sw $ra, 0($sp)      # guarda $ra en la pila
    
    # Calcula a % b
    rem $t3, $a0, $a1
    
    # Realiza la llamada recursiva: gcd(b, a % b)
    move $a0, $a1
    move $a1, $t3
    jal gcd
    
    # Restaura el registro de retorno
    lw $ra, 0($sp)      # recupera $ra de la pila
    addiu $sp, $sp, 4   # aumenta el puntero de pila
    
    # Retorna de la funcion
    jr $ra
    
done:
    # Si b es 0, retorna a
    move $v0, $a0
    jr $ra
