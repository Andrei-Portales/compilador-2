class Main {
    var1: Int <- 1;

    main(): SELF_TYPE {{
        var1 <- 20 + 30;
        var1 <- 50 / 5;
        var1 <- 20 * 30;
        var1 <- 40 / 30;

        self;
    }};
};