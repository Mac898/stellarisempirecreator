import tkinter as tk
import StellarisData.government as government

class StellarisEmpireCreator():
    def __init__(self, master):
        self.master = master
        master.title("Stellaris Empire Creator")
    def newGovernmentIco(self, data):
        govData = data
        self.button = Button(self.master, text=govData["name"])
        self.tooltip = Label(self.master, text=govData["tooltip"])
        

governmentFile = government.StellarisDataLibraryGov()


root = tk.Tk()
mainGUI = StellarisEmpireCreator(root)
mainGUI.newGovernmentIco(governmentFile.Democratic)
root.mainloop()


