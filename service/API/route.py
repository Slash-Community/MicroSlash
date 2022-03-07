from .views import ApiViews

class ApiRoute:
    @staticmethod
    def main(responce=None):
        return ApiViews.main_display()
