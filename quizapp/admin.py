from django.contrib import admin


from .models import Question, QuizType, Answer, Result


@admin.register(QuizType)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['name', 'is_right']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['name', 'quiz']
    list_display = ['name', 'quiz', ]
    inlines = [AnswerInlineModel]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_right', 'question']

@admin.register(Result)
class ResultAdmiin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'total_question', 'corrent_question', 'total', 'create_at']
    list_filter = ['quiz']