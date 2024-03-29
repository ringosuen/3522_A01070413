"""
This module depicts the use of the Abstract Factory Pattern for a garment
factory that needs groups of brands for different clothing types.
"""
import abc
import enum
import json

import pandas
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


class MenSize(enum.Enum):
    S = 1,
    M = 2,
    L = 3,
    XL = 4,
    XXL = 5


class WomenSize(enum.Enum):
    XS = 0,
    S = 1,
    M = 2,
    L = 3,
    XL = 4,
    XXL = 5


class SockSize(enum.Enum):
    S = 1,
    M = 2,
    L = 3,


class ShirtMen(abc.ABC):
    """
    ShirtMen defines the interface for one of the products the
    Brand Factory is responsible to create.
    """

    def __init__(self, style: str, size: MenSize, colour: str, textile: str):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class ShirtMenLulu(ShirtMen):
    """
    ShirtMenLulu is a type of ShirtMen
    """

    def __init__(self, style: str, size: MenSize, colour: str, textile: str,
                 design: str, hidden_zippers: int):
        super().__init__(style, size, colour, textile)
        self.design = design
        self.hidden_zippers = hidden_zippers

    def __str__(self):
        return f"---- Style: {self.style} ----\n" \
               f"Size: {self.size}\n" \
               f"Colour: {self.colour}\n" \
               f"Design: {self.textile}\n" \
               f"Design: {self.design}\n" \
               f"Hidden Zippers: {self.hidden_zippers}"


class ShirtMenPineappleRepublic(ShirtMen):
    """
    ShirtMenPineappleRepublic is a type of ShirtMen
    """

    def __init__(self, style: str, size: MenSize, colour: str, textile: str,
                 ironing: str, buttons: int):
        super().__init__(style, size, colour, textile)
        self.ironing = ironing
        self.buttons = buttons

    def __str__(self):
        return f"---- Style: {self.style} ----\n" \
               f"Size: {self.size}\n" \
               f"Colour: {self.colour}\n" \
               f"Design: {self.textile}\n" \
               f"Ironing: {self.ironing}\n" \
               f"Buttons: {self.buttons}"


class ShirtMenNika(ShirtMen):
    """
    ShirtMenNika is a type of ShirtMen
    """

    def __init__(self, style: str, size: MenSize, colour: str, textile: str,
                 in_out: str):
        super().__init__(style, size, colour, textile)
        self.in_out = in_out

    def __str__(self):
        return f"---- Style: {self.style} ----\n" \
               f"Size: {self.size}\n" \
               f"Colour: {self.colour}\n" \
               f"Design: {self.textile}\n" \
               f"Outdoor or Indoor: {self.in_out}\n"


class ShirtWomen(abc.ABC):
    """
    ShirtWomen defines the interface for one of the products the
    Brand Factory is responsible to create.
    """

    def __init__(self, style: str, size: WomenSize, colour: str, textile: str):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class ShirtWomenLuluLime(ShirtWomen):
    """
    ShirtWomenLuluLime is a type of ShirtWomen.
    """

    def __init__(self, style: str, size: WomenSize, colour: str, textile: str,
                 design: str, hidden_zippers: int):
        super().__init__(style, size, colour, textile)
        self.design = design
        self.hidden_zippers = hidden_zippers

    def __str__(self):
        return f"---- Style: {self.style} ----\n" \
               f"Size: {self.size}\n" \
               f"Colour: {self.colour}\n" \
               f"Design: {self.textile}\n" \
               f"Design: {self.design}\n" \
               f"Hidden Zippers: {self.hidden_zippers}"


class ShirtWomenPineappleRepublic(ShirtWomen):
    """
    ShirtWomenPineappleRepublic is a type of ShirtWomen.
    """

    def __init__(self, style: str, size: WomenSize, colour: str, textile: str,
                 ironing: str, buttons: int):
        super().__init__(style, size, colour, textile)
        self.ironing = ironing
        self.buttons = buttons

    def __str__(self):
        return f"---- Style: {self.style} ----\n" \
               f"Size: {self.size}\n" \
               f"Colour: {self.colour}\n" \
               f"Design: {self.textile}\n" \
               f"Ironing: {self.ironing}\n" \
               f"Buttons: {self.buttons}"


class ShirtWomenNika(ShirtWomen):
    """
    ShirtWomenNika is a type of ShirtWomen.
    """

    def __init__(self, style: str, size: WomenSize, colour: str, textile: str,
                 in_out: str):
        super().__init__(style, size, colour, textile)
        self.in_out = in_out

    def __str__(self):
        return f"---- Style: {self.style} ----\n" \
               f"Size: {self.size}\n" \
               f"Colour: {self.colour}\n" \
               f"Design: {self.textile}\n" \
               f"Outdoor or Indoor: {self.in_out}\n"


