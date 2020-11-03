import unittest
import world.text.world
from unittest.mock import patch
import sys
from io import StringIO
from test_base import run_unittests
import robot
from world import obstacles

class MyOwnTestCase(unittest.TestCase):

    def test_step1_toy4_if_world_module_exists(self):

        self.assertTrue('world' in sys.modules, "world module should be found")


    @patch('sys.stdin', StringIO('Metros\nForward 1\nright\nforward 10\noff\n'))
    def test_check_obstacles_finds_an_obstacles(self):
        
        output = robot.capture_io()
        obstacles.random.randint = lambda a, b: 1
        robot.robot_start()

        self.assertEqual('''What do you want to name your robot? Metros: Hello kiddo!
There are some obstacles:
- At position 1,1 (to 5,5)
Metros: What must I do next?  > Metros moved forward by 1 steps.
 > Metros now at position (0,1).
Metros: What must I do next?  > Metros turned right.
 > Metros now at position (0,1).
Metros: What must I do next?  > Metros: Sorry, there is an obstacle in the way.
 > Metros now at position (0,1).
Metros: What must I do next? Metros: Shutting down..\n''', output.getvalue())



if __name__ == "__main__":
    unittest.main()