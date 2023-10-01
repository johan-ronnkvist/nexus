from abc import ABC, abstractmethod
from typing import List

from nexus.model.tile import Tile


class TileMap(ABC):
    @abstractmethod
    def get_tiles(self) -> List[Tile]:
        ...

    @abstractmethod
    def get_adjacent_tiles(self, tile: Tile) -> List[Tile]:
        ...
