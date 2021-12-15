from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'control/index.html')

def register(request):
    if request.method == "POST":
        #아이디 넘겨 받음
        userid = request.POST['userid']
        #아이디 보내주기
        return render(request, 'control/reg_result.html', {'userid': userid})

        #html로 렌더링할때 딕셔너리구조로 자료를 보냄
    else:       #get 방식
        return render(request, 'control/register.html')