from tkinter import *
import random
import MainMenu

class Help:
    def __init__(self,window):
        self.window = window
        self.window.configure(background="black")
        
        icon="a"
        maxHealth = "10"
        maxMana = "02"
        strength = "03"
        crit = "05%"
        archery = "05"
        dodge = "05%"
        title=Label(self.window, text = "Help",font=("ms serif",100,"bold"),bg= "gray2", fg = "red")
        title.grid(row = 0,column=0,columnspan=3, sticky = W)
        #CLASS
        archerB = Button(self.window,text ="Archer",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=7,command=self.archerP)
        archerB.grid(row = 1, sticky = NW)

        rogueB = Button(self.window,text ="Rogue",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=7,command=self.rogueP)
        rogueB.grid(row = 1,column = 1, sticky = NW)

        warriorB = Button(self.window,text ="Warrior", font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=7,command=self.warriorP)
        warriorB.grid(row = 1,column = 2, sticky = NW)

        mageB = Button(self.window,text ="Mage", font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=7,command=self.mageP)
        mageB.grid(row = 1,column = 3, sticky = NW)

        jackB = Button(self.window,text ="Jack",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=7,command=self.jackP)
        #jackB.bind("<Button-1>",jackP)
        #jackB.pack(fill = X)
        jackB.grid(row = 1,column = 4, sticky = NW)

        levelB = Button(self.window,text ="Level",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=7,command=self.levelP)
        levelB.grid(row = 1,column = 5, sticky = NW)

        itemB = Button(self.window,text ="Items",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=6,command=self.itemP)
        itemB.grid(row = 1,column = 6, sticky = NW)

    
        iconL=Label(self.window, text = "Icon:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=0, sticky = W)

        iconL=Label(self.window, text = icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=1, sticky = W)


        healthL=Label(self.window, text = "Health:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=0, sticky = W)

        manaL=Label(self.window, text = "Mana:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=0, sticky = W)
        
        strengthL=Label(self.window, text = "Strength:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 5,column=0, sticky = W)
        
        archeryL=Label(self.window, text = "Archery:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 6,column=0, sticky = W)

        critL=Label(self.window, text = "critical:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 7,column=0, sticky = W)

        dodgeL=Label(self.window, text = "Dodge:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=0, sticky = W)
        

        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 5,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 6,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 7,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=1, sticky = W)
        
        backB = Button(self.window,text ="Back",font = ("ms serif",40,"bold"), bg = "grey5", fg = "white",height=1, width=50,command=self.mainmenu)
        backB.grid(row = 9,column = 0,columnspan=999, sticky = W)
       
        
        self.window.mainloop()

    def clear(self):

        iconL=Label(self.window, text = "               ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=0, sticky = W)
        
        healthL=Label(self.window, text = "                ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=0, sticky = W)

        manaL=Label(self.window, text = "               ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=0, sticky = W)
        
        strengthL=Label(self.window, text = "                ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 5,column=0, sticky = W)
        
        archeryL=Label(self.window, text = "                 ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 6,column=0, sticky = W)

        critL=Label(self.window, text = "               ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 7,column=0, sticky = W)

        dodgeL=Label(self.window, text = "                 ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=0, sticky = W)

        iconL=Label(self.window, text = "                 ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=1, sticky = W)

        healthL=Label(self.window, text = "       ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=1, sticky = W)

        manaL=Label(self.window, text = "       ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=1, sticky = W)
        
        strengthL=Label(self.window, text = "      ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 5,column=1, sticky = W)
        
        archeryL=Label(self.window, text = "       ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 6,column=1, sticky = W)

        critL=Label(self.window, text = "        ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 7,column=1, sticky = W)

        dodgeL=Label(self.window, text = "        ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=1, sticky = W)

        dodgeL=Label(self.window, text = "       ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=1, sticky = W)


    def playerLabel(self):
        self.clear()

        iconL=Label(self.window, text = "Icon:    ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=0, sticky = W)

        healthL=Label(self.window, text = "Health:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=0, sticky = W)

        manaL=Label(self.window, text = "Mana:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=0, sticky = W)
        
        strengthL=Label(self.window, text = "Strength:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 5,column=0, sticky = W)
        
        archeryL=Label(self.window, text = "Archery:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 6,column=0, sticky = W)

        critL=Label(self.window, text = "critical:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 7,column=0, sticky = W)

        dodgeL=Label(self.window, text = "Dodge:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=0, sticky = W)
    
    def itemP(self):
        self.playerLabel()
        iconL=Label(self.window, text = "             ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=0, sticky = W)

        healthL=Label(self.window, text = "  ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=1, sticky = W)

        dodgeL=Label(self.window, text = "Arrows:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=0, sticky = W)

        
        healthL=Label(self.window, text = " !      ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=1, sticky = W)

        manaL=Label(self.window, text = " *      ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=1, sticky = W)
        
        strengthL=Label(self.window, text = " &     ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 5,column=1, sticky = W)
        
        archeryL=Label(self.window, text = " >      ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 6,column=1, sticky = W)

        critL=Label(self.window, text = " !       ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 7,column=1, sticky = W)

        dodgeL=Label(self.window, text = " ?       ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=1, sticky = W)

        dodgeL=Label(self.window, text = " ^      ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=1, sticky = W)

    def levelP(self):
        self.clear()

        iconL=Label(self.window, text = "Room:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=0, sticky = W)
        
        healthL=Label(self.window, text = "Corridor:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=0, sticky = W)

        manaL=Label(self.window, text = "Stairs:",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=0, sticky = W)       

        iconL=Label(self.window, text = " -   ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=1, sticky = W)
        
        healthL=Label(self.window, text = " #   ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=1, sticky = W)

        manaL=Label(self.window, text = " @   ",font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=1, sticky = W)
        

    def archerP(self):
        self.playerLabel()
        icon="a  "
        maxHealth = "10"
        maxMana = "02"
        strength = "03"
        crit = "05%"
        archery = "05"
        dodge = "05%"

        iconL=Label(self.window, text = icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=1, sticky = W)
        
        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 5,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 6,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 7,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=1, sticky = W)

           
    def rogueP(self,):
        self.playerLabel()
        icon="r  "
        maxHealth = "08"
        maxMana = "01"
        strength = "03"
        crit = "10%"
        archery = "01"
        dodge = "10%"

        iconL=Label(self.window, text = icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=1, sticky = W)

        
        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 5,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 6,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 7,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=1, sticky = W)  

    def warriorP(self,):
        self.playerLabel()
        icon="w "
        maxHealth = "15"
        maxMana = "02"
        strength = "06"
        crit = "02%"
        archery = "02"
        dodge = "02%"

        iconL=Label(self.window, text = icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=1, sticky = W)

        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 5,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 6,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 7,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=1, sticky = W)

    def mageP(self,):
        self.playerLabel()
        icon="m  "
        maxHealth = "10"
        maxMana = "10"
        strength = "01"
        crit = "05%"
        archery = "02"
        dodge = "05%"

        iconL=Label(self.window, text = icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=1, sticky = W)
        
        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 5,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 6,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 7,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=1, sticky = W)
      
    def jackP(self,):
        self.playerLabel()
        icon="j  "
        maxHealth = "12"
        maxMana = "05"
        strength = "05"
        crit = "05%"
        archery = "05"
        dodge = "05%"

        iconL=Label(self.window, text = icon,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        iconL.grid(row = 2,column=1, sticky = W)

        healthL=Label(self.window, text = maxHealth,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        healthL.grid(row = 3,column=1, sticky = W)

        manaL=Label(self.window, text = maxMana,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        manaL.grid(row = 4,column=1, sticky = W)
        
        strengthL=Label(self.window, text = strength,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        strengthL.grid(row = 5,column=1, sticky = W)
        
        archeryL=Label(self.window, text = archery,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        archeryL.grid(row = 6,column=1, sticky = W)

        critL=Label(self.window, text = crit,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        critL.grid(row = 7,column=1, sticky = W)

        dodgeL=Label(self.window, text = dodge,font=("ms serif",40,"bold"),bg= "gray2", fg = "white")
        dodgeL.grid(row = 8,column=1, sticky = W)
        
    def mainmenu(self):
        self.window.destroy()
        mainmenu=MainMenu.MainMenu(Tk())
        
        

    
if __name__=="__main__":
    helpM=Help(Tk())

