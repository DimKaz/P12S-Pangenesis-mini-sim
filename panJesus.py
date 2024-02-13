import tkinter as tk
import math
import random
from PIL import Image, ImageTk
import time

class CircleButtonsGUI:
    curPlayer = -1
    players = []
    towers = []
    correct = -1
    playerWidth = 5
    
    def __init__(self):
        # Initialize GUI
        self.root = tk.Tk()
        self.root.title("Pan Jesus")
        self.root.geometry("1000x700")
        self.root.resizable(False,False)
        
        self.background_image = Image.open("arena.png")
        self.background_image = self.background_image.resize((1200, 700), Image.LANCZOS)
        self.background_image_resized = ImageTk.PhotoImage(self.background_image)
        
        self.duration = 0

        self.astralImg = tk.PhotoImage(file="astral.PNG")
        self.umbralImg = tk.PhotoImage(file="umbral.PNG")
        self.criticalImg = tk.PhotoImage(file="critical.PNG")
        
        # Resize and scale background image to new canvas size
        self.bg_label = tk.Label(self.root, image=self.background_image_resized)
        self.bg_label.pack()
        self.bg_label.place(x=0, y=0, width=1000, height=700)

        #NEW GAME
        self.newButton = tk.Button(self.bg_label, text="New Game", command=lambda: self.button_newGame())
        self.newButton.pack()
        self.newButton.place(x=0, y=0)
        
        #TIME BOX
        self.timeBox = tk.Text(self.bg_label, bg="dark blue", fg="white", bd=1, height=1, width=10)
        self.timeBox.pack()
        self.timeBox.place(relx=1, rely=0, anchor='ne')
        #######################################################################

        # PLAYERS
        for i in range(8):
            player = tk.Button(self.root, text=f"player", bg="white", command=lambda idx=i: self.player_select(idx), width=self.playerWidth)
            player.place(x=i * (self.playerWidth + 50)+300, rely=0.8, anchor='center')
            #player.pack(side=tk.LEFT, padx=5, pady=5)  # Add buttons from left to right with padding
            self.players.append(player)  # Save buttons to access them later
            
            
        # DEBUFF 1 Stacks
        self.debuffFrame1 = tk.Frame(self.bg_label, bg='white', bd=0, width=0)
        self.debuffFrame1.pack()
        self.debuffFrame1.place(relx=0.48, rely=0.6, anchor='center')
        self.debuff1 = tk.Label(self.debuffFrame1)
        self.debuffStacks = tk.Label(self.debuffFrame1, text="", font=("Courrier", 20), bg='black', fg='white')
        
        # DEBUFF 2 Color
        self.debuffFrame2 = tk.Frame(self.bg_label, bg='white', bd=0, width=0)
        self.debuffFrame2.pack()
        self.debuffFrame2.place(relx=0.52, rely=0.6, anchor='center')
        self.debuff2 = tk.Label(self.debuffFrame2)
        self.debuffTime = tk.Label(self.debuffFrame2, text="", font=("Courrier", 20), bg='black', fg='white')

        # TOWERS
        self.neTowerFrame = tk.Frame(self.root, bg='')
        self.neTowerFrame.pack()
        self.neTowerFrame.place(relx=0.65, rely=0.25, anchor='center')
        
        self.eTowerFrame = tk.Frame(self.root, bg='')
        self.eTowerFrame.pack()
        self.eTowerFrame.place(relx=0.85, rely=0.35, anchor='center')
        
        self.seTowerFrame = tk.Frame(self.root, bg='')
        self.seTowerFrame.pack()
        self.seTowerFrame.place(relx=0.65, rely=0.45, anchor='center')
        
        
        self.nwTowerFrame = tk.Frame(self.root, bg='')
        self.nwTowerFrame.pack()
        self.nwTowerFrame.place(relx=0.35, rely=0.25, anchor='center')
        
        self.wTowerFrame = tk.Frame(self.root, bg='')
        self.wTowerFrame.pack()
        self.wTowerFrame.place(relx=0.15, rely=0.35, anchor='center')
        
        self.swTowerFrame = tk.Frame(self.root, bg='')
        self.swTowerFrame.pack()
        self.swTowerFrame.place(relx=0.35, rely=0.45, anchor='center')
        
                
        w1Tower = tk.Button(self.wTowerFrame, text=f"W1", bg="light gray", command=lambda idx=0: self.tower_select(idx), width=16, height = 6)
        nw1Tower = tk.Button(self.nwTowerFrame, text=f"NW1", bg="light gray", command=lambda idx=1: self.tower_select(idx), width=16, height = 6)
        nw2Tower = tk.Button(self.nwTowerFrame, text=f"NW2", bg="light gray", command=lambda idx=2: self.tower_select(idx), width=16, height = 6)
        sw1Tower = tk.Button(self.swTowerFrame, text=f"SW1", bg="light gray", command=lambda idx=3: self.tower_select(idx), width=16, height = 6)
        sw2Tower = tk.Button(self.swTowerFrame, text=f"SW2", bg="light gray", command=lambda idx=4: self.tower_select(idx), width=16, height = 6)
        
        e1Tower = tk.Button(self.eTowerFrame, text=f"E1", bg="light gray", command=lambda idx=5: self.tower_select(idx), width=16, height = 6)
        ne1Tower = tk.Button(self.neTowerFrame, text=f"NE2", bg="light gray", command=lambda idx=6: self.tower_select(idx), width=16, height = 6)
        ne2Tower = tk.Button(self.neTowerFrame, text=f"NE1", bg="light gray", command=lambda idx=7: self.tower_select(idx), width=16, height = 6)
        se1Tower = tk.Button(self.seTowerFrame, text=f"SE2", bg="light gray", command=lambda idx=8: self.tower_select(idx), width=16, height = 6)
        se2Tower = tk.Button(self.seTowerFrame, text=f"SE1", bg="light gray", command=lambda idx=9: self.tower_select(idx), width=16, height = 6)

        
        e1Tower.pack(side=tk.LEFT, padx=5, pady=5)
        ne1Tower.pack(side=tk.LEFT, padx=5, pady=5)
        ne2Tower.pack(side=tk.LEFT, padx=5, pady=5)
        se1Tower.pack(side=tk.LEFT, padx=5, pady=5)
        se2Tower.pack(side=tk.LEFT, padx=5, pady=5)
        
        w1Tower.pack(side=tk.LEFT, padx=5, pady=5)
        nw1Tower.pack(side=tk.LEFT, padx=5, pady=5)
        nw2Tower.pack(side=tk.LEFT, padx=5, pady=5)
        sw1Tower.pack(side=tk.LEFT, padx=5, pady=5)
        sw2Tower.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.towers.append(w1Tower)
        self.towers.append(nw1Tower)
        self.towers.append(nw2Tower)
        self.towers.append(sw1Tower)
        self.towers.append(sw2Tower)
        self.towers.append(e1Tower)
        self.towers.append(ne1Tower)
        self.towers.append(ne2Tower)
        self.towers.append(se1Tower)
        self.towers.append(se2Tower)
        
            
    def update_arena(self):
        self.debuff1.destroy()
        self.debuffStacks.destroy()
        self.debuff2.destroy()
        self.debuffTime.destroy()
        self.timeBox.destroy()
        self.root.update()
        
