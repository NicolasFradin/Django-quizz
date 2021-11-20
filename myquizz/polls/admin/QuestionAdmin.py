from django.contrib import admin
from polls.models import *
from polls.CustomModelAdminMixin import CustomModelAdminMixin

# Register your models here.
# Add your models where to show them in the Django admin panel
# 		LOCAL -> http://127.0.0.1:8000/admin/




class ChoiceInline(admin.TabularInline):  #Affichage : StackedInline / TabularInline
	model = Choice
	extra = 4


class QuestionAdmin(admin.ModelAdmin):
	#Set fieldsets to control the layout of admin “add” and “change” pages.
	# fieldsets = [
	# 	("TEXT",               {'fields': ['question_text']}),
	# 	('DATE', {'fields': ['pub_date'], 'classes': ['collapse']}),
	# ]

	#showing only a subset of available fields, modifying their order, or grouping them into rows.
	# fields = (('question_text', 'pub_date'), 'quizz')

	inlines = [ChoiceInline]		#This tells Django: “Choice child objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”

	list_display = ('question_text', 'created_at', 'was_published_recently') #By default, Django displays the str() of each object. But sometimes it’d be more helpful if we could display individual fields. To do that, use the list_display admin option, which is a tuple of field names to display, as columns, on the change list page for the object
	list_filter = ['created_at']  #That adds a “Filter” sidebar that lets people filter the change list by the pub_date field
	search_fields = ['question_text'] #That adds a search box at the top of the change list.


admin.site.register(Question, QuestionAdmin)