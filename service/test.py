import requests


r = requests.Session()
#r.post(
#    "http://127.0.0.1:8888/api/insert",
#    json={
#        "dbname": "Slash",
#        "table": "users",
#        "columns": ["useraname", "password"],
#        "data": [["TEXT", "123"], ["HIDDEN", "123"]]
#    }
#)
#r.post(
#    "http://127.0.0.1:8888/api/update",
#    json={
#        "dbname": "Slash",
#        "table": "users",
#        "columns": ["useraname", "password"],
#        "data": [["TEXT", "m_o_d_e_r"], ["HIDDEN", "123"]]
#    }
#)
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
        "condition": [["useraname", "==", ["TEXT", "1"]]]#, "or" ["useraname", "==", ["TEXT", "M_O_D_E_R"]]]
    }
)
