from django.contrib import admin
from .models import Question,Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text']
    fieldsets = [
        ('Text Information', {'fields': ['question_text']}),
        ("Date Information", {'fields': ['pub_date'],'classes': ['collapse']})
    ]
    list_display = ('question_text', 'pub_date','was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
