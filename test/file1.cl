class Object {
    abort(): Object { false };
    type_name(): String { "" };
    copy(): SELF_TYPE { self };
};

class OI {
    out_string(x: String): SELF_TYPE { self };
    out_int(x: Int): SELF_TYPE { self };
    in_string(): String { "" };
    in_int(): Int { 0 };
};
