from django.http import HttpResponse


def hello(request):
    return HttpResponse("框架搭建完成！")
def article(request):
    return HttpResponse("这是文章界面")
def test(request):
    return HttpResponse("这是测试界面")