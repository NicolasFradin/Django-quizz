from django.contrib import admin
from django.forms import ModelForm
from polls.models import *
from polls.CustomModelAdminMixin import CustomModelAdminMixin

# Register your models here.
# Add your models where to show them in the Django admin panel
# 		LOCAL -> http://127.0.0.1:8000/admin/



# class ChoiceForm(ModelForm):
# 	class Meta:
# 		model = Choice
# 		fields = '__all__'		#Permet d'afficher le parent dans Admin


class ChoiceAdmin(CustomModelAdminMixin, admin.ModelAdmin):

	#form = ChoiceForm

	# ##########################
	# #         DISPLAY 	     #
	# ##########################

	#list_display = ('choice_text', 'created_at', 'is_correct') #By default, Django displays the str() of each object. But sometimes it’d be more helpful if we could display individual fields. To do that, use the list_display admin option, which is a tuple of field names to display, as columns, on the change list page for the object
	

	# ##########################
	# #     FILTER SIDEBAR 	 #
	# ##########################

	list_filter = ['created_at']  #That adds a “Filter” sidebar that lets people filter the change list by the pub_date field
	

	# ##########################
	# #       SEARCH BOX       #
	# ##########################

	search_fields = ['choice_text'] #That adds a search box at the top of the change list.


admin.site.register(Choice)