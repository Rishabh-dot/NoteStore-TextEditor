from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - NoteStore")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - NoteStore")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - NoteStore")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("NoteStore", "This Software is built and developed by Rishabh.")

if __name__ == "__main__":
    #Basic tkinter setup

    root = Tk()
    root.title("Untitled - NoteStore")
    
    root.geometry("844x540")

    #Adding TextArea

    TextArea = Text(root, font="Calibri 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    #Creating a menu bar

    MenuBar = Menu(root)

    #File menu Starts

    FileMenu = Menu(MenuBar, tearoff=0)

    #To open new file

    FileMenu.add_command(label="New", command=newFile)

    #To Open Already Existing File

    FileMenu.add_command(label="Open", command = openFile)

    #To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)

    #File Menu Ends

    #Edit Menu Starts

    EditMenu = Menu(MenuBar, tearoff=0)

    #To give a feature of cut, copy and paste

    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    #Edit Menu Ends

    #Help Menu Starts

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About NoteStore", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    #Help Menu Starts


    root.config(menu=MenuBar)

    #Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)



    root.mainloop()