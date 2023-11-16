package javaPractice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class functionalInterfaces {

    public static void main(String[] args){
        Employee e1 = new Employee("bob", 24);
        Employee e2 = new Employee("cat", 35);
        Employee e3 = new Employee("de", 10);
        Employee e4 = new Employee("xander", 44);
        Employee e5 = new Employee("page", 75);

//          Arrays have a .length attribute, arraylists have a size attribute
//        Employee[] ea = {e1, e2, e3};
//        System.out.println(ea.length);
//        List<Employee> el = new ArrayList<>(Arrays.asList(e4, e5, e1, e2, e3));

//        Map<Integer, Listing > mapOfVinToListing = listings.stream().collect(Collectors.toMap(Listing::getVin, Functions.identity()); // Assuming vin is unique per listing
//        mapOfVinToListing.get(456);// O(1)

        List<Employee> el = new ArrayList<>();
        Employee[] ee = {e1, e2};
        Arrays.stream(ee).forEach((x) -> {
            System.out.println(x.getName());
        });
        el.addAll(Arrays.asList(ee));
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
    }
}
