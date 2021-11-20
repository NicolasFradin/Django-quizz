from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin
from .Quizz import Quizz
import random
from django.utils.translation import gettext_lazy as _ 		#used for translation
from polls.TimeStampMixin import TimeStampMixin				#Abstract class for dates
""
class Question(TimeStampMixin):
	
	NB_MAX_CHOICES = 4
	SCALES = (
		(0, _('Fundamental')),
		(1, _('Beginner')),
		(2, _('Intermediate')),
		(3, _('Advanced')),
		(4, _('Expert')),
	)
	TYPES = (
		(0, _('Multiple Choice Question')),
	)


	class Meta:
		verbose_name = _('Question')
		verbose_name_plural = _('Questions')
		ordering = ['id']

	quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=255, verbose_name="Title")
	question_text = models.CharField(max_length=2000, verbose_name="Text of Question")
	difficulty = models.IntegerField(choices=SCALES, default=0, verbose_name="Difficulty")
	techique = models.IntegerField(choices=TYPES, default=0, verbose_name="Type of Question")
	is_active = models.BooleanField(default=True, verbose_name="Active Status")
	

	@admin.display(				#Permet de changer le display dans l'admin panel
		boolean=True,			#remplace le str 'True' ou 'False' par un logo
		ordering='created_at',
		description='Published recently?',
	)



	def was_published_recently(self):
		'''
		* If the question was published recently
		*
		* @param  void
		* @return bool
		'''
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.created_at <= now



	def get_choices(self):
		'''
		* Returns only the limited number of choices
		* Select random correct and incorrect choices among all choices available
		* At least there is one correct choice
		*
		* @param  void
		* @return bool
		'''
		nb_correct_random = random.randint(1, 4)
		choices_list = self.choice_set.filter(is_correct=True)
		print(choices_list)

		return self.choice_set.all()		



	def __str__(self):
		return self.question_text