from django.db import models
from .Question import Question
from polls.TimeStampMixin import TimeStampMixin				#Abstract class for dates
from django.utils.translation import gettext_lazy as _ 		#used for translation

class Choice(TimeStampMixin):
	
	class Meta:
		verbose_name = _('Choice')
		verbose_name_plural = _('Choices')
		ordering = ['id']

	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200, verbose_name="Choice Text")
	is_correct = models.BooleanField(default=False, verbose_name="Is Correct ?")
	is_active = models.BooleanField(default=True, verbose_name="Active Status ?")



	def __str__(self):
		return self.choice_text