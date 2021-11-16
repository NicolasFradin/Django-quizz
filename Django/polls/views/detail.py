# Create your views here.
#
# The "controllers" in Django are basically what Django calls views. 
# So you have your model classes, which are the M obviously. 
# The templates/HTML are basically the V in MVC. 
# Django views (either functions or classes) are effectively callbacks that run for a particular URL, and they tend to be where a lot of the logic is. 
# So for example, you'll have a Django view called get_foo_bar that runs when someone makes a GET request to /foo/bar, and the Django view effectively becomes the C in MVC.
#
# Each view is responsible for doing one of two things: 
#		->returning an HttpResponse object containing the content for the requested page, 
#		->or raising an exception such as Http404.


#from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from ..models import Question


def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")

	#question = get_object_or_404(Question, pk=question_id)
	
	return render(request, 'polls/detail.html', {'question': question})