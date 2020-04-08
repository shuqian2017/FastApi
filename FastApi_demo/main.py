# -*-coding:utf-8 -*-
"""
@project: 新建文件夹
@author: Administrator
@file: main.py
@time: 2020-04-07 17:52:37
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
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resent = 'resent'
    lenet = 'lenet'

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id : int, q: str= None):
    return {"item_id" : item_id, "q" : q}

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == 'lenet':
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

# 假如想接收一个路径参数，它本身就是一个路径就像/files/{file_path},而这个路径是home/fke/123.txt时，可以写成/files/{file_path:path}
@app.get("/files/{file_path:path}")
async def read_user_me(file_path: str):
    return {"file_path": file_path}

'''




"""
# eg2 获取查询参数
from fastapi import FastAPI

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# 因为在定义方法的时候，分别给skip和limit赋了默认值，所以当没有querystring时，就会使用默认值。因此http://127.0.0.1:8000/items/?skip=0&limit=3 和http://127.0.0.1:8000/items/ 结果一样。

"""



# eg3 假如不给参数默认值
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# 继续请求http://127.0.0.1:8000/items/1 ,会发现返回报错