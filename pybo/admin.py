from django.contrib import admin

# Register your models here.
from .models import Question,Answer,Header_home
from django_summernote.admin import SummernoteModelAdmin

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = 'content'

class Header_homeAdmin(admin.ModelAdmin):
    search_fields = ['content']
    

admin.site.register(Question)
# admin.site.register(Answer,QuestionAdmin)
admin.site.register(Answer, SummerAdmin)
admin.site.register(Header_home)
