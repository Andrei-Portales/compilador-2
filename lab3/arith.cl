class Main inherits IO {
    var1: Int <- 3;
    var2: Int <- 8;

    main(): SELF_TYPE {{
        var1 <- var2 + 10;
        var2 <- var1 - var2;
        out_int(var2);

        self;
    }};
};