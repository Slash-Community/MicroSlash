import requests


r = requests.Session()
#r.post(
#    "http://127.0.0.1:8888/api/insert",
#    json={
#        "table": "Slash",
#        "columns": [1, 2, 3],
#        "data": [3, 2, 1]
#    }
#)
r.post(
    "http://127.0.0.1:8888/api/update",
    json={
        "table": "Slash",
        "columns": [1, 2, 3],
        "data": [3, 2, 1]
    }
)
#r.post(
#    "http://127.0.0.1:8888/api/select",
#    json={
#        "table": "Slash",
#        "columns": [1, 2, 3]
#    }
#)
r.post(
    "http://127.0.0.1:8888/api/delete",
    json={
        "table": "Slash",
        "columns": [1, 2, 3]
    }
)
