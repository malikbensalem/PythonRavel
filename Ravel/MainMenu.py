from tkinter import *
import Help
import ClassPicker
class MainMenu():
    def __init__(self,window):
        self.window=window
        self.window.configure(background="black")
        
        title = Label(self.window, text = "Ravel",font = ("ms serif",139,"bold"),bg= "gray2", fg = "red")
        title.grid(row = 0,column=0,columnspan=2, sticky = N)

        startGameB = Button(self.window,text ="New Game",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=3, width=49,command=self.classpicker)
        startGameB.grid(row = 1,column = 0,columnspan=2, sticky = W)
        
        helpB = Button(self.window,text ="Help", font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=2, width=49,command=self.helpP)
        helpB.grid(row = 2,column = 0, sticky = E)

        quitGameB = Button(self.window,text ="Quit Game",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=2, width=49,command=quit)
        quitGameB.grid(row = 3,column = 0,columnspan=2, sticky = W)
        self.window.mainloop()

    def helpP(self):
        self.window.destroy()
        Help.help=Help.Help(Tk())
        
    def classpicker(self):
        self.window.destroy()
        classPicker=ClassPicker.ClassPicker(Tk())

        
if __name__=="__main__":
    mainmenu=MainMenu(Tk())
