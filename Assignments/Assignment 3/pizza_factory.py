"""
This module depicts the decorator pattern in action and how it adds
toppings and cheese on top of a base pizza. It tallys up the toppings and
generates the total price of the pizza.
"""

import abc
import sys


class Pizza(abc.ABC):
    """
    The pizza interface that all concrete Pizza and decorators
    must adhere to. Thie interface defines getting the toppings and
    getting the price methods that do not have an implementation.
    """

    @abc.abstractmethod
    def get_toppings(self):
        pass

    @abc.abstractmethod
    def get_cost(self):
        pass


class BasePizza(Pizza):
    """
    The base pizza is responsible for getting the toppings and getting the
    costs of the pizza and the toppings added to the pizza. It implements the
    pizza interface as defined by the parent Pizza class. This is the object we
    are adding behaviours to.
    """
    def __init__(self):
        pass

    def get_toppings(self):
        """
        The base topping of the pizza is a minimum of one ingredient: The crust
        at 4.99. Decorators will modify the price accordingly.
        :return: Signature Crust $4.99
        """
        return "\n   Signature Crust $4.99\n"

    def get_cost(self):
        """
        The base price of the is 4.99. The decorators will modify and
        change the price accordingly.
        :return: 4.99
        """
        return 4.99


class BaseToppingDecorator(Pizza):
    """
    The base decorator that wraps around a Pizza concrete class. It does not
    add any new behaviours. Every other decorator inherit from this class.
    """
    def __init__(self, decorated_pizza):
        self.decorated_pizza = decorated_pizza

    def get_toppings(self):
        return self.decorated_pizza.get_toppings()

    def get_cost(self):
        return self.decorated_pizza.get_cost()


class Parmigiano(BaseToppingDecorator):
    """
    Decorator that adds Permigiano Reggiano
    cheese to a concrete Pizza. The cost is $4.99.
    """
    def get_cost(self):
        """
        Returns additional 4.99 on top of base pizza.
        :return: self.decorated_pizza.get_cost() + 4.99
        """
        return self.decorated_pizza.get_cost() + 4.99

    def get_toppings(self):
        """
        Returns additional Permigiano Rreggiano cheese on top of pizza.
        :return: self.decorated_pizza.get_toppings() + " + Parmigiano " \
                                                     "Reggiano Cheese $4.99"
        """
        return self.decorated_pizza.get_toppings() + " + Parmigiano " \
                                                     "Reggiano Cheese $4.99\n"


class Mozzarella(BaseToppingDecorator):
    """
    Decorator that adds Mozzarella cheese to the base concrete pizza.
    """
    def get_cost(self):
        """
        Returns an additional cost of 3.99 to base crust pizza.
        :return: self.decorated_pizza.get_cost() + 3.99
        """
        return self.decorated_pizza.get_cost() + 3.99

    def get_toppings(self):
        """
        Returns additional Fresh Mozzarella cheese on top of base pizza
        :return: self.decorated_pizza.get_toppings() + " + Fresh Mozzarella
        """
        return self.decorated_pizza.get_toppings() + " + Fresh Mozzarella" \
                                                     " $3.99\n"


class VeganCheese(BaseToppingDecorator):
    """
    Decorator that adds Vegan cheese to the base concrete pizza.
    """
    def get_cost(self):
        """
        Returns an additional cost of 5.99 to the base pizza.
        :return: self.decorated_pizza.get_cost() + 5.99
        """
        return self.decorated_pizza.get_cost() + 5.99

    def get_toppings(self):
        """
        Returns additional Vegan cheese on top of base pizza.
        :return: self.decorated_pizza.get_toppings() + " + Vegan Cheese $5.99"
        """
        return self.decorated_pizza.get_toppings() + " + Vegan Cheese $5.99\n"


class Peppers(BaseToppingDecorator):
    """
    Decorator that adds Pepper to the base concrete pizza.
    """
    def get_cost(self):
        """
        Returns an additional cost of 1.50 to the base pizza.
        :return: self.decorated_pizza.get_cost() + 1.50
        """
        return self.decorated_pizza.get_cost() + 1.50

    def get_toppings(self):
        """
        Returns peppers on top of base pizza.
        :return: self.decorated_pizza.get_toppings() + " + Peppers $1.50"
        """
        return self.decorated_pizza.get_toppings() + " + Peppers $1.50\n"


