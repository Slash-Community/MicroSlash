from flask import render_template, make_response, request, redirect, flash
import json
import os

class MainViews:
    @staticmethod
    def main_display(responce=None):
        json_data = None
        with open(str(os.environ.get("JSON_DATA_FILE")), "r") as file_:
            json_data = json.load(file_)

        return render_template(
            "index.html",
            data={
                "title": "Slash Bridge",
                "count_of_rows": json_data["count_of_rows"],
                "requests": json_data["reqests_lh"],
                "answers": json_data["answers_lh"],
                "new_users": json_data["new_entry_lh"],
                "count_of_insert": json_data["count_of_insert"],
                "count_of_update": json_data["count_of_update"],
                "count_of_delete": json_data["count_of_delete"],
                "insert_p": json_data["count_of_insert"] * 100 // json_data["reqests_lh"],
                "update_p": json_data["count_of_update"] * 100 // json_data["reqests_lh"],
                "delete_p": json_data["count_of_delete"] * 100 // json_data["reqests_lh"]
            }
        )

    @staticmethod
    def login_display(responce=None):
        if request.method == "POST":
            login = request.form.get("login")
            password = request.form.get("password")
            if not request.cookies.get("SlashBridgeLogin") or not request.cookies.get("SlashBridgePassword"):
                responce = make_response(redirect("/admin"))
                responce.set_cookie("SlashBridgeLogin", login)
                responce.set_cookie("SlashBridgePassword", password)
                return responce
            else:
                if request.cookies.get("SlashBridgeLogin") != login or request.cookies.get("SlashBridgePassword") != password:
                    flash('Invalid password or login', 'error')
                    return redirect("/")

                return redirect("/admin")

        return render_template("login.html")

    @staticmethod
    def error_404_display(error):
        return render_template("error.html", data={"title": "404", "code": 404, "error": "Not found...)"})

    @staticmethod
    def error_500_display(error):
        return render_template("error.html", data={"title": "500", "code": 500, "error": "Чот на серваке, лол..."})