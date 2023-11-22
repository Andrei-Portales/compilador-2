
.data
nialfr: .asciiz "hello" ;
znrowg: .word 20 ;
rtgg_x: .word 0 ;
szswxq: .asciiz "world" ;



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

qgynqm:
    la $t0, nialfr;
    li $t1, "Adios";
    sw $t1, 0($t0);
    la $t0, znrowg;
    li $t1, 70;
    sw $t1, 0($t0);
    la $t0, _t0;
    li $t1, znrowg;
    sw $t1, 0($t0);
    la $t0, znrowg;
    li $t1, 50;
    sw $t1, 0($t0);
    lw $t0, vrlgbh;
    beq $t0, $zero, _L0;
    j _L1;
    _L0:
    _L1:
    la $v0, nialfr;
    jr $ra;

xngocb:
    jr $ra;

xqd_ez:
    la $v0, szswxq;
    jr $ra;

lsmupe:
    la $v0, self;
    jr $ra;