class Pineapple(BaseToppingDecorator):
    """
    Decorator that adds Pineapple to the base concrete pizza.
    """

    def get_cost(self):
        """
        Returns an additional cost of 2.00 to the base pizza.
        :return: self.decorated_pizza.get_cost() + 2.00
        """
        return self.decorated_pizza.get_cost() + 2.00

    def get_toppings(self):
        """
        Returns pineapple on top of base pizza.
        :return: self.decorated_pizza.get_toppings() + " + Pineapple $2.00"
        """
        return self.decorated_pizza.get_toppings() + " + Pineapple $2.00\n"


class Mushrooms(BaseToppingDecorator):
    """
    Decorator that adds Mushrooms to the base concrete pizza.
    """

    def get_cost(self):
        """
        Returns an additional cost of 1.50 to the base pizza.
        :return: self.decorated_pizza.get_cost() + 1.50
        """
        return self.decorated_pizza.get_cost() + 1.50

    def get_toppings(self):
        """
        Returns mushrooms on top of base pizza.
        :return: self.decorated_pizza.get_toppings() + " + Mushrooms $1.50"
        """
        return self.decorated_pizza.get_toppings() + " + Mushrooms $1.50\n"


class FreshBasil(BaseToppingDecorator):
    """
    Decorator that adds Fresh Basil to the base concrete pizza.
    """

    def get_cost(self):
        """
        Returns an additional cost of 2.00 to the base pizza.
        :return: self.decorated_pizza.get_cost() + 2.00
        """
        return self.decorated_pizza.get_cost() + 2.00

    def get_toppings(self):
        """
        Returns fresh basil on top of base pizza.
        :return: self.decorated_pizza.get_toppings() + " + Fresh Basil $2.00
        """
        return self.decorated_pizza.get_toppings() + " + Fresh Basil $2.00\n"


class Spinach(BaseToppingDecorator):
    """
    Decorator that adds Spinach to the base concrete pizza.
    """

    def get_cost(self):
        """
        Returns an additional cost of 1.00 to the base pizza.
        :return: self.decorated_pizza.get_cost() + 1.00
        """
        return self.decorated_pizza.get_cost() + 1.00

    def get_toppings(self):
        """
        Returns spinach on top of base pizza.
        :return: self.decorated_pizza.get_toppings() + " + Spinach $1.00"
        """
        return self.decorated_pizza.get_toppings() + " + Spinach $1.00\n"


class Pepperoni(BaseToppingDecorator):
    """
    Decorator that adds Pepperoni to the base concrete pizza.
    """

    def get_cost(self):
        """
        Returns an additional cost of 3.00 to the base pizza.
        :return: self.decorated_pizza.get_cost() + 3.00
        """

        return self.decorated_pizza.get_cost() + 3.00

    def get_toppings(self):
        """
        Returns pepporoni on top of base pizza.
        :return: self.decorated_pizza.get_toppings() + " + Pepperoni $3.00"
        """
        return self.decorated_pizza.get_toppings() + " + Pepperoni $3.00\n"


class BeyondMeat(BaseToppingDecorator):
    """
    Decorator that adds Beyond Meat to the base concrete pizza.
    """

    def get_cost(self):
        """
        Returns an additional cost of 4.00 to the base pizza.
        :return: self.decorated_pizza.get_cost() + 4.00
        """
        return self.decorated_pizza.get_cost() + 4.00

    def get_toppings(self):
        """
        Returns beyond meat on top of base pizza.
        :return: self.decorated_pizza.get_toppings() + " + Beyond Meat $4.00"
        """
        return self.decorated_pizza.get_toppings() + " + Beyond Meat $4.00\n"


