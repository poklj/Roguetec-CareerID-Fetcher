import URLUtilities
from App import App
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class ButtonModule(App):

    def __init__(self):
        print("subclassin")
        self.buttonFrame = ttk.Frame(self.RootFrame)
        self.buttonFrame.grid(column=0, row=1)

        ttk.Button(self.buttonFrame, text="Set Battletech Install location", command=self.prompt_installPath).grid(column=1, row=0)
        ttk.Button(self.buttonFrame, text="Join the Roguewar Discord", command=URLUtilities.open_roguewar).grid(column=2, row=0)

    def prompt_installPath(self):
        filepath = filedialog.askdirectory()
        if not self.appOptions.check_valid_rtInstall(filepath):
            messagebox.showerror("Error", "Could not find mod logfile in the given install directory, Are you sure you've installed Roguetech and are running / have run it at least once?")
        else:
            self.appOptions.shelf["bt_installDir"] = filepath
            print("set appoptions (bt_installDir) to " + filepath)
