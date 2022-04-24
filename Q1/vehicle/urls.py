from django.urls.conf import path
from vehicle.views import NavigationRecortList


app_name = "vehicle"


urlpatterns = [
    path("last-navigation-records/", NavigationRecortList.as_view()),
]