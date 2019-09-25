from pet import Pet, Snorlax, Charizard, Dragonite
import time
import random

start_time = int(time.time())


class Game:
    @staticmethod
    def hatch_new_egg():
        random_choice = random.randint(0, 2)

        if random_choice == 0:
            print("SNOOOOOOR .. lax")
            new_egg = Snorlax("Snorlax", 100, 100, 0, 0)
            return new_egg
        elif random_choice == 1:
            print("CHAAAAAAR CHAAAAAR CHAAAAR")
            new_egg = Charizard("Charizard", 100, 100, 0, 2)
            return new_egg
        elif random_choice == 2:
            print("DRA DRAGON DRAGONITE")
            new_egg = Dragonite("Dragonite", 100, 100, 0, 1)
            return new_egg

    @staticmethod
    def reset_stats(egg):
        egg.set_health(100)
        egg.set_happiness(100)
        egg.set_hunger(0)

    @staticmethod
    def status(egg):
        # time_elapsed = (int(time.time()) - start_time)
        # print(f"Time elapsed: {time_elapsed} seconds")
        egg.speak()
        egg.decrease_health()
        egg.decrease_happiness()
        egg.increase_hunger()
        Pet.display_stats(egg)
        egg.get_favorite_food()


# def display_menu(self):


def main():
    print("Lets hatch a new tamagotchi! Let's give it a couple seconds to hatch ... ...")
    time.sleep(2)
    new_hatch = Game.hatch_new_egg()

    print(f"Nice! Let's see what you hatched below: \n\n {new_hatch}")

    while True:
        if new_hatch.get_health() <= 0:
            print("YOUR TAMAGOTCHI IS DEAD! I GUESS WE'LL HATCH A NEW ONE...\n")
            time.sleep(3)
            Game.reset_stats(new_hatch)
            main()
        print(""" ======WHAT WOULD YOU LIKE TO DO?=======
            1. Status
            2. Feed
            3. Play
            4. Exit
            """)
        choice = int(input("Enter Choice:"))
        if choice == 1:
            # Pet.status(new_hatch)
            Game.status(new_hatch)
            # Pet.display_stats(new_hatch)
        elif choice == 2:
            new_hatch.feed()
        elif choice == 3:
            main()
        elif choice == 4:
            break
        else:
            print("Could not process input. ")


if __name__ == '__main__':
    main()
