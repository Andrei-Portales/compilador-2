class Object {
    variable_copy: Object;

    abort(): Object { "" };
    type_name(): String { "" };

    copy(): SELF_TYPE {{
        variable_copy <- self;
        if variable_copy = void then{
            variable_copy <- self;
        }else
            variable_copy <- variable_copy
        fi;
    }};
};

class OI {
    out_string(x: String): SELF_TYPE { self };
    out_int(x: Int): SELF_TYPE { self };
    in_string(): String { "" };
    in_int(): Int { 0 };
};