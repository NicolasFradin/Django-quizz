from rest_framework import serializers
from ..models import Quizz, Question, Choice

#Why Django API REST ?
#Now, let’s say you want to use a frontend framework. 
#If you do not have a REST API, and your frontend code try to request data from one of your URLs, 
#you will get a string data or an HTML page like what you get from using curl, 
#it is not useful to get that data for your frontend. 
#However, if you have a REST API, your backend data will be serialized in the way that your frontend code can understand and deserialize the returned data into some data objects like dictionary which you can use right the way.

#Serializers define the representation of our model in JSON format and convert object instances to a more transferable format. 
#This will simplify the parsing of data for our API. 

#The serializer will handle this scenario gracefully, without you having to write any such logic in views.py. 
#You can simply add validation and other constraints that are needed to the attribute of the serializer class.

#By default, required for every field is set to True. 
#Hence, the serializer will not proceed unless it gets them.

#Deserializers do the opposite - they convert JSON data into our models as object instances.
class QuizzSerializer(serializers.ModelSerializer):
	"""
	Serializer for Quizz data model.
	"""
	class Meta:
		model = Quizz
		# fields = [				#The data we want to collect and serialize
		# 	'name',
		# ]

		fields = '__all__'			#serialize all fields

class ChoiceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Choice 
		fields = [
			'id',
			'choice_text',
			'is_correct',
		]

class RandomQuestionSerializer(serializers.ModelSerializer):

	# choice_set = serializers.StringRelatedField(many=True) #utilise la méthode __str__
	choice_set = ChoiceSerializer(many=True, read_only=True) #

	class Meta:
		model = Question
		fields = [
			'title',
			'difficulty',
			'choice_set',
		]


class QuestionSerializer(serializers.ModelSerializer):

	# choice_set = serializers.StringRelatedField(many=True) #utilise la méthode __str__
	quizz = QuizzSerializer(many=False, read_only=True) #ajoute l'object parent 'Quizz' au JSON de la question dans le champs 'quizz'
	choice_set = ChoiceSerializer(many=True, read_only=True) #

	class Meta:
		model = Question
		fields = [
			'quizz',
			'title',
			'difficulty',
			'choice_set',
		]








