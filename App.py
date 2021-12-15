from tkinter import *
from tkinter import ttk
from Options import Options



class App:
    App_modules = []
    destructionRegister = []
    processRegister = []

    tkRoot = None
    RootFrame = None
    is_loaded = False

    appOptions = Options()

    def __init__(self):
        print("mainclassin")
        if self.is_loaded is False:
            self.tkRoot = Tk()
            self.frame = ttk.Frame(self.tkRoot, padding=10)
            self.frame.grid()
            self.is_loaded = True
            self.tkRoot.protocol("WM_DELETE_WINDOW", self.on_close)
            self.load_modules()
            self.tkRoot.mainloop()


    def load_modules(self):
        for i in self.App_modules:
            i()
        for i in self.processRegister:
            i()


    def on_close(self):
        #Sync and close the shelf upon window termination
        self.appOptions.shelf.close()
        for cls in self.destructionRegister:
            cls()
        self.tkRoot.destroy()


    #Use a "module registry to load application extensions into itself, without needing to add the new classes to the main application
    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.App_modules.append(cls)
