class Main {

    method1(): Int {
        1
    };

    method2(param1: String, param2: Int) : String {
        param1
    };

    method3(): Int {{
        let x: Int <- 1, y: String in {
            x <- 2;
            y <- "hello";
            x;
        };

        x; -- dara error ya que x no esta definido en este scope solo en let
    }};

    main(): SELF_TYPE{
        self
    };
};