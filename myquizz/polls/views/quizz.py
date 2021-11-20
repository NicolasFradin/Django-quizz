from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from ..models import Quizz, Question
from django.contrib.auth.decorators import login_required

from rest_framework import generics
from ..serializers import QuizzSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# ...
# @login_required
class QuizzView(generics.ListAPIView):

	serializer_class = QuizzSerializer
	queryset = Quizz.objects.all()


class RandomQuestionView(APIView):

	def get(self, request, format=None, **kwargs):
		'''
		Récupérer toutes les catégories en utilisant l’ORM de Django ;

		Sérialiser les données à l’aide de notre serializer ;

		Renvoyer une réponse qui contient les données sérialisées.
		'''

		question = Question.objects.filter(quizz__name=kwargs['topic']).order_by('?')[:1]
		serializer = RandomQuestionSerializer(question, many=True)
		return Response(serializer.data)


class QuizzQuestion(APIView):
	def get(self, request, format=None, **kwargs):
		question = Question.objects.filter(quizz__name=kwargs['topic'])
		serializer = QuestionSerializer(question, many=True)
		return Response(serializer.data)