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


def createRoom(request):
    form =RoomForm()
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)

    if request.method=="POST":
        form=RoomForm(request.POSTc, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    

    context={'form':form}
    return render(request, "base/room_form.html", context)


def deleteRoom(request, pk):
    room=Room.objects.get(id=pk)
    if request.method=="POST":
        room.delete()
        return redirect('home')
    

    context={'obj':room}
    return render(request, "base/delete.html", context)
    

