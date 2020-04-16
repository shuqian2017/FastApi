# -*-coding:utf-8 -*-
"""
@project: self
@author: Administrator
@file: 2_Path_Parameter.py
@time: 2020-04-09 14:22:14
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

from enum import Enum
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    """
    路径参数 访问http://127.0.0.1:8000/items/foo
    :param item_id: foo
    :return: {"item_id":"foo"}
    """
    return {"item_id": item_id}






@app.get("/items/{item_d}")
async def read_item(item_id: int):
    """
    路径参数与类型，在这种情况下item_id 被声明为int
    :param item_id: 3
    :return: {"item_id":3}
    """
    return {"item_id": item_id}






# 声明的顺序也很重要，如下/users/me. 否则它认为user_id的参数值为‘me’
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}







class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = 'resnet'
    lenet = 'lenet'

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    """
    使用标准的Python Enum类，预定义可能有效的路径参数ModelName
    :param model_name:
    :return:
    """
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}







@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """
    路径参数中包含路径
    /files/{file_path:path} 参数的名称是file_path,最后一部分:path它告诉参数应与什么路径匹配
    :param file_path:
    :return:
    """
    return {"file_path": file_path}

