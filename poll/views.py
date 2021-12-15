from django.http import HttpResponse
from django.shortcuts import render
from poll.models import Question


def index(request):
    #db에 있는 모든 데이터 조회 : Question.objects.all() = SELECT *
    question_list = Question.objects.all()
    return render(request, 'poll/index.html', {'question_list' : question_list})
    # return HttpResponse("Welcome~ 환영합니다!!")

def detail(request, question_id):
    #해당 ID(숫자)로 자료 조회
    question = Question.objects.get(id=question_id)
    return render(request, 'poll/detail.html', {'question': question})