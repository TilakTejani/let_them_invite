from tkinter import *
from time import sleep

import userInput
import pdfeditor
import file_sender
import util

DIR_LIST=["img_src","edited_images","saved_pdfs"]

def file_inputs(INPUTS, root, statusLabel):

    statusLabel.config(text = "..Taking input Files")
    fileInputFrame = LabelFrame(root, text = "File Input Frame")
    fileInputFrame.pack(padx = 5, pady = 10)
    
    userInput.FileInputDisplay(fileInputFrame, INPUTS)
    statusLabel.config(text = ".. Input Files taken")


def loc_inputs(INPUTS, statusLabel):
    statusLabel.config(text = ".. taking location inputs")
    IMGS = pdfeditor.pdftopil(INPUTS.pdf)
    util.create_dirs("img_src")
    pdfeditor.save_pil_images(IMGS)
    INPUTS.locs = userInput.LocInputs(len(IMGS))
    statusLabel.config(text = "..Locations Taken")

def generate_pdfs(INPUTS, statusLabel):
    start_time = util.get_time()
    statusLabel.config(text = ".. generating Pdfs")
    pdfeditor.create_pdfs(INPUTS.pdf, INPUTS.csv, INPUTS.locs)
    statusLabel.config(text = f"..pdf generated\nTime taken: {util.get_time() - start_time}")

def connect_sel(INPUTS, root, statusLabel):
    start_time = util.get_time()
    statusLabel.config(text = "..Connecting Whatsapp")
    INPUTS.driver = file_sender.create_driver()
    file_sender.connect_whatsapp(INPUTS.driver)
    statusLabel.config(text = f"..Whatsapp Connected \nTime taken: {util.get_time() - start_time}")


def send_files(INPUTS, root, statusLabel):
    start_time = util.get_time()
    LogWindow = Tk()
    LogWindow.title("Log Window")
    LogWindow.geometry("500x500")
    txt = Text(LogWindow)
    txt.insert(INSERT, "Logs:")
    txt.pack(padx = 5, pady = 5)
    statusLabel.config(text = "..sending files")
    file_sender.send_files(INPUTS.csv, INPUTS.driver, txt)
    LogWindow.mainloop()
    statusLabel.config(text = f"..files sent from {INPUTS.csv}.\nTime taken: {util.get_time() - start_time}")


def clear_all(status_label):
    status_label.config(text = "..Removing Directories")
    for dir in DIR_LIST:
        util.rm_dir(dir)



def main():
    INPUTS = userInput.InputResults()
    
    root = Tk("main")
    root.title("main")    
    root.geometry("400x500")
    
    mainFrame = LabelFrame(root, text = "Main Frame")
    mainFrame.pack(padx = 5, pady = 5)
    
    statusFrame = LabelFrame(root, text = "Status Frame")
    statusFrame.pack(padx= 5 ,pady= 5)
    
    statusLabel= Label(statusFrame, text = "")
    statusLabel.pack()

    btn1 = Button(mainFrame, text = "File Inputs", command= lambda:file_inputs(INPUTS, root, statusLabel))
    btn2 = Button(mainFrame, text = "Location Inputs", command = lambda:loc_inputs(INPUTS, statusLabel))
    btn3 = Button(mainFrame, text = "Generate Pdfs", command = lambda:generate_pdfs(INPUTS, statusLabel))
    btn4 = Button(mainFrame, text = "Connect Whatsapp", command = lambda:connect_sel(INPUTS, root, statusLabel))
    btn5 = Button(mainFrame, text = "Send Files", command = lambda:send_files(INPUTS, root, statusLabel))
    btn1.pack(padx = 5, pady = 5)
    btn2.pack(padx = 5, pady = 5)
    btn3.pack(padx = 5, pady = 5)
    btn4.pack(padx = 5, pady = 5)
    btn5.pack(padx = 5, pady = 5)
    Button(mainFrame, text = "Delete All Temp Data" , command = lambda:clear_all(statusLabel)).pack(padx = 5, pady = 5)

    mainloop()
    

if __name__ == "__main__":
    main()