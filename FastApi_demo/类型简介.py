# -*-coding:utf-8 -*-
"""
@project: self
@author: Administrator
@file: 类型简介.py
@time: 2020-04-08 16:53:19
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG。   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

'''
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age
'''



"""
# eg2
# 相当于是申明变量items是list，并且list中的每个元素都是str。而且编辑器知道它是str，从而可以提供错误检测
from typing import List

def process_items(items: List[str]):
    for item in items:
        try:
            print(item.index("c"))
        except Exception as e:
            print(e)

process_items(["abc", "cde", "fgh", "ijk"])

# 同理，dict也是一样
from typing import Dict

def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name + " ￥" + str(item_price))

goods = {"猪肉": 32.5, "牛肉": 47, "白菜": 3.67, "胡萝卜": 8}
process_items(goods)

"""




# eg3 将类作为变量的类型的进行申明
class Person(object):
    def __init__(self, name: str):
        self.name = name + "s"

def get_peerson_name(one_person: Person):
    return one_person.name

print(get_peerson_name(Person("fke")))



"""
取自Pydantic官方文档， 为类的每个属性申明类型，它将自动验证这些值，并将它们转换为适当的类型
from datetime import datetime
from typing import List

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: datetime = None
    friends: List[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"]
}

user = User(**external_data)
print(user)
print(user.id)
"""