#############################################################################################

        
        possibility, towerColor = self.generate_scenario()
        
        if(towerColor): # West is white
            self.towers[0].config(bg="white", fg="black")
            self.towers[1].config(bg="black", fg="white")
            self.towers[2].config(bg="black", fg="white")
            self.towers[3].config(bg="white", fg="black")
            self.towers[4].config(bg="white", fg="black")
            self.towers[5].config(bg="black", fg="white")
            self.towers[6].config(bg="white", fg="black")
            self.towers[7].config(bg="white", fg="black")
            self.towers[8].config(bg="black", fg="white")
            self.towers[9].config(bg="black", fg="white")
        
        else: # West is black
            self.towers[0].config(bg="black", fg="white")
            self.towers[1].config(bg="white", fg="black")
            self.towers[2].config(bg="white", fg="black")
            self.towers[3].config(bg="black", fg="white")
            self.towers[4].config(bg="black", fg="white")
            self.towers[5].config(bg="white", fg="black")
            self.towers[6].config(bg="black", fg="white")
            self.towers[7].config(bg="black", fg="white")
            self.towers[8].config(bg="white", fg="black")
            self.towers[9].config(bg="white", fg="black")
                
        ###Debuff Possibilities
        ##   1 2   7 6
        ## 0           5
        ##   3 4   9 8
        ## 0: 0
        ## 1: 0
        ## 2: 1
        ## 3: 1
        ## 4: 2 short astral
        ## 5: 2 short umbral
        ## 6: 2 long astral
        ## 7: 2 long umbral
        if(possibility == 0 or possibility == 1):
            self.debuff1 = tk.Label(self.debuffFrame1, image=self.criticalImg)
            self.debuffStacks = tk.Label(self.debuffFrame1, text="0", font=("Courrier", 20))
            self.debuff1.pack()
            self.debuffStacks.pack()
        elif(possibility == 2 or possibility == 3):
            self.debuff1 = tk.Label(self.debuffFrame1, image=self.criticalImg)
            self.debuffStacks = tk.Label(self.debuffFrame1, text="1", font=("Courrier", 20))
            self.debuff1.pack()
            self.debuffStacks.pack()
        elif(possibility == 4):
            self.debuff1 = tk.Label(self.debuffFrame1, image=self.criticalImg)
            self.debuffStacks = tk.Label(self.debuffFrame1, text="2", font=("Courrier", 20))
            self.debuff2 = tk.Label(self.debuffFrame2, image=self.astralImg)
            self.debuffTime = tk.Label(self.debuffFrame2, text="16", font=("Courrier", 20))
            self.debuff1.pack()
            self.debuffStacks.pack()
            self.debuff2.pack()
            self.debuffTime.pack()
        elif(possibility == 5):
            self.debuff1 = tk.Label(self.debuffFrame1, image=self.criticalImg)
            self.debuffStacks = tk.Label(self.debuffFrame1, text="2", font=("Courrier", 20))
            self.debuff2 = tk.Label(self.debuffFrame2, image=self.umbralImg)
            self.debuffTime = tk.Label(self.debuffFrame2, text="16", font=("Courrier", 20))
            self.debuff1.pack()
            self.debuffStacks.pack()
            self.debuff2.pack()
            self.debuffTime.pack()
        elif(possibility == 6):
            self.debuff1 = tk.Label(self.debuffFrame1, image=self.criticalImg)
            self.debuffStacks = tk.Label(self.debuffFrame1, text="2", font=("Courrier", 20))
            self.debuff2 = tk.Label(self.debuffFrame2, image=self.astralImg)
            self.debuffTime = tk.Label(self.debuffFrame2, text="20", font=("Courrier", 20))
            self.debuff1.pack()
            self.debuffStacks.pack()
            self.debuff2.pack()
            self.debuffTime.pack()
        elif(possibility == 7):
            self.debuff1 = tk.Label(self.debuffFrame1, image=self.criticalImg)
            self.debuffStacks = tk.Label(self.debuffFrame1, text="2", font=("Courrier", 20))
            self.debuff2 = tk.Label(self.debuffFrame2, image=self.umbralImg)
            self.debuffTime = tk.Label(self.debuffFrame2, text="20", font=("Courrier", 20))
            self.debuff1.pack()
            self.debuffStacks.pack()
            self.debuff2.pack()
            self.debuffTime.pack()
        
        self.timeBox = tk.Text(self.bg_label, bg="dark blue", fg="white", bd=1, height=1, width=10)
        self.timeBox.pack()
        self.timeBox.place(relx=1, rely=0, anchor='ne')
