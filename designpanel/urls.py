from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name ="index"),
    path("quizzes/",views.get_quizzes,name="quizzes"),
    path("quizzes/<int:quiz_id>/",views.get_quiz_questions,name="details"),
    path("questions/<int:question_id>",views.get_question,name="question")
]