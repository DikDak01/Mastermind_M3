from colorama import *
import datetime as dt
import random

#Initialize colorama
init(autoreset=True)

class Information:
    def __init__(self):        
        self.field = ['0','1','2','3']

    def playground(self):
        print(self.field[0] + "|" + self.field[1] + "|" + self.field[2] + "|" + self.field[3])
    
    def introduction(self):
        asci_title = open('ASCI-ART/ascii-art_1.txt', 'r')
        print(asci_title.read())

        introductions = open('ASCI-ART/rules_1.txt', 'r')
        print(introductions.read())

class Players(Information):   
    
    def colors(self):
        self.colors_cm_cb = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
    
    def codemaker(self):
        cm_code = {'' + "|" + '' + "|" + '' + "|" + ''}
        self.cm_choice = input(f"Codemaker {self.cm_name}, please enter your code here: {cm_code}")

    def codebreaker(self):   
        cb_code = {'' + "|" + '' + "|" + '' + "|" + ''}
        self.cb_choice = input(f"Codemaker {self.cb_name}, please enter your code here: {cb_code}")
            
    def computer(self):
        return random.sample(self.colors_cm_cb, 4)       

class Check(Players):
    max_attempts = 7
    
    
    def codegeneration(self):
        self.computer.instance = self.computer()
        self.codemaker.instance = self.codemaker()
        
        self.secret_code = (self.computer.instance, self.codemaker.instance)

class Database(Check):
    def human_computer(self):
        question = input("Do you want to play alone or with a friend (computer/friend)?")
        
        if question == 'computer' or 'Computer':
            print("Great, you will play against the computer!")
        
        else:    
            #individual playernames
            self.cm_name = input("Codemaker, please write your player name in the field:")
            self.cb_name = input("Codebreaker, please write your player name in the field:")

class Game(Database):
    def __init__(self):
        super().__init__()

    def play_game(self):
        self.introduction()
        self.human_computer()

        while self.max_attempts > 0:
            self.playground()
            self.codegeneration()
            self.codebreaker()

            if self.cb_choice == self.secret_code:
                print(Fore.GREEN + "Congratulations! You've cracked the code!")
                break
            else:
                print(Fore.RED + "Incorrect code. Try again!")
                self.max_attempts -= 1

        if self.max_attempts == 0:
            print(Fore.RED + "Sorry, you've run out of attempts. The secret code was:", self.secret_code)

if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
    
    
    
