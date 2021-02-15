package za.co.wethinkcode.fizzbuzz;

import java.util.Arrays;

public class FizzBuzz {
    public static String checkNumber(int number) {
        boolean divisibleBy3 = number % 3 == 0;
        boolean divisibleBy5 = number % 5 == 0;

        if ( divisibleBy3 && divisibleBy5 ) {
            return "FizzBuzz";
        }
        if(divisibleBy3){return "Fizz";}
        if(divisibleBy5){return "Buzz";}

        return String.valueOf(number);
    }

    public static String countTo(int number) {
        String[] numbers = new String[number];
        int j = 1;
        for(int i = 0; i < number; i++) {
            numbers[i] = checkNumber(j);
            j++;
        }

        return Arrays.toString(numbers);
    }

    public static void main(String[] args) {

        System.out.println(countTo(50));
    }
}
