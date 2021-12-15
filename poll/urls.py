from django.urls import path
from poll import views

#네임 스페이스

app_name = 'poll'       #app_name 변수에 poll 앱 저장

urlpatterns = [
    # 127.0.0.1:8000/poll/ 로 접속하는 것
    path('', views.index, name='index'),       #views.py의 index로 찾아가라
    path('<int:question_id>/', views.detail, name ='detail'),
]