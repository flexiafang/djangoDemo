import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # 问题描述
    question_text = models.CharField(max_length=200)
    # 发布时间
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text

    # 优化管理页面展示效果
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    # 每个Choice对象都关联到一个Question对象
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 选项描述
    choice_text = models.CharField(max_length=200)
    # 当前票数
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
