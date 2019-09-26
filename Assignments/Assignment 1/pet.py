import random
import time
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
                  f"Hunger Level: {int(self.hunger)}\n")
        elif self.happiness <= 0:
            print(f"---- Tamagotchi Type: {self.get_name()} ----\n"
                  f"Health Level: {int(self.health)}\n"
                  f"Happiness Level: 0\n"
                  f"Hunger Level: {int(self.hunger)}\n")
        elif self.health <= 0:
            print(f"---- Tamagotchi Type: {self.get_name()} ----\n"
                  f"Health Level: 0\n"
                  f"Happiness Level: {int(self.happiness)}\n"
                  f"Hunger Level: {int(self.hunger)}\n")
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
            if choice == 1 and self.hunger > 0:
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
            print(f"{self.name} has been fed a Potion! 🍶\n")
            self.health += 50
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
            print(f"Bonus: -25 hunger! That's {self.name}'s favorite food!\n")
            self.hunger -= 25
            return self.hunger
        else:
            if food_choice == 0:
                print(f"{self.name} has been fed berries! 🍒🍈🍒\n")
                self.hunger -= 23
                return self.hunger

            elif food_choice == 1:
                print(f"{self.name} has been fed Magikarp! 🐟🐟🐟\n")
                self.hunger -= 23
                return self.hunger

            elif food_choice == 2:
                print(f"{self.name} has been fed rare candy! 🍬🍭🍬\n")
                self.hunger -= 23
                return self.hunger


class Snorlax(Pet):
    """
    Snorlax has a slow decrease in health and is always happy! But he gets hungry real quick.
    """

    def __init__(self, name, health, happiness, hunger, favorite_food):
        super().__init__(name, health, happiness, hunger, favorite_food)

    def speak(self):
        print("\n💤 ZZZZ.... ZZZZ... ZZZZZ 💤\n")

    def decrease_health(self):
        if self.health > 100:
            self.health = 100
        print(f"Health Before:  { int(self.health)}")
        if self.hunger > 99 and self.health < 75:
            self.health = self.health - ((int(time.time()) - self.start_time) / 10)
            print("Your Snorlax's hunger is at 100! Double health decrease!")
            print("Snorlax's health is below 75! Snorlax has fallen a little sick..")
        elif self.hunger > 99:
            self.health = self.health - ((int(time.time()) - self.start_time) / 10)
            print("Your Snorlax's hunger is at 100! Double health decrease!")
        elif self.health < 75:
            print("Snorlax's health is below 75! Snorlax has fallen a little sick..")
            self.health = self.health - ((int(time.time()) - self.start_time) / 2)
        else:
            self.health = self.health - ((int(time.time()) - self.start_time) / 20)
        if self.health < 1:
            self.health = 0
        print(f"Health After: {int(self.health)}\n")

    def decrease_happiness(self):
        print(f"Happiness Before: {int(self.happiness)}")
        if self.happiness >= 99:
            self.happiness = 100
        self.happiness = self.happiness - ((int(time.time()) - self.start_time) / 5)
        if self.happiness < 1:
            self.happiness = 0
        print(f"Happiness After: {int(self.happiness)}\n")

    def increase_hunger(self):
        self.hunger += ((int(time.time()) - self.start_time) / 2)
        if self.hunger >= 99:
            self.hunger = 100
        if self.hunger < 1:
            self.hunger = 0
        print(f"New Hunger: {int(self.hunger)}")


class Charizard(Pet):
    """
    Charizard is hard to please, it's happiness drops quickly, but it doesn't get hungry too fast.
    """

    def __init__(self, name, health, happiness, hunger, favorite_food):
        super().__init__(name, health, happiness, hunger, favorite_food)

    def speak(self):
        print("\nCHAR CHAR CHAAAAR CHAR CHAR 🔥\n")

    def decrease_health(self):
        if self.health > 99:
            self.health = 100
        print(f"Health before: {int(self.health)}")
        if self.hunger > 99 and self.health < 60:
            self.health = self.health - ((int(time.time()) - self.start_time) / 1.5)
            print("Your Charizard's hunger is at 100! Double health decrease!")
            print("Charizard's health is below 75! Charizard has fallen a little sick..")
        elif self.hunger > 99:
            self.health = self.health - ((int(time.time()) - self.start_time) / 1.5)
            print("Your Charizard's hunger is at 100! Double health decrease!")
        elif self.health < 60:
            print("Charizard's health is below 60! Charizard has fallen sick..")
            self.health = self.health - ((int(time.time()) - self.start_time) / 2)
        else:
            self.health = self.health - ((int(time.time()) - self.start_time) / 3)
        if self.health < 1:
            self.health = 0
        print(f"Health after: {int(self.health)}\n")

    def decrease_happiness(self):
        print(f"Happiness Before: {int(self.happiness)}")
        self.happiness = self.happiness - ((int(time.time()) - self.start_time) / 2)
        if self.happiness < 1:
            self.happiness = 0
        print(f"Happiness after: {int(self.happiness)}\n")

    def increase_hunger(self):
        self.hunger += ((int(time.time()) - self.start_time) / 10)
        if self.hunger >= 99:
            self.hunger = 100
        if self.hunger < 1:
            self.hunger = 0
        print(f"New Hunger: {int(self.hunger)}")


class Dragonite(Pet):
    """
    Dragonite is fair game. It's health, happiness and hunger drop at a balanced rate.
    """

    def __init__(self, name, health, happiness, hunger, favorite_food):
        super().__init__(name, health, happiness, hunger, favorite_food)

    def speak(self):
        print("\nDRAGONIIIIIIIIIIITE\n")

    def decrease_health(self):
        if self.health > 99:
            self.health = 100
        print(f"Health before: {int(self.health)}")
        if self.hunger > 99 and self.health < 70:
            self.health = self.health - ((int(time.time()) - self.start_time) / 2)
            print("Your Charizard's hunger is at 100! Double health decrease!")
            print("Charizard's health is below 75! Charizard has fallen a little sick..")
        if self.hunger > 99:
            self.health = self.health - ((int(time.time()) - self.start_time) / 2)
            print("Your Dragonite's hunger is at 100! Double health decrease!")
        elif self.health < 70:
            print("Dragonite's health is below 70! Dragonite has fallen sick..")
            self.health = self.health - ((int(time.time()) - self.start_time) / 3)
        else:
            self.health = self.health - ((int(time.time()) - self.start_time) / 4)

        if self.health < 1:
            self.health = 0
        print(f"Health After: {int(self.health)}\n")

    def decrease_happiness(self):
        print(f"Happiness Before: {int(self.happiness)}")
        self.happiness = self.happiness - ((int(time.time()) - self.start_time) / 4)
        if self.happiness < 1:
            self.happiness = 0
        print(f"Happiness After: {int(self.happiness)}\n")

    def increase_hunger(self):
        self.hunger = self.hunger + ((int(time.time()) - self.start_time) / 5)
        if self.hunger >= 99:
            self.hunger = 100
        if self.hunger < 1:
            self.hunger = 0
        print(f"New Hunger: {int(self.hunger)}")
