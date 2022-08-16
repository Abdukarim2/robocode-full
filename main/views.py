from django.shortcuts import render
from django.http import JsonResponse
from .models import Course, Videos
from .forms import CourseUserForm
from django.views.decorators.csrf import csrf_exempt
import telebot
bot = telebot.TeleBot(token='1720356473:AAHYnusESxOqJc2PRXSlsNUkr8slIh6Vs-8')
courses_list = ["Bolalar uchun dasturlash", 
                "Arduino", "Kompyuter fani",
                "Grafik dizayn", "WEB dasturlash (frontend)",
                "WEB dasturlash (backend)"]

def home(request):
    context = {
        "videos": Videos.objects.all()
    }
    return render(request, 'home.html', context)


def gallery(request):
    return render(request, 'gallery.html')


def detail(request, slug):
    context = {
        "course": Course.objects.get(slug=slug),
    }
    return render(request, 'detail.html', context)


@csrf_exempt
def api_register(request):
    data = {}
    if request.method == 'POST':
        form = CourseUserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                data['status'] = 200
                #bot
                # fullname = form.data.get("full_name")
                # age = form.data.get("age")
                # phonenumber = form.data.get("number")
                # course = courses_list[int(form.data.get("course"))-1]
                # messageCheck = form.data.get("message") 
                # message = messageCheck  if messageCheck  else "Habar yo'q"
                # bot.send_message(-1001383923135, f"""Yangi o'quvchi\n\nIsmi-familyasi:\n{fullname}\n\nYoshi:\n{age}\n\nTelefo'n raqami:\n{phonenumber}\n\nTanlagan kursi:\n{course}\n\nQo'shimcha habar:\n{message}""")
                bot.send_message(-1001383923135, "test")
                #/bot
            except Exception as e:
                data['error'] = e
        else:
            data['status'] = 500
    return JsonResponse(data, safe=False)

