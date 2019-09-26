import random
import time
import sys
import datetime
from datetime import datetime
from abc import ABC, abstractmethod


class Pet(ABC):
    @abstractmethod
    def __init__(self, name, health, happiness, hunger, favorite_food):
        self.name = name
        self.health = int(health)
        self.happiness = int(happiness)
        self.hunger = int(hunger)
        self.favorite_food = favorite_food
        self.start_time = int(time.time())

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def set_health(self, amount):
        self.health = amount

    def get_happiness(self):
        return self.happiness

    def set_happiness(self, amount):
        self.happiness = amount

    def get_hunger(self):
        return self.hunger

    def set_hunger(self, amount):
        self.hunger = amount

    def get_favorite_food(self):
        print(f"favorite food is: {self.favorite_food}")
        return self.favorite_food

    def set_favorite_food(self, food):
        self.favorite_food = food

    # if you have divide by 5, then it increases by 1 every 5s, if you divide by 10, then increase by 1 every 10s.
    # higher the number, faster it goes down

    def display_stats(self):

        time_elapsed = (int(time.time()) - self.start_time)
        print(f"\nTime elapsed: {time_elapsed} seconds\n")

        if self.health <= 0 and self.health <= 0:
            print(f"---- Tamagotchi Type: {int(self.health)} ----\n"
                  f"Health Level: 0\n"
                  f"Happiness Level: 0\n"
                  f"Hunger Level: {self.hunger}\n")
        elif self.happiness <= 0:
            print(f"---- Tamagotchi Type: {self.get_name()} ----\n"
                  f"Health Level: {int(self.health)}\n"
                  f"Happiness Level: 0\n"
                  f"Hunger Level: {self.hunger}\n")
        elif self.health <= 0:
            print(f"---- Tamagotchi Type: {self.get_name()} ----\n"
                  f"Health Level: 0\n"
                  f"Happiness Level: {int(self.happiness)}\n"
                  f"Hunger Level: {self.hunger}\n")
        else:
            print(f"---- Tamagotchi Type: {self.get_name()} ----\n"
                  f"Health Level: {int(self.health)}\n"
                  f"Happiness Level: {int(self.happiness)}\n"
                  f"Hunger Level: {int(self.hunger)}\n")

    def __str__(self):
        return f"---- Tamagotchi Type: {self.get_name()} ----\n" \
               f"Health Level: {int(self.health)}\n" \
               f"Happiness Level: {int(self.happiness)}\n" \
               f"Hunger Level: {int(self.hunger)}\n"

    @abstractmethod
    def decrease_health(self):
        pass

    # feed a random number from a list. if say number == print oh it's the favorite food
    @abstractmethod
    def decrease_happiness(self):
        pass

    @abstractmethod
    def increase_hunger(self):
        pass

    @abstractmethod
    def speak(self):
        pass

    def play(self):
        # play_choice = random.randint(0, 2)
        if self.happiness > 99:
            print(f"{self.name} is already really happy!! It's happiness is at 100!")
        else:
            while True:
                print("""  WHAT DO YOU WANT TO PLAY?\n
                1. Play Fetch  
                2. Pet your Pokemon 
                3. Go walk your Pokemon
                                """)
                play_choice = int(input("Enter Choice:"))

                if play_choice == 1:
                    print(f"{self.name} played fetch with you! 🎾")
                    self.happiness += 10
                    if self.happiness > 99:
                        self.happiness = 100
                    print(f"Happiness increased to: {int(self.happiness)}")
                    return self.happiness

                elif play_choice == 2:
                    print(f"You started petting {self.name}! 😊")
                    self.happiness += 10
                    if self.happiness > 99:
                        self.happiness = 100
                    print(f"Happiness increased to: {int(self.happiness)}")
                    return self.happiness

                elif play_choice == 3:
                    print(f"{self.name} enjoyed the walk! 🏃🏃‍️")
                    self.happiness += 10
                    if self.happiness > 99:
                        self.happiness = 100
                    print(f"Happiness increased to: {int(self.happiness)}")
                    return self.happiness
                else:
                    print("Invalid Choice")

    def feed(self):
        while True:
            print("""  WHAT DO YOU WANT TO FEED?
                    1. Feed Food 
                    2. Feed Medicine
                """)
            choice = int(input("Enter Choice:"))
            if choice == 1 and self.hunger > 1:
                Pet.eat_food(self)
                break
            elif choice == 2:
                Pet.eat_potion(self)
                break
            elif choice > 2:
                print("Invalid Choice")
            else:
                print(f"{self.name}'S HUNGER LEVEL IS AT 0 AND NOT HUNGRY")
                break

    def eat_potion(self):
        if self.health > 99:
            print(f"{self.name} is MAX HEALTH ALREADY")
        else:
            print(f"{self.name} has been fed a Potion!")
            self.health += 5
            return self.health

    def eat_food(self):

        food_choice = random.randint(0, 2)

        if food_choice == self.favorite_food:
            if food_choice == 0:
                print(f"Fed {self.name} Berries 🍒🍈🍒")
            elif food_choice == 1:
                print(f"Fed {self.name} Magikarp 🐟🐟🐟")
            elif food_choice == 2:
                print(f"Fed {self.name} Rare Candy 🍬🍭🍬")
            print(f"Bonus: -25 hunger! That's {self.name}'s favorite food!")
            self.hunger -= 15
            return self.hunger
        else:
            if food_choice == 0:
                print(f"{self.name} has been fed berries! 🍒🍈🍒")
                self.hunger -= 23
                return self.hunger

            elif food_choice == 1:
                print(f"{self.name} has been fed Magikarp! 🐟🐟🐟")
                self.hunger -= 23
                return self.hunger

            elif food_choice == 2:
                print(f"{self.name} has been fed rare candy! 🍬🍭🍬")
                self.hunger -= 23
                return self.hunger

            # print(f"Bonus: -5 hunger! That's {self.name}'s favorite food!")
            # self.hunger -= 2
            # return self.hunger

        # if self.hunger < 1:
        #     print(f"{self.name} is NOT HUNGRY")
        # else:
        #     if food_choice == 0:
        #         print(f"{self.name} has been fed berries!")
        #         self.hunger -= 20
        #         return self.hunger
        #
        #     elif food_choice == 1:
        #         print(f"{self.name} has been fed Magikarp!")
        #         self.hunger -= 20
        #         return self.hunger
        #
        #     elif food_choice == 2:
        #         print(f"{self.name} has been fed rare candy!")
        #         self.hunger -= 20
        #         return self.hunger

        # elif food_choice == 3:
        #     print(f"{self.name} has been fed a Potion!")
        #     self.health += 5
        #     return self.hunger
        # if self.hunger < 1:
        #     pass
        # else:

        # if self.hunger > 1 or food_choice == Pet.get_favorite_food(self):
        #     self.hunger -= 2
        #     print(f"Bonus: -5 hunger! That's {self.name}'s favorite food!")
        #     return self.hunger

        # if self.health == 0 or self.health < 90:
        #     self.health += 20
        #     print(f"{self.name} health is {self.health}")
        # elif self.health >= 90:
        #     print(f"{self.name} is not hungry")
        # elif self.health == 100:
        #     print("Already max health")

    # # you just need to change decrease health and decrease happiness methods
    # def status(self):
    #     time_elapsed = (int(time.time()) - self.start_time)
    #     print(f"Time elapsed: {time_elapsed} seconds")
    #     Pet.decrease_happiness(self)
    #     Pet.decrease_health(self)


