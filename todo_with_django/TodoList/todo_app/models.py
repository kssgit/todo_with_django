from django.db import models

# Create your models here.
# entity - models.Model 상속


class Todo(models.Model):
    # models 객체안의 charField 를 이용해서 크기
    # objects=models.Manager() object 에러 날경우
    content = models.CharField(max_length=255)
