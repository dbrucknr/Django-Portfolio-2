from django.urls import path
from .views import ZipcodeList, ZipcodeDetail

urlpatterns = [
    path('', ZipcodeList.as_view()),
    path('<int:pk>', ZipcodeDetail.as_view())
]