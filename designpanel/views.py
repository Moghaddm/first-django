from django.shortcuts import render
from django.http import HttpResponse
from designpanel.models import Quiz,Question
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request): return HttpResponse("hi this is just simple text.") 

def get_single_quiz(request,quiz_id): 
    try: quiz = Quiz.objects.get(pk=quiz_id)
    except: raise Http404("quiz does not exist.")
    return HttpResponse(quiz.title)

def get_quizzes(request):
    quizzes = Quiz.objects.all()[:2]
    return render(request,"designpanel/index.html",{"quizzes": quizzes})

def create_quiz(request):
    q = Quiz(title="flutter course",desciption="this is flutter description.")
    q.save()
    return HttpResponse(f"quiz {q.title} created.")

def delete_quiz(request,quiz_id):
    q = Quiz.objects.get(pk = quiz_id)
    q.delete()
    q.save()
    return HttpResponse(f"quiz {q.title} deleted.")

def get_quiz_questions(request,quiz_id):
    q = Quiz.objects.get(pk= quiz_id)
    questions = Question.objects.filter(quiz=q)
    context = {
        "title" : q.title,
        "questions" : questions
    } 
    return render(request,"designpanel/details.html",context)   
    
def get_question(request,question_id):
    q = get_object_or_404(Question,pk=question_id)
    return render(request,"designpanel/question.html",{ "text":q.text,"score":q.score })