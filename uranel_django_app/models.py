from pydoc import doc
from pyexpat import model
from statistics import quantiles
from tabnanny import verbose
from xml.dom.minidom import Document
from django.db import models
from django.contrib.auth.models import User,Group
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from simple_history.models import HistoricalRecords
# Create your models here.
class Type_operation(models.Model):
    libelle_type=models.CharField( max_length=20)
    class Meta:
        verbose_name = ("Type_operation")
        verbose_name_plural = ("Type_operations")

    def __str__(self):
        return self.libelle_type

    def get_absolute_url(self):
        return reverse("Type_operation_detail", kwargs={"pk": self.pk})


class MatierePremiereLunette(models.Model):
    MatierePremiereLunette=models.CharField(max_length=30)
    class Meta:
        verbose_name = ("MatierePremiereLunettes")
        verbose_name_plural = ("MatièrePremiereLunette")
    def __str__(self):
        return self.MatierePremiereLunette



class PointFocalLunette(models.Model):
    PointFocalLunette=models.CharField(max_length=30)
    class Meta:
        verbose_name = ("PointFocalLunettes")
        verbose_name_plural = ("PointFocalLunette")
    def __str__(self):
        return self.PointFocalLunette


class TeinteLunette(models.Model):
    TeinteLunette=models.CharField(max_length=30)
    class Meta:
        verbose_name = ("TeinteLunettes")
        verbose_name_plural = ("TeinteLunette")
    def __str__(self):
        return self.TeinteLunette


class TraitementLunette(models.Model):
    TraitementLunette=models.CharField(max_length=30)
    class Meta:
        verbose_name = ("TraitementLunettes")
        verbose_name_plural = ("TraitementLunette")
    def __str__(self):
        return self.TraitementLunette


class Lunette(models.Model):
    MatierePremiereLunette=models.ForeignKey(MatierePremiereLunette,on_delete=models.CASCADE)
    PointFocalLunette=models.ForeignKey(PointFocalLunette,on_delete=models.CASCADE)
    TeinteLunette=models.ForeignKey(TeinteLunette,on_delete=models.CASCADE)
    TraitementLunette=models.ForeignKey(TraitementLunette,on_delete=models.CASCADE)
    prix_article=models.FloatField()
    class Meta:
        verbose_name = ("Lunettes")
        verbose_name_plural = ("Lunette")
    def __str__(self):
        return f" {self.MatierePremiereLunette} - {self.PointFocalLunette} - {self.TeinteLunette } - {self.TraitementLunette } "


class stock_lunette(models.Model):
    dates=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    site=models.ForeignKey(Group,on_delete=models.CASCADE)
    Lunette=models.ForeignKey(Lunette,on_delete=models.CASCADE)
    type_operation=models.ForeignKey(Type_operation,on_delete=models.CASCADE)
    quantites=models.FloatField()
    prix_unitaire=models.FloatField()
    motif=models.TextField()
    class Meta:
        verbose_name = ("stock_lunettes")
        verbose_name_plural = ("stock_lunette")


class Information(models.Model):
    numero_telephone1=models.CharField(max_length=30)
    numero_telephone2=models.CharField(max_length=30)
    mail1=models.CharField(max_length=50)
    mail2=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)
    class Meta:
        verbose_name = ("informations")
        verbose_name_plural = ("information")





class Depense(models.Model):
    initule_depense=models.CharField(max_length=50)
    class Meta:
        verbose_name=("depens")
        verbose_name_plural=("depenses")
    def __str__(self):
        return self.initule_depense

    def get_absolute_url(self):
        return reverse("Depense_detail", kwargs={"pk": self.pk})



class Sexe(models.Model):
    libelle_sexe=models.CharField(max_length=20)
    class Meta:
        verbose_name = ("Sexe")
        verbose_name_plural = ("Sexes")

    def __str__(self):
        return self.libelle_sexe

    def get_absolute_url(self):
        return reverse("Civilite_detail", kwargs={"pk": self.pk})

class type_verre(models.Model):
    libelle_type_verre=models.CharField(max_length=30)
    class Meta:
        verbose_name = ("Type_verre")
        verbose_name_plural = ("Type_verres")

    def __str__(self):
        return self.libelle_type_verre

    def get_absolute_url(self):
        return reverse("Type_verre_detail", kwargs={"pk": self.pk})

class Client(models.Model):
    dates_client=models.DateTimeField(auto_now_add=True)
    nom_client=models.CharField(max_length=120)
    numero_client=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    site=models.ForeignKey(Group, on_delete=models.CASCADE)
    sexe= models.ForeignKey(Sexe, on_delete=models.CASCADE)
    adresse=models.CharField(max_length=120)
    age=models.FloatField()
    # history = AuditlogHistoryField()
    history = HistoricalRecords()
    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")

    def __str__(self):
        return self.nom_client

    def get_absolute_url(self):
        return reverse("Client_detail", kwargs={"pk": self.pk})


class Categorie(models.Model):
    libelle_categorie=models.CharField(max_length=50)
    class Meta:
        verbose_name = ("Categorie")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.libelle_categorie

    def get_absolute_url(self):
        return reverse("Categorie_detail", kwargs={"pk": self.pk})


class Article(models.Model):
    libelle_article=models.CharField( max_length=50)
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    prix=models.FloatField()
    # history = AuditlogHistoryField()
    history = HistoricalRecords()
    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.libelle_article

    def get_absolute_url(self):
        return reverse("Article_detail", kwargs={"pk": self.pk})


