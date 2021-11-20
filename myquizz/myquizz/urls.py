"""myquizz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#Avec DRF, il est fréquent de voir cette bonne pratique oubliée et pour cause : 
#tous les routeurs sont déclarés dans le fichier d'URLconf racine. 
#Les applications n'ont pas leur mot à dire sur le chemin souhaité. Tous les imports de Viewset sont faits dans le fichier d'URLconf racine à la bourrin. 
#La séparation n'est plus stricte.
#C'est la méthode officielle rrecommandée

from django.contrib import admin
from django.urls import include, path

#WITHOUT ROUTER
urlpatterns = [
	# Some Web views
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),			#Add Django site authentication urls (for login, logout, password management)
    path('polls/', include('polls.urls', namespace='polls')),
]


#WITH ROUTER 
from rest_framework.routers import DefaultRouter

# from bar.viewsets import BarViewSet		#Fichier contenant uniquement les vues API
# from baz.viewsets import BazViewSet
# from foo.viewsets import FooViewSet

router = DefaultRouter()
router.register('api/bar', BarViewSet)
router.register('api/baz', BazViewSet)
router.register('api/foo', FooViewSet)

# Append our API views
urlpatterns += router.urls






