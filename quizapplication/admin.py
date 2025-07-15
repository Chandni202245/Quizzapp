from django.contrib import admin
from .models import Quiz, Question, UserQuiz

# If you have custom admin classes, define them here
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_limit']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'quiz', 'text']

class UserQuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'quiz', 'score', 'submitted_at']  # or taken_on, whichever you're using

# Register with the admin site
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserQuiz, UserQuizAdmin)
