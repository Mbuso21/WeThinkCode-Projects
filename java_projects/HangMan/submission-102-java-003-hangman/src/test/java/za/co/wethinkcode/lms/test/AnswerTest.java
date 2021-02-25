package za.co.wethinkcode.lms.test;

import org.junit.jupiter.api.Test;
import za.co.wethinkcode.examples.hangman.Answer;

import static org.junit.jupiter.api.Assertions.*;

// tag::class[]
public class AnswerTest {
    // tag::test1[]
    @Test
    public void shouldConvertItselfToAString() {
        Answer answer = new Answer("tree");                                                             // <1>
        assertEquals("tree", answer.toString());                                                        // <2>
    }

    // end::test1[]
    // tag::test2[]
    @Test
    public void checkEquality() {
        Answer a = new Answer("cat");
        Answer b = new Answer("cat");
        assertTrue(a.equals(b));                                                                        //<1>
    }

    // end::test2[]
    // tag::test3[]
    @Test
    public void giveAHint() {
        Answer solution = new Answer("test");                                                           // <1>
        Answer lastAnswer = new Answer("t__t");                                                         // <2>
        Answer hint = solution.getHint(lastAnswer, 'e');                                                // <3>
        assertEquals(new Answer("te_t"), hint);
    }

    // end::test3[]
    // tag::test4[]
    @Test
    public void hasLetter() {
        Answer answer = new Answer("test");
        assertTrue(answer.hasLetter('t'));
        assertFalse(answer.hasLetter('x'));
    }

    // end::test4[]
    // tag::test5[]
    @Test
    public void generateRandomHint() {
        Answer wordToGuess = new Answer("test");
        Answer hint = wordToGuess.generateRandomHint();                                                 //<1>

        for (int i = 0; i < hint.toString().length(); i++) {                                            //<2>
            char hintLetter = hint.toString().charAt(i);
            char expectedLetter = wordToGuess.toString().charAt(i);
            if (hintLetter != '_') {
                assertEquals(expectedLetter, hintLetter);
            }
        }
    }
    // end::test5[]
    // tag::test6[]
    @Test
    public void checkGuess() {
        Answer wordToGuess = new Answer("test");
        Answer currentAnswer = new Answer("t__t");
        assertTrue(currentAnswer.isGoodGuess(wordToGuess,'e'));                                         //<1>
        assertFalse(currentAnswer.isGoodGuess(wordToGuess,'x'));                                        //<2>
        assertFalse(currentAnswer.isGoodGuess(wordToGuess,'t'));                                        //<3>
    }
    // end::test6[]
}
// end::class[]
