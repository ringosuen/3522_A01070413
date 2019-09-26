from pet import Pet, Snorlax, Charizard, Dragonite
import time
import random

start_time = int(time.time())


class Game:
    """
    Represents a UI for the game.
    Allows the user to interact with the Pokemon through
    menu selection.
    """

    @staticmethod
    def hatch_new_egg():
        """
        Hatches a new Pokemon at random and displays a special message.
        :return: new_egg
        """
        random_choice = random.randint(0, 2)

        if random_choice == 0:
            print("🍱🌰🍚🍗🍰🍟🍩🍟🍹🍋 SNOOOOOOR? .. lax\n")
            new_egg = Snorlax("Snorlax", 100, 100, 0, 0)
            return new_egg
        elif random_choice == 1:
            print(" 🔥🔥🔥 CHAAAAAAR CHAAAAAR CHAAAAR 🔥🔥🔥 \n")
            new_egg = Charizard("Charizard", 100, 100, 0, 2)
            return new_egg
        elif random_choice == 2:
            print("💨☁️🌪🌤 🐲 DRA DRAGOOOOON DRAGONITE \n")
            new_egg = Dragonite("Dragonite", 100, 100, 0, 1)
            return new_egg

    @staticmethod
    def reset_stats(egg):
        """
        Resets the stats when a Pokemon dies and the game hatches a new egg.
        """
        egg.set_health(100)
        egg.set_happiness(100)
        egg.set_hunger(0)

    @staticmethod
    def status(egg):
        """
        This is responsible for allowing the player
        to check the status of their Pokemon. It checks the time elapsed since
        the last time the player has checked and updates the stats accordingly.
        """

        egg.speak()
        egg.decrease_health()
        egg.decrease_happiness()
        egg.increase_hunger()
        Pet.display_stats(egg)

    @staticmethod
    def display_menu():
        """
        A guide for the user to know what's going on and
        allows user to interact with the Pokemon.
        """

        print("\nLets hatch a new Pokemon! Let's give it a couple seconds to hatch\n ... \n ... \n")
        time.sleep(2)
        new_hatch = Game.hatch_new_egg()
        print(f"Nice! Let's see what you hatched below: \n\n {new_hatch}")

        while True:
            if new_hatch.get_health() <= 0:
                print("YOUR POKEMON IS DEAD! I GUESS WE'LL HATCH A NEW ONE...\n")
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
                Game.status(new_hatch)
            elif choice == 2:
                new_hatch.feed()
            elif choice == 3:
                new_hatch.play()
            elif choice == 4:
                print("Bye!")
                break
            else:
                print("Could not process input. ")


def main():
    """
    The main method that calls the display menu method.
    """
    Game.display_menu()


if __name__ == '__main__':
    main()
