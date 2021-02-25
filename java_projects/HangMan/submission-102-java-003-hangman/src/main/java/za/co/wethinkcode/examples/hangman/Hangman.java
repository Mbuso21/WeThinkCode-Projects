package za.co.wethinkcode.examples.hangman;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Random;

// tag::hangman-class[]
public class Hangman {

    public static void main(String[] args) throws IOException {

        Player player = new Player();
        Answer wordToGuess = pickWord(player);
        Answer currentAnswer = start(wordToGuess);
        System.out.println(run(player, wordToGuess, currentAnswer));
    }
    private static List<String> getWords(Player player) throws IOException {

        System.out.println("Words file? [leave empty to use short_words.txt]");
        String fileName = player.getWordsFile();

        return Files.readAllLines(Path.of(fileName));
    }

    private static Answer pickWord(Player player) throws IOException{

        Random random = new Random();
        List<String> words = getWords(player);

        int randomIndex = random.nextInt(words.size());
        String randomWord = words.get(randomIndex).trim();
        return new Answer(randomWord);
    }

    private static Answer start(Answer wordToGuess) {
        Answer currentAnswer = wordToGuess.generateRandomHint();
        System.out.println("Guess the word: " + currentAnswer);
        return currentAnswer;
    }

    private static String run(Player player, Answer wordToGuess, Answer currentAnswer) {
        while (!currentAnswer.equals(wordToGuess)) {
            String guess = player.getGuess();
            if (player.wantsToQuit()) {
                System.out.println("Bye!");
                break;
            }

            char guessedLetter = guess.charAt(0);
            if (currentAnswer.isGoodGuess(wordToGuess, guessedLetter)) {
                currentAnswer = wordToGuess.getHint(currentAnswer, guess.charAt(0));
                System.out.println(currentAnswer);
            } else {
                player.lostChance();
                System.out.println("Wrong! Number of guesses left: " + player.getChances());
                if (player.hasNoChances()) {
                    return "Sorry, you are out of guesses. The word was: " + wordToGuess;
                }
            }
        }
        return  "That is correct! You escaped the noose .. this time.";

    }
}