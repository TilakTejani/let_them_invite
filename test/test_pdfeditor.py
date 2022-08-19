import unittest
import sys
import os
from time import sleep

current = os.path.dirname(os.path.realpath(__file__))
 
parent = os.path.dirname(current)
 
sys.path.append(parent)

import pdfeditor



class Test_PdfEditor(unittest.TestCase):
    def test_pdfeditor(self):
        LOCS = [[1,1]] * 6
        pdfeditor.create_pdfs("demo.pdf", "list.csv", LOCS)
        print("something")



if __name__ == "__main__":
    unittest.main()