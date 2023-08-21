class A {
    var : Integer <- 0;

    method1(asd:Integer) : Integer { 10 };
};

class B inherits A {
    var2: Integer <- 0;
    var3: String <- "";

    method1(asd:Integer) : Integer {{
        var <- 10;

        while ((10 + 5) < var)  loop {
            var <- var % 1;
        } pool;

        if var = 10 then
            var <- 20
        else
            var <- 3
        fi;
    }};
};
