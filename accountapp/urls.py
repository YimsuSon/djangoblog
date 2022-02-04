from django.urls import path,include

from accountapp.views import hello_world
app_name = 'accountapp'


# url, 뷰애 선언한 함수 , path 이름 설정
urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world')
]