from django.urls import path
from .views import *


# URLconf file who redirect all url of this application
# Need to be added to root URLconf as 'app/'

app_name = 'polls'		#add namespaces to your URLconf to use the {% url %} template tag and Django will target the right app view name
urlpatterns = [
    # ex: /polls/
    path('', index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', vote, name='vote'),
]
