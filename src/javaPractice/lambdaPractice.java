package javaPractice;

import java.util.*;

public class lambdaPractice {

//    public void idk2 () {
//        Employee e1 = new Employee("bob");
//        Employee e2 = new Employee("cat");
//        Employee e3 = new Employee("de");
//        Employee e4 = new Employee("xander");
//        Employee e5 = new Employee("page");
//
////          Arrays have a .length attribute, arraylists have a size attribute
////        Employee[] ea = {e1, e2, e3};
////        System.out.println(ea.length);
//        List<Employee> el = new ArrayList<>(Arrays.asList(e4, e5, e1, e2, e3));
//        el.forEach(fuck::notstatic);
//    }

    public static void main(String[] args) {
        Employee e1 = new Employee("bob", 24);
        Employee e2 = new Employee("cat", 35);
        Employee e3 = new Employee("de", 10);
        Employee e4 = new Employee("xander", 44);
        Employee e5 = new Employee("page", 75);

//          Arrays have a .length attribute, arraylists have a size attribute
//        Employee[] ea = {e1, e2, e3};
//        System.out.println(ea.length);
        List<Employee> el = new ArrayList<>(Arrays.asList(e4, e5, e1, e2, e3));

//        Collections.sort(el, new Comparator<Employee>() {
//            @Override
//            public int compare(Employee e1, Employee e2) {
//              return e1.getName().compareTo(e2.getName());
//            };
//        });

        Collections.sort(el, (ee1, ee2) -> {
            return ee1.getName().compareTo(ee2.getName());
        });

            // This will not work bc i is not final, we cannot use non-final values in a lambda function
//        for (int i = 0; i < el.size(); i++) {
//            System.out.println(el.get(i).getName());
//            new Thread(() -> {
//                System.out.println(el.get(i).getName());
//            });
//        }

//        for (Employee e : el) {
//            System.out.println(e.getName());
//            new Thread(() -> {
//                System.out.println(e.getName());
//            }).start();
//        }

        el.forEach((e) -> {
            System.out.println(e.getName());
            new Thread(() -> {
                e.setName("adkfasd");
                System.out.println(e.getName());
                e.getName();
            }).start();
        });


        el.forEach((e) -> {
            System.out.println(e.getName());
        });
        // double colon is the reference operator. It is used to call a method by referring to the class directly.
        // When the method is called, it will affect the
//        el.forEach(fuck::idk);
//        System.out.println(fuck.getCount());

//        String ss = doStuff(new UpperConcat() {
//            @Override
//            public String upperAndConcat(String s1, String s2) {
//                return s1.toUpperCase() + s2.toUpperCase();
//            };
//        }, e1.getName(), e2.getName());

        UpperConcat uc = (s1, s2) -> {
            String r =  s1 + s2;
            return r;
        };

//        System.out.println(uc.upperAndConcat(e1.getName(), e2.getName()));
//        AnotherClass ac = new AnotherClass();
//        System.out.println(ac.doSomething());
    }


    public static String doStuff(UpperConcat c1, String s1, String s2) {
        return c1.upperAndConcat(s1, s2);
    }

}

//class Employee {
//    private String name;
//
//    Employee(String name){
//        this.name = name;
//    }
//
//    public String getName() {
//        return name;
//    }
//
//    public void setName(String name) {
//        this.name = name;
//    }
//}

class fuck {
    static int count = 0;

    public static void idk(Employee e){
        count++;
        System.out.println(e.getName());
    }

    public void notstatic() {

    }

    public static int getCount() {
        return count;
    }

}

@FunctionalInterface
interface UpperConcat {
    String upperAndConcat(String s1, String s2);
}

class AnotherClass {
    public String doSomething() {
        int count = 0;
        UpperConcat uc = (s1, s2) -> {
            System.out.println("The lambda expressions class is "+getClass().getSimpleName());
            System.out.println(count);
          return s1 + s2;
        };

        return lambdaPractice.doStuff(uc, "s1", "s2");
    }
}
