import abc


class Pizza(abc.ABC):

    @abc.abstractmethod
    def get_toppings(self):
        pass

    @abc.abstractmethod
    def get_cost(self):
        pass


class BasePizza(Pizza):
    def __init__(self):
        pass

    def get_toppings(self):
        return "Signature crust"

    def get_cost(self):
        return 4.99


class BaseToppingDecorator(Pizza):
    def __init__(self, decorated_pizza):
        self.decorated_pizza = decorated_pizza

    def get_toppings(self):
        return self.decorated_pizza.get_toppings()

    def get_cost(self):
        return self.decorated_pizza.get_cost()

class Parmigiano(BaseToppingDecorator):
    def get_cost(self):
        return self.decorated_pizza.get_cost() + 4.99

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Parmigiano " \
                                                     "Reggiano Cheese "

class Mozzarella(BaseToppingDecorator):
    def get_cost(self):
        return self.decorated_pizza.get_cost() + 3.99

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Fresh Mozzarella"

class VeganCheese(BaseToppingDecorator):
    def get_cost(self):
        return self.decorated_pizza.get_cost() + 5.99

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Vegan Cheese"

class Peppers(BaseToppingDecorator):

    # def __init__(self, decorated_pizza):
    #     BaseToppingDecorator.__init__(self, decorated_pizza)

    def get_cost(self):
        return self.decorated_pizza.get_cost() + 1.50

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Peppers"


class Pineapple(BaseToppingDecorator):
    def get_cost(self):
        return self.decorated_pizza.get_cost() + 2.00

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Pineapple"


class Mushrooms(BaseToppingDecorator):
    def get_cost(self):
        return self.decorated_pizza.get_cost() + 1.50

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Mushrooms"


class FreshBasil(BaseToppingDecorator):
    def get_cost(self):
        return self.decorated_pizza.get_cost() + 2.00

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Fresh Basil"


class Spinach(BaseToppingDecorator):
    def get_cost(self):
        return self.decorated_pizza.get_cost() + 1.00

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Spinach"


class Pepperoni(BaseToppingDecorator):
    def get_cost(self):
        return self.decorated_pizza.get_cost() + 3.00

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Pepperoni"


class BeyondMeat(BaseToppingDecorator):
    def get_cost(self):
        return self.decorated_pizza.get_cost() + 4.00

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Beyond Meat"


def main():
    pizza_test = BasePizza()
    pizza_test = Peppers(pizza_test)

    print('Ingredients: ' + pizza_test.get_toppings() +
          '; Cost: ' + str(pizza_test.get_cost()))


if __name__ == '__main__':
    main()
