#from logging import info
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Buyer,Game,News

#def index(request):
#    Games  = Game.objects.all()
#    Buyers = Buyer.objects.all()
#    context = {
#        "Games" : Games,
#        "Buyers" : Buyers,
#    }
#    return render(request,'headerPage.html',context)

def index(request):
    return render(request,'general_list.html')

def Games_page(request):
    Games = Game.objects.all()
    context = {
            "Games" : Games,
            }
    return render(request,'fist_list.html',context)

def Basket_page(request):
    return render(request,'second_list.html')

def Registration_page(request):
    info = {}
    user_list = Buyer.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        balance = request.POST.get('balance')
        if not (password != repeat_password) and (username in user_list):
            user_list.append(username)
            return HttpResponse(f"Приветствуем, {username}!")

        if password != repeat_password:
            info["error"] = "Пароли не совпадают"
            return HttpResponse(f"Пароли не совпадают!")

        for user in user_list:
            if user.name == username:
                return HttpResponse(f"Пользователь уже существует!")


        Buyer.objects.create(name=username, balance=balance, age=age)



    return render(request,'registration_page.html')

def Wiew_news(request):
    news = News.objects.all().order_by('-date')
    paginatior = Paginator(news,3)
    page_number = request.GET.get('page')
    page_obj = paginatior.get_page(page_number)
    return render(request,'news.html',{'page_obj':page_obj})
#,{news}