# Create your views here.

#
# The "controllers" in Django are basically what Django calls views. 
# So you have your model classes, which are the M obviously. 
# The templates/HTML are basically the V in MVC. 
# Django views (either functions or classes) are effectively callbacks that run for a particular URL, and they tend to be where a lot of the logic is. 
# So for example, you'll have a Django view called get_foo_bar that runs when someone makes a GET request to /foo/bar, and the Django view effectively becomes the C in MVC.
#


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from ..models import Choice, Question
from django.contrib.auth.decorators import login_required

# ...
@login_required
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
		    'question': question,
		    'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))