class Main {

    method1(): Int {
        1
    };

    method2(param1: String, param2: Int) : String {
        param1
    };

    method3(): SELF_TYPE {{
        method1();

        method2("a", 1);

        --method2(1, " "); -- dara error porque los parametros no coinciden con los tipos definidos

        --method2("", 2, 2); -- dara error porque el numero de parametros ingresados no coincide con los parametros definidos

        self;
    }};

    main(): SELF_TYPE{
        self
    };
};