import robot
import unittest
from unittest.mock import patch
from io import StringIO
import sys

class MyTestCase(unittest.TestCase):

    maxDiff = None

    @patch('sys.stdin', StringIO('Metros\n'))
    def test_step1_get_robot_name(self):
        
        text_capture = robot.capture_io()
        robot.get_robot_name()

        self.assertEqual('What do you want to name your robot? ' ,text_capture.getvalue())

    
    @patch('sys.stdin', StringIO('Metros\nStand\noFf'))
    def test_step2_get_robot_command(self):

        text_capture = robot.capture_io()
        robot.robot_start()

        self.assertEqual('''What do you want to name your robot? Metros: Hello kiddo!\nMetros: What must I do next? Metros: Sorry, I did not understand 'Stand'.\nMetros: What must I do next? Metros: Shutting down..\n''',text_capture.getvalue())


    @patch('sys.stdin', StringIO('help\n'))
    def test_step3_help(self):

        self.assertEqual((True, '''I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replay previous commands
REPLAY SILENT - replays previous commands with no steps\n'''), robot.do_help())

    @patch('sys.stdin', StringIO('HAL\nforward 10\noff\n'))
    def test_step5_fwd10_then_off(self):

        text_capture = StringIO()
        sys.stdout = text_capture
        robot.robot_start()

        self.assertEqual('What do you want to name your robot? HAL: Hello kiddo!\nHAL: What must I do next?  > HAL moved forward by 10 steps.\n > HAL now at position (0,10).\nHAL: What must I do next? HAL: Shutting down..\n',text_capture.getvalue())

    @patch('sys.stdin', StringIO('HAL\nFORWARD 10\noff\n'))
    def test_step6_fwd10_then_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()
        self.assertEqual('What do you want to name your robot? HAL: Hello kiddo!\nHAL: What must I do next?  > HAL moved forward by 10 steps.\n > HAL now at position (0,10).\nHAL: What must I do next? HAL: Shutting down..\n', text_capture.getvalue())
    

    @patch('sys.stdin', StringIO('HAL\nback 10\noff\n'))
    def test_step7_back10_then_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()
        self.assertEqual('What do you want to name your robot? HAL: Hello kiddo!\nHAL: What must I do next?  > HAL moved back by 10 steps.\n > HAL now at position (0,-10).\nHAL: What must I do next? HAL: Shutting down..\n', text_capture.getvalue())


    @patch('sys.stdin', StringIO('HAL\nright\noff\n'))
    def test_step8_right_then_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()
        self.assertEqual('What do you want to name your robot? HAL: Hello kiddo!\nHAL: What must I do next?  > HAL turned right.\n > HAL now at position (0,0).\nHAL: What must I do next? HAL: Shutting down..\n', text_capture.getvalue())

    @patch('sys.stdin', StringIO('HAL\nleft\nforward 10\noff\n'))
    def test_step9_left_then_fwd10_then_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()
        self.assertEqual('What do you want to name your robot? HAL: Hello kiddo!\nHAL: What must I do next?  > HAL turned left.\n > HAL now at position (0,0).\nHAL: What must I do next?  > HAL moved forward by 10 steps.\n > HAL now at position (-10,0).\nHAL: What must I do next? HAL: Shutting down..\n', text_capture.getvalue())

    @patch('sys.stdin', StringIO('HAL\nforward 201\nforward 10\noff\n'))
    def test_step10_fwd201_then_fwd10_then_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()
        self.assertEqual('What do you want to name your robot? HAL: Hello kiddo!\nHAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.\n > HAL now at position (0,0).\nHAL: What must I do next?  > HAL moved forward by 10 steps.\n > HAL now at position (0,10).\nHAL: What must I do next? HAL: Shutting down..\n', text_capture.getvalue())

    @patch('sys.stdin', StringIO('HAL\nleft\nforward 101\noff\n'))
    def test_step10_left_then_fwd101_then_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()
        
        self.assertEqual('What do you want to name your robot? HAL: Hello kiddo!\nHAL: What must I do next?  > HAL turned left.\n > HAL now at position (0,0).\nHAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.\n > HAL now at position (0,0).\nHAL: What must I do next? HAL: Shutting down..\n',text_capture.getvalue())

    @patch('sys.stdin', StringIO('HAL\nsprint 5\noff\n'))
    def test_step11_sprint5_then_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()

        self.assertEqual('What do you want to name your robot? HAL: Hello kiddo!\nHAL: What must I do next?  > HAL moved forward by 5 steps.\n > HAL moved forward by 4 steps.\n > HAL moved forward by 3 steps.\n > HAL moved forward by 2 steps.\n > HAL moved forward by 1 steps.\n > HAL now at position (0,15).\nHAL: What must I do next? HAL: Shutting down..\n', text_capture.getvalue())

    
    def test_step1_toy3_history_is_list(self):
        
        self.assertIsInstance(robot.command_history('forward 10', []), list)


    def test_step1_toy3_history_commands_saved_then_off(self):

        history_list = []
        self.assertEqual(['forward 10'],robot.command_history('forward 10', history_list))

    def test_step2_toy3_replay_command_removes_help_from_history_off(self):
        history_list = []
        self.assertEqual([], robot.command_history('help',history_list))

    
    @patch('sys.stdin', StringIO('HAL\nforward 10\nforward 5\nreplay\noff\n'))
    def test_step2_toy3_replay_command_displays_replayed_commands_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,25).
 > HAL moved forward by 5 steps.
 > HAL now at position (0,30).
 > HAL replayed 2 commands.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..\n""", text_capture.getvalue())

    @patch('sys.stdin', StringIO('HAL\nforward 10\nreplay silent\noff\n'))
    def test_step3_toy3_replay_silent_command_then_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()

        self.assertEqual('''What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL replayed 1 commands silently.
 > HAL now at position (0,20).
HAL: What must I do next? HAL: Shutting down..\n''', text_capture.getvalue())


    @patch('sys.stdin', StringIO('HAL\nforward 10\nforward 5\nreplay reversed\noff\n'))
    def test_step4_toy3_replay_reversed_then_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()

        self.assertEqual('''What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,20).
 > HAL moved forward by 10 steps.
 > HAL now at position (0,30).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..\n''', text_capture.getvalue())
        

    @patch('sys.stdin', StringIO('HAL\nforward 10\nforward 5\nREPLAY REVERSED\noff\n'))
    def test_step4_toy3_replay_reversed_UPPERCASE_then_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()

        self.assertEqual('''What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,20).
 > HAL moved forward by 10 steps.
 > HAL now at position (0,30).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..\n''', text_capture.getvalue())

    @patch('sys.stdin', StringIO('HAL\nforward 10\nforward 5\nreplay reversed silent\noff\n'))
    def test_step5_toy3_replay_silent_reversed_off(self):

        text_capture = robot.capture_io()
        robot.robot_start()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL replayed 2 commands in reverse silently.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..\n""", text_capture.getvalue())
    
    @patch('sys.stdin', StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 2\noff\n'))
    def test_step6_toy3_replay_range_last2(self):

        text_capture = robot.capture_io()
        robot.robot_start()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,8).
 > HAL moved forward by 1 steps.
 > HAL now at position (0,9).
 > HAL replayed 2 commands.
 > HAL now at position (0,9).
HAL: What must I do next? HAL: Shutting down..\n""", text_capture.getvalue())


    @patch('sys.stdin', StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 3-1\noff\n'))
    def test_step6_replay_range_3_to_1(self):

        text_capture = robot.capture_io()
        robot.robot_start()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,9).
 > HAL moved forward by 2 steps.
 > HAL now at position (0,11).
 > HAL replayed 2 commands.
 > HAL now at position (0,11).
HAL: What must I do next? HAL: Shutting down..\n""", text_capture.getvalue())

    

if __name__ == "__main__":
    unittest.main()