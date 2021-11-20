from django.contrib import admin


#Class which can be inherited to plot all field in admin panel
class CustomModelAdminMixin(object):

	def __init__(self, model, admin_site):
		self.list_display = [field.name for field in model._meta.fields]
		super(CustomModelAdminMixin, self).__init__(model, admin_site)