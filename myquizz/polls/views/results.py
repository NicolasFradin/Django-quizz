# Create your views here.

#
# The "controllers" in Django are basically what Django calls views. 
# So you have your model classes, which are the M obviously. 
# The templates/HTML are basically the V in MVC. 
# Django views (either functions or classes) are effectively callbacks that run for a particular URL, and they tend to be where a lot of the logic is. 
# So for example, you'll have a Django view called get_foo_bar that runs when someone makes a GET request to /foo/bar, and the Django view effectively becomes the C in MVC.
#


# from django.shortcuts import get_object_or_404, render
# from ..models import Choice, Question


# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'question': question})



#Using generic views : 

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from ..models import Choice, Question

class ResultsView(generic.DetailView):
    model = Question  	#model = Question is really just shorthand for saying queryset = Question.objects.all()
    template_name = 'polls/results.html'