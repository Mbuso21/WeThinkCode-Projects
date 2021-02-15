package za.co.wethinkcode.lms.test;

import org.junit.jupiter.api.Test;
import za.co.wethinkcode.fizzbuzz.FizzBuzz;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class FizzBuzzSolutionTest {
    // tag::first-test[]
    @Test
    public void notDivisibleBy3or5() {             // <1>
        FizzBuzz fizzBuzz = new FizzBuzz();        // <2>
        String result = fizzBuzz.checkNumber(13);  // <3>
        assertEquals("13", result);        // <4>
    }
    // end::first-test[]

    @Test
    public void divisibleBy3() {
        FizzBuzz fizzBuzz = new FizzBuzz();
        String result = fizzBuzz.checkNumber(9);
        assertEquals("Fizz", result);
    }

    @Test
    public void divisibleBy5() {
        FizzBuzz fizzBuzz = new FizzBuzz();
        String result = fizzBuzz.checkNumber(10);
        assertEquals("Buzz", result);
    }

    @Test void divisibleBy3And5() {
        FizzBuzz fizzBuzz = new FizzBuzz();
        String result = fizzBuzz.checkNumber(15);
        assertEquals("FizzBuzz", result);
    }

    @Test
    public void generateUpTo15() {
        FizzBuzz fizzBuzz = new FizzBuzz();
        String result = fizzBuzz.countTo(15);
        assertEquals("[1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz]", result);
    }
}
