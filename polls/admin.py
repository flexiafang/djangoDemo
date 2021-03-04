from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    """
    优化管理界面
    """
    # 修改默认的表单显示列表
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    # Choice 对象要在 Question 后台页面编辑。默认提供 1 个足够的选项字段。
    inlines = [ChoiceInline]
    # 自定义后台管理列表
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 添加过滤器侧边栏
    list_filter = ['pub_date']
    # 增加搜索框
    search_fields = ['question_text']


# 向管理页面中注册模型
admin.site.register(Question, QuestionAdmin)
