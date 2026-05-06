from django.shortcuts import render, redirect
import telebot
from django.http import HttpResponse

# Create your views here.

bot = telebot.TeleBot('8240591162:AAGOkbKm-F__4Ayeq6MndTcYSiL3pJ23K7E')
group_id = -1003798480119



def home_page(request):
    return render(request, 'home.html')


def free_lesson(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone_number')
        comment = request.POST.get('comment')
        text = (f'Новый клиент! \n\n'
                f'Имя: {name}\n'
                f'Номер телефона: {phone}\n'
                f'Коментарий: {comment}\n')
        bot.send_message(group_id, text)
    return redirect('/')


def robots_txt(request):
    content = """User-agent: *
Allow: /

Disallow: /admin/
Disallow: /static/
Disallow: /media/
Disallow: /api/
Disallow: /*?*

Sitemap: https://sonata-music.uz/sitemap.xml

User-agent: Googlebot
Allow: /

User-agent: Yandexbot
Allow: /

User-agent: bingbot
Allow: /"""
    return HttpResponse(content, content_type='text/plain')