from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

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
		return self.question_text