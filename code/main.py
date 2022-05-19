from fastapi import FastAPI
from fastapi import FastAPI, Response
from typing import List  # ネストされたBodyを定義するために必要
from starlette.middleware.cors import CORSMiddleware  # CORSを回避するために必要
from db import session  # DBと接続するためのセッション
from model import UserTable, User  # 今回使うモデルをインポート
from datetime import date, datetime

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

# CORSを回避するために設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Total-Count"], # React Adminで受け取る際にx-total-countがheaderにないと受け取れない
)

# ----------APIの実装------------
# テーブルにいる全ユーザ情報を取得 GET
@app.get("/users")
def read_users(response: Response):
    users = session.query(UserTable).all()
    

    response.headers['X-Total-Count'] = '30' 
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    return users

# idにマッチするユーザ情報を取得 GET
@app.get("/users/{id}")
def read_user(id: int):
    user = session.query(UserTable).\
        filter(UserTable.id == id).first()
    return user

# ユーザ情報を登録 POST
@app.post("/user")
# クエリで各パラメータを受け取る
# /user?id=11&name=Saeki&sex=female&email=saeki%40test.com&prefecture=Gunma&birthday=1990-11-20&created_at=2022-05-10T04%3A26%3A22&updated_at=2022-05-10T04%3A26%3A22'
async def create_user(id: int, name: str, sex: str, email: str, prefecture: str, birthday: date, created_at: datetime, updated_at: datetime):
    user = UserTable()
    user.id = id
    user.name = name
    user.sex = sex
    user.email = email
    user.prefecture = prefecture
    user.birthday = birthday
    user.created_at = created_at
    user.updated_at = updated_at

    session.add(user)
    session.commit()

# 複数のユーザ情報を更新 PUT
@app.put("/users")
# modelで定義したUserモデルのリクエストbodyをリストに入れた形で受け取る
# users=[{"id": 1, "name": "一郎", "age": 16},{"id": 2, "name": "二郎", "age": 20}]
async def update_users(users: List[User]):
    for new_user in users:
        user = session.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.name = new_user.name
        user.sex = new_user.sex
        user.email = new_user.email
        user.prefecture = new_user.prefecture
        user.birthday = new_user.birthday
        user.created_at = new_user.created_at
        user.updated_at = new_user.updated_at
        session.commit()
