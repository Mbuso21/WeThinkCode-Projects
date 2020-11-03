import robot
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os.path
import world.obstacles as obsta

class MyObstaclesTest(unittest.TestCase):

    maxDiff = None
    
    def test_obstacles_generated_is_a_list(self):

        self.assertIsInstance(obsta.obstacles, list)

    def test_obstacles_generated_list_has_box_coordinates(self):
        
        obsta.random.randint = lambda a,b:1
        self.assertEqual([[(1, 1), (5, 1), (5, 5), (1, 5)]], obsta.get_obstacles())


    def test_is_position_blocked_True(self):

        obsta.random.randint = lambda a, b: 1
        self.assertTrue(obsta.is_position_blocked(1, 1))

    def test_is_position_blocked_False (self):

        obsta.random.randint = lambda a, b: 1
        self.assertFalse(obsta.is_position_blocked(0, 0))

    @patch('sys.stdin', StringIO('Metros\nForward 1\nright\nforward 10\noff\n'))
    def test_if_is_path_blocked_blocks_the_robot(self):
        
        output = robot.capture_io()
        obsta.random.randint = lambda a, b: 1
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        self.assertIsInstance(obsta.is_path_blocked(1, 1, 1, 1), bool)

    
    

    
if __name__ == "__main__":
    unittest.main()

