from django.urls import path, include
from .views import index, QuestionAPI, latest, getUsers,getQuestions,getLatestQuestions
from rest_framework import routers
from stackapi import views as stackapi # Edit 10

router = routers.DefaultRouter()
router.register("questions", QuestionAPI)

urlpatterns = [
    path('', index, name="index"),
    path('', include(router.urls)),
    path('latest', latest, name="latest"),
    path('getUsers',getUsers,name="getUsers"), # Edit 11
    path('getQuestions',getQuestions,name="getQuestions"), 
    path('getLatestQuestions',getLatestQuestions,name="getLatestQuestions"), 
    # path('',stackapi.index,name="index"), # Edit 4
]