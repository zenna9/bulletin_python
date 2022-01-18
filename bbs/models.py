#<<bbs.models>===================
from django.db import models

class Board(models.Model):
    b_title = models.CharField(max_length=30)
    b_author= models.CharField(max_length=20)
    b_content= models.CharField(max_length=200)
    b_date= models.DateTimeField(auto_now=True)
    b_comment_count=models.IntegerField(default=0)
    b_like_count=models.IntegerField(default=0)

    def __str__(self):
        return self.b_title
    # 원래 클래스의 객체는 화면에 문자열로 출력할 때 메모리 주소로 출력됨
    # 그럼 알아볼수가 없음
    # __str__을 사용하면 객체를 화면에 문자열로 출력할때 함수 결과로 출력

class Comment(models.Model):
    c_author = models.CharField(max_length=20)
    c_content = models.CharField(max_length=200)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.c_content