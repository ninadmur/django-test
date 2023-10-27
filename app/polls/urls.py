
from django.urls import path, include
from .views import (
QuestionList,QuestionDetail,ChoiceList,ChoiceDetail,ChoiceByQuestion
)

urlpatterns = [
    path('question/', QuestionList.as_view()),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('choice/', ChoiceList.as_view()),
    path('choice/<int:pk>/', ChoiceDetail.as_view()),
    path('question/<int:question_id>/choices/', ChoiceByQuestion.as_view()),
]