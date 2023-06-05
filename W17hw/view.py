from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    if 'user' not in request.COOKIES:#(For first time user)
        response = HttpResponse("這是第一次瀏覽本網站")
        response.set_cookie("user","simon")
        return response
    else:
        return render(request, 'template.html', {})
