
.data
onsqwd: .asciiz "hello" ;
zqwnqu: .word 20 ;
rrqemo: .word 0 ;
f_tgot: .asciiz "world" ;



.text
out_int:
    li $v0, 1;
    syscall;
    jr $ra;

out_string:
    li $v0, 4;
    syscall;
    jr $ra;

in_int:
    li $v0, 5;
    syscall;
    jr $ra;

in_string:
    li $v0, 8;
    li $a1, 1024;
    la $a0, buffer;
    syscall;
    jr $ra;

tnhcsm:
    lw $t0, rrqemo;
    beq $t0, $zero, _L0;
    j _L1;
    _L0:
    _L1:
    la $v0, onsqwd;
    jr $ra;

mccohn:
    jr $ra;

sfrrxm:
    la $v0, f_tgot;
    jr $ra;

jccuid:
    la $v0, self;
    jr $ra;
