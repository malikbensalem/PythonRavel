import random
import os
from msvcrt import getch
import ClassPicker
from tkinter import *

class Item:
    def __init__(self, type):
        self.x = -1#intialises coordinates not being on the map
        self.y = -1#same here
        self.type = type#intialised as an argument

    def setRandomLocation(self, roomWidth, roomHeight):#puts the item on the map
        self.x = random.randint(1, roomWidth-1)#sets x value in the room
        self.y = random.randint(1, roomHeight-1)#sets y value in the room

    def getPurpose(self):#tells the user what the potion does
        if self.type == "+":#healing
            return ("health potion: this is used to heal")
        if self.type == "*":#mana
            return ("mana potion: this is used to increse mana")
        if self.type == "!":#crit
            return ("crit potion: this is used to increase crit chance")
        if self.type == "?":#dodge
            return ("dodge potion: this is used for increase dodge chance")
        if self.type == "^":#arrows #not a potion
            return ("arrows: this is used to add arrows to your inventory")
        if self.type == ">":#achery
            return ("archery potion: this is used to increase archery")
        if self.type == "&":#strength
            return ("strength potion: this is used to increase strength")

class Room:
    def __init__(self, myLevel):

        self.hasExit = False#assumes there is no exit in the room
        self.exitx = -1#sets the exit as not exsisting 
        self.exity = -1#sets the exit as not exsisting

        self.myLevel = myLevel#takes 'mylevel' object as an argument 
        self.enemies = []#this will store all the 'enemy' objects inside this room
        self.items = []#this will store all the 'item' objects inside this room

        self.__setupRoom()#intially puts the room in

        self.__roomOverlaps()#makes sure the room doesnt overlap with any other rooms
            
        self.__insertDoor()#puts the doors inside the rooms
        self.__setRoomType()#decides what will be in room


    def addExit(self):#add access to the next level
        self.exitx=self.x#sets it as the rooms x#left
        self.exity=self.y#sets it as the rooms y #top #left corner
        self.exitx += random.randint(1, self.width-1)#random on x axis in room
        self.exity += random.randint(1, self.height-1)#random on y axis in room
        
        self.hasExit = True#tells room that the room has an exit

    def clearRoom(self):#clears the room of any object
        self.enemies = []#clears 'enemy' objects
        self.items = []#clears 'item' objects
        
    def __addEnemies(self):#adds the enemy object to the room####
        enemyAmount = random.randint(self.myLevel.level - 1, self.myLevel.level + 1)#decides how many 'enemy' objects will be inside the room
        enemyAmount = max([enemyAmount, 1])#if enemyAmount=0 then make it 1
        enemyAmount = min([enemyAmount, 11])#if enemyAmount >11 then make it 11

        for x in range(0, enemyAmount):#do this enemyAmount times
            self.enemies.append(Enemy(self.x+random.randint(1, self.width - 1), self.y+random.randint(1, self.height -1), self))#adds enemy object to self.enemies
            
    def getDoorLocation(self):#gets the location of the door###
        myDoor = [self.x + self.doorx, self.y+self.doory]#asigns the values to the variable
        return myDoor#return the variable myDoor


    def __insertDoor(self):#puts the door insdie the room###
        walls = ["up", "down", "left", "right"]#all the possible places the door can be

        wall = random.choice(walls)#selects one of the possible positions 
        if wall == "up":#if 'up' was picked
            self.doorx = random.randint(1, self.width-1)#pick a random x inside the room
            self.doory = 0#at the top of the room

        elif wall == "down":#if 'down' was picked
            self.doorx = random.randint(1, self.width-1)#pick a random x inside the room
            self.doory = self.height-1#at the bottom of the room

        elif wall == "left":#if 'left' was picked
            self.doorx = 0#at the left of the room
            self.doory = random.randint(1, self.height-1)#pick a random y inside the room
        else:#if 'right' was picked
            self.doorx = self.width-1#if 'right' was picked
            self.doory = random.randint(1, self.height-1)#pick a random y inside the room


    def __setupRoom(self):#puts the room onto the level####
        self.width = random.randint(7, 15)#sets the width of the room
        self.height = random.randint(4, 10)#sets the height of the room
        self.x = random.randint(1, self.myLevel.leftRight - 15)#sets where the room will be in the level's x
        self.xx = self.x + self.width#sets the far point of the room (x)
        self.y = random.randint(1, self.myLevel.upDown - 10)#sets where the room will be in the level's y
        self.yy = self.y + self.height#sets the far point of the room (y)


    def __addItem(self, itemType):#adds item to the room
        item = Item(itemType)#creates the item object
        item.x=self.x+random.randint(2,self.width-2)#sets the location inside the room
        item.y =self.y+random.randint(2,self.height-2)#sets the location inside the room
        self.items.append(item)#adds the item object to the item array
        print("added item:", itemType)#shows what type of item was added

    def pickUp(self,person):#allows the player/enemy(person) to pick up items
        for item in self.items:#for each item in the room
            if item.x == person.x and item.y == person.y:#if the person is on the same tile as the item
                if item.type == "+":#if its a health potion
                    person.healthP+=1#add the item to persons inventory
                elif item.type == "*":#if its a mana potion
                    person.manaP+=1#add the item to persons inventory
                elif item.type == "!":#if its a crit potion
                    person.critP+=1#add the item to persons inventory
                elif item.type == "?":#if its a dodge potion
                    person.dodgeP+=1#add the item to persons inventory
                elif item.type == "^":#if its a arrows
                    person.arrows+=1#add the item to persons inventory
                elif item.type == ">":#if its a archery potion
                    person.archeryP+=1#add the item to persons inventory
                elif item.type == "&":#if its a strength potion
                    person.strengthP+=1#add the item to persons inventory
                item.type="-"#turn the potion into a room tile
                person.score+=1#adds 1 to the persons score
            return True
        return False



    def __setRoomType(self):#tells the room what will be inside it####
        roomType = random.randint(1, 15)#decides the type 
        if roomType >= 5:#if the number is bigger than 4
            print("Put enemies in here")
            self.__addEnemies()#adds enemies into the room

        elif roomType == 4:#if the number = 4
            modType = random.randint(1, 14)
            if modType == 1:#if the number =1
                print("Add potions (critical)")
                self.__addItem("!")#add critical potion

            elif modType==2:#if the number =2
                print("add dodge potion")
                self.__addItem("?")#add dodge potion

            elif modType == 3:#if the number =3
                print("add archery potion")
                self.__addItem(">")#add archery
                
            elif modType==4:#if the number =4
                self.__addItem("&")#add strength potion
                print("add strength potion")

            else:#if the number is greater than 4
                self.__addItem("^")#add arrows
                print("add arrows")

        else:#if the number is less than 4
            itemType = random.randint(1, 3)
            if itemType==1:#if number =1
                print("add health potions")
                self.__addItem("+")#add a health potion

            else:#if it doesnt
                print("add magic potion")
                self.__addItem("*")#add mana potion


    def __roomOverlaps(self):
        #gap_between_rooms
        gap = 2# the gap between each room

        for anotherRoom in self.myLevel.rooms:#for each room
            for xcorner in [self.x, self.xx]:#for each x corner
                for ycorner in [self.y, self.yy]:#for each y corner
                    if xcorner >= anotherRoom.x -gap and xcorner <= anotherRoom.xx +gap and ycorner >= anotherRoom.y -gap and ycorner <= anotherRoom.yy + gap:#if room overlap with another rooms
                        self.__setupRoom()#rooms are overlapping
                        self.__roomOverlaps()

        return False#rooms are not overlapping 

    def addToLayout(self, levelLayout):#adds rooms to the level print
        for rowPosition in range(self.width):#for width
            for colPosition in range(self.height):#for height
                levelLayout[self.x + rowPosition][self.y + colPosition] = "-"#adds to the level's layout

        levelLayout[self.x + self.doorx][self.y + self.doory] = "-"#add door to layout

        for enemy in self.enemies:#for each enemy in the room
            levelLayout[enemy.x][enemy.y] = enemy.icon#adds the enemy to the layout

        for item in self.items:#for each item in the room
            levelLayout[item.x][item.y] = item.type#adds the item to the layout

        if self.hasExit:#if the room has an exit
            levelLayout[self.exitx][self.exity] = "@"#adds the exit to the layout


