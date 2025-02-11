from .view import main


urlpatterns = [
    path(' ', main, name="Home View")
]
