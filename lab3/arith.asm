.data
var1: .word 1   # Espacio de almacenamiento para var1

.text
main:
    # var1 <- 20 + 30
    li $t0, 20      # Cargar 20 en $t0
    li $t1, 30      # Cargar 30 en $t1
    add $t2, $t0, $t1 # Sumar $t0 y $t1, resultado en $t2
    sw $t2, var1    # Guardar el resultado en var1

    # var1 <- 50 / 5
    li $t0, 50      # Cargar 50 en $t0
    li $t1, 5       # Cargar 5 en $t1
    div $t0, $t1    # Dividir $t0 por $t1
    mflo $t2        # Mover el resultado de la división a $t2
    sw $t2, var1    # Guardar el resultado en var1

    # var1 <- 20 * 30
    li $t0, 20      # Cargar 20 en $t0
    li $t1, 30      # Cargar 30 en $t1
    mul $t2, $t0, $t1 # Multiplicar $t0 por $t1, resultado en $t2
    sw $t2, var1    # Guardar el resultado en var1

    # var1 <- 40 / 30
    li $t0, 40      # Cargar 40 en $t0
    li $t1, 30      # Cargar 30 en $t1
    div $t0, $t1    # Dividir $t0 por $t1
    mflo $t2        # Mover el resultado de la división a $t2
    sw $t2, var1    # Guardar el resultado en var1

    # Terminar el programa
    li $v0, 10      # Código para terminar el programa
    syscall