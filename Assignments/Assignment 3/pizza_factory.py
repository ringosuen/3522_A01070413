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
        return self.decorated_pizza.get_cost() + 2.00

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Peppers"

class Mozzarella(BaseToppingDecorator):
    pass

class VeganCheese(BaseToppingDecorator):
    pass

class Peppers(BaseToppingDecorator):

    # def __init__(self, decorated_pizza):
    #     BaseToppingDecorator.__init__(self, decorated_pizza)

    def get_cost(self):
        return self.decorated_pizza.get_cost() + 2.00

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + " + Peppers"


class Pineapple(BaseToppingDecorator):
    pass


class Mushrooms(BaseToppingDecorator):
    pass


class FreshBasil(BaseToppingDecorator):
    pass


class Spinach(BaseToppingDecorator):
    pass


class Pepperoni(BaseToppingDecorator):
    pass


class BeyondMeat(BaseToppingDecorator):
    pass


def main():
    pizza_test = BasePizza()
    pizza_test = Peppers(pizza_test)

    print('Ingredients: ' + pizza_test.get_toppings() +
          '; Cost: ' + str(pizza_test.get_cost()))


if __name__ == '__main__':
    main()
