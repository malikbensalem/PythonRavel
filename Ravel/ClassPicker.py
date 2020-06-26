from tkinter import *
import random
import MainMenu
import r6

class ClassPicker:
    def __init__(self,window):
        self.window = window
        self.window.configure(background="black")
        title = Label(self.window, text = "Pick Your Class",font = ("ms serif",50,"bold"),bg= "gray2", fg = "red")
        title.grid(row = 0,column=0,columnspan=5, sticky = W)
        self.icon="a"
        maxHealth = "10"
        maxMana = "02"
        strength = "03"
        crit = "05%"
        archery = "05"
        dodge = "05%"
        
        #CLASS
        archerB = Button(self.window,text ="Archer",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=10,command=self.archerP)
        archerB.grid(row = 2, sticky = NW)

        rogueB = Button(self.window,text ="Rogue",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=10,command=self.rogueP)
        rogueB.grid(row = 2,column = 1, sticky = NW)

        warriorB = Button(self.window,text ="Warrior", font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=10,command=self.warriorP)
        warriorB.grid(row = 2,column = 2, sticky = NW)

        mageB = Button(self.window,text ="Mage", font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=10,command=self.mageP)
        mageB.grid(row = 2,column = 3, sticky = NW)

        jackB = Button(self.window,text ="Jack",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=9,command=self.jackP)
        jackB.grid(row = 2,column = 4, sticky = NW)



        self.iconL=Label(self.window, text = "Icon:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        self.iconL.grid(row = 3,column=0, sticky = W)

        self.iconL=Label(self.window, text = self.icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        self.iconL.grid(row = 3,column=1, sticky = W)


        healthL=Label(self.window, text = "Health:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 4,column=0, sticky = W)

        manaL=Label(self.window, text = "Mana:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 5,column=0, sticky = W)
        
        strengthL=Label(self.window, text = "Strength:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 6,column=0, sticky = W)
        
        archeryL=Label(self.window, text = "Archery:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 7,column=0, sticky = W)

        critL=Label(self.window, text = "critical:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 8,column=0, sticky = W)

        dodgeL=Label(self.window, text = "Dodge:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 9,column=0, sticky = W)
        

        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 4,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 5,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 6,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 7,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 8,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 9,column=1, sticky = W)
        
        backB = Button(self.window,text ="Back",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=21,command=self.mainmenu)
        backB.grid(row = 10,column = 0,columnspan=3, sticky = W)


        startB = Button(self.window,text ="Start",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=30,command=self.start)
        startB.grid(row = 10,column = 2,columnspan=999, sticky = W)
        
        self.window.mainloop()
        
    def start(self):
        self.window.destroy()
        r6.play(self.icon)   
        

    def clearI(self):
        self.iconL=Label(self.window, text = "     ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        self.iconL.grid(row = 3,column=1, sticky = W)

    def archerP(self):
        self.clearI()
        self.icon="a"
        maxHealth = "10"
        maxMana = "02"
        strength = "03"
        crit = "05"
        archery = "05"
        dodge = "05"

        self.iconL=Label(self.window, text = self.icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        self.iconL.grid(row = 3,column=1, sticky = W)
        
        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 4,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 5,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 6,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 7,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 8,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 9,column=1, sticky = W)
           
    def rogueP(self,):
        self.clearI()
        self.icon="r"
        maxHealth = "08"
        maxMana = "01"
        strength = "03"
        crit = "10"
        archery = "01"
        dodge = "10"

        self.iconL=Label(self.window, text = self.icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        self.iconL.grid(row = 3,column=1, sticky = W)
  
        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 4,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 5,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 6,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 7,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 8,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 9,column=1, sticky = W)  

    def warriorP(self,):
        self.clearI()
        self.icon="w"
        maxHealth = "15"
        maxMana = "02"
        strength = "06"
        crit = "02"
        archery = "02"
        dodge = "02"

        self.iconL=Label(self.window, text = self.icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        self.iconL.grid(row = 3,column=1, sticky = W)

        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 4,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 5,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 6,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 7,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 8,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 9,column=1, sticky = W)

    def mageP(self,):
        self.clearI()
        self.icon="m"
        maxHealth = "10"
        maxMana = "10"
        strength = "01"
        crit = "05"
        archery = "02"
        dodge = "05"

        self.iconL=Label(self.window, text = self.icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        self.iconL.grid(row = 3,column=1, sticky = W)
        
        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 4,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 5,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 6,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 7,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 8,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 9,column=1, sticky = W)
      
    def jackP(self,):
        self.clearI()
        self.icon="j"
        maxHealth = "12"
        maxMana = "05"
        strength = "05"
        crit = "05"
        archery = "05"
        dodge = "05"

        self.iconL=Label(self.window, text = self.icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        self.iconL.grid(row = 3,column=1, sticky = W)

        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 4,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 5,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 6,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 7,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 8,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 9,column=1, sticky = W)
        
    def mainmenu(self):
        self.window.destroy()
        mainmenu=MainMenu.MainMenu(Tk())        
    

    
if __name__=="__main__":
    classPicker=ClassPicker(Tk())

