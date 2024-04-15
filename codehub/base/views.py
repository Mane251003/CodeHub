from django.shortcuts import render
from .models import Question, Topic, Message

def home(request):
    questions=Question.objects.all()
    context={"questions": questions}
    return render(request, "base/home.html", context)

def question(request, pk):
    question=Question.objects.get(id=pk)
    message=Message.objects.get(id=pk)
    context={"question":question, "message": message}
    return render(request, "base/question.html", context)



    

