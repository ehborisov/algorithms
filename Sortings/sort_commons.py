from typing_extensions import Protocol
from abc import abstractmethod
from typing import TypeVar, Any, List

C = TypeVar("C", bound="Comparable")


class Comparable(Protocol):
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __lt__(self: C, other: C) -> bool:
        pass

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other


def swap(storage: List, i: int, j: int) -> None:
    tmp = storage[j]
    storage[j] = storage[i]
    storage[i] = tmp