##########################################################################################


    def generate_scenario(self):
        for player in self.players:
            player.destroy()  # Remove players from the frame
        self.players.clear()
        
        towerColor = bool(random.getrandbits(1))
        playerList = [0,1,2,3,4,5,6,7]
        zeroes = random.sample(playerList, 2)
        zeroes.sort()
        playerList = list(set(playerList) - set(zeroes))
        ones = random.sample(playerList, 2)
        ones.sort()
        playerList = list(set(playerList) - set(ones))
        
        for i in range(8):
            if(i != self.curPlayer):
                playerColor = "white"
            else:
                playerColor = "blue"
                
            player = tk.Button(self.root,
                      text=f"player",
                      bg=playerColor,
                      command=lambda idx=i: self.player_select(idx))
            if(i in playerList):
                player.place(x=i * (self.playerWidth + 50)+300, rely=0.8, anchor='center')
            elif(i in zeroes):
                player.place(x=i * (self.playerWidth + 50)+300, rely=0.75, anchor='center')
            elif(i in ones):
                player.place(x=i * (self.playerWidth + 50)+300, rely=0.85, anchor='center')
                
            self.players.append(player)  # Save buttons to access them later
            
            
        #Now solve it
        if(self.curPlayer in zeroes):
            if(self.curPlayer == zeroes[0]):
                self.correct = 0
                possibility = 0
            else:
                self.correct = 5
                possibility = 1
        elif(self.curPlayer in ones):
            if(self.curPlayer == ones[0]):
                self.correct = 3
                possibility = 2
            else:
                self.correct = 9
                possibility = 3
        else:
            possibility = random.randint(4, 7)
            if(possibility == 4): # 2 short astral
                if(towerColor):#Go East
                    self.correct = 5
                else: #Go West
                    self.correct = 0
            if(possibility == 5): # 2 short umbral
                if(towerColor): #Go West
                    self.correct = 0
                else: #Go East
                    self.correct = 5
            if(possibility == 6): # 2 long astral
                if(towerColor): #Go East
                    self.correct = 9
                else: #Go West
                    self.correct = 3
            if(possibility == 7): # 2 long umbral
                if(towerColor): #Go West
                    self.correct = 3
                else: #Go East
                    self.correct = 9
            print(self.correct)
        return possibility, towerColor
        
        ###Debuff Possibilities
        ##   1 2   6 7
        ## 0           5
        ##   3 4   8 9
        ## 0: 0
        ## 1: 0
        ## 2: 1
        ## 3: 1
        ## 4: 2 short astral
        ## 5: 2 short umbral
        ## 6: 2 long astral
        ## 7: 2 long umbral
        ##towerColor = True : West is white
        ##towerColor = false : West is black
            
    def player_select(self, button_index):
        for i in range(8):
            self.players[i].config(bg="white")
        self.curPlayer = button_index
        self.players[button_index].config(bg="blue")
        
    def tower_select(self, button_index):
        if button_index == self.correct:
            self.towers[button_index].config(bg="green")
            self.duration = (time.time() - self.duration)
            self.timeBox.insert(tk.END, str(self.duration))
        else:
            self.towers[button_index].config(bg="red")
                
    def button_newGame(self):
        if( self.curPlayer >= 0):
            self.update_arena()
            self.duration = time.time()
            

                
    def run(self):
        self.root.mainloop()

# Create and run GUI
gui = CircleButtonsGUI()
gui.run()
