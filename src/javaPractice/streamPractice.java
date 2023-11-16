package javaPractice;

import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.util.Arrays.asList;

public class streamPractice {

    public static void main(String[] args) {
//         You can Arrays.stream(), Stream.of(String[] or input strings manually, or Arrays.asList(strings[]).stream()
//        String[] strings = {"N40", "N50", "i17", "O90", "E55"};
//        Arrays.stream(strings).count();
//        Stream.of("N40", "N50", "i17", "O90", "E55").count();
//        Arrays.asList(strings).stream().count();
//        List<String> s = Arrays.asList(strings);
        List<String> strings = asList("N90", "G10", "N50", "i17", "O90", "E55");

//        System.out.println(strings[0]);
//        Arrays.stream(strings).peek(s -> {
//            System.out.println(s);
//            System.out.println("in peek");
//        });
        List<String> newList = strings.stream()
                .map(s -> s.toUpperCase())
                .filter(s -> s.startsWith("N"))
                .sorted((s1, s2) -> s1.compareTo(s2))
                .collect(ArrayList::new, ArrayList::add, ArrayList::addAll);

//        newList.add("hi");
//        newList.forEach(s -> System.out.println(s));

        List<String> strings2 = asList("N90", "G10", "N50", "i17", "O90", "E55", "E55", "E55", "E55");

//        Long ans = strings2.stream()
//                .distinct()
//                .peek(s -> System.out.println(s))
//                .count();
//        System.out.println(ans);
//        strings.stream().forEach(s -> {
//            if (s.startsWith("N")) {
//                newList.add(s);
//            }
//        });
//
//        newList.forEach(s -> {
//            System.out.println(s);
//        });
//
//        newList.sort((s1, s2) -> {
//            return s1.compareTo(s2);
//        });
//
//        newList.forEach(s -> System.out.println(s));


        Employee e1 = new Employee("bob", 24);
        Employee e2 = new Employee("cat", 35);
        Employee e3 = new Employee("de", 35);
        Employee e4 = new Employee("xander", 44);
        Employee e5 = new Employee("page", 75);

        Department hr = new Department("HR");
        hr.addEmployee(e1);
        hr.addEmployee(e2);
        hr.addEmployee(e3);
        Department accounting = new Department("Accounting");
        accounting.addEmployee(e4);
        accounting.addEmployee(e5);

        List<Department> ds = Arrays.asList(hr, accounting);

        /**
         * flat map testing
         */
        // flat map is useful for one-to-many relations. each department has a list of employees, and we have a list of departments
        // but we want to operate on the lists inside the objects!
//        ds.stream()
//                .flatMap(d -> d.getEmployees().stream())
//                .forEach(s -> System.out.println(s));

        /**
         * testing map functions with collect
         */
//        Map<Integer, List<Employee>> ages = ds.stream()
//                .flatMap(d -> d.getEmployees().stream())
//                .collect(Collectors.groupingBy(e -> e.getAge()));
//
//        ages.forEach((x, y) -> {
//            System.out.println("Key: " + x);
//            y.forEach(s -> System.out.println(s));
//        });

        // filtering values and counting them or then doing something on them
        long l = ds.stream().filter(d -> {
            if (d.getName().equals("Accounting")) {
                return true;
            } else{
                return false;
            }
        }).count();
        System.out.println(l);

        // Sorting with Comparator.comparing(method reference operator)
        ds.stream()
                .flatMap(d -> d.getEmployees().stream())
                .sorted((x1, x2) -> {
                    return x1.getName().compareTo(x2.getName());
                })
                .forEach(s -> System.out.println(s.getName()));

        ds.stream().map(g -> {
            return "bob";
        }).forEach(g -> System.out.println(g));

        // make sure all values in stream match a condition
        boolean validEmployees = ds.stream()
                .flatMap(d -> d.getEmployees().stream())
                .allMatch(e -> e.getAge() > 18);
        System.out.println(validEmployees);

//        boolean i = ds.stream()
//                .noneMatch(d -> d.getName().equals("HR"));
//        System.out.println(i);

        // Can use flatmap to stream items in a list, to do something like this
        List<String> phrases = Arrays.asList(
                "sporadic perjury",
                "confounded skimming",
                "incumbent jailer",
                "confounded jailer");

        List<String> uniqueWords = phrases
                .stream()
                .flatMap(phrase -> Stream.of(phrase.split("\\s+")))
                .distinct()
               .sorted()
                .collect(Collectors.toList());
//        System.out.println("Unique words: " + uniqueWords);

        // Limits the stream, both the following limits have different outputs
        // Bc we are limiting the stream before and after we flatmap,
//        ds.stream()
//                .limit(1)
//                .flatMap(d -> d.getEmployees().stream())
//                .forEach(e -> System.out.println(e.getName()));
//        ds.stream()
//                .flatMap(d -> d.getEmployees().stream())
//                // The flatmap goes in order of concatenating the lists, list1 will go first then list2
//                .limit(3)
//                .forEach(e -> System.out.println(e.getName()));

//         You have to know max/min/ifpresent all return optionals, check ispresent first then .get()
//        Optional<Department> dd = ds.stream().max(Comparator.comparing(Department::getName));
//        if (dd.isPresent()){
//            System.out.println(dd.get().getName());
//        }

//        Set<Employee> ss= ds.stream().flatMap(d -> d.getEmployees().stream()).collect(Collectors.toSet());
//        for (Employee e : ss){
//            System.out.println(e.getName());
//        }

//        Optional<Employee> eage = ds.stream()
//                .flatMap(d -> d.getEmployees().stream())
//                .reduce((ee1, ee2) -> ee1.getAge() < ee2.getAge() ? ee1 : ee2);
//        eage.ifPresent(s -> System.out.println(s));

//        System.out.println("c".compareTo("b"));



    }

}