class Snorlax(Pet):
    """
    Snorlax has a slow decrease in health and is always happy! But he gets hungry real quick.
    """

    def __init__(self, name, health, happiness, hunger, favorite_food):
        super().__init__(name, health, happiness, hunger, favorite_food)

    def speak(self):
        print("\n💤 ZZZZ.... ZZZZ... ZZZZZ 💤\n")

    def decrease_health(self):
        print(f"Health Before:  {1 + int(self.health)}")
        print("Your Snorlax's Health Decreased")
        if self.hunger > 99:
            self.health = self.health - ((int(time.time()) - self.start_time) / 25)
            print("Your Snorlax's hunger is at 100! Double health decrease!")
        else:
            self.health = self.health - ((int(time.time()) - self.start_time) / 50)
        if self.health < 1:
            self.health = 0
        print(f"Health After: {1 + int(self.health)}\n")

    def decrease_happiness(self):
        print(f"Happiness before: {int(self.happiness)}")
        print("Your Snorlax's Happiness Decreased")
        if self.happiness >= 99:
            self.happiness = 100
        self.happiness = self.happiness - ((int(time.time()) - self.start_time) / 25)
        if self.happiness < 1:
            self.happiness = 0
        print(f"Happiness after: {int(self.happiness)}\n")

    def increase_hunger(self):
        self.hunger += ((int(time.time()) - self.start_time) / 2)
        if self.hunger >= 99:
            self.hunger = 100
        if self.hunger < 1:
            self.hunger = 0
        print(f"New Hunger: {self.hunger}")


