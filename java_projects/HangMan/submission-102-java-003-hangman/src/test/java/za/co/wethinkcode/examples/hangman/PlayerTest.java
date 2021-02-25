package za.co.wethinkcode.examples.hangman;


import org.junit.jupiter.api.Test;
import za.co.wethinkcode.examples.hangman.Player;

//import static org.junit.Assert.assertFalse;
import java.io.ByteArrayInputStream;
import java.io.InputStream;

import static org.junit.jupiter.api.Assertions.*;

public class PlayerTest {

    @Test
    public void shouldStartWith5Chances() {
        Player player = new Player();
        assertEquals(5, player.getChances());
    }

    @Test
    public void canLoseAChance() {
        Player player = new Player();
        int chances = player.getChances();
        player.lostChance();
        assertEquals(chances - 1, player.getChances());
    }

    @Test
    public void noMoreChances() {
        Player player = new Player();
        int chances = player.getChances();
        for (int i = 0; i < chances; i++) {
            assertFalse(player.hasNoChances());
            player.lostChance();
        }
        assertTrue(player.hasNoChances());
    }

    @Test
    public void cannotLoseChanceIfNoneAvailable() {
        Player player = new Player();
        int chances = player.getChances();
        for (int i = 0; i < chances + 1; i++) {
            player.lostChance();
        }
        assertEquals(0, player.getChances());
    }

    @Test
    public void shouldProvideWordFile() {
        byte[] inputStreamData = "flowers.txt\n".getBytes();
        InputStream inputStream = new ByteArrayInputStream(inputStreamData);
        Player player = new Player(inputStream);
        assertEquals("flowers.txt", player.getWordsFile());
    }

    @Test
    public void useDefaultWordFile() {
        byte[] inputStreamData = "\n".getBytes();
        InputStream inputStream = new ByteArrayInputStream(inputStreamData);

        Player player = new Player(inputStream);
        assertEquals("short_words.txt", player.getWordsFile());
    }

    @Test
    public void takeAGuess() {
        byte[] inputStreamData = "e\n".getBytes();
        InputStream inputStream = new ByteArrayInputStream(inputStreamData);

        Player player = new Player(inputStream);
        assertEquals("e", player.getGuess());
    }

    @Test
    public void quitWithQuit() {
        byte[] inputStreamData = "quit\n".getBytes();
        InputStream inputStream = new ByteArrayInputStream(inputStreamData);

        Player player = new Player(inputStream);
        assertEquals("quit", player.getGuess());
        assertTrue(player.wantsToQuit());
    }

    @Test
    public void quitWithExit() {
        byte[] inputStreamData = "exit\n".getBytes();
        InputStream inputStream = new ByteArrayInputStream(inputStreamData);

        Player player = new Player(inputStream);
        assertEquals("exit", player.getGuess());
        assertTrue(player.wantsToQuit());
    }
}
