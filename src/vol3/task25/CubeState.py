from dataclasses import dataclass

@dataclass(frozen=True)
class CubeState:
    x : int
    y : int
    top : int
    front : int
    right : int

    def __repr__(self):
        return f"Позиция: ({self.x}, {self.y}. Грани: top: {self.top}, front: {self.front}, right: {self.right})"

    def __lt__(self, other):
        return ((self.x, self.y, self.top, self.front, self.right) <
                (other.x, other.y, other.top, other.front, other.right))

    def __eq__(self, other):
        return ((self.x, self.y, self.top, self.front, self.right) ==
                (other.x, other.y, other.top, other.front, other.right))

    def __hash__(self):
        return hash((self.x, self.y, self.top, self.front, self.right))