class SockPairUnisex(abc.ABC):
    """
    SocksPairUnisex defines the interface for one of the products the
    Brand Factory is responsible to create.
    """

    def __init__(self, style: str, size: SockSize, colour: str, textile: str):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class SocksPairUnisexLuluLime(SockPairUnisex):
    """
    SocksPairUnisexLuluLime is a type of SockPairUnisex.
    """

    def __init__(self, style: str, size: SockSize, colour: str, textile: str,
                 contains_silver: str, contrasting_stripe: str):
        super().__init__(style, size, colour, textile)
        self.contains_silver = contains_silver
        self.contrasting_stripe = contrasting_stripe

    def __str__(self):
        return f"---- Style: {self.style} ----\n" \
               f"Size: {self.size}\n" \
               f"Colour: {self.colour}\n" \
               f"Design: {self.textile}\n" \
               f"Has Silver: {self.contains_silver}\n" \
               f"Contrasting Stripe: {self.contrasting_stripe}"


class SocksPairUnisexPineappleRepublic(SockPairUnisex):
    """
    SocksPairUnisexPineappleRepublic is a type of SockPairUnisex.
    """

    def __init__(self, style: str, size: SockSize, colour: str, textile: str,
                 require_drycleaning: str):
        super().__init__(style, size, colour, textile)
        self.require_drycleaning = require_drycleaning

    def __str__(self):
        return f"---- Style: {self.style} ----\n" \
               f"Size: {self.size}\n" \
               f"Colour: {self.colour}\n" \
               f"Design: {self.textile}\n" \
               f"Dry Cleaning: {self.require_drycleaning}\n"


class SocksPairUnisexNika(SockPairUnisex):
    """
    SocksPairUnisexNika is a type of SockPairUnisex.
    """

    def __init__(self, style: str, size: SockSize, colour: str, textile: str,
                 articulated: str, sock_length: str):
        super().__init__(style, size, colour, textile)
        self.articulated = articulated
        self.sock_length = sock_length

    def __str__(self):
        return f"---- Style: {self.style} ----\n" \
               f"Size: {self.size}\n" \
               f"Colour: {self.colour}\n" \
               f"Design: {self.textile}\n" \
               f"Articulated: {self.articulated}\n" \
               f"Sock Length: {self.sock_length}"


class BrandFactory(abc.ABC):
    """
    The base factory class. The BrandFactory class defines an interface
    to create the a Brand family consisting of Lululime, PineappleRepublic,
    and Nika.
    """

    @abc.abstractmethod
    def create_shirt_men(self) -> ShirtMen:
        pass

    @abc.abstractmethod
    def create_shirt_women(self) -> ShirtWomen:
        pass

    @abc.abstractmethod
    def create_socks_unisex(self) -> SockPairUnisex:
        pass


