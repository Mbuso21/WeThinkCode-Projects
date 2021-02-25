package za.co.wethinkcode.examples.hangman;

import java.util.*;

public class Answer {

    private String value;

    public Answer(String value) {
        this.value = value;
    }
    @Override
    public String toString() {
        return this.value;
    }

    @Override
    public boolean equals(Object obj) {
        Answer otherAnswer = (Answer) obj;
        return this.value.equalsIgnoreCase(otherAnswer.toString());
    }

    public Answer getHint(Answer guessedAnswer, char guessedLetter) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < this.value.length(); i++) {
            if (guessedLetter == this.value.charAt(i)) {
                result.append(guessedLetter);
            } else {
                result.append(guessedAnswer.toString().charAt(i));
            }
        }
        return new Answer(result.toString());
    }

    public boolean hasLetter(char letter) {
        return this.value.indexOf(letter) >= 0;
    }

    public Answer generateRandomHint() {
        Random random = new Random();
        int randomIndex = random.nextInt(this.value.length() - 1);

        String noLetters = "_".repeat(this.value.length());
        return this.getHint( new Answer(noLetters),
                this.value.charAt(randomIndex));
    }
    public boolean isGoodGuess(Answer wordToGuess, char letter) {
            return wordToGuess.hasLetter(letter) && !this.hasLetter(letter);
    }
}
