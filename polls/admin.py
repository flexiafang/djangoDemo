from django.contrib import admin

from polls.models import Question, Choice

# 向管理页面中加入投票应用
admin.site.register(Question)
admin.site.register(Choice)
