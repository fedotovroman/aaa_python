import json
from typing import Iterator
from keyword import iskeyword

class AttributeConstructor:
    """
     A class that converts a nested structure in JSON format into an object with
     fields of type list or dict.
    ...
    Methods
    ----------
    construct_attr(json_item: Iterator) -> object: A method that recursively
    converts a json dictionary into an object with fields specified in json.

    """
    @staticmethod
    def construct_attr(json_item: Iterator) -> object:
        """
        param:
        - json_item: Iterator -  part of JSON inner structure (list, dict, str, int)
        return:
        - construct_attr: object -  object with fields of setted type from JSON
        """
        if isinstance(json_item, dict):
            obj = type('__object', (object,), {})
            for key, value in json_item.items():
                setattr(obj, key, AttributeConstructor.construct_attr(value))
            return obj
        elif isinstance(json_item, list):
            list_attr = []
            for l in json_item:
                list_attr.append(AttributeConstructor.construct_attr(l))
            return list_attr
        else:
            return json_item

class ColorizeMixin:
    """
    Mixin that allows to override the __repr__ method to colorize the
    information output.
    """
    def __repr__(self):
        adv_repr = super().__repr__()
        return f'\33[{self.repr_color_code}m{adv_repr}'

class BaseAdvert():
    """
     A base class for mixin realisation.
    ...
    """
    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class Advert(ColorizeMixin, BaseAdvert):
    """
     A class that converts a nested structure in JSON format into an object with
     fields of type list or dict.

    Attributes:
    price(json_item: Iterator) -> object: A method that recursively
    converts a json dictionary into an object with fields specified in json.

    """
    repr_color_code = 35

    def __init__(self, adv):
        self._price = 0
        self.title = ''
        for item in adv:
            item_name = item + '_' if iskeyword(item) else item
            setattr(self, item_name, AttributeConstructor.construct_attr(adv[item]))


    @property
    def price(self) -> int:
        """
        Get or set the current price of advert. Setting price >= 0 to a new value
        will reconfigure the price.
        """
        return self._price

    @price.setter
    def price(self, price):
        if price >= 0:
            self._price = price
        else:
            raise ValueError('Price must be >= 0')




def main():
    lesson_str1 = """{
  "title": "Вельш-корги",
  "some1": {"h":1},
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
  }
    }
    """

    lesson1 = json.loads(lesson_str1)
    adv1 = Advert(lesson1)
    print(adv1.location.address)

    lesson_str2 = """{
  "title": "iPhone X",
  "price": 100,
  "location": {
    "address": "город Самара, улица Мориса Тореза, 50",
    "metro_stations": ["Спортивная", "Гагаринская"]
  }
}"""

    lesson_json = json.loads(lesson_str2)
    adv2 = Advert(lesson_json)
    print(adv2.price)


if __name__ == '__main__':
    main()