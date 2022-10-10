#################################################################
# Name: Skylar Randall, Aaron Earp, Joe Sullivan
# Date: 5/20/20
# Description: 
#################################################################
from Tkinter import *
from random import *
from copy import *

class Move(object):
    def __init__(self, name = "", move_type = "", power = 0, dmg_type = "", accuracy = 0):
        self.name = name
        self.move_type = move_type
        self.power = power
        self.dmg_type = dmg_type
        self.accuracy = accuracy

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, string):
        self._name = string

    @property
    def move_type(self):
        return self._move_type

    @move_type.setter
    def move_type(self, string):
        self._move_type = string

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    @property
    def dmg_type(self):
        return self._dmg_type

    @dmg_type.setter
    def dmg_type(self, string):
        self._dmg_type = string

    @property
    def accuracy(self):
        return self._accuracy

    @accuracy.setter
    def accuracy(self, string):
        self._accuracy = string

    
class Pokemon(object):
    def __init__(self, name = "??????????", ability = "None", pk_type = "None", hp = 1.0, attack = 1, defense = 1, spatk = 1, spdef = 1, spd = 1, moves = []):
        self.name = name
        self.ability = ability
        self.pk_type = pk_type
        self.hp = hp
        self.attack = attack
        self.spatk = spatk
        self.defense = defense
        self.spdef = spdef
        self.spd = spd
        self.moves = moves

    attack_mod_den = 2
    defense_mod_den = 2

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, string):
        self._name = string

    @property
    def ability(self):
        return self._ability

    @ability.setter
    def ability(self, string):
        self._ability = string

    @property
    def pk_type(self):
        return self._pk_type

    @pk_type.setter
    def pk_type(self, string):
        self._pk_type = string

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        
    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = value
        
    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        self._defense = value
        
    @property
    def spatk(self):
        return self._spatk

    @spatk.setter
    def spatk(self, value):
        self._spatk = value
        
    @property
    def spdef(self):
        return self._spdef

    @spdef.setter
    def spdef(self, value):
        self._spdef = value
        
    @property
    def spd(self):
        return self._spd

    @spd.setter
    def spd(self, value):
        self._spd = value
        
    @property
    def moves(self):
        return self._moves

    @moves.setter
    def moves(self, moveset):
        self._moves = moveset

class Trainer(object):
    def __init__(self, name = "", party = [], current_pokemon = 0):
        self.name = name
        self.party = party
        self.current_pokemon = current_pokemon

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, string):
        self._name = string
        
    @property
    def party(self):
        return self._party

    @party.setter
    def party(self, p):
        self._party = p

    @property
    def current_pokemon(self):
        return self._current_pokemon

    @current_pokemon.setter
    def current_pokemon(self, poke):
        self._current_pokemon = poke

