import unittest
import sys
import os
from time import sleep

current = os.path.dirname(os.path.realpath(__file__))
 
parent = os.path.dirname(current)
 
sys.path.append(parent)

import connection

class Test_Connection(unittest.TestCase):
    def test_connection(self):
       driver = connection.create_driver()
       driver.get("https://web.whatsapp.com")
       sleep(25)

if __name__ == "__main__":
    unittest.main()