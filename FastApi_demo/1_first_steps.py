# -*-coding:utf-8 -*-
"""
@project: self
@author: Administrator
@file: 1_first_steps.py
@time: 2020-04-09 14:04:02
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



from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """
    定义路径操作功能
    :return:
    """
    return {"message": "Hello World"}

