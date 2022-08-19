import unittest
import sys
import os
from time import sleep

current = os.path.dirname(os.path.realpath(__file__))
 
parent = os.path.dirname(current)
 
sys.path.append(parent)

import file_sender

class Test_File_Sender(unittest.TestCase):
    def test_file_sender(self):
        file_sender.send_files("list.csv")


if __name__ == "__main__":
    unittest.main()

