class Main inherits IO {
   bool: Boolean <- false;
   number: Integer <- 0;
   
   main(): SELF_TYPE {{
      bool <- not true;
      bool <- not false;
      bool <- false;

      number <- 10 + 20;

   }};
};
