from django.urls import path
from .views import home
from .views import groupe 
from .views import paiementt
from .views import add
from .views import addrec
from .views import delete
from .views import update
from .views import uprec
from .views import contributions
from .views import addd
from .views import addrecc
from .views import deletee
from .views import updatee
from .views import uprecc
from .views import  groupe_details
from .views import  new_groupe
from .views import  edit_groupe
from .views import  liste









urlpatterns = [
    path('', home, name='home'),
    path('groupe/' , groupe, name= 'groupe'),
    path('groupe/liste/' , liste, name= 'liste'),
    path('groupe/<int:id>/' , groupe_details, name= 'details'),
    path('groupe/new/' , new_groupe, name= 'new'),
    path('groupe/edit/<int:id>/' , edit_groupe, name= 'edit'),
    path('paiementt/' , paiementt, name= 'paiementt'),
    path('add/', add, name="add"),
    path("addrec/",  addrec, name="addrec"),
    path('delete/<int:id>/', delete,name="delete"),
    path('update/<int:id>/', update,name="update"),
    path('update/uprec/<int:id>/', uprec,name="uprec"),
    path('contributions/' , contributions, name= 'contributions'),
    path('addd/', addd, name="addd"),
    path("addrecc/",  addrecc, name="addrecc"),
    path('deletee/<int:id>/', deletee,name="deletee"),
    path('updatee/<int:id>/', updatee,name="updatee"),
    path('updatee/uprecc/<int:id>/', uprecc,name="uprecc"),

]