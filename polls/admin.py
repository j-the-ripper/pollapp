from django.contrib import admin

# Register your models here.

from . models import Question, Choice

admin.site.site_header = "PollApp"
admin.site.site_title = "PollApp Admin"
admin.site.index_title = "Welcome to PollApp"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Data Information', {'fields': ['pub_date'],
                                       'classes':['collapse']})]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)

# admin.site.register(Choice)
