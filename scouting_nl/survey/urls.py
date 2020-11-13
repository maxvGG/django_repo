from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:questionnaire_id>/', views.questionnaire_detail),
    # path('register/', views.save),
    # path('<int:questionnaire_pk>/', views.answerpage)
    
]