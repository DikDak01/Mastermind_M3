import time
import sys
from pymongo import *

class Mastermind:
    def __init__(self):
        self.max_attempts = 7
        self.secret_code = None
        self.field = ['0', '1', '2', '3']
        self.players = []
        self.computer = []
        self.colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
 

    def gametitle(self):
        with open('./ASCI-ART/Mastermind_Title.txt', 'r') as gametitle:
            print(gametitle.read())

class Questions(Mastermind):             
    def language_question(self):
        print("In which language you wanna play:\n1. German\n2. English\n3. Shut up!")
        self.language = int(input("Enter the number corresponding to your preferred language:"))

    def opponent_question(self):    
        print("Do you want to compete against a computer or friend:\n1. Computer\n2. Friend\n3. with myself")
        self.opponent = int(input("Enter the number corresponding to your preferred opponent:"))
        
    def playername1_question(self):
        print("Player 1, what do you want to be called in the game?")
        self.player1_name = input("Enter the name corresponding to your preferred playername:")
        
    def playername2_question(self):   
        print("Player 2 now it's your turn")
        self.player2_name = input("Enter the name corresponding to your preferred playername:")
        
    def codemaker_question(self):   
        print(f"Who wants to be the codemaker?\n1. {self.player1_name}\n2. {self.player2_name}")
        self.codemaker_choice = int(input("Enter the number corresponding to your preferred opponent:"))

class Language_Decision(Questions):    
    def lang_decision_german(self):
        if self.language == 1:
            print("Sehr gut, du willst also das Spiel auf Deutsch spielen,\ndann gehts weiter mit der nächsten Frage:")
            time.sleep(5)        
        elif self.language == 2:
            print("Very good, so you want to play the game in English,\nthen move on to the next question")
            time.sleep(5)
        elif self.language == 3:
            #funny answer :)
            with open('./ASCI-ART/Goodbye.txt', 'r') as language:
                print(language.read())
                time.sleep(10)
                sys.exit()              

class Oppenent_Decision(Language_Decision):
    def op_decision_german(self):
        if self.opponent == 1:
            print("Du spielst gegen den Computer, zeigs ihm!")
            time.sleep(5)       
        elif self.opponent == 2:
            print("Du spielst also gegen ein Freund, möge der bessere gewinnen!")
            time.sleep(5)
        elif self.opponent == 3:
            #funny answer
            with open('./ASCI-ART/Idiot.txt', 'r') as opponent:
                print(opponent.read())
                time.sleep(10)
                sys.exit() 
                 
    def op_decision_english(self):
        if self.opponent == 1:
            print("You're playing against the computer, show it what you've got!")
                 
        elif self.opponent == 2:
            print("So, you're playing against a friend, may the better one win!")
           
        elif self.opponent == 3:
            #funny answer
            with open('./ASCI-ART/Idiot.txt', 'r') as opponent:
                print(opponent.read())
                time.sleep(10)
                sys.exit()   
                
class Results_Decisions(Oppenent_Decision):
    
    client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000", 27017)
    db = client.Resultsdb
    decisions = db.decisions    
        
    def save_results(self):
        self.scenario_1 = self.decisions.insert_one({"language:": self.language, "opponent:": self.opponent, "player1 name:": self.player1_name, "player2 name:": self.player2_name, "codemaker:": self.codemaker})
        print("Results saved successfully.")
    
        for self.db.decisions in self.db.decisions.find():
            print(self.scenario_1)  
    


if __name__ == "__main__":
    game = Results_Decisions()
    game.gametitle()
    game.language_question()
    game.opponent_question()
    game.playername1_question()
    game.playername2_question()
    game.codemaker_question()
    game.save_results()
    
    if game.language == 1:
        game.lang_decision_german()
    elif game.language == 2:
        game.lang_decision_english()

    if game.language == 1:
        game.op_decision_german()
    elif game.language == 2:
        game.op_decision_english()

    game.save_results()
