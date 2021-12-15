import re
import tkinter

from App import App
from tkinter import ttk
from tkinter import Entry

class Fetcher(App):

    def __init__(self):
        self.fetcherFrame = ttk.Frame(self.RootFrame)
        self.fetcherFrame.grid(column=0, row=0)
        self.CareerID = tkinter.StringVar()
        self.idLabel = ttk.Label(self.fetcherFrame, text="CareerID")
        self.id_text = Entry(self.fetcherFrame, textvariable=self.CareerID, width=len(self.CareerID.get()))
        self.id_text.configure(state="readonly")
        self.idLabel.grid(column=0, columnspan=3, row=0)
        self.id_text.grid(column=0, row=1, columnspan=3)
        self.regex = re.compile("^.* Career ID Loaded: (.*)$")
        self.file = open(self.appOptions.get_log_path(), 'r')
        self.destructionRegister.append(self.close_file)
        self.readLogs()


    def close_file(self):
        self.file.close()

    def readLogs(self):
        self.file.seek(0,0)
        found = False
        for line in self.file.readlines():
            match = self.regex.match(line)
            if match:
                self.CareerID.set(match.group(1))
                found = True
        if not found:
            self.CareerID.set("NONE FOUND")
        self.fetcherFrame.after(100, self.readLogs)