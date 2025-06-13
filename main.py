from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

from fastapi.responses import HTMLResponse #インポート

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return {"result" : omikuji_list[random.randrange(10)]}

    

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Pythonよくわからない</title>
        </head>
        <body>
            <h1 style="color: #ffffff; background-color: #8888ff;">Pythonよくわからない</h1>
            <p style="color: #ffff00">がんばります</p>
            <h2 style="color: #ff0000; background-color: #00ff00;">HTMLもよくわからない</h2>
            <p style="color: #ff00ff">がんばります</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
    
@app.post("/present")
async def give_present(present):
    present_list = [
        "Switch2",
        "Switch2台",
        "3DS",
        "2DS",
        "DSLite",
        "プレステ5",
        "プレステ4",
        "PSP",
        "キャンディー1年分",
        "クッキー"
    ]
    ind = len(present)
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しは{present_list[ind]}です。"}  # f文字列というPythonの機能を使っている