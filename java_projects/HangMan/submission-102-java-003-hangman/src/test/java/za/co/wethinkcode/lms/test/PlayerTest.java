package za.co.wethinkcode.lms.test;

import org.junit.jupiter.api.Test;
import za.co.wethinkcode.examples.hangman.Player;

import java.io.ByteArrayInputStream;
import java.io.InputStream;

import static org.junit.jupiter.api.Assertions.*;

public class PlayerTest {

    // tag::test1[]
    @Test
    public void shouldStartWith5Chances() {                                                             //<1>
        Player player = new Player();                                                                   //<2>
        assertEquals(5, player.getChances());                                                           //<3>
    }
    // end::test1[]
    // tag::test2[]
    @Test
    public void canLoseAChance() {
        Player player = new Player();
        int chances = player.getChances();
        player.lostChance();                                                                            // <1>
        assertEquals(chances - 1, player.getChances());                                                 // <2>
    }
    // end::test2[]
    // tag::test3[]
    @Test
    public void noMoreChances() {
        Player player = new Player();
        int chances = player.getChances();
        for (int i = 0; i < chances; i++) {                                                             // <1>
            assertFalse(player.hasNoChances());                                                         // <2>
            player.lostChance();
        }
        assertTrue(player.hasNoChances());                                                              // <3>
    }
    // end::test3[]
    // tag::test4[]
    @Test
    public void cannotLoseChanceIfNoneAvailable() {
        Player player = new Player();
        int chances = player.getChances();
        for (int i = 0; i < chances + 1; i++) {                                                         // <1>
            player.lostChance();
        }
        assertEquals(0, player.getChances());                                                           // <2>
        // end::test4[]
    }
    // tag::test5[]
    @Test
    public void shouldProvideWordFile() {
        byte[] inputStreamData = "flowers.txt\n".getBytes();                                            // <1>
        InputStream inputStream = new ByteArrayInputStream(inputStreamData);                            // <2>

        Player player = new Player(inputStream);                                                        // <3>
        assertEquals("flowers.txt", player.getWordsFile());                                             // <4>
    }
    // end::test5[]
    // tag::test6[]
    @Test
    public void useDefaultWordFile() {
        byte[] inputStreamData = "\n".getBytes();                                                       // <1>
        InputStream inputStream = new ByteArrayInputStream(inputStreamData);

        Player player = new Player(inputStream);
        assertEquals("short_words.txt", player.getWordsFile());                                         // <2>
    }
    // end::test6[]
    // tag::test7[]
    @Test
    public void takeAGuess() {
        byte[] inputStreamData = "e\n".getBytes();                                                      // <1>
        InputStream inputStream = new ByteArrayInputStream(inputStreamData);

        Player player = new Player(inputStream);
        assertEquals("e", player.getGuess());                                                           // <2>
    }
    // end::test7[]
    // tag::test8[]
    @Test
    public void quitWithQuit() {
        byte[] inputStreamData = "quit\n".getBytes();                                                   // <1>
        InputStream inputStream = new ByteArrayInputStream(inputStreamData);

        Player player = new Player(inputStream);
        assertEquals("quit", player.getGuess());                                                        // <2>
        assertTrue(player.wantsToQuit());                                                               // <3>
    }
    // end::test8[]
    // tag::test9[]
    @Test
    public void quitWithExit() {
        byte[] inputStreamData = "exit\n".getBytes();                                                   // <1>
        InputStream inputStream = new ByteArrayInputStream(inputStreamData);

        Player player = new Player(inputStream);
        assertEquals("exit", player.getGuess());                                                        // <2>
        assertTrue(player.wantsToQuit());                                                               // <3>
    }
    // end::test9[]
}
