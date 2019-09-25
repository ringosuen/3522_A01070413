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
        self.health = health
        self.happiness = happiness
        self.hunger = hunger
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
        print(f"Time elapsed: {time_elapsed} seconds")

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
                  f"Health Level: {1 + int(self.health)}\n"
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
            else:
                print(f"{self.name}'S HUNGER LEVEL IS AT 0 AND NOT HUNGRY")

    def eat_potion(self):
        if self.health > 99:
            print(f"{self.name} is MAX HEALTH ALREADY")
        else:
            print(f"{self.name} has been fed a Potion!")
            self.health += 5
            return self.health

    def eat_food(self):

        food_choice = random.randint(0, 2)

        print(food_choice)

        if food_choice == self.favorite_food:
            if food_choice == 0:
                print("Fed Berries")
            elif food_choice == 1:
                print("Fed Magikarp")
            elif food_choice == 2:
                print("Fed rare candy")
            print(f"Bonus: -5 hunger! That's {self.name}'s favorite food!")
            self.hunger -= 2
            print("after sbtract")
            return self.hunger
        else:
            if food_choice == 0:
                print(f"{self.name} has been fed berries!")
                self.hunger -= 20
                return self.hunger

            elif food_choice == 1:
                print(f"{self.name} has been fed Magikarp!")
                self.hunger -= 20
                return self.hunger

            elif food_choice == 2:
                print(f"{self.name} has been fed rare candy!")
                self.hunger -= 20
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
        print("ZZZZ.... ZZZZ... ZZZZZ")

    def decrease_health(self):
        print(f"Health before: {int(self.health)}")
        print("Your Snorlax's Health Decreased")
        # print((int(time.time()) - self.start_time))
        self.health = self.health - ((int(time.time()) - self.start_time) / 50)
        if self.health < 1:
            self.health = 0

        print(f"health after: {int(self.health)}")

    def decrease_happiness(self):
        print("DECREASE SNORLAX HAPPINESS")
        print(self.happiness)
        print((int(time.time()) - self.start_time))
        self.happiness = self.happiness - ((int(time.time()) - self.start_time))
        if self.happiness < 1:
            self.happiness = 0
        print(int(self.happiness))

    def increase_hunger(self):
        self.hunger = self.hunger + int(time.time()) - self.start_time
        if self.hunger >= 99:
            self.hunger = 100


class Charizard(Pet):
    """
    Charizard is hard to please, it's happiness drops quickly, but it doesn't get hungry too fast.
    """

    def __init__(self, name, health, happiness, hunger, favorite_food):
        super().__init__(name, health, happiness, hunger, favorite_food)

    def speak(self):
        print("CHAR CHAR CHAAAAR CHAR CHAR ")

    def decrease_health(self):
        print(f"Health before: {int(self.health)}")
        print("HEALTH CHAR DECREASE")
        # print((int(time.time()) - self.start_time))
        self.health = self.health - ((int(time.time()) - self.start_time) / 30)
        if self.health < 1:
            self.health = 0
        print(f"health after: {int(self.health)}")

    def decrease_happiness(self):
        print("DECREASE CHAR HAPPINESS")
        print(self.happiness)
        print((int(time.time()) - self.start_time))
        self.happiness = self.happiness - ((int(time.time()) - self.start_time))
        if self.happiness < 1:
            self.happiness = 0
        print(int(self.happiness))

    def increase_hunger(self):
        self.hunger = self.hunger + int(time.time()) - self.start_time
        if self.hunger >= 99:
            self.hunger = 100
        if self.hunger < 1:
            self.hunger = 0


class Dragonite(Pet):
    """
    Dragonite is fair game. It's health, happiness and hunger drop at a balanced rate.
    """

    def __init__(self, name, health, happiness, hunger, favorite_food):
        super().__init__(name, health, happiness, hunger, favorite_food)

    def speak(self):
        print("DRAGONIIIIIIIIIIITE")

    def decrease_health(self):
        print(f"Health before: {int(self.health)}")
        # print((int(time.time()) - self.start_time))
        self.health = self.health - ((int(time.time()) - self.start_time) / 10)
        if self.health < 1:
            self.health = 0
        print(f"health after: {int(self.health)}")

    def decrease_happiness(self):
        print("DECREASE DRAGONITE HAPPINESS")
        print(self.happiness)
        print((int(time.time()) - self.start_time))
        self.happiness = self.happiness - ((int(time.time()) - self.start_time))
        if self.happiness < 1:
            self.happiness = 0
        print(int(self.happiness))

    def increase_hunger(self):
        self.hunger = self.hunger + int(time.time()) - self.start_time
        if self.hunger >= 99:
            self.hunger = 100
