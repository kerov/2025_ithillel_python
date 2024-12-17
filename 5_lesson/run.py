"""
    Classes...


Operation :=  OPERAND_A OPERATOR OPERAND_B -> RESULT
Opeartion :=   int(4)      *        int(2) ->  16
"""

import json
from pathlib import Path
from typing import Any


class Price:
    def __init__(self, value: int, currency: str):
        self.value: int = value
        self.currency: str = currency

    def __str__(self) -> str:
        return f"Price: {self.value} {self.currency}"

    def __add__(self, other: Any) -> "Price":
        if not isinstance(other, Price):
            raise ValueError("Can perform operation only with Pirces objects")
        else:
            converted_other = self.convert(
                _price=other, convert_to=self.currency)
            return Price(value=round(self.value + converted_other.value, 2), currency=self.currency)

    def __sub__(self, other: Any) -> "Price":
        if not isinstance(other, Price):
            raise ValueError("Can perform operation only with Pirces objects")
        else:
            converted_other = self.convert(
                _price=other, convert_to=self.currency)
            return Price(value=round(self.value - converted_other.value, 2), currency=self.currency)

    @staticmethod
    def convert(_price: Any, convert_to: str):
        _exchanger = Exchanger(files_dir / storage_file)
        converted_value = _exchanger.convert(
            _price.value, _price.currency, convert_to)
        return Price(value=converted_value, currency=convert_to)


files_dir = Path(__name__).absolute().parent / "files"
storage_file = "rates.json"


class Exchanger:
    def __init__(self, file_path: str) -> None:
        self.rates = self.retrieve_rates(file_path)

    def retrieve_rates(self, file_path: str) -> dict:
        with open(file_path) as file:
            return json.load(file)

    def convert(self, value: int, from_currency: str, to_currency: str) -> int:
        try:
            return value * self.rates[from_currency][to_currency]
        except:
            print(f"The currency {
                  from_currency} cannot be converted to {to_currency}")


phone = Price(value=200, currency="USD")
tablet = Price(value=400, currency="GBP")

total: Price = phone + tablet
total2: Price = tablet - phone
total3: Price = tablet - phone + tablet
print(total)
print(total2)
print(total3)
