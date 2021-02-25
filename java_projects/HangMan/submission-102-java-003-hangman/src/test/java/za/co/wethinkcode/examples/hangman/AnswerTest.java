package za.co.wethinkcode.examples.hangman;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;


class AnswerTest {

    @Test
    public void shouldConvertItselfToAString() {
        Answer answer = new Answer("tree");
        assertEquals("tree", answer.toString());
    }
    @Test
    public void checkEquality() {
        Answer a = new Answer("cat");
        Answer b = new Answer("cat");
        assertTrue(a.equals(b));
    }

    @Test
    public void giveAHint() {
        Answer solution = new Answer("test");
        Answer lastAnswer = new Answer("t__t");
        Answer hint = solution.getHint(lastAnswer, 'e');
        assertEquals(new Answer("te_t"), hint);
    }

    @Test
    public void hasLetter() {
        Answer answer = new Answer("test");
        assertTrue(answer.hasLetter('t'));
        assertFalse(answer.hasLetter('x'));
    }

    @Test
    public void generateRandomHint() {
        Answer wordToGuess = new Answer("test");
        Answer hint = wordToGuess.generateRandomHint();

        for (int i = 0; i < hint.toString().length(); i++) {
            char hintLetter = hint.toString().charAt(i);
            char expectedLetter = wordToGuess.toString().charAt(i);
            if (hintLetter != '_') {
                assertEquals(expectedLetter, hintLetter);
            }
        }
    }
    @Test
    public void checkGuess() {
        Answer wordToGuess = new Answer("test");
        Answer currentAnswer = new Answer("t__t");
        assertTrue(currentAnswer.isGoodGuess(wordToGuess,'e'));
        assertFalse(currentAnswer.isGoodGuess(wordToGuess,'x'));
        assertFalse(currentAnswer.isGoodGuess(wordToGuess,'t'));
    }
}