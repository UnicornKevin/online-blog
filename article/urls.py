# 引入path
from django.urls import path,include

# 正在部署的应用的名称
import views

app_name = 'article'

urlpatterns = [
    path('test', views.test)
    # 目前还没有urls
]