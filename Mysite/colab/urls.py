from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('predict_student/', PredictStudent.as_view(), name='predict_student'),
    path('predict_house/', PredictHouse.as_view(), name='predict_house'),
    path('predict_bank/', PredictBank.as_view(), name='predict_bank'),
    path('predict_avocado/', PredictAvocado.as_view(), name='predict_avocado'),
    path('predict_telecom/', PredictTelecom.as_view(), name='predict_telecom'),
    path('predict_diabet/', PredictDiabet.as_view(), name='predict_diabet'),
    path('predict_mashrooms/', PredictMashrooms.as_view(), name='predict_mashrooms'),
    path('predict_titanic/', PredictTitanic.as_view(), name='predict_titanic'),

]