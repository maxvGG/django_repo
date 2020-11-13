from django.contrib import admin
from survey.models import Questionnaire, Question, Answer

# Register your models here.

admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(Answer)