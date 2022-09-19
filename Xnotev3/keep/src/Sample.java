import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;

public class Sample {
    public static void main(String[] args) {
        Sample.question1();
        Sample.question2();
        Sample.question3();
        Sample.question4();
        Sample.question5();
        Sample.question6();
        Sample.question7();
        Sample.question8();
        Sample.question9();
        Sample.question10();
    }

    public static void question1() {
        int korean = 80;
        int english = 75;
        int math = 55;
        System.out.println((korean + english + math) / 3);
    }

    public static void question2() {
        int n = 13;
        boolean check = 1 == n % 2;
        System.out.println(check); // true=홀수, false=짝수
    }

    public static void question3() {
        String pin = "881120-1068234";
        System.out.println(pin.substring(0, 2) + "00" + pin.substring(2, 6));

    }

    public static void question4() {
        String pin = "881120-1068234";
        System.out.println(pin.charAt(0));
    }

    public static void question5() {
        String a = "a:b:c:d";
        System.out.println(a.replace(":", "#"));

    }

    public static void question6() {
        ArrayList<Integer> myList = new ArrayList<>(Arrays.asList(1, 3, 5, 4, 2));
        System.out.println(myList);
        myList.sort(Comparator.reverseOrder());
        System.out.println(myList);
    }

    public static void question7() {
        ArrayList<String> myList = new ArrayList<>(Arrays.asList("Life", "is", "too", "short"));
        System.out.println(myList); // [Life, is, too, short] 출력
        String result = String.join(" ", myList);
        System.out.println(result);
    }

    public static void question8() {
        HashMap<String, Integer> grade = new HashMap<>();
        grade.put("A", 90);
        grade.put("B", 80);
        grade.put("C", 70);

        System.out.println(grade.remove("B"));
        System.out.println(grade);
    }

    public static void question9() {
        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5));
        System.out.println(numbers);
        HashSet<Integer> numbers_set = new HashSet<>(numbers);
        System.out.println(numbers_set);
    }

    enum CoffeType {
        AMERICANO,
        ICE_AMERICANO,
        CAFE_LATTE
    };

    public static void printCofficePrice(CoffeType type) {
        HashMap<CoffeType, Integer> priceMap = new HashMap<>();
        priceMap.put(CoffeType.AMERICANO, 3000);
        priceMap.put(CoffeType.ICE_AMERICANO, 4000);
        priceMap.put(CoffeType.CAFE_LATTE, 5000);
        int price = priceMap.get(type);
        System.out.println(String.format("가격은 %d원 입니다.", price));
    }

    public static void question10() {
        printCofficePrice(CoffeType.AMERICANO);
    }
}