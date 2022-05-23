from django.http import HttpResponse


def hello(request):
    return HttpResponse("框架搭建完成！")
