import random

class Game:
    def __init__(self):
        self.target_number = random.randint(1,10)
        self.guess_takken = 0
    
    def play (self):
        print ("Masukkan angka 1-10")
        
        while True:
            guess = int(input("Tebak Angka : "))
            self.guess_takken +=1
            
            if guess < self.target_number:
                print ("Angka anda terlalu kecil")
            elif guess > self.target_number:
                print ("Angka anda terlalu besar")
            else:
                print ("Jawaban anda benar")
                break
        print (f"Jumlah percobaan : {self.guess_takken}")
        
game = Game()
game.play()