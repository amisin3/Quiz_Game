from django.contrib import admin
from .models import Question, Answer, Result, User_specific_model
# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(User_specific_model)
