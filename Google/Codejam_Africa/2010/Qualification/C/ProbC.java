


import java.util.*;

public class ProbC {

    public static void main(String[] args) {

        HashMap<Character, String> prep = new HashMap<Character, String>();

        prep.put('a', "2");
        prep.put('b', "22");
        prep.put('c', "222");
        prep.put('d', "3");
        prep.put('e', "33");
        prep.put('f', "333");
        prep.put('g', "4");
        prep.put('h', "44");
        prep.put('i', "444");
        prep.put('j', "5");
        prep.put('k', "55");
        prep.put('l', "555");
        prep.put('m', "6");
        prep.put('n', "66");
        prep.put('o', "666");
        prep.put('p', "7");
        prep.put('q', "77");
        prep.put('r', "777");
        prep.put('s', "7777");
        prep.put('t', "8");
        prep.put('u', "88");
        prep.put('v', "888");
        prep.put('w', "9");
        prep.put('x', "99");
        prep.put('y', "999");
        prep.put('z', "9999");
        prep.put(' ', "0");

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.nextLine();

        for (int k = 0; k < N; k++) {

            String msg = sc.nextLine();

            String output = "";

            boolean first = true;

            for (char c : msg.toCharArray()) {

                String add = prep.get(c);

                if (!first) {
                    if (add.charAt(0) == output.charAt(output.length() - 1)) add = " " + add;
                } else {
                    first = false;
                }

                output += add;

            }

            System.out.println("Case #" + (k+1) + ": " + output);

        }


    }

}
