from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Node:
    key: int
    value: str
    height: int = 0
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    def swap_nodes(self, other: 'Node') -> None:
        self.key, other.key = other.key, self.key
        self.value, other.value = other.value, self.value
