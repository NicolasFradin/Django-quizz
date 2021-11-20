from django.db import models
from django.utils import timezone

#This class is used to create (created_at, updated_at, deleted_at) fields for each object where inherited
# auto_now_add -> update the date only when model created
# auto_now -> update the date at each .save()
class TimeStampMixin(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		abstract = True			#abstract_class (can't be instanciated)



