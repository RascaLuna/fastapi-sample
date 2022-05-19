# -*- coding: utf-8 -*-
# モデルの定義
from datetime import date, datetime
from sqlalchemy import Column, Integer, String, Date, TIMESTAMP
from pydantic import BaseModel
from db import Base
from db import ENGINE


# userテーブルのモデルUserTableを定義
class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    sex = Column(String(4), nullable=False)
    email = Column(String(256), nullable=False)
    prefecture = Column(String(10), nullable=False)
    birthday = Column(Date(), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)


# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class User(BaseModel):
    id: int
    name: str
    sex: str
    email: str
    prefecture: str
    birthday: date
    created_at: datetime
    updated_at: datetime

class PointTable(Base):
    __tablename__ = 'points'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, autoincrement=True)
    total_point = Column(Integer)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)


# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class Point(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

def main():
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