def main():
    """
    User menu that asks user to add Cheese, then toppings or checkout
    """
    pizza = BasePizza()

    print("Welcome to Python Pizza Factory, let's build your pizza!")

    print(""" ======First, Select a Cheese=======
                           1. Reggiano Cheese
                           2. Fresh Mozzarella
                           3. Vegan Cheese
                           """)
    try:
        cheese_choice = int(input("Choose 1,2 or 3:"))
        if cheese_choice == 1:
            print("Reggiano cheese added")
            has_reggiano = True
        else:
            has_reggiano = False
        if cheese_choice == 2:
            print("Fresh Mozzearella added")
            has_mozzarella = True
        else:
            has_mozzarella = False
        if cheese_choice == 3:
            print("Vegan Cheese Added")
            has_vcheese = True
        else:
            has_vcheese = False

        if has_reggiano:
            pizza = Parmigiano(pizza)
        if has_mozzarella:
            pizza = Mozzarella(pizza)
        if has_vcheese:
            pizza = VeganCheese(pizza)
        else:
            if cheese_choice == 0 or cheese_choice >= 4:
                print("Invalid number choice. Enter a number between 1 and 3")
                main()

        print('\nCurrent Ingredients: ' + pizza.get_toppings() +
              'Current Cost: ' + f"$%.2f" % pizza.get_cost())
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter an integer between 1-3")
        main()

    while True:
        try:
            add_more_cheese = input("\nAdd more cheese? Y/N: ")
            if add_more_cheese.lower() == 'n':
                print("Add toppings or checkout now")
                break
            elif add_more_cheese.lower() is not 'n' or 'y':
                print("=== Input Y or N Please! ===")
            if add_more_cheese.lower() == 'y':
                print("LET'S ADD MORE CHEESE!")
                print(""" ======Select a Cheese=======
                        1. Reggiano Cheese
                        2. Fresh Mozzarella
                        3. Vegan Cheese
                                          """)
                cheese_choice = int(input("Choose 1,2 or 3:"))
                if cheese_choice == 1:
                    print("Reggiano cheese added")
                    has_reggiano = True
                else:
                    has_reggiano = False
                if cheese_choice == 2:
                    print("Fresh Mozzearella added")
                    has_mozzarella = True

                else:
                    has_mozzarella = False
                if cheese_choice == 3:
                    print("Vegan Cheese Added")
                    has_vcheese = True
                else:
                    has_vcheese = False
                if has_reggiano:
                    pizza = Parmigiano(pizza)

                if has_mozzarella:
                    pizza = Mozzarella(pizza)

                if has_vcheese:
                    pizza = VeganCheese(pizza)

                elif cheese_choice == 0 or cheese_choice >= 4:
                    print("No cheese added! Input an integer between 1-3."
                          " Try Again")

                print('\nIngredients: ' + pizza.get_toppings() +
                      'Cost: ' + f"$%.2f" % pizza.get_cost())
        except ValueError as e:
            print(f"{e}. Try Again")

    while True:
        print("""       ======ADD TOPPINGS OR CHECKOUT=======
                                1. Add Toppings
                                2. Checkout
                                        """)
        try:
            choice = int(input("Please Select 1 or 2: "))
            if choice == 1:
                print("""                   ======ADD TOPPINGS =======
                               1. Add Peppers
                               2. Add Pineapple 
                               3. Add Mushrooms
                               4. Add Fresh Basil 
                               5. Add Spinach
                               6. Add Pepperoni 
                               7. Add Beyond Meat 
                     """)
                topping_choice = int(input("Please select 1-7: "))
                if topping_choice == 1:
                    print("Peppers added")
                    has_pepper = True
                else:
                    has_pepper = False
                if topping_choice == 2:
                    print("Pineapple added")
                    has_pineapple = True
                else:
                    has_pineapple = False
                if topping_choice == 3:
                    print("Mushrooms added")
                    has_mushrooms = True
                else:
                    has_mushrooms = False
                if topping_choice == 4:
                    print("Fresh Basil Added")
                    has_freshbasil = True
                else:
                    has_freshbasil = False
                if topping_choice == 5:
                    print("Spinach Added")
                    has_spinach = True
                else:
                    has_spinach = False
                if topping_choice == 6:
                    print("Pepperoni Added")
                    has_pepperoni = True
                else:
                    has_pepperoni = False
                if topping_choice == 7:
                    print("Beyond Meat Added")
                    has_beyondmeat = True
                else:
                    has_beyondmeat = False
                if topping_choice == 0 or topping_choice >= 8:
                    print("Invalid Choice. Nothing Added. Choose 1-7 next "
                          "time")
                if has_pepper:
                    pizza = Peppers(pizza)
                if has_pineapple:
                    pizza = Pineapple(pizza)
                if has_mushrooms:
                    pizza = Mushrooms(pizza)
                if has_freshbasil:
                    pizza = FreshBasil(pizza)
                if has_spinach:
                    pizza = Spinach(pizza)
                if has_pepperoni:
                    pizza = Pepperoni(pizza)
                if has_beyondmeat:
                    pizza = BeyondMeat(pizza)

                print('Current Ingredients: ' + pizza.get_toppings() +
                      'Current Cost: ' + f"$%.2f" % pizza.get_cost())

            if choice == 2:
                print("ENJOY THE PIZZA! Here's the total: ")
                print('\nToppings Added:\n' + pizza.get_toppings())

                print('\nTotal Cost: ' + f"$%.2f" % pizza.get_cost())

                sys.exit()
            elif choice == 0 or choice >= 3:
                print("Invalid choice. Please choose 1 or 2")
        except ValueError as e:
            print(f"{e} Invalid Value. Please choose 1 or 2.")


if __name__ == '__main__':
    main()
