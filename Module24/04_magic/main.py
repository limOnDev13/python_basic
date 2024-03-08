from typing import Any


class Water:
    def __add__(self, other: Any) -> Any | None:
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Soil):
            return Dirt()
        else:
            return None


class Air:
    def __add__(self, other: Any) -> Any | None:
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Flash()
        elif isinstance(other, Soil):
            return Dust()
        else:
            return None


class Fire:
    def __add__(self, other: Any) -> Any | None:
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Flash()
        elif isinstance(other, Soil):
            return Lava()
        else:
            return None


class Soil:
    def __add__(self, other: Any) -> Any | None:
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        else:
            return None


class Storm:
    pass


class Steam:
    pass


class Dirt:
    pass


class Flash:
    pass


class Dust:
    pass


class Lava:
    pass


# Тест
# print(f'type(Water() + Air()) = {type(Water() + Air())}')
# print(f'type(Water() + Fire()) = {type(Water() + Fire())}')
# print(f'type(Water() + Soil()) = {type(Water() + Soil())}')
# print(f'type(Air() + Fire()) = {type(Air() + Fire())}')
# print(f'type(Soil() + Air()) = {type(Soil() + Air())}')
# print(f'type(Soil() + Fire()) = {type(Soil() + Fire())}')
