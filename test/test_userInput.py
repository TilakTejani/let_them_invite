import unittest
import userInput
class test_UserInput(unittest.TestCase):
    def test_userinput(self):
        file_input = userInput.FileInputResults()
        userInput.FileInputDisplay(file_input)
        print("\n\n\n\n=================  File Input Taken ============")
        print(file_input.csv, file_input.pdf)


if __name__ == "__main__":
    unittest.main()