# Packages need to execute script
import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    __root = Tk()
    __thisWidth = 600
    __thisHeight = 800
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisEditMenu, tearoff=0)
    # Add Scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):
        # Set icon
        try:
            self.__root.wm_iconbitmap('Notepad.ico')
        except:
            pass
        # Set Window Size default (600x800)
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass
        # Set the window text
        self.__root.title('Untitled - Notepad')
        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        # Left alignment
        left = (screenWidth / 2) - (self.__thisWidth / 2)
        # Right alignment
        top = (screenHeight / 2) - (self.__thisHeight / 2)
        # Top alignment
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))
        # Make dynamic text area
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        # Add controls
        self.__thisTextArea.grid(sticky=N + E + S + W)
        # Open File
        self.__thisFileMenu.add_command(label='New', command=self.__newFile)
        # Open existing file
        self.__thisFileMenu.add_command(label='Open', command=self.__openFile)
        # Save File
        self.__thisFileMenu.add_command(label='Save', command=self.__saveFile)
        # Create a lne in dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label='Exit')
        self.__thisMenuBar.add_cascade(label='File', menu=self.__thisFileMenu)
        # Add cut feature
        self.__thisEditMenu.add_command(label='Cut', command=self.__cut)
        # Add copy feature
        self.__thisEditMenu.add_command(label='Copy', command=self.__copy)
        # Add paste feature
        self.__thisEditMenu.add_command(label='Paste', command=self.__paste)
        # Add edit feature
        self.__thisMenuBar.add_cascade(label='Edit', menu=self.__thisEditMenu)
        # Add description of Notepad
        self.__thisHelpMenu.add_command(label='About Notepad', command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label='Help', menu=self.__thisHelpMenu)
        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        # Scroll bar automatically adjust
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    # Quit Notepad
    def __quitApplication(self):
        self.__root.destroy()

    # About Notepad info
    def __showAbout(self):
        showinfo('Notepad Text Editor', 'Text editor for .txt files \n Author: Wade Chriestenson')

    # Open File
    def __openFile(self):
        self.__file = askopenfilename(defaulttextextension='.txt',
                                      filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
        if self.__file == '':
            # No file to open
            self.__file = None
        else:
            # Try to open file
            # Set window title
            self.__root.title(os.path.basename(self.__file) + ' - Notepad')
            self.__thisTextArea.delete(1.0, END)
            file = open(self.__file, 'r')
            self.__thisTextArea.insert(1.0, file.read())
            file.close()

    # Create new file
    def __newFile(self):
        self.__root.title('Untitled - Notepad')
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    # Save File
    def __saveFile(self):
        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                            filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
            if self.__file == '':
                self.__file = None
            else:
                # Try to save file
                file = open(self.__file, 'w')
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                # Change window title
                self.__root.title(os.path.basename(self.__file) + ' - Notepad')
        else:
            file = open(self.__file, 'w')
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate('<<Cut>>')

    def __copy(self):
        self.__thisTextArea.event_generate('<<Copy>>')

    def __paste(self):
        self.__thisTextArea.event_generate('<<Paste>>>')

    def run(self):
        # Run main App
        self.__root.mainloop()


# Run Notepad
notepad = Notepad(width=600, height=800)
notepad.run()
