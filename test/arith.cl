class A {

   var : Integer <- 0;
   value() : Integer { var };

   set_var(num : Integer) : SELF_TYPE {
      {
         var <- num;
         self;
      }
   };

   method1(num : Integer) : SELF_TYPE {  -- same
      self
   };

   method2(num1 : Integer, num2 : Integer) : B {  -- plus
      (let x : Integer in
	 {
            x <- num1 + num2;
	    (new B).set_var(x);
	 }
      )
   };

   method3(num : Integer) : C {  -- negate
      (let x : Integer in
	 {
            x <- ~num;
	    (new C).set_var(x);
	 }
      )
   };

   method4(num1 : Integer, num2 : Integer) : D {  -- diff
            if num2 < num1 then
               (let x : Integer in
		  {
                     x <- num1 - num2;
	             (new D).set_var(x);
	          }
               )
            else
               (let x : Integer in
		  {
	             x <- num2 - num1;
	             (new D).set_var(x);
		  }
               )
            fi
   };

   method5(num : Integer) : E {  -- factorial
      (let x : Integer <- 1 in
	 {
	    (let y : Integer <- 1 in
	       while y <= num loop
	          {
                     x <- x * y;
	             y <- y + 1;
	          }
	       pool
	    );
	    (new E).set_var(x);
	 }
      )
   };

};

class B inherits A {  -- B is a number squared

   method5(num : Integer) : E { -- square
      (let x : Integer in
	 {
            x <- num * num;
	    (new E).set_var(x);
	 }
      )
   };

};

class C inherits B {

   method6(num : Integer) : A { -- negate
      (let x : Integer in
         {
            x <- ~num;
	    (new A).set_var(x);
         }
      )
   };

   method5(num : Integer) : E {  -- cube
      (let x : Integer in
	 {
            x <- num * num * num;
	    (new E).set_var(x);
	 }
      )
   };

};

class D inherits B {  
		
   method7(num : Integer) : Bool {  -- divisible by 3
      (let x : Integer <- num in
            if x < 0 then method7(~x) else
            if 0 = x then true else
            if 1 = x then false else
	    if 2 = x then false else
	       method7(x - 3)
	    fi fi fi fi
      )
   };

};

class E inherits D {

   method6(num : Integer) : A {  -- division
      (let x : Integer in
         {
            x <- num / 8;
	    (new A).set_var(x);
         }
      )
   };

};


class Main inherits IO {
   
   char : String;
   avar : A; 
   a_var : A;
   flag : Bool <- true;



   is_even(num : Integer) : Bool {
      (let x : Integer <- num in
            if x < 0 then is_even(~x) else
            if 0 = x then true else
	    if 1 = x then false else
	          is_even(x - 2)
	    fi fi fi
      )
   };

   main() : Object {
      {
         avar <- (new A);
         avar.set_var(2);
         out_int(avar.value());
         
         if is_even(avar.value()) then
	          out_string(" es par!\n")
	     else
	          out_string(" es impar!\n")
	     fi;
	     
         a_var <- (new A).set_var(3);
	     avar <- (new B).method2(avar.value(), a_var.value());
         out_int(avar.value());
         out_string("\n");
         
         
         avar <- (new C).method6(avar.value());
         out_int(avar.value());
         out_string("\n");
        
         a_var <- (new A).set_var(5);
         avar <- (new D).method4(avar.value(), a_var.value());
         out_int(avar.value());
         out_string("\n");
        
         avar.set_var(5);
         avar <- (new C)@A.method5(avar.value());
         out_int(avar.value());
         out_string("\n");
      	 
         avar.set_var(6);
         avar <- (new C)@B.method5(avar.value());
         out_int(avar.value());
         out_string("\n");

      }
   };

};

