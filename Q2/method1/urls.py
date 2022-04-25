from django.urls.conf import path
from method1.views import BinOperationList


app_name = "method1"


urlpatterns = [
    path("bin-operations/", BinOperationList.as_view()),
]