class LululimeFactory(BrandFactory):
    """
    This factory class implements the BrandFactory Interface. It
    returns a product family consisting of ShirtMenLulu, ShirtWomenLuluLime,
    and SocksPairUnisexLuluLime.
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        """
        :param kwargs:
        :return: ShirtMenLulu
        """
        return ShirtMenLulu(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        """
        :param kwargs:
        :return: ShirtWomenLuluLime
        """
        return ShirtWomenLuluLime(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        """
        :param kwargs:
        :return: SocksPairUnisexLuluLime
        """
        return SocksPairUnisexLuluLime(**kwargs)


class PineappleRepublicFactory(BrandFactory):
    """
    This factory class implements the BrandFactory Interface. It
    returns a product family consisting of ShirtMenPineappleRepublic,
    ShirtWomenPineappleRepublic, and SocksPairUnisexPineappleRepublic.
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        """
        :param kwargs:
        :return: ShirtMenPineappleRepublic
        """
        return ShirtMenPineappleRepublic(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        """
        :param kwargs:
        :return: ShirtWomenPineappleRepublic
        """
        return ShirtWomenPineappleRepublic(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        """
        :param kwargs:
        :return: SocksPairUnisexPineappleRepublic
        """
        return SocksPairUnisexPineappleRepublic(**kwargs)


class NikaFactory(BrandFactory):
    """
    This factory class implements the BrandFactory Interface. It
    returns a product family consisting of ShirtMenNika,
    ShirtWomenNika, and SocksPairUnisexNika.
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        """
        :param kwargs:
        :return: ShirtMenNika
        """
        return ShirtMenNika(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        """
        :param kwargs:
        :return: ShirtWomenNika
        """
        return ShirtWomenNika(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        """
        :param kwargs:
        :return: SocksPairUnisexNika
        """
        return SocksPairUnisexNika(**kwargs)


class GarmentMaker:
    """
    A driver class that initializes three arraylist instance variables
    called shirtsMen, shirtsWomen, and socksUnisex. The day's orders are placed
    into each ArrayList and then sent at the end of each working day
    """

    def __init__(self, brand_factory: BrandFactory):
        self.shirt_men = []
        self.shirt_women = []
        self.socks_unisex = []
        self.populate_factory = brand_factory

        for i in range(3):
            self.shirt_men.append(self.populate_factory.create_shirt_men())
        for i in range(3):
            self.shirt_women.append(self.populate_factory.create_shirt_women())
        for i in range(3):
            self.socks_unisex.append(
                self.populate_factory.create_socks_unisex())

    def make_lulu(self):
        for shirtm in self.shirt_men:
            print(f"{shirtm.style}")


def jprint(obj):
    """
    Create and print a formatted string of the Python JSON object
    """
    #
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


class OrderProcessor:
    """
    Responsible for processing the excel file. Object must be instantiated
    by the GarmentMaker class and must be an instance variable for the
    orderProcessor object tot he GarmentMaker.
    """

    def __init__(self, file_path):
        """
        Initializes a CityDatabase object by reading an excel file of
        city information using pandas, converting the data into a City
        object and storing it in a list.
        :param file_path: the file path to an excel file.
        :precondition file_path: the excel file at the specified path should
        have 3 columns with the headers "city_ascii", "lat", and "lng"
        """
        # will raise an error if the path is invalid, we don't need an
        # if statement here
        df = pandas.read_excel(file_path)

        """
        read in the cities using a dictionary comprehension
        dictionary = { key: value for elem in iterable }
        In this case we are reading in the name of the city as the key
        and its corresponding CityLocation object as the value. We
        have made the assumption that each city has a unique name.
        """
        #
        self.lulu = [Order(row[1]["Date"], row[1]["Order Number"],
                                 row[1]["Brand"], row[1]["Garment"],
                                 row[1]["Count"], row[1]["Style name"])
                           for row in df.iterrows()
                           if row[1]["Brand"] == "Lululime"]
        self.lulu = LululimeFactory()
        GarmentMaker(self.lulu)
        # brand = self.lulu[0].brand
        # garment = self.lulu[0].garment
        # print(brand)
        # print(garment)

        lulu_order = ((row[1]["Date"], row[1]["Garment"],
                       row[1]["Brand"], row[1]["Garment"])
                      for row in df.iterrows() if
                      row[1]["Brand"] == "Lululime")
        for item in lulu_order:
            print(item)

        lulu_order = LululimeFactory()
        # test = GarmentMaker(lulu_order)
        # print(test)

        # for lulu in self.lulubrand:
        #     print(lulu)
        # print(*self.lulubrand)

    def openOrderSheet(self) -> BrandFactory:
        pass
        # df = pandas.read_excel(file_path)
        # self.garment_db = [Order(row[1]["city_ascii"], row[1]["lat"],
        #                          row[1]["lng"])
        #                    for row in df.iterrows()]

    def processNextOrder(self):
        pass


class Order:

    def __init__(self, date: str, ord_num: int, brand: str, garment: str,
                 count: str, style: str):
        self.date = date
        self.ord_num = ord_num
        self.brand = brand
        self.garment = garment
        self.count = count
        self.style = style

    def __str__(self):
        return f"Date: {self.date}, Ord Num: {self.ord_num}, " \
               f"Brand: {self.brand}, " \
               f"Garment: {self.garment}, " \
               f"Count: {self.count}, " \
               f"Style: {self.style} "


def main():
    df = pd.read_excel('COMP_3522_A4_orders.xlsx', sheet_name=0)

    style = df['Style name']

    data = OrderProcessor('COMP_3522_A4_orders.xlsx')
    # lulu_list = data.lulubrand
    lulu_list = data.lulu
    for item in lulu_list:
        print(item)
    # data_list = LululimeFactory()
    # print(data_list)
    # garment = GarmentMaker(data_list)
    # print(garment)
    # for item in lulu_list:
    #     print(item)

    # print(pd.read_excel('COMP_3522_A4_orders.xlsx', index_col=5))
    lululime = LululimeFactory()
    pineapple_republic = PineappleRepublicFactory()
    nika = NikaFactory()
    # garment_maker = GarmentMaker(data_list)
    # garment_maker.garment_type()
    # garment_maker2 = GarmentMaker(pineapple_republic)
    # print(garment_maker)
    # print(garment_maker2)

    shirt = lululime.create_shirt_men(style=style,
                                      size=MenSize.S,
                                      colour="BLACK",
                                      textile="COTTON",
                                      design="Yoga",
                                      hidden_zippers=5)
    # shirt1 = data_list.create_shirt_men(style="hi",
    #                                   size=MenSize.S,
    #                                   colour="BLACK",
    #                                   textile="COTTON",
    #                                   design="Yoga",
    #                                   hidden_zippers=5)
    # print(shirt)
    # print(type(shirt))
    # print((shirt1))

    df = pd.read_excel('COMP_3522_A4_orders.xlsx', sheet_name=0)

    lulu = df['Brand']
    # if lulu == "Lululime":
    # print(lulu)
    # sepalLength = df['Sepal length']
    # petalLength = df['Petal length']

    test_shirt = ShirtMenLulu("a", MenSize.s, "c", "d", "e", 2)

    # GarmentMaker()


if __name__ == '__main__':
    main()
