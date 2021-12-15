from django.db import models

# Create your models here.

# SQL의 단점: 개발자에 따라 너무 다른 문장을 사용 / 개발자의 역량에 따라 시스템 성능이 저하되기도 함
# ORM (Object Relational Mapping) : 테이블을 모델화(Class 객체)하여 DB관리 /SQL 언어 문법 사용 x

#질문 모델 (Model을 상속받음) - 테이블과 같은 의미
class Question(models.Model):       #SQL이 아닌 파이썬의 테이블 생성
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

# 질문 내용이 문자로 출력됨
    def __str__(self):
        return self.question_text

#Choice 모델
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   #외래키

    def __str__(self):
        return self.choice_text
