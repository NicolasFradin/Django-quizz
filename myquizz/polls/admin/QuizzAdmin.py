from django.contrib import admin
from polls.models import Quizz
from polls.models import Question
from polls.CustomModelAdminMixin import CustomModelAdminMixin

# Register your models here.
# Add your models where to show them in the Django admin panel
# 		LOCAL -> http://127.0.0.1:8000/admin/


class QuestionsInline(admin.TabularInline):  #Affichage : StackedInline / TabularInline
	model = Question
	extra = 10


class QuizzAdmin(CustomModelAdminMixin, admin.ModelAdmin):
	#Set fieldsets to control the layout of admin “add” and “change” pages.
	# fieldsets = [
	# 	("TEXT",               {'fields': ['question_text']}),
	# 	('DATE', {'fields': ['pub_date'], 'classes': ['collapse']}),
	# ]

	#showing only a subset of available fields, modifying their order, or grouping them into rows.
	# fields = (('question_text', 'pub_date'), 'quizz')

	inlines = [QuestionsInline]

admin.site.register(Quizz, QuizzAdmin)