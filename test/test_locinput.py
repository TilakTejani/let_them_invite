from lib2to3.pgen2.tokenize import untokenize
import unittest

import sys
import os
from time import sleep

current = os.path.dirname(os.path.realpath(__file__))
 
parent = os.path.dirname(current)
 
sys.path.append(parent)

import main
from tkinter import *

class Test_LocInput(unittest.TestCase):
    def test_locInput(self):

        main.loc_inputs( "demo.pdf")
        


if __name__ == "__main__":
    unittest.main()