from typing import Any


class MyDict(dict):
    def get(self, key):
        item: Any | None = super().get(key)
        if item is None:
            return 0
        else:
            return item


my_dict: MyDict = MyDict()
print(my_dict.get(1))
