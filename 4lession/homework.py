import json
from keyword import iskeyword
from sty import fg, bg, ef, rs

print(fg.red + 'This is red text!' + fg.rs)

class AttributeConstructor:
    @staticmethod
    def construct_attr(item):
        if isinstance(item, dict):
            obj = type('__object', (object,), {})
            for key, value in item.items():
                setattr(obj, key, AttributeConstructor.construct_attr(value))
            return obj
        elif isinstance(item, list):
            l = []
            for i in item:
                l.append(AttributeConstructor.construct_attr(i))
            return l
        else:
            return item

class ColorizeMixin:
    def __repr__(self):
        pass




class Advert(ColorizeMixin):
    repr_color_code = 32
    def __init__(self, adv):
        self._price = 0
        self.title = ''
        for item in adv:
            item_name = item + '_' if iskeyword(item) else item
            setattr(self, item_name, AttributeConstructor.construct_attr(adv[item]))

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price >= 0:
            self._price = price
        else:
            raise ValueError('Price must be >= 0')



lesson_str = """{
  "title1": "Вельш-корги",
  "class": "dogs",
  "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
  }
}
    """

lesson = json.loads(lesson_str)
adv1 = Advert(lesson)
print(adv1)
