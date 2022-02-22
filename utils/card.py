"""
In this file the Symbol class and Card class are set up
"""


class Symbol:
    """
    This class represents the suit of a card as a symbol.

    Attributes
    ----------
    icon: represents the suit of a card.
    color: depending on the icon this is red or black.
    """

    def __init__(self, icon: str):
        """
        Function to initialize Symbol class objects
        :param icon: a str that represents the suit of a card

        :initializes:
        icon: as param icon
        color: as str 'black' or 'red' depending on the param icon
        """
        self.icon = icon
        if icon in ["♥", "♦"]:
            self.color = "red"
        elif icon in ["♣", "♠"]:
            self.color = "black"

    def __str__(self) -> str:
        return f"The icon is {self.icon} and the color is {self.color}"


class Card(Symbol):
    """
    This class represents a card.
    This class inherits from the Symbol class.

    Attributes
    ----------
    value:  a str that represents the value of the card

    inherited from Symbol class:
    icon: a str is the suit of the card
    color: a str to represent the color of the suit
    """

    def __init__(self, value: str, icon: str):
        """
        Function that initializes Card Class objects

        :param value: a str that represents the value of the card
        :param icon: a str that represents the suit of the card

        :initializes:
        value as param value
        icon as param icon
        """
        super().__init__(icon)
        self.value = value

    def __str__(self) -> str:
        return f"The value of this card is {self.value} and the icon is {self.icon}"
