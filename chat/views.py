from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render (request,'home.html')
def room(request, room):
    username =  request.GET.get('username')
    roomDetails = Room.objects.get(roomName = room)

    return render(request,'room.html',{
        'username':username,
        'room':room,
        'roomDetails': roomDetails
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(roomName = room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        newRoom = Room.objects.create(roomName=room)
        newRoom.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    roomID = request.POST['roomID']

    newMessage = Message.objects.create(value= message, user = username, roomName = roomID)
    newMessage.save()
    return HttpResponse('Message Sent Successfully')

def getMessages(request,room):
    room_details = Room.objects.get(roomName = room)
    messages = Message.objects.filter(roomName=room_details.id)
    return JsonResponse({'messages':list(messages.values())})