class Vente(models.Model):
    dates_stock=models.DateField( auto_now_add=True)
    numero_facture=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    site=models.ForeignKey(Group,on_delete=models.CASCADE)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    article=models.ForeignKey("Article", on_delete=models.CASCADE)
    quantite=models.FloatField()
    montant_fixe=models.FloatField()
    prix_convenu=models.FloatField()
    remise=models.FloatField()
    total=models.FloatField()
    # history = AuditlogHistoryField()
    history = HistoricalRecords()
   
    class Meta:
        verbose_name = ("Vente")
        verbose_name_plural = ("ventes")

    # def __str__(self):
    #     return self.pk

    def get_absolute_url(self):
        return reverse("Stock_detail", kwargs={"pk": self.pk})

class Consultation(models.Model):
    dates_consultation=models.DateField( auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    site=models.ForeignKey(Group,on_delete=models.CASCADE)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    plainte=models.TextField()
    diagnostique=models.TextField()
    traitement=models.TextField()
    # history = AuditlogHistoryField()
    history = HistoricalRecords()
    

    class Meta:
        verbose_name = ("Consultation")
        verbose_name_plural = ("Consultations")
    # def __str__(self):
    #     return self.pk

    def get_absolute_url(self):
        return reverse("Consultation_detail", kwargs={"pk": self.pk})

class Prescription(models.Model):
    dates_prescription=models.DateField( auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    site=models.ForeignKey(Group,on_delete=models.CASCADE)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    Prescription=models.TextField()
    # history = AuditlogHistoryField()
    history = HistoricalRecords()
    class Meta:
        verbose_name = ("Prescription")
        verbose_name_plural = ("Prescriptions")
    # def __str__(self):
    #     return self.pk

    def get_absolute_url(self):
        return reverse("prescription_detail", kwargs={"pk": self.pk})


class Ordonnance_lunette(models.Model):
    dates_ordonnance=models.DateField( auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    site=models.ForeignKey(Group,on_delete=models.CASCADE)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    type_verre=models.CharField(max_length=100)
    # history = AuditlogHistoryField()
    history = HistoricalRecords()
    #oeil droit 
    sphere_vl_od=models.CharField(default='(vide)',max_length=30)
    cylindre_vl_od=models.CharField(max_length=30,default='(vide)')
    axe_vl_od=models.CharField(max_length=30,default='(vide)')
    addition_vl_od=models.CharField(max_length=30,default='(vide)')

    sphere_vp_od=models.CharField(max_length=30,default='(vide)')
    cylindre_vp_od=models.CharField(max_length=30,default='(vide)')
    axe_vp_od=models.CharField(max_length=30,default='(vide)')
    addition_vp_od=models.CharField(max_length=30,default='(vide)')
    

    # oeil gauche

    sphere_vl_og=models.CharField(max_length=30,default='(vide)')
    cylindre_vl_og=models.CharField(max_length=30,default='(vide)')
    axe_vl_og=models.CharField(max_length=30,default='(vide)')
    addition_vl_og=models.CharField(max_length=30,default='(vide)')

    sphere_vp_og=models.CharField(max_length=30,default='(vide)')
    cylindre_vp_og=models.CharField(max_length=30,default='(vide)')
    axe_vp_og=models.CharField(max_length=30,default='(vide)')
    addition_vp_og=models.CharField(max_length=30,default='(vide)')
    
    
    class Meta:
        verbose_name = ("Ordonnance_lunette")
        verbose_name_plural = ("Ordonnance_lunettes")
    # def __str__(self):
    #     return self.pk

    def get_absolute_url(self):
        return reverse("Ordonnance_lunette_detail", kwargs={"pk": self.pk})

class Paiement(models.Model):
    dates_paiement=models.DateField( auto_now_add=True)
    site=models.ForeignKey(Group, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    facture=models.CharField(max_length=50)
    montant=models.FloatField()
    # history = AuditlogHistoryField()
    history = HistoricalRecords()
    class Meta:
        verbose_name = ("Paiement")
        verbose_name_plural = ("Paiements")
    def get_absolute_url(self):
        return reverse("Paiement_detail", kwargs={"pk": self.pk})

class Sortie(models.Model):
    dates_sortie=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    site=models.ForeignKey(Group,on_delete=models.CASCADE)

    depense=models.ForeignKey(Depense,on_delete=models.CASCADE)
    montant_depense=models.FloatField()
    # history = AuditlogHistoryField()
    history = HistoricalRecords()
    class Meta:
        verbose_name = ("Sortie")
        verbose_name_plural = ("Sorties")

    def get_absolute_url(self):
        return reverse("Sortie_detail", kwargs={"pk": self.pk})

class stock_autre(models.Model):
    dates_entree=models.DateField( auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    site=models.ForeignKey(Group,on_delete=models.CASCADE)
    type_operation=models.ForeignKey(Type_operation,on_delete=models.CASCADE)
    article=models.ForeignKey("Article", on_delete=models.CASCADE)
    quantite=models.FloatField()
    prix_unitaire=models.FloatField()
    motif=models.TextField()
   

auditlog.register(Client)
auditlog.register(Article)
auditlog.register(Vente)


auditlog.register(Consultation)
auditlog.register(Prescription)
auditlog.register(Ordonnance_lunette)


auditlog.register(Paiement)
auditlog.register(Sortie)
