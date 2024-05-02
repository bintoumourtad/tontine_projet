from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=10)
    email = models.CharField(max_length=25)
    motdepasse = models.CharField(max_length=30)
    date_naissance = models.DateTimeField(auto_now_add=True)
    adress = models.CharField(max_length=20)
    numero_telephon = models.CharField(max_length=20)

    def __str__(self):
       return  f"{self.nom}{self.prenom}{self.adress}{self.date_naissance}{self.email}{self.numero_telephon}"


class groupetontinee(models.Model):
    nom = models.CharField(max_length=150)
    cotisation_amount = models.CharField(max_length=150)
    frequence_despaiement = models.CharField(max_length=50)
    date_decréation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom}{self.cotisation_amount}{self.frequence_despaiement}{self.date_decréation}"

  
class rolee(models.Model):
    nom = models.CharField(max_length=150)
    def __str__(self):
       return f"{self.nom}"

class paiements(models.Model):
    nom =models.CharField(max_length=150)
    prenom =models.CharField(max_length=150)
    montant_paiement =models.CharField(max_length=150)
    date_paeiement =models.DateTimeField()
    def __str__(self):
        return f"{self.montant_paiement}{self. date_paeiement}{self. nom}{self. prenom}"


class contribution(models.Model):
    nom =models.CharField(max_length=150)
    prenom =models.CharField(max_length=150)
    montant =models.CharField(max_length=150)
    date =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nom}{self.prenom}{self.date}"


class membree(models.Model):
    nom_groupe = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=10)
    numero_telephon = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.nom_groupe}{self.nom}{self.prenom}{self.numero_telephon}"


