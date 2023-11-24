
.data
_lyn_s: .word 3
psxtre: .word 8
v_thof: .word 



.text
main:
    la $t0, psxtre
    lw $t1, 0($t0)
    li $t2, 10
    add $t0, $t1, $t2
    sw $t0, _lyn_s
    la $t0, _lyn_s
    lw $t1, 0($t0)
    la $t2, psxtre
    lw $t3, 0($t2)
    sub $t0, $t1, $t3
    sw $t0, psxtre
    la $a0, v_thof
    jal out_int
    li $v0, 10
    syscall

out_int:
    li $v0, 1
    syscall
    jr $ra

out_string:
    li $v0, 4
    syscall
    jr $ra

in_int:
    li $v0, 5
    syscall
    jr $ra
