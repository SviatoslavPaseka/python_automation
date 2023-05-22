from enum import Enum


class ProductSorting(Enum):
    ALPHABET = ("az", "Name (A to Z)")
    ALPHABET_REVERSE = ("za", "Name (Z to A)")
    PRICE = ("lohi", "Price (low to high)")
    PRICE_REVERSE = ("hilo", "Price (high to low)")
