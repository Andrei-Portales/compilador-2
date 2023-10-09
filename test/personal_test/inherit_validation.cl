class A {
    var3: Int <- 30;
    var4: Bool <- true;
    var5: String <- "Hello World";

    method0(param1: Int, param2: Int, param3: Int, param4: Int, param5: Int): Int {{
        

        0;
    }};

    method1(param1: Int): Int {{
        --var3 <- 60 + 10 % var3 * 50 * 60 * 60 * var3;
        --var3 <- var3 * var3 + 10 * 5;
        --var4 <-  not (false && (true || false));

        --if (var3 <= 20) then {
        --    var3 <- 2;
        --} else {
        --    var3 <- 2 + 10;
        --} fi;

        --if (var3 <= 20) then {
        --    var3 <- 2;
        --} else {
        --    var3 <- 2 + 10;
        --} fi;

        --if (var3 <= 20) then {
        --    var3 <- 2;
        --} else {
        --    var3 <- 2 + 10;
        --} fi;

        --while 10 < 30 loop {
        --    var3 <- var3 + ~1;
        --    var3 <- var3 + 20 * 50 / 60;
        --} pool;

        --let x: Int <- 10 in {
        --    x <- 30 + var3;
        --    x;
        --};

        --method0(var3, 10, var3, 10, 10);

        (new A).method0(var3, 10, var3, 10, 10);

        var3;
    }};

    method2(): Int {{
        var5 <- "Hello asdasd";
        var3 <- 10;
        var3 <- 20 * 50 / var3 + 10 + 10 + 20;
        var3;
    }};
};



class Main {
    --class_a: A <- new A;

    main(): Int {
        0
    };
};