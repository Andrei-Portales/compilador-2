class Main inherits IO {
    var3: Int <- 3;
    var4: Int <- 2;

    ackerman(m:Int, n:Int): Int {{
        if (m = 0) then {
            n+1 
        } else {
            if (n=0) then {
                ackerman(m - 1, 1)
            } else {
                ackerman(m - 1, ackerman(m, n-1))
            } fi;
        }};
        fi;
    };

    main(): Int {
        {
            ackerman(var3,var4);
        }
    }
}