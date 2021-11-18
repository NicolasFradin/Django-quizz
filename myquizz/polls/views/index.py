
# Create your views here.

#
# The "controllers" in Django are basically what Django calls views. 
# So you have your model classes, which are the M obviously. 
# The templates/HTML are basically the V in MVC. 
# Django views (either functions or classes) are effectively callbacks that run for a particular URL, and they tend to be where a lot of the logic is. 
# So for example, you'll have a Django view called get_foo_bar that runs when someone makes a GET request to /foo/bar, and the Django view effectively becomes the C in MVC.
#


# from django.shortcuts import render
# #from django.http import HttpResponse
# #from django.template import loader
# from ..models import Question

# #The context is a dictionary mapping template variable names to Python objects.
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	context = {'latest_question_list': latest_question_list}
# 	return render(request, 'polls/index.html', context)		#render() returns an HttpResponse object of the given template rendered with the given context


#Using generic views : 

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from ..models import Choice, Question

from django.utils import timezone
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
	template_name = 'polls/index.html'				#the ListView generic view uses a default template called <app name>/<model name>_list.html; we use template_name to tell ListView to use our existing "polls/index.html" template.
	context_object_name = 'latest_question_list' 	#ListView, the automatically generated context variable is 'question_list'. To override this we provide the context_object_name attribute, specifying that we want to use latest_question_list instead.



		#Specifying model = Publisher is really just shorthand for saying queryset = Publisher.objects.all(). 
		#However, by using queryset to define a filtered list of objects you can be more specific about the objects that will be visible in the view 
	#Handily, the ListView has a get_queryset() method we can override. 
	#Previously, it has just been returning the value of the queryset attribute, but now we can add more logic.
	def get_queryset(self):
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]  #returns a queryset containing Questions whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.
