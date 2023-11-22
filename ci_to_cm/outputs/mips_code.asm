
.data
qrjmdi: .asciiz "Hello, World.\n"



.text
main:
    la $a0, qrjmdi
    jal out_string
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
