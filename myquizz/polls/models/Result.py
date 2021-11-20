from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
from .Quizz import Quizz
from polls.TimeStampMixin import TimeStampMixin				#Abstract class for dates


class Result(TimeStampMixin):
	
	quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	score = models.FloatField()


	def __str__(self):
		return str(self.pk)