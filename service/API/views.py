from flask import request, render_template
import json
import os

from Slash.Core.operations_ import *
from Slash.Core.core import Connection
from Slash.types_ import *

from .models import Users


class ApiViews:
    @staticmethod
    def main_display():
        return render_template("api.html")

    @staticmethod
    def insert(*args):
        json_data = None

        conn = Connection("Slash", "postgres", "root", "127.0.0.1", 5432)

        users = Users()
        conn.create(users)
        Operations(conn).insert(
            users,
            request.get_json()["columns"],
            [BasicTypes.ORM_TYPES_LIST[i[0]](i[1]) for i in request.get_json()["data"]]
        )

        with open(str(os.environ.get("JSON_DATA_FILE")), "r") as file_:
            json_data = json.load(file_)

        json_data["reqests_lh"] += 1
        json_data["answers_lh"] += 1
        json_data["count_of_insert"] += 1
        json_data["new_entry_lh"] += 1
        json_data["count_of_rows"] += 1

        with open(str(os.environ.get("JSON_DATA_FILE")), "w") as file_:
            json.dump(json_data, file_, indent=4)

        return {"code": 0}

    @staticmethod
    def update(*args):
        json_data = None

        conn = Connection("Slash", "postgres", "root", "127.0.0.1", 5432)

        users = Users()
        conn.create(users)
        Operations(conn).update(
            users,
            request.get_json()["columns"],
            [BasicTypes.ORM_TYPES_LIST[i[0]](i[1]) for i in request.get_json()["data"]]
        )

        with open(str(os.environ.get("JSON_DATA_FILE")), "r") as file_:
            json_data = json.load(file_)

        json_data["reqests_lh"] += 1
        json_data["answers_lh"] += 1
        json_data["count_of_update"] += 1

        with open(str(os.environ.get("JSON_DATA_FILE")), "w") as file_:
            json.dump(json_data, file_, indent=4)

        return {"code": 0}

    @staticmethod
    def select(*args):
        return {"code": 0}

    @staticmethod
    def delete(*args):
        json_data = None

        conn = Connection("Slash", "postgres", "root", "127.0.0.1", 5432)
        table = Users()

        recved_data: dict = request.get_json()
        not_processed_condition: list = recved_data["condition"]
        processed_condition: list = []

        for item in not_processed_condition:
            column: Column = table.__getattribute__(item[0])
            condition_symbol = SQLCnd.EQ
            condition_data = BasicTypes.ORM_TYPES_LIST[item[2][0]](item[2][1])
            processed_condition.append([column, condition_symbol, condition_data])

        Operations(conn).delete(table, condition=SQLCnd.where(*processed_condition))

        with open(str(os.environ.get("JSON_DATA_FILE")), "r") as file_:
            json_data = json.load(file_)

        json_data["reqests_lh"] += 1
        json_data["answers_lh"] += 1
        json_data["count_of_delete"] += 1
        json_data["count_of_rows"] -= 1

        with open(str(os.environ.get("JSON_DATA_FILE")), "w") as file_:
            json.dump(json_data, file_, indent=4)

        return {"code": 0}

    @staticmethod
    def logs(*args):
        if request.method == "POST":
            with open("D:\pyrus\ORM_bridge\data.log", "r", encoding="utf-8") as file_:
                return file_.read()
