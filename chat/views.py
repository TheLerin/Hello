from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
from django.views.decorators.csrf import csrf_exempt

def index(request):
    """Render the main chat page"""
    return render(request, 'chat/index.html')

@csrf_exempt
def send_message(request):
    """Send a message"""
    if request.method == 'GET':  # Simple GET for demo
        sender = request.GET.get('sender', '')
        receiver = request.GET.get('receiver', '')
        text = request.GET.get('text', '')
        
        if sender and receiver and text:
            Message.objects.create(
                sender=sender,
                receiver=receiver,
                text=text
            )
            return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'}, status=400)

def get_messages(request):
    """Get messages between two users"""
    user = request.GET.get('user', '')
    friend = request.GET.get('friend', '')
    
    if not user or not friend:
        return JsonResponse({'messages': []})
    
    # Get all messages between these two users
    messages = Message.objects.filter(
        sender__in=[user, friend],
        receiver__in=[user, friend]
    ).order_by('timestamp')
    
    message_list = []
    for msg in messages:
        message_list.append({
            'sender': msg.sender,
            'receiver': msg.receiver,
            'text': msg.text,
            'time': msg.timestamp.strftime('%H:%M')
        })
    
    return JsonResponse({'messages': message_list})

