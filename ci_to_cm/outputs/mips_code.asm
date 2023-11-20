
.data
ntgewz: .asciiz "hello" ;
xgstom: .word 20 ;
wsvcbb: .word 0 ;
tvaysd: .asciiz "world" ;



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

uejb_w:
    la $t0, ntgewz;
    li $t1, "Adios";
    sw $t1, 0($t0);
    la $t0, xgstom;
    li $t1, 70;
    sw $t1, 0($t0);
    la $t0, _t0;
    li $t1, xgstom;
    sw $t1, 0($t0);
    la $t0, xgstom;
    li $t1, 50;
    sw $t1, 0($t0);
    lw $t0, wsvcbb;
    beq $t0, $zero, _L0;
    j _L1;
    _L0:
    _L1:
    la $v0, ntgewz;
    jr $ra;

ysvrrz:
    jr $ra;

ktjfjs:
    la $v0, tvaysd;
    jr $ra;

rajdcz:
    la $v0, self;
    jr $ra;
