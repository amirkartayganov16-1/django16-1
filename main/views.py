import datetime

from django.shortcuts import render
from django.http import HttpResponse
now = datetime.datetime.now().replace(microsecond=0)

def index(request):
    return HttpResponse('<h1 style="color:red;">Тут могла бы быть ваша реклама, но вы не программист.</h1>')

def test1(request):
    dict ={
        'title': 'Science app',
        'text': '1ctddrl-breakfhyew'
    }
    return render(request, template_name='index.html', context=dict)

def test2(request):
    dict = {
        'title': 'Как придумать дизайн сайта, который клиент примет с первого раза?',
        'text':  'Клиенту изначально требуется минимум 2 варианта'
                 'Клиент не хочет вникать в вопрос и надеется, что вы как-нибудь сами догадаетесь о его потребностях'
                 'Клиент понятия не имеет, как должен выглядеть его сайт, и надеется выбрать из предложенных вариантов подходящий и с помощью правок довести его до идеала (а дизайнера – до нервного тика).'}

    return render(request, template_name='index.html', context=dict)


def test3(request):
    dict={
        'title': 'Какой Интернет–ресурс вызовет интерес?',
        'text': 'Изначально сеть Интернет воспринималась многими как одно из средств развлечения. Можно было пойти в кино, отправиться на прогулку, встретиться с друзьями или же посвятить это время странствию по сети Интернет.'
    }
    return render(request, template_name='index.html', context=dict)


def test4(request):
    dict={
        'title': 'Как создать успешный сайт?',
        'text': 'Уделяйте внимание оформлению контента. Опытные владельцы сайтов понимают важность наполнения. Ведь именно за ним обычно приходят на ресурс пользователи Сети.'
                'ему обязательно нужен оригинальный привлекательный дизайн, грамотная вёрстка и программирование',
        'data': f"{now}"


    }
    return render(request, template_name='index.html', context=dict)
