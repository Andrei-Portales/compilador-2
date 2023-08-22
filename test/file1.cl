class A {
    var : Integer <- 0;

    method1(asd:Integer, das: String) : Integer { 10 };
};

class B inherits A {
    var2: Integer <- 0;
    var3: String <- "";
    var4: B <- (new B);
    isVar4Void: Boolean;
};

class C inherits B {
    var5: Integer <- 0;
    var6: String <- "";
    var7: B <- (new B);
    isVar7Void: Boolean;

    test() : A {
        (new A) 
    };
};

class D {
    var1: C <- (new C);
    var2: Integer <- 0;

    run(asd: Integer): Integer {{
        var0.dfgdfgdfg();
    }};
};

class Main {

    var: SELF_TYPE <- (new Main);

    main() : SELF_TYPE {{
        self;
    }};
};
