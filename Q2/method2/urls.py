from django.urls.conf import path
from method2.views import BinOperationList


app_name = "method2"


urlpatterns = [
    path("bin-operations/", BinOperationList.as_view()),
]