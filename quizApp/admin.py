from django.contrib import admin
from .models import Quiz, Question, Answer, UserAttempt

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserAttempt)


# Register your models here.
