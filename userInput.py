from tkinter import *
from tkinter.filedialog import askopenfile
from time import sleep
  

# This function will be used to open
# file in read mode and only Python files
# will be opened
class InputResults():
    pdf = ""
    csv = ""
    locs = []
    def open_pdf_file(self):
        file = askopenfile(mode ='r', filetypes =[("pdf", f'*.pdf')])
        if file is not None:
            self.pdf = file.name

    def open_csv_file(self):
        file = askopenfile(mode ='r', filetypes =[("csv", f'*.csv')])
         
        if file is not None:
            self.csv = file.name

    def checkFile(self, root, lbl):
        if self.pdf == "" or self.csv == "":
            lbl.config(text = "!!!!Not valid Input!!!!")
        else:
            root.destroy()
    
    def checkLocation(self, root, locs, ent, lbl):
        for i, [a, b] in enumerate(ent):
            try:
                x = int(a.get())
                y = int(b.get())
                locs[i] = [x, y]
            except Exception as err:
                lbl.config(text = f"Invalid Input at {i + 1}", fg = 'red')
                return

        root.quit()
        root.destroy()

def FileInputDisplay( root, obj = InputResults()):
    lbl = Label(root, text = "", fg = 'red')
    btn1 = Button(root, text ='Select pdf file', command = lambda:obj.open_pdf_file())

    btn2 = Button(root, text ='Select csv file', command = lambda:obj.open_csv_file())

    btn3 = Button(root, text ='Go', command = lambda:obj.checkFile(root, lbl))

    btn1.grid(row = 2, column= 1)
    btn2.grid(row = 3, column= 1)
    btn3.grid(row = 4, column= 1)
    lbl.grid(row = 5, column = 1)

def LocInputs(no, obj = InputResults()):
    root = Tk()
    root.title("Location Inputs")
    
    locs = [[-1, -1]]* no
    ent = []
    for i in range(no):
        # root.destroy()
        frame = LabelFrame(root, text=f"Location For Page:{i + 1}")
        frame.grid(row = 1, column = i + 1)
        Label(frame, text=f"X loc: ").grid(row = 1, column = 1, padx = 10, pady = 10)
        entryx = Entry(frame, width = 20)
        entryx.grid(row = 1, column = 2,padx = 10, pady = 10)
        entryx.insert(0, "-1")
        Label(frame, text=f"Y loc: ").grid(row = 2, column = 1,padx = 10, pady = 10)
        entryy = Entry(frame, width = 20)
        entryy.grid(row = 2, column = 2,padx = 10, pady = 10)
        entryy.insert(0, "-1")
        
        ent.append([entryx, entryy])
    
    
    lbl = Label(root, text = "")
    lbl.grid(row = 3, columnspan=no)
    btn = Button(root, text = "Add loc", command=lambda:obj.checkLocation(root, locs, ent, lbl))
    btn.grid(row = 2, columnspan=no)
    root.mainloop()
    return locs



