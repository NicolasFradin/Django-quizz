
# Create your views here.

#
# The "controllers" in Django are basically what Django calls views. 
# So you have your model classes, which are the M obviously. 
# The templates/HTML are basically the V in MVC. 
# Django views (either functions or classes) are effectively callbacks that run for a particular URL, and they tend to be where a lot of the logic is. 
# So for example, you'll have a Django view called get_foo_bar that runs when someone makes a GET request to /foo/bar, and the Django view effectively becomes the C in MVC.
#


from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from ..models import Question

#The context is a dictionary mapping template variable names to Python objects.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)		#render() returns an HttpResponse object of the given template rendered with the given context