class Player:
    def __init__(self, icon:str,myLevel):
        self.icon = icon#how the player will look on the screen
        self.x = -1#intially not on the map
        self.y = -1#intially not on the map
        self.level = myLevel#takes the 'myLevel' object as an argument
        self.level.setPlayer(self)#allows the level to track the player
        self.SetInitialLocationInCurrentRoom()#puts the player on the map
        self.arrows = 4#how many arrows they start off with
        self.healthP = 1#how many health potions they start off with
        self.manaP = 3##how many mana potions they start off with
        self.strengthP=1#how many strength potions they start off with
        self.dodgeP=1#how many dodge potions they start off with
        self.archeryP=1#how many archery potions they start off with
        self.critP=1#how many archery potions they start off with
        self.RNG = random.randint(0, 100)#the random nummber generator 
        self.kills = 0#how many kills they have
        self.moves = 0#how many  moves they made
        self.score = 0#how much score they have
        self.health=1#make sure they dont die straight away
        self.maxHealth = 10 #the players max health
        self.mana = 0#the players actual mana
        self.maxMana = 0
        self.strength = 0#the players strength (__melee damage)
        self.crit = 0#the players crit chance 
        self.archery = 0#the players achery skill (arrow damage)
        self.dodge = 0#the players dodge chance
            
        
        if self.icon == "a":#if the player is an archer
            self.maxHealth = 10 #the players max health
            self.health = self.maxHealth #the players actual health
            self.maxMana = 2#the players max mana
            self.mana = self.maxMana#the players actual mana
            self.strength = 3#the players strength (__melee damage)
            self.crit = 5#the players crit chance 
            self.archery = 5#the players achery skill (arrow damage)
            self.dodge = 5#the players dodge chance
            #same for the rest

        elif self.icon == "m":#if the player is a mage
            self.maxHealth = 10
            self.health = self.maxHealth
            self.maxMana = 10
            self.mana = self.maxMana
            self.strength = 1
            self.crit = 5
            self.archery = 2
            self.dodge = 5

        elif self.icon == "w":#if the player is a warrior
            self.maxHealth = 15
            self.health = self.maxHealth
            self.maxMana = 2
            self.mana = self.maxMana
            self.strength = 6
            self.crit = 2
            self.archery = 2
            self.dodge = 2

        elif self.icon == "r":#if the player is a rogue
            self.maxHealth = 8
            self.health = self.maxHealth
            self.maxMana = 1
            self.mana = self.maxMana
            self.strength = 3
            self.crit = 10
            self.archery = 1
            self.dodge = 10

        elif self.icon == "j":#if the player is a jack (of all trades)
            self.maxHealth = 12
            self.health = self.maxHealth
            self.maxMana = 5
            self.mana = self.maxMana
            self.strength = 5
            self.crit = 5
            self.archery = 5
            self.dodge = 5

    def inventory(self):#this displays what the player's inventory
        print("Crit(Y):",self.critP,"| Arrows(Q):",self.arrows,"| Health Potions(P):",self.healthP,"| Mana Potions(O):",self.manaP,"| Strength Potions(I)",self.strengthP,"| Dodge Potions(T):",self.dodgeP,"| Archery Potions(U):",self.archeryP)

    def help(self):#gives helpful info to the player###
        print("move: Up(W),Down(S),Left(A),Right(D)")
        print("Use Potions: Health(P),Mana(O),Archery(U),Crit(Y),Dodge(T),Strength(I)")
        print("Attack: Arrows(Q),Mana(E)")
        
    def SetInitialLocationInCurrentRoom(self):#sets the players locaton
        currentRoom = self.level.getPlayerRoom()#gets the location of the first room
        self.x = random.randint(2, currentRoom.width-2)#sets a random place in the room (x)
        self.y = random.randint(2, currentRoom.height-2)#sets a random place in the room (y)
        self.x += currentRoom.x#puts the player inside the room
        self.y+= currentRoom.y#puts the player inside the room 

    def levelUp(self):#improves the player once they have reached the next level 
        if self.icon == "a":#if the player is an archer
            self.maxHealth  += (self.level.level // 6) #improves max health
            self.health = self.maxHealth#sets health to max health
            self.maxMana += (self.level.level // 10)#improves max mana
            self.mana = self.maxMana#sets mana to max mana
            self.strength += (self.level.level // 10)#improves strength
            self.crit += (self.level.level // 4)#improves crrit chance
            self.archery +=  (self.level.level // 2)#improves archery
            self.dodge += (self.level.level // 6)#improves dodge chance
        #same goes for the rest
        elif self.icon == "m":#if the player is a mage
            self.maxHealth += (self.level.level // 4)
            self.health = self.maxHealth
            self.maxMana += (self.level.level // 2)
            self.mana = self.maxMana
            self.strength += (self.level.level // 10)
            self.crit += (self.level.level // 8)
            self.archery += (self.level.level // 10)
            self.dodge += (self.level.level // 8)

        elif self.icon == "w":#if the player is a warrior
            self.maxHealth += (self.level.level // 2)
            self.health = self.maxHealth
            self.maxMana += (self.level.level // 10)
            self.mana = self.maxMana
            self.strength += (self.level.level // 2)
            self.crit += (self.level.level // 10)
            self.archery += (self.level.level // 10)
            self.dodge += (self.level.level // 10)

        elif self.icon == "r":#if the player is a rogue
            self.maxHealth += (self.level.level // 6)
            self.health = self.maxHealth
            self.maxMana += (self.level.level // 10)
            self.mana = self.maxMana
            self.strength += (self.level.level // 6)
            self.crit += (self.level.level // 3)
            self.archery += (self.level.level // 10)
            self.dodge += (self.level.level // 3)

        elif self.icon == "j":#if the player is a jack
            self.maxHealth += (self.level.level // 6)
            self.health = self.maxHealth
            self.maxMana += (self.level.level // 6)
            self.mana = self.maxMana
            self.strength += (self.level.level // 6)
            self.crit += (self.level.level // 6)
            self.archery += (self.level.level // 6)
            self.dodge += (self.level.level // 6)
    #__pHealth / __pMana are similar
    def __pHealth(self):#called when the player uses a health potion
        if self.healthP >=1 and self.health < self.maxHealth:#checks if the player has the potion and if there health is maxed
            self.health+=self.maxHealth//4#adds health
            self.healthP-=1#takes away the potion away
            if self.maxHealth < self.health:#if the players health is greater than max health
                self.health=self.maxHealth#set the health as max health
        elif self.healthP <1:#checks if they dont have potion
            print("I dont have that potion")
            chr(ord(getch()))#this is an single character input
            
        else:#if they have full health
            print("It's already full")
            chr(ord(getch()))
    
    def __pMana(self):#called when the player uses a mana potion
        if self.manaP >=1 and self.mana < self.maxMana:#checks if the player has the potion and if there mana is maxed
            self.mana+=self.maxMana//4#adds mana
            self.manaP-=1#takes away the potion away
            if self.maxMana < self.maxMana:#if mana is bigger than max mana
                self.mana=self.maxMana#make mana = max mana
        elif self.manaP <1:#if the player doesnt have any potions
            print("I dont have that potion")
            chr(ord(getch()))
        else:#if the player has full mana
            print("It's already full")
            chr(ord(getch()))
    #__pStrength / __pDodge/ __pArchery / __pCrit are similar
    def __pStrength(self):#called when the player uses a strength potion
        if self.strengthP>=1 and self.strength < 20 and self.dodge > 1:#checks if the player has the potion and if there strength stat is less 20 and there dodge stat is more than 1
            self.strengthP-=1#take away 1 strength potion
            self.strength+=1#add 1 to strength stat
            self.dodge-=1#takes away the potion away
        elif self.strengthP<1:#checks to make sure they have the potion
            print("I dont have that potion")
            chr(ord(getch()))
            
        else:#if there strength is above or equal to 20 or dodge stat 1 or less
            print("It would make me unstable")
            chr(ord(getch()))
            
            
    def __pDodge(self):#called when the player uses a dodge potion
        if self.dodgeP>=1 and self.dodge < 20 and self.maxHealth > 1:#checks if the player has the potion and if there dodge stat is less 20 and there max health stat is more than 1
            self.dodgeP-=1#takes away the potion away
            self.dodge+=1#adds 1 to dodge stat
            self.maxHealth-=1#takes away 1 from max health
            if self.maxHealth<self.health:#if max health is less than health
                self.health=self.maxHealth#set health to max health
        elif self.dodgeP<1:#make sure they have the potion
            print("I dont have that potion")
            chr(ord(getch()))
        else:#if there dodge is above or equal to 20 or maxhealth stat 1 or less
            print("It would make me unstable")
            chr(ord(getch()))

    def __pArchery(self):#called when the player uses a archery potion
        if self.archeryP>=1 and self.archery < 20 and self.strength > 1:
            self.archeryP-=1#takes away the potion away
            self.archery+=1#adds 1 to archery stat
            self.strength-=1#minus 1 to strength stat
        elif self.archeryP<1:#checks if they dont have the potion
            print("I dont have that potion")
            chr(ord(getch()))           
        else:#checks to if there archery stat is 20 or above or  strength stat is less than 2
            print("It would make me unstable")
            chr(ord(getch()))
            
    def __pCrit(self):#called when the player uses a crit potion
        if self.critP>=1 and self.crit < 20 and self.strength > 1:#checks if the player has the potion and if there crit stat is less 20 and there strength stat is more than 1
            self.critP-=1#takes away the potion away
            self.crit+=1#add 1 to crit stat
            self.strength-=1#take away from strength
        elif self.critP<1:#if the player doesnt have any potions left
            print("I dont have that potion")
            chr(ord(getch()))            
        else:#if they have the crit stat greater than 19 or strength is greater than 0
            print("It would make me unstable")
            chr(ord(getch()))

    def __fire(self,thing,stat):#called when the player uses a far ranged attack
        if thing > 0:#checks if thing (mana or arrows (depending on the arguement)) is more than 0
            for room in self.level.rooms:#for all the rooms
                for enemy in room.enemies:#for all the enemies 
                    if abs(self.x - enemy.x) + abs(self.y - enemy.y) <= 3 and enemy.health>1:#checks to make sure if the enemy is in range and the enemy is alive
                        self.RNG=random.randint(0,100)
                        if self.RNG <= enemy.dodge:#checks to see if the player missed
                            print("miss")
                            chr(ord(getch()))
                        elif self.RNG <= self.crit:#checks to see if the player got a critical hit
                            enemy.health-=stat * 3#stat (max mana or archery (depending on argument) timesed by 3 and taken away from enemy's health
                            print(enemy.name," hit! (",stat * 3,")")
                            chr(ord(getch()))
                        else:
                            enemy.health-=stat#stat takes away enemy health
                            print(enemy.name," hit. (",stat,")")
                            chr(ord(getch()))
                        if enemy.health<=0:#checks if enemy is dead
                            self.score+=2#gives player score
                        if thing == self.mana:#checks if thing is mana
                            self.mana-=1#takes away 1 mana
                        else:#checks if its arrows
                            self.arrows-=1#takes away 1 arrow
                

    def __melee(self):#called when the player moves up, down, left or right
        for room in self.level.rooms:#for all the rooms
            for enemy in room.enemies:#for all the enemies 
                if abs(self.x - enemy.x) + abs(self.y - enemy.y) <= 1 and enemy.health>=1:#checks to make sure if the enemy is in range and the enemy is alive
                    self.spaceFree=False#the space is not free
                    self.RNG=random.randint(0,100)
                    if self.RNG <= enemy.dodge:#checks if they
                        print("miss")
                        chr(ord(getch()))
                    elif self.RNG <= self.crit:#checks to see if the player got a critical hit
                        enemy.health-=self.strength * 3#strength timesed by 3 and taken away from enemy's health
                        print(enemy.name," hit! (",self.strength * 3,")")
                        chr(ord(getch()))
                    else:
                        enemy.health-=self.strength#strength takes away enemy health
                        print(enemy.name," hit. (",self.strength,")")
                        chr(ord(getch()))
                    if enemy.health<=0:#checks if player is dead
                        self.score+=2#gives player score
                    return
                else:#no enemies near by
                    self.spaceFree=True#the player can move there

    def performAction(self):
        print("_")
        action = chr(ord(getch())).upper()#the player's input for an action
        self.spaceFree = False#assuming that the player cannot move

        #"W","S","A","D" are similar
        if action == "W":#if "W" was pressed
            if self.level.move(self.x, self.y - 1,self) == True:#if th player moves into a valid space
                self.__melee()#if the player is within 1 tile of an enemy
            if self.spaceFree:#if nothing is in that space
                self.y -= 1#move
        
        elif action == "S":#if "S" was pressed
            if self.level.move(self.x, self.y + 1,self) == True:
                self.__melee()
            if self.spaceFree:
                self.y += 1

        elif action == "A":#if "A" was pressed
            if self.level.move(self.x-1, self.y,self) == True:
                self.__melee()
            if self.spaceFree:
                self.x -= 1

        elif action == "D":#if "D" was pressed
            if self.level.move(self.x+1, self.y,self) == True:
                self.__melee()
            if self.spaceFree:
                self.x += 1

        elif action =="E":#if "E" was pressed
            self.__fire(self.mana,self.maxMana)#__fire mana
        elif action =="Q":
            self.__fire(self.arrows,self.archery)#__fire arrows
            
        elif action=="P":#if "P" was pressed
            self.__pHealth()#use health potion
        elif action=="O":#if "O" was pressed
            self.__pMana()  #use mana potion
        elif action=="I":#if "I" was pressed
            self.__pStrength()#use strength potion
        elif action=="U":#if "U" was pressed
            self.__pArchery()#use archery potion
        elif action=="Y":#if "Y" was pressed
            self.__pCrit()#use crit potion
        elif action=="T":#if "T" was pressed
            self.__pDodge()#use dodge potion
        else:#if it was a non valid input
            print("I can't do that?")
            self.help()#show the possible buttons they can press
            self.performAction()#call the function again
        for room in self.level.rooms:#for each room
            room.pickUp(self)#if the player is on an item pick it up
            if room.pickUp == True:#if they picked up something
                self.score+=1#increase score by1 
                

class Enemy():
    def __init__(self, x, y, room):
        self.name = "Enemy "#the enemy's name
        self.score=0#there score
        self.x = x#there position (will be inside a room)
        self.y = y#there position (will be inside a room)
        self.health = 1#intial health
        self.level = room.myLevel.level#there enemy's level
        self.room = room#the room that they spawn in
        self.arrows = 0#how many arrows they have
        self.healthP = 0#how many health potions they have
        self.manaP = 0#how many mana potions they have
        self.dodgeP = 0#how many dodge potions they have
        self.critP = 0#how many crit potions they have
        self.strengthP = 0#how many strength potions they have
        self.archeryP = 0#how many archery potions they have
        self.myLevel = self.__getLevel()#the actual level

        self.ePick = ["A", "M", "R", "J", "W", "H"]#all the possible enemy types
        self.icon = random.choice(self.ePick)#the actual type of the enemy
        #the icon checks are similar
        if self.icon == "A":#if it is an archer
            self.name += "Archer"#the name is now "Enemy Archer"
            self.maxHealth = 5 + (self.level // 6)#max health is 5 + (enemy level ÷ 6)
            self.health = self.maxHealth#health = max health
            self.maxMana = 1#make max mana = 1
            self.mana = self.maxMana#make mana = max mana (1)
            self.strength = 2#make strength = 2
            self.crit = 3 + (self.level // 4)#crit is 3 + (enemy level ÷ 4)
            self.archery = 3 + (self.level // 2)#archery is 3 + (enemy level ÷ 3)
            self.dodge = 2 + (self.level // 6)#dodge is 2 + (enemy level ÷ 6)
            self.arrows += 10#add more arrows

        elif self.icon == "M":#if its a mage
            self.name += "Mage"
            self.maxHealth = 5 + (self.level // 4)
            self.health = self.maxHealth
            self.maxMana = 5 + (self.level // 2)
            self.mana = self.maxMana
            self.strength = 1
            self.crit = 2 + (self.level // 8)
            self.archery = 1
            self.dodge = 2 + (self.level // 8)

        elif self.icon == "W":#if its a warrior
            self.name += "Warrior"
            self.maxHealth = 7 + (self.level // 2)
            self.health = self.maxHealth
            self.maxMana = 1
            self.mana = self.maxMana
            self.strength = 4 + (self.level // 2)
            self.crit = 1
            self.archery = 1
            self.dodge = 1

        elif self.icon == "R":#if its a rogue
            self.name += "Rogue"
            self.maxHealth = 4 + (self.level // 6)
            self.health = self.maxHealth
            self.maxMana = 1
            self.mana = self.maxMana
            self.strength = 3 + (self.level // 6)
            self.crit = 5 + (self.level // 3)
            self.archery = 1
            self.dodge = 5 + (self.level // 3)

        elif self.icon == "J":#if its a jack (of all trades)
            self.name += "Jack"
            self.maxHealth = 6 + (self.level // 6)
            self.health = self.maxHealth
            self.maxMana = 2 + (self.level // 6)
            self.mana = self.maxMana
            self.strength = 2 + (self.level // 6)
            self.crit = 2 + (self.level // 6)
            self.archery = 2 + (self.level // 6)
            self.dodge = 2 + (self.level // 6)
            self.arrows += 10

        elif self.icon == "H":#if its a healer
            self.name += "healer"
            self.maxHealth = 5 + (self.level // 8)
            self.health = self.maxHealth
            self.maxMana = 5 + (self.level // 5)
            self.mana = self.maxMana
            self.strength = 1
            self.crit = 2 + (self.level // 10)
            self.archery = 1
            self.dodge = 2 + (self.level // 10)

    def __getPlayer(self):#gets the player
        return self.room.myLevel.thePlayer#rturns player's value
    

    def __getLevel(self):#gets the level
        return self.room.myLevel#returns level object

    def usePotion(self):#called when the enemy needs a potion (health or mana)
        if self.maxHealth // 5 >= self.health and self.healthP > 0:#makes sure they have a health potion and it is optimal to use the potion
            self.health+=  self.maxHealth//5#gives the enemy health
            if self.health <self.maxHealth:#checks if the health is over max health
                self.health=self.maxHealth#makes health = max health
        elif self.maxMana // 5 >= self.mana and self.manaP > 0:#makes sure they have a mana potion and it is optimal to use the potion
            self.mana+=  self.maxMana//5#gives the enemy mana
            if self.maxMana <self.mana:#checks if the mana is over max mana
                self.mana=self.maxMana#makes mana = max mana

    #__pStrength / __pDodge/ __pArchery / __pCrit are similar
    def __pStrength(self):#called when the enemy uses a strength potion
        if self.strengthP>=1 and self.strength < 20 and self.dodge > 1:#checks if the enemy has the potion and if there strength stat is less 20 and there dodge stat is more than 1
            self.strengthP-=1#take away 1 strength potion
            self.strength+=1#add 1 to strength stat
            self.dodge-=1#takes away the potion away            
            
    def __pDodge(self):#called when the enemy uses a dodge potion
        if self.dodgeP>=1 and self.dodge < 20 and self.maxHealth > 1:#checks if the enemy has the potion and if there dodge stat is less 20 and there max health stat is more than 1
            self.dodgeP-=1#takes away the potion away
            self.dodge+=1#adds 1 to dodge stat
            self.maxHealth-=1#takes away 1 from max health

    def __pArchery(self):#called when the enemy uses a archery potion
        if self.archeryP>=1 and self.archery < 20 and self.strength > 1:
            self.archeryP-=1#takes away the potion away
            self.archery+=1#adds 1 to archery stat
            self.strength-=1#minus 1 to strength stat
            
    def __pCrit(self):#called when the enemy uses a crit potion
        if self.critP>=1 and self.crit < 20 and self.strength > 1:#checks if the enemy has the potion and if there crit stat is less 20 and there strength stat is more than 1
            self.critP-=1#takes away the potion away
            self.crit+=1#add 1 to crit stat
            self.strength-=1#take away from strength

    def randomMove(self):#used for when the player is out of range
        self.myLevel = self.__getLevel()#gets the level obejct
        if self.health <=0:#makes sure the player is alive
            self.icon="X"#makes them "X" on screen
            return#stop
        
        self.usePotion()#call this function
        counter = 0#this will make sure the function doesnt loop forever
        self.moved = False#assuming they have not moved
        while not self.moved and counter <= 10:#while the enmey has not moved and the loop has not gone on for too long
            player = self.__getPlayer()#get the player
            if abs(self.x - player.x) + abs(self.y - player.y) > 8:#while player are not in range (more than 8 tiles away)
                if self.archery > self.maxMana and self.archery > self.strength:#if archery is strongest stat
                    self.__pArchery()#use this potion (if they have)
                elif self.archery < self.strength and self.strength > self.maxMana:#if strength is the strongest stat
                    self.__pStrength()#use this potion (if they have)
                elif self.crit > self.strength:#if crit is more than strength
                    self.__pCrit()#use this potion (if they have)
                elif self.maxHealth < self.dodge:#if maxhealth more than dodge
                    self.__pDodge()#use this potion (if they have)
                else:#if they are equal 
                    pType = random.randint(1, 5)#pick randomly
                    if pType == 1:#if its 1
                        self.__pArchery()#use this potion (if they have)
                    elif pType == 2:#if its 2
                        self.__pCrit()#use this potion (if they have)
                    elif pType == 3:#if its 3
                        self.__pDodge()#use this potion (if they have)
                    elif pType == 4:#if its 4
                        self.__pStrength()#use this potion (if they have)
                        
                direction = random.randint(1, 4)#choose a direction
                if direction == 1:#if its 1 (down)
                    if self.myLevel.move(self.x, self.y+1,self) == True:#check if the tile is valid
                        self.y = self.y + 1#move
                        self.moved = True#break the loop because they moved

                elif direction == 2:#if its 2 (up)
                    if self.myLevel.move(self.x, self.y-1,self) == True:#check if the tile is valid
                        self.y = self.y - 1#move
                        self.moved = True#break the loop because they moved

                elif direction == 3:#if its 3 (left)
                    if self.myLevel.move(self.x-1, self.y,self) == True:#check if the tile is valid
                        self.x = self.x - 1#move
                        self.moved = True#break the loop because they moved

                elif direction == 4:#if its 4 (right)
                    if self.myLevel.move(self.x+1, self.y,self) == True:#check if the tile is valid
                        self.x += 1#move
                        self.moved = True#break the loop because they moved
            else:
                self.moved = True#break the loop because the player is in range
            counter += 1#make sure that the loop doesnt go on forever
        self.room.pickUp(self)  # pickup an item if they are on it
        
    def __fire(self,thing,stat):#called when the enemy uses a far ranged attack
        player = self.__getPlayer()#gets the player
        if thing > 0:#checks if thing (mana or arrows (depending on the arguement)) is more than 0
            if abs(self.x - player.x) + abs(self.y - player.y) <= 3:#if the player is in range
                self.RNG=random.randint(0,100)
                if self.RNG <= player.dodge:#checks to see if the enemy missed
                    print("miss")
                    chr(ord(getch()))
                elif self.RNG <= self.crit:#checks to see if the enemy got a critical hit
                    player.health-=stat * 3#stat (max mana or archery (depending on argument) timesed by 3 and taken away from player's health
                    print("Player hit! (",stat * 3,")")
                    chr(ord(getch()))
                else:
                    player.health-=stat#stat takes away player health
                    print("Player hit. (",stat,")")
                    chr(ord(getch()))
                if player.health<=0:#checks if player is dead
                    self.score+=2#gives enemy score
                if thing == self.mana:#checks if thing is mana
                    self.mana-=1#takes away 1 mana
                else:#checks if its arrows
                    self.arrows-=1#takes away 1 arrow

    def __melee(self):#called when the enemy is within 1 tile of the player
        player = self.__getPlayer()#gets the player object
        self.RNG=random.randint(1,100)#the random number generator
        if self.RNG <= player.dodge:#if it was a miss
            print(self.name, " missed")
            chr(ord(getch()))
        elif self.RNG <= self.crit:#if it was a crit
            player.health -= self.strength * 3#takes health away using strength *3
            print("player is hit! (", self.strength * 3, ")")
            chr(ord(getch()))
        else:#if it was a normal hit
            player.health -= self.strength#takes health away using strength
            print("player is hit. (",self.strength, ")")
            chr(ord(getch()))

    def move(self):#called when the enemy is in range of the player (8 tiles)
        player = self.__getPlayer()#get the player
        if self.health<=0:#if the enemy is dead
            return#stop
        self.myLevel = self.__getLevel()#get the level
        if abs(player.x - self.x) + abs(player.y - self.y) <= 8:#if the enemy is in range
            if ((self.strength > self.maxMana or self.strength > self.archery) or (self.arrows <= 0 and self.mana <= 0)) and (abs(player.x - self.x) + abs(player.y - self.y) <= 1):#if the enemy is in range and strength is the strongest attribute
                self.__melee()#melee attack
            elif (self.arrows >= 1 or self.mana >= 1 and (self.strength < self.maxMana or self.strength < self.archery)) and  (abs(player.x - self.x) + abs(player.y - self.y) <= 3) :#if they have mana or arrows and there ranged attack is better than there strength
                if self.archery > self.maxMana and self.arrows <=1:#if they have arrows and archery is more than max mana
                    self.__fire(self.arrows,self.archery)#__fire arrows

                elif self.archery < self.maxMana and self.mana<=1:#if they have mana and max mana is more than archery 
                    self.__fire(self.mana,self.maxMana)#use mana

                else:#if they are =
                    if random.randint(1, 2) == 1 and self.mana>=1:#if random number =1 and mana is not empty
                        self.__fire(self.mana,self.maxMana)#use mana

                    else:#if random number =2
                        if self.arrows>=1:#arrows is not empty
                            self.__fire(self.arrows,self.archery)#fire arrows

            else:#track if they are not in range of attack
                if self.x == player.x:#if the enemy's x anf player's x is =
                    if self.y < player.y:#if the enemy's y is less than player's y (below the enemy)
                        if self.myLevel.move(self.x, self.y+1,self) == True:#if its a valid move (moving down)
                            self.y = self.y + 1#go towards the player (go down)
                    else:#if the enemy's y is more than player's y (above the enemy)
                        if self.myLevel.move(self.x, self.y-1,self) == True:#if its a valid move (moving up)
                            self.y = self.y - 1#go towards the player (go up)
                elif self.y == player.y:#if the enemy's y and player's y is =
                    if self.x < player.x:#if the enemy's x is less than player's x (right to the enemy)
                        if self.myLevel.move(self.x+1, self.y,self) == True:#if its a valid move (moving right)
                            self.x = self.x + 1#go towards the player (go right)

                    else:#if the enemy's x is less than player's x (left to the enemy)
                        if self.myLevel.move(self.x-1, self.y,self) == True:#if its a valid move (moving left)
                            self.x = self.x - 1#go towards the player (go left)

                else:#if the enemy's x and player's x is not = and the enemy's y and player's y is =
                    moveDirection = random.randint(0, 1)#which direction they will go x or y (up / down or left / right)
                    counter = 0#make sure the loop doesnt go on forever
                    move=False#assuming they havent moved
                    while counter <= 1 and move == False:#while the loop hasnt gone on for too long and the enemy hasnt moved
                        if moveDirection == 0:#if move direction was y(0) (up/down)
                            if self.y < player.y:#if the enemy's y is less than player's y (above the enemy)
                                if self.myLevel.move(self.x, self.y+1,self) == True:#if its a valid move (moving down)
                                    self.y = self.y + 1#go towards the player (go down)
                                    move=True#they have moved (break out of the loop)
                                else:#if the enemy couldnt move 
                                    counter += 1#add 1 to the counter (make sure the loop doesnt go on forever)
                                    moveDirection = 1#try using x (left/right)
                                    
                            else:#if the enemy's y is more than player's y (above the enemy)
                                if self.myLevel.move(self.x, self.y-1,self) == True:#if its a valid move (moving up)
                                    self.y = self.y - 1#go towards the player (go up)
                                    move=True#they have moved (break out of the loop)
                                else:#if the enemy couldnt move 
                                    counter += 1#add 1 to the counter (make sure the loop doesnt go on forever)
                                    moveDirection = 1#try using x (left/right)
                        else:#if move direction was x(1) (left/right)
                            if self.x < player.x:#if the enemy's x is less than player's x (right to the enemy)
                                if self.myLevel.move(self.x+1, self.y,self) == True:#if its a valid move (moving right)
                                    self.x = self.x + 1#go towards the player (go right)
                                    move=True#they have moved (break out of the loop)
                                else:#if the enemy couldnt move 
                                    counter += 1#add 1 to the counter (make sure the loop doesnt go on forever)
                                    moveDirection = 0#try using y (up/down)
                            else:#if the enemy's x is more than player's x (left to the enemy)
                                if self.myLevel.move(self.x-1, self.y,self) == True:#if its a valid move (moving left)
                                    self.x = self.x - 1#go towards the player (go left)
                                    move=True#they have moved (break out of the loop)
                                else:#if the enemy couldnt move 
                                    counter += 1#add 1 to the counter (make sure the loop doesnt go on forever)
                                    moveDirection = 0#try using y (up/down)
                                    
        self.room.pickUp(self)  # check if they can pickup an item

class Level:
    def __init__(self):
        self.rooms = []#this will be the array of all the rooms (all room objects will be stored here)
        self.upDown = 40#how high the level will be
        self.leftRight = 150#how wide the level will be
        self.level = 1#what level the level is (as level 1, level 2 etc)
        self.thePlayer = None#the player object 
        self.playerRoomLocation = 0#the player's room they are currently in
        
        self.generateRooms()#makes all the rooms in the level
        self.generateCorridor()#connects all the rooms togther (using the reference points (doors)

        self.addExit()#adds the exit (next level access) to the last room in the self.rooms array
        self.clearFirstRoom()#this clears the first room of the array in the self.rooms array

    def getPlayerRoom(self):#gets the player's room that they are in
        return self.rooms[self.playerRoomLocation]#return the value of the player's room

    def setPlayer(self, p: Player):#sets the initial value of the player
        self.thePlayer = p

    def addExit(self):#adds exit to the last room
        self.rooms[-1].addExit()#adds exit to the the last room in the self.rooms array

    def clearFirstRoom(self):#clears first room
        self.rooms[0].clearRoom()

    def move(self, x, y,person):#checks if the player/enemy (person) is doing a valid move)
        self.canMove=False#assuming they cannot move
        
        for room in self.rooms:#for each room
            if (x >= room.x and x < room.xx) and (y >= room.y and y < room.yy):#if the move they are making is inside a room 
                self.canMove=True#they can move
                return True#stop#return value True
        for walk in self.cor:#for each corridor tile
            if x == walk[0] and y == walk[1]:#if the step is on a corridor tile
                self.canMove=True#then they can move
                return True#stop#return value True

    def generateCorridor(self):
        self.corIcon = "#"#what it will display
        self.cor = []#all corridor tiles will be stored here
        for room in self.rooms:#for each room
            if len(self.cor) == 0:#if cor array is empty
                self.cor.append(room.getDoorLocation())#add the first room's door location to the cor array
            else:#if it is not empty
                reached = False#assuming the corridor does not yet reach the other room's door
                while not reached:#whilst the corridor has not yet reach the other room's door
                    roomDoor = room.getDoorLocation()#get the location of the current room's door
                    x = roomDoor[0]#room's door's x value
                    y = roomDoor[1]#room's door's y value
                    if self.cor[-1][0] < x:  #  x #if the last corridor tile's x value is smaller than the door's x value (door is below)
                        self.cor.append([self.cor[-1][0] + 1, self.cor[-1][1]])#go towards the door (go down)
                    elif self.cor[-1][0] > x:# if the last corridor tile's x value is biger than the door's x value (door is above)
                        self.cor.append([self.cor[-1][0] - 1, self.cor[-1][1]])#go towards the door (go up)
                    elif self.cor[-1][1] < y:  # y # if the last corridor tile's y value is smaller than the door's y value (door is to the right)
                        self.cor.append([self.cor[-1][0], self.cor[-1][1] + 1])#go towards the door (go right)
                    elif self.cor[-1][1] > y:# if the last corridor tile's y value is bigger than the door's y value (door is to the left)
                        self.cor.append([self.cor[-1][0], self.cor[-1][1] - 1])#go towards the door (go left)
                    else:#if it is not up,down,left, or right 
                        reached = True#then the last corridor tile is equal to the roomDoor's value

    def generateRooms(self):
        roomAmount=random.randint(8,10)#how many rooms will be generated
        for x in range(roomAmount):#for roomAmount times
            self.rooms.append(Room(self))#add a room object to self.rooms

    def __addPlayerToPrintLayout(self, printLayout):#prints the player on the level
        currentRoom = self.getPlayerRoom()#gets the room of the player
        printLayout[self.thePlayer.x][self.thePlayer.y] = self.thePlayer.icon#adds the player onto the level

    def __addCorridorToPrintLayout(self, printLayout):#adds the corridor to the print layout
        for eachStep in self.cor:#for each corridor tile
            x = eachStep[0]#corridor tile's x value
            y = eachStep[1]#corridor tile's y value
            printLayout[x][y] = "#"#adds the corridor tile onto the level



    def printRooms(self):#prints the level and its contents
        printLayout = []#create a 2D list to store what will be printed on screen
        for x in range(self.leftRight):#for width of the level
            row = []#have an array
            for y in range(self.upDown):#for height of the level
                row.append(" ")#make spaces in row
            printLayout.append(row)#add this to the print layout

        self.__addCorridorToPrintLayout(printLayout)#overwrite the areas where the corridors are

        #each room adds its own data into the 2D list
        for room in self.rooms:
            room.addToLayout(printLayout)

        #prepare to print out
        levelString = ""

        self.__addPlayerToPrintLayout(printLayout)

        for y in range(self.upDown):#for height
            for x in range(self.leftRight):#for width
                levelString += printLayout[x][y]#add the printLayout's value to the levelString

            levelString += "\n"#go to the next line

        print(levelString)#actually print the level
        

def play(icon):#the actual game function
    myLevel=Level()#create the level object
    player = Player(icon,myLevel)#create player object
    
    while player.health >=1:#while the player is alive
        print("Health:",player.health,"/",player.maxHealth," | ","Mana:",player.mana,"/",player.maxMana," | Score:",player.score)
        myLevel.printRooms()#print the level
        player.inventory()#show player's inventory
        print("Strength:",player.strength,"| Archery:",player.archery,"| crit:",player.crit,"%","| Dodge:",player.dodge,"%")
        player.performAction()#allow the player to perform an action
        player.moves+=1#add 1 to player moves
        
        for room in myLevel.rooms:#for each room
            for enemy in room.enemies:#for each enemy iside the room
                enemy.randomMove()#make a random move (if necessary)
                enemy.move()#make a move towards the player (if possible)
                
        if player.x==myLevel.rooms[-1].exitx and player.y == myLevel.rooms[-1].exity:#if the player has reached the exit (next level)
            player.levelUp()#buff the player's stat
            myLevel.level+=1#make the level increase by 1
            myLevel.rooms=[]#reset the rooms
            myLevel.generateRooms()#make new rooms
            myLevel.generateCorridor()#make the corridors for the new rooms (corridors will reset  when it is function is called)
            myLevel.addExit()#adds the exit for the level (to the last room)
            myLevel.clearFirstRoom()#clears the first room
            player.score+=5#adds 5 score to the player
            player.x=myLevel.rooms[0].x+random.randint(2,myLevel.rooms[0].width-2)#spawns the player inside the first room #x (which is empty)
            player.y=myLevel.rooms[0].y+random.randint(2,myLevel.rooms[0].height-2)#spawns the player inside the first room #x
            if player.arrows <5:
                player.arrows=5
        os.system('cls')#when running in the command prompt it will clear the screen (making only one print appear at a time)
    print("You Have Died ;(")
    print("Score:",player.score)
    print("Kills:",player.kills)
    print("Moves:",player.moves)
    input("_")#buffer

if __name__ == "__main__":#only run if it runs this file directly #only i will ever experience this bit
    print("Choose a,j,m,w,r")#to remind me of the classes
    play(chr(ord(getch()))).lower()#allows me to choose a class and start the game
            

