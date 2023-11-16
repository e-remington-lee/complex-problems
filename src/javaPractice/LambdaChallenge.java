package javaPractice;

import java.util.*;
import java.util.function.Function;
import java.util.function.Supplier;
import java.util.stream.*;

public class LambdaChallenge {
    public static void main(String[] args) {
//        c1();

        /**
         * Challenge 2, both work apparently
         */
        ChallengeLambdas obj = (s) -> {
          StringBuilder b = new StringBuilder();
          for (int i=0; i<s.length(); i ++) {
              if (i % 2 == 0){
                  b.append(s.charAt(i));
              }
          }
          return b.toString();
        };

        Function<String, String> o = (s) -> {
            StringBuilder b = new StringBuilder();
            for (int i=0; i<s.length(); i ++) {
                if (i % 2 == 0){
                    b.append(s.charAt(i));
                }
            }
            return b.toString();
        };

        System.out.println(c2(o));

//        System.out.println(o.apply("idkfdafd"));

        /**
         * Challenge 3
         */

        Supplier<String> ilj = () -> {
            return "I love java";
        };

        System.out.println(ilj.get());

    }

    public static String c2 (Function<String, String> l ){
        return l.apply("12352134");
    }

    public static void c1 () {
        String s = "yo bro wtf is goin on here?";
        new Thread(() -> {
            Stream.of(s.split(" "))
                    .forEach(si -> System.out.println(si));
        }).start();
    }
}

interface ChallengeLambdas {
    String everySecondCharacter(String src);
}
