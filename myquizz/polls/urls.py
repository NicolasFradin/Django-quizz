from django.urls import path
from . import views

# URLconf file who redirect all url of this application
# Need to be added to root URLconf as 'app/'

#Avec Django, on prend vite l'habitude d'utiliser naturellement le mécanisme d'inclusion d'URLconf. 
#Cela permet de conserver la logique métier des chemins dans les applications respectives et de mettre les préfixes de chemins uniquement dans le projet pour les personnaliser.


# app_name = 'polls'		#add namespaces to your URLconf to use the {% url %} template tag and Django will target the right app view name
# urlpatterns = [
#     # ex: /polls/
#     path('', index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', vote, name='vote'),
# ]

#Using Generic views : third patterns has changed from <question_id> to <pk>
app_name = 'polls'
urlpatterns = [
	# path('', views.IndexView.as_view(), name='index'),
	# path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	# path('<int:question_id>/vote/', views.vote, name='vote'),

	path('', views.QuizzView.as_view(), name='quizz'),
	path('r/<str:topic>', views.RandomQuestionView.as_view(), name='random'),
	path('q/<str:topic>', views.QuizzQuestion.as_view(), name='questions'),


]
