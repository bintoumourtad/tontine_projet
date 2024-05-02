from django.shortcuts import render, get_object_or_404 ,redirect
from .models import groupetontinee 
from .models import paiements
from .models import contribution
from .models import membree
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
  return render(request,'pages/index.html')
 
def groupe(request):
  groupe = groupetontinee.objects.all()
  return render(request,"pages/groupe.html",{"groupe": groupe})

def groupe_details(request, id):
  groupe = get_object_or_404(groupetontinee, id=id)
  return render(request, "groupe/groupe_details.html", {"groupe" :groupe})


def new_groupe(request):
  if request.method == "POST":
    nom =request.POST['nom']
    cotisation_amount =request.POST['cotisation_amount']
    frequence_despaiement =request.POST['frequence_despaiement']
    date_decréation =request.POST['date_decréation']
    groupe = groupetontinee.objects.create(
    nom=nom,
    cotisation_amount=cotisation_amount,
    frequence_despaiement=frequence_despaiement,
    date_decréation= date_decréation,
    )
    return redirect('/groupe/')
    

  return render(request, "groupe/new_groupe.html")

def edit_groupe(request, id):
  groupe = get_object_or_404(groupetontinee, id=id)
  if request.method == "POST":
    nom =request.POST['nom']
    cotisation_amount =request.POST['cotisation_amount']
    frequence_despaiement =request.POST['frequence_despaiement']
    date_decréation =request.POST['date_decréation']
    groupe_to_update = groupetontinee.objects.filter (pk= groupe.id)
    groupe_to_update.update(
    nom=nom,
    cotisation_amount=cotisation_amount,
    )

    return redirect('/groupe/')
    


  return render(request, "groupe/edit_groupe.html", {"groupe":groupe})
 


def paiementt(request):
  paiementt = paiements.objects.all()
  return render(request,"pages/paiementt.html",{"paiementt": paiementt})

def contributions(request):
  contributions = contribution.objects.all()
  return render(request,"pages/contribution.html",{"contributions": contributions})
 

def addd(request):
    return render(request,'pages/addd.html')

def addrecc(request):
    x=request.POST['nom']
    y=request.POST['prenom']
    s=request.POST['montant']
    a=request.POST['date']
    contributions=contribution(nom=x,prenom=y,montant=s,date=a)
    
    contributions.save()
    
    return redirect("/contributions/")

def deletee(request,id):
    contributions=contribution.objects.get(id=id)

    contributions.delete()

    return redirect("/contributions/")

def updatee(request,id):
    contributions=contribution.objects.get(id=id)
    return render(request,'pages/updatee.html',{'contributions':contributions})

def uprecc(request,id):
     x=request.POST['nom']
     y=request.POST['prenom']
     s=request.POST['montant']
     a=request.POST['date']
     contributions=contribution.objects.get(id=id)
     contributions.nom=x
     contributions.prenom=y
     contributions.montant=s
     contributions.date=a


     return redirect("/contributions/")


def liste(request):
  liste = membree.objects.all()
  return render(request,"groupe/liste_membre.html",{"liste": liste})


def add(request):
    return render(request,'groupe/add.html')

def addrec(request):
    x=request.POST['nom']
    y=request.POST['prenom']
    z=request.POST['numero_telephon']
    a=request.POST['nom_groupe']
    liste=membree(nom=x,prenom=y,numero_telephon=z,nom_groupe=a)
    liste.save()
    
    return redirect("/groupe/liste/")

def delete(request,id):
    liste=membree.objects.get(id=id)
    liste.delete()
    return redirect("/groupe/liste/")

def update(request,id):
    liste=membree.objects.get(id=id)
    return render(request,'groupe/update.html',{'liste':liste})

def uprec(request,id):
     x=request.POST['nom']
     y=request.POST['prenom']
     z=request.POST['numero_telephon']
     a=request.POST['nom_groupe']
     liste=membree.objects.get(id=id)
     liste.nom=x
     liste.prenom=y
     liste.numero_telephon=z
     liste.nom_groupe=a

     liste.save()
     return redirect("/groupe/liste/")