class Game(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

    battle_won = 0
    all_fainted = 0

    def setupGUI(self):
        self.pack(fill=BOTH, expand=1)
        
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        
        text_frame = Frame(self, width=WIDTH / 2)
        
        Game.text = Text(text_frame, bg="cyan", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

        if(crand == 2):
            img = PhotoImage(file = "squirtle-front.gif")
            Game.image = Label(self, bg="blue", width=WIDTH, image=img)
            Game.image.image = img
            Game.image.pack(side=RIGHT, fill=Y)
            Game.image.pack_propagate(False)

        elif(crand == 0):
            img = PhotoImage(file = "bulbusaur-front.gif")
            Game.image = Label(self, bg="green", width=WIDTH, image=img)
            Game.image.image = img
            Game.image.pack(side=RIGHT, fill=Y)
            Game.image.pack_propagate(False)

        elif(crand == 1):
            img = PhotoImage(file = "charmander-front.gif")
            Game.image = Label(self, bg="red", width=WIDTH, image=img)
            Game.image.image = img
            Game.image.pack(side=RIGHT, fill=Y)
            Game.image.pack_propagate(False)

        if(prand == 2):
            img = PhotoImage(file = "squirtle-back.gif")
            Game.image = Label(self, bg="blue", width=WIDTH, image=img)
            Game.image.image = img
            Game.image.pack(side=LEFT, fill=Y)
            Game.image.pack_propagate(False)

        elif(prand == 0):
            img = PhotoImage(file = "bulbusaur-back.gif")
            Game.image = Label(self, bg="green", width=WIDTH, image=img)
            Game.image.image = img
            Game.image.pack(side=LEFT, fill=Y)
            Game.image.pack_propagate(False)

        elif(prand == 1):
            img = PhotoImage(file = "charmander-back.gif")
            Game.image = Label(self, bg="red", width=WIDTH, image=img)
            Game.image.image = img
            Game.image.pack(side=LEFT, fill=Y)
            Game.image.pack_propagate(False)


    def setText(self, game_text):
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)

        t = ""
        
        if(Game.all_fainted == 1):
            Game.text.insert(END, "You lost. All your Pokemon have fainted.\n\n")
        elif(Game.battle_won == 1):
            Game.text.insert(END, "You won! You earned $100!\n\n")
        else:
            t += cpu.name + "'s " + cpu.current_pokemon.name + ": " + str(round(cpu.current_pokemon.hp, 1)) + " HP\n"
            t += player.name + "'s " + player.current_pokemon.name + ": " + str(round(player.current_pokemon.hp, 1)) + " HP\n\n"

            t += "-\n" + player.current_pokemon.name + "'s moves:\n"
            for i in range(len(player.current_pokemon.moves)):
                t += "[{}] ".format(player.current_pokemon.moves[i].name)
            t += "\n-\n\n"
            

        Game.text.insert(END, t + "" + game_text)
        Game.text.config(state=DISABLED)

    def play(self):
        self.setupGUI()
        
        response = ""
        self.setText(response)

        

    
    def process(self, event):
        action = Game.player_input.get()
        action = action.lower()

        # default response
        response = "I don't understand."
        
        if(action == "quit" or action == "exit" or action == "bye" or action == "sionara!"):
            exit(0)

        else:
            for i in range(len(player.current_pokemon.moves)):
                if(action == player.current_pokemon.moves[i].name.lower()):
                    if(player.current_pokemon.moves[i].power > 0):
                        damage = ((((4.0 * player.current_pokemon.moves[i].power * (player.current_pokemon.attack * 2.0 /(player.current_pokemon.attack_mod_den))) / (cpu.current_pokemon.defense * (2.0 / cpu.current_pokemon.defense_mod_den))) / 50) + 2)
                    else:
                        damage = 0

                    if(action == "growl" and cpu.current_pokemon.attack_mod_den <= 8):
                        cpu.current_pokemon.attack_mod_den += 1
                    elif(action == "tail whip" and cpu.current_pokemon.defense_mod_den <= 8):
                        cpu.current_pokemon.defense_mod_den += 1
                        

                    if(cpu.current_pokemon.hp > damage):
                        cpu.current_pokemon.hp -= damage
                    else:
                        cpu.current_pokemon.hp = 0
                    response = player.name + "'s " + player.current_pokemon.name + " used " + player.current_pokemon.moves[i].name + "! " + cpu.name + "'s " + cpu.current_pokemon.name + " took " + str(round(damage, 1)) + " damage.\n"
                    if(cpu.current_pokemon.hp == 0):
                        Game.battle_won = 1
                        response += cpu.name + "'s " + cpu.current_pokemon.name + " has fainted!"

                    if(Game.battle_won == 0):
                        rand_move = cpu.current_pokemon.moves[randint(0, len(cpu.current_pokemon.moves) - 1)]
                        if(rand_move.power > 0):
                            damage = ((((4.0 * rand_move.power * (cpu.current_pokemon.attack * (2.0 / cpu.current_pokemon.attack_mod_den))) / (player.current_pokemon.defense * (2.0 / player.current_pokemon.defense_mod_den))) / 50) + 2)
                        else:
                            damage = 0

                        if(rand_move.name.lower() == "growl" and player.current_pokemon.attack_mod_den <= 8):
                            player.current_pokemon.attack_mod_den += 1
                        elif(rand_move.name.lower() == "tail whip" and player.current_pokemon.defense_mod_den <= 8):
                            player.current_pokemon.defense_mod_den += 1
                        
                        if(player.current_pokemon.hp > damage):
                            player.current_pokemon.hp -= damage
                        else:
                            player.current_pokemon.hp = 0
                        response += cpu.name + "'s " + cpu.current_pokemon.name + " used " + rand_move.name + "! " + player.name + "'s " + player.current_pokemon.name + " took " + str(round(damage, 1)) + " damage.\n"
                        if(player.current_pokemon.hp == 0):
                            Game.all_fainted = 1
                            response += player.name + "'s " + player.current_pokemon.name + " has fainted!"


                    
                    

        self.setText(response)
        Game.player_input.delete(0, END)


tackle = Move("Tackle", "Normal", 40, "Physical", 100.0)
scratch = Move("Scratch", "Normal", 40, "Physical", 100.0)
growl = Move("Growl", "None", 0, "Status", 100.0)
tail_whip = Move("Tail Whip", "None", 0, "Status", 100.0)
vine_whip = Move("Vine Whip", "Grass", 45, "Physical", 100.0)
ember = Move("Ember", "Fire", 40, "Special", 100.0)
bubble = Move("Bubble", "Water", 40, "Special", 100.0)


move_list = [tackle, scratch, growl, tail_whip, vine_whip, ember, bubble]
    
bulbasaur = Pokemon("Bulbasaur", "Overgrow", "Grass", 45.0, 49.0, 49.0, 65.0, 65.0, 45.0, [tackle, growl, vine_whip])
charmander = Pokemon("Charmander", "Blaze", "Fire", 39.0, 52.0, 43.0, 60.0, 50.0, 65.0, [scratch, growl, ember])
squirtle = Pokemon("Squirtle",  "Torrent", "Water", 44.0, 48.0, 65.0, 50.0, 64.0, 43.0, [tackle, tail_whip, bubble])
Cyndaquil = Pokemon("Cyndaquil",  "Blaze", "Fire", 39.0, 52.0, 43.0, 60.0, 50.0, 65.0, [tackle, growl, ember])
Totodile = Pokemon("Totodile",  "Torrent", "Water", 50.0, 65.0, 64.0, 44.0, 48.0, 43.0, [scratch, tail_whip, bubble])
Torchic = Pokemon("Torchic",  "Blaze", "Fire", 45.0, 60.0, 40.0, 70.0, 50.0, 45.0, [scratch, tail_whip, ember])
Treecko = Pokemon("Treecko",  "Overgrow", "Grass", 40.0, 45.0, 35.0, 65.0, 55.0, 70.0, [tackle, tail_whip, vine_whip])
Mudkip = Pokemon("Mudkip",  "Torrent", "Water", 50.0, 70.0, 50.0, 50.0, 50.0, 40.0, [tackle, tail_whip, bubble])
Chikorita = Pokemon("Chikorita",  "Overgrow", "Grass", 45.0, 49.0, 65.0, 49.0, 65.0, 45.0, [tackle, tail_whip, vine_whip])


pokemon_list = [bulbasaur, charmander, squirtle]


prand = randint(0, 2)
p_poke = copy(pokemon_list[prand])
player = Trainer("Player", [p_poke])
player.current_pokemon = player.party[0]

crand=randint(0,2)
c_poke = copy(pokemon_list[crand])
cpu = Trainer("Opponent", [c_poke])
cpu.current_pokemon = cpu.party[0]


##########################################################
WIDTH = 800
HEIGHT = 600

window = Tk()
window.title("Pokemon")

g = Game(window)
g.play()

window.mainloop()
