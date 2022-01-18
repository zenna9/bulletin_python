#<<bbs.admin.py>>----
from django.contrib import admin
from bbs.models import Board, Comment
admin.site.register(Board)
admin.site.register(Comment)