class Charizard(Pet):
    """
    Charizard is hard to please, it's happiness drops quickly, but it doesn't get hungry too fast.
    """

    def __init__(self, name, health, happiness, hunger, favorite_food):
        super().__init__(name, health, happiness, hunger, favorite_food)

    def speak(self):
        print("\nCHAR CHAR CHAAAAR CHAR CHAR 🔥\n")

    def decrease_health(self):
        print(f"Health before: {int(self.health)}")
        print("Your Charizard's health decreased")
        if self.hunger > 99:
            self.health = self.health - ((int(time.time()) - self.start_time) / 2)
            print("Your Charizard's hunger is at 100! Double health decrease!")
        else:
            self.health = self.health - ((int(time.time()) - self.start_time) / 4)
        if self.health < 1:
            self.health = 0
        print(f"Health after: {int(self.health)}\n")

    def decrease_happiness(self):
        print(f"Happiness before: {self.happiness}")
        print("Your Charizard's happiness decreased")
        self.happiness = self.happiness - ((int(time.time()) - self.start_time) / 5)
        if self.happiness < 1:
            self.happiness = 0
        print(f"Happiness after: {int(self.happiness)}\n")

    def increase_hunger(self):
        self.hunger += ((int(time.time()) - self.start_time) / 10)
        if self.hunger >= 99:
            self.hunger = 100
        if self.hunger < 1:
            self.hunger = 0
        print(f"New Hunger: {self.hunger}")


class Dragonite(Pet):
    """
    Dragonite is fair game. It's health, happiness and hunger drop at a balanced rate.
    """

    def __init__(self, name, health, happiness, hunger, favorite_food):
        super().__init__(name, health, happiness, hunger, favorite_food)

    def speak(self):
        print("\nDRAGONIIIIIIIIIIITE\n")

    def decrease_health(self):
        print(f"Health before: {int(self.health)}")
        print("Your Dragonite's Health decreased")
        if self.hunger > 99:
            self.health = self.health - ((int(time.time()) - self.start_time) / 8)
            print("Your Dragonite's hunger is at 100! Double health decrease!")
        else:
            self.health = self.health - ((int(time.time()) - self.start_time) / 16)
        if self.health < 1:
            self.health = 0
        print(f"Health After: {int(self.health)}\n")

    def decrease_happiness(self):
        print(f"Happiness before: {self.happiness}")
        print("Your Dragonite's happiness decreased")
        self.happiness = self.happiness - ((int(time.time()) - self.start_time) / 20)
        if self.happiness < 1:
            self.happiness = 0
        print(f"Happiness After: {int(self.happiness)}\n")

    def increase_hunger(self):
        self.hunger = self.hunger + ((int(time.time()) - self.start_time) / 5)
        if self.hunger >= 99:
            self.hunger = 100
        if self.hunger < 1:
            self.hunger = 0
        print(f"New Hunger: {self.hunger}")
