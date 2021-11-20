from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin
from polls.TimeStampMixin import TimeStampMixin				#Abstract class for dates

class Quizz(TimeStampMixin):
	
	DIFF_CHOICES = (
		('easy', 1),
		('medium', 2),
		('hard', 3),
	)



	class Meta:
		#ordering = [‘created’,]
		verbose_name ="Quizz"
		verbose_name_plural ="Quizzes"

	name = models.CharField(max_length=200)
	difficulty = models.CharField(max_length=6, null=True, choices=DIFF_CHOICES, help_text="difficulty of the quizz")

	@admin.display(				#Permet de changer le display dans l'admin panel
		boolean=True,			#remplace le str 'True' ou 'False' par un logo
		ordering='pub_date',
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
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	def __str__(self):
		return self.name