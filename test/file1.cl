class A inherits B {
    var : Int <- 0;

    method1(asd:Int, das: String) : Int { 10 };
};

class B {
    var1 : Int <- 0;

    method2(asd:Int, das: String) : Int { 10 };
};

class Main {

    var: A <- new A;

    main() : Int {{
        var.method2(10, "asd");
    }};
};
