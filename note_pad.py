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
        self.__thisTextArea.grid(sticky= N + E + S + W)
        # Open File
        self.__thisFileMenu.add_command(label='New', command=self.__newFile)
        # Open existing file
        self.__thisFileMenu.add_command(label='Open', command=self.__openFile)




    def run(self):
        # Run main App
        self.__root.mainloop()


# Run Notepad
notepad = Notepad(width=600, height=800)
notepad.run()
