import sys
from urllib import response
sys.path.append('../')
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Tanaka",
        "email": "tanaka@test.com",
        "prefecture": "Tokyo",
        "created_at": "2022-05-11T01:19:36",
        "id": 1,
        "sex": "male",
        "birthday": "1980-04-22",
        "updated_at": "2022-05-11T01:19:36"
    }

# def test_create_user():
#     response = client.post(
#         "/user",
#         json={
#             "id": 11,
#             "name": "Satou",
#             "sex": "male",
#             "email": "satou@test.com",
#             "prefecture": "Tokyo",
#             "birthday": "1999-09-99",
#             "created_at": "2022-05-11T01:19:36",
#             "updated_at": "2022-05-11T01:19:36"
#         },
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": 11,
#         "name": "Satou",
#         "sex": "male",
#         "email": "satou@test.com",
#         "prefecture": "Tokyo",
#         "birthday": "1999-09-99",
#         "created_at": "2022-05-11T01:19:36",
#         "updated_at": "2022-05-11T01:19:36"
#     }
