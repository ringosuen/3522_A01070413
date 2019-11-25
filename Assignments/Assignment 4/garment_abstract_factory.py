import abc
import enum


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

    def __init__(self, style: str, size: MenSize, colour: str, textile: str,
                 design: str, hidden_zippers: int):
        super().__init__(style, size, colour, textile)
        self.design = design
        self.hidden_zippers = hidden_zippers


class ShirtMenPineappleRepublic(ShirtMen):

    def __init__(self, style: str, size: MenSize, colour: str, textile: str,
                 ironing: bool, buttons: int):
        super().__init__(style, size, colour, textile)
        self.ironing = ironing
        self.buttons = buttons


class ShirtMenNika(ShirtMen):

    def __init__(self, style: str, size: MenSize, colour: str, textile: str,
                 in_out: str):
        super().__init__(style, size, colour, textile)
        self.in_out = in_out


class ShirtWomen(abc.ABC):

    def __init__(self, style: str, size: WomenSize, colour: str, textile: str):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class ShirtWomenLuluLime(ShirtWomen):
    def __init__(self, style: str, size: WomenSize, colour: str, textile: str,
                 design: str, hidden_zippers: int):
        super().__init__(style, size, colour, textile)
        self.design = design
        self.hidden_zippers = hidden_zippers


class ShirtWomenPineappleRepublic(ShirtWomen):
    def __init__(self, style: str, size: WomenSize, colour: str, textile: str,
                 ironing: bool, buttons: int):
        super().__init__(style, size, colour, textile)
        self.ironing = ironing
        self.buttons = buttons


class ShirtWomenNika(ShirtWomen):
    def __init__(self, style: str, size: WomenSize, colour: str, textile: str,
                 in_out: str):
        super().__init__(style, size, colour, textile)
        self.in_out = in_out


class SockPairUnisex(abc.ABC):

    def __init__(self, style: str, size: SockSize, colour: str, textile: str):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class SocksPairUnisexLuluLime(SockPairUnisex):
    def __init__(self, style: str, size: SockSize, colour: str, textile: str,
                 contains_silver: bool, contrasting_stripe: str):
        super().__init__(style, size, colour, textile)
        self.contains_silver = contains_silver
        self.contrasting_stripe = contrasting_stripe


class SocksPairUnisexPineappleRepublic(SockPairUnisex):
    def __init__(self, style: str, size: SockSize, colour: str, textile: str,
                 require_drycleaning: bool):
        super().__init__(style, size, colour, textile)
        self.require_drycleaning = require_drycleaning


class SocksPairUnisexNika(SockPairUnisex):
    def __init__(self, style: str, size: SockSize, colour: str, textile: str,
                 articulated: bool, sock_length: str):
        super().__init__(style, size, colour, textile)
        self.articulated = articulated
        self.sock_length = sock_length


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
    def create_socks_unisex(self) -> SockSize:
        pass


class LululimeFactory(BrandFactory):
    pass


class PineappleRepublicFactory(BrandFactory):
    pass


class NikaFactory(BrandFactory):
    pass
