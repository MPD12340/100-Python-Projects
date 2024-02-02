import random


     
class Character:
    def __init__(self , name , health  ):
        self.health = health
        self.name = name

    def is_alive(self):
        return self.health > 0
    
    def take_damage(self , damage):
         self.health -= damage
         if self.health < 0:
              self.health = 0

    def attack(self , target):
            damage = random.randint(1 , 10)
            target.take_damage(damage)
            print(f"${self.name} attacked ${target.name} and made ${damage} damages")



class Player(Character):
     def __init__(self , name, health, experience=0):
          super().__init__(name , health)
          self.experience = experience

     def level_Up(self):
          self.experience += 10
          print(f"{self.name} leveled up! Current experience: {self.experience}")

 
class Enemy(Character):
    def __init__(self, name, health):
        super().__init__(name, health)


class Game:
     def __init__(self , player , enemy):
          self.player = player
          self.enemy = enemy

     def play(self):
          print('Let the battle begin')             
          while self.player.is_alive() and self.enemy.is_alive():
                self.player.attack(self.enemy)
                if not self.enemy.is_alive():
                     print('Enemy died')
                     self.player.level_Up();
                     break
                
                self.enemy.attack(self.player)
                if not self.player.is_alive():
                 print('Player is dead !')
                 break


player1 = Player("Hero", 50)
enemy1 = Enemy("Evil Monster", 30)

game1 = Game(player1, enemy1)
try:
 game1.play()     
except Exception as e:
     print('something went wrong')            
     print(e)            