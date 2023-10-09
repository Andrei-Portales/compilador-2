class A {
    var3: Int <- 1;
    var4: Bool <- true;

    method0(param1: Int, param2: String): Int {{
        

        0;
    }};

    method1(param1: Int): Int {{
        var3 <- var3 + param1 % 5;
        var4 <- false && (true || false);

        if (false = (var3 <= 20)) then {
            var3 <- 2;
        } else {
            var3 <- 2 + 10;
        } fi;

        while 10 < 30 loop {
            var3 <- var3 + ~1;
            var3 <- var3 + 20 * 50 / 60;
        } pool;

        method0(var3, "2");

        var3;
    }};
};



class Main {
    main(): SELF_TYPE {
        self
    };
};