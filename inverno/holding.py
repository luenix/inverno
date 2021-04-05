from typing import Optional, Union
from .price import Price

class Holding:
    def __init__(
        self,
        quantity: float,
        name: Optional[str] = None,
        ticker: Optional[str] = None,
        isin: Optional[str] = None,
    ):
        self.quantity = quantity
        self.name = name
        self.ticker = ticker
        self.isin = isin

    def get_key(self):
        # prioritize stronger identifiers
        if self.isin is not None:
            return self.isin
        elif self.ticker is not None:
            return self.ticker
        elif self.name is not None:
            return self.name
        raise ValueError("Cannot construct holding name")

    def __repr__(self):
        return f"{self.quantity} {self.get_key()}"

    def __add__(self, other: Union["Holding", Price, float]):
        new_quantity = self.quantity

        if isinstance(other, float):
            new_quantity += other

        elif isinstance(other, Holding):
            if self.get_key() != other.get_key():
                raise ValueError(
                    "Trying to add up holding with different keys:"
                    f" {self.get_key()} {other.get_key()}"
                )
            new_quantity += other.quantity
        else:
            raise ValueError(f"Incompatible type {type(other)}")

        return Holding(
            quantity=new_quantity,
            name=self.name,
            ticker=self.ticker,
            isin=self.isin,
        )

    def __sub__(self, other: Union["Holding", Price, float]):
        new_quantity = self.quantity

        if isinstance(other, float):
            new_quantity -= other

        elif isinstance(other, Holding):
            if self.get_key() != other.get_key():
                raise ValueError(
                    "Trying to add up holding with different keys:"
                    f" {self.get_key()} {other.get_key()}"
                )
            new_quantity -= other.quantity
        else:
            raise ValueError(f"Incompatible type {type(other)}")

        return Holding(
            quantity=new_quantity,
            name=self.name,
            ticker=self.ticker,
            isin=self.isin,
        )

    def __neg__(self):
        return Holding(
            quantity=-self.quantity,
            name=self.name,
            ticker=self.ticker,
            isin=self.isin,
        )