from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.utils.dateparse import parse_datetime

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = []
    def list(self,request,*args,**kwargs):
        return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    def create(self,request,*args,**kwargs):
        return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    def update(self,request,*args,**kwargs):
        return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    def partial_update(self,request,*args,**kwargs):
        return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    def destroy(self,request,*args,**kwargs):
        return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    @action(detail=False, methods=['get'])
    def group_site(self,request):
        site= Group.objects.values("name","id").filter(name__startswith="SITE")
        return Response (site)
    @action(detail=False, methods=['get'])
    def group_fonction(self,request):
        site= Group.objects.values("name","id").exclude(name__startswith="SITE")
        return Response (site)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    def create(self,request,*args,**kwargs):
        return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    # def update(self,request,*args,**kwargs):
    #         return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    # def partial_update(self,request,*args,**kwargs):
            # return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    def destroy(self,request,*args,**kwargs):
            return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def destroy(self,request,*args,**kwargs):
            return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    def list(self,request):
        clients =Client.objects.values("site__name","sexe__libelle_sexe","nom_client","numero_client","adresse","id").order_by('-dates_client') 
        return Response(clients)
    @action(detail=False, methods=['get'])
    def medecin_list(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            Consultation=Client.objects.values("id","nom_client","sexe","sexe__libelle_sexe","age","consultation","consultation__site__name","consultation__dates_consultation").filter(consultation__site=site_id).order_by("-id")
            Prescription=Client.objects.values("id","nom_client","sexe","sexe__libelle_sexe","age","prescription","prescription__dates_prescription","prescription__site__name").filter(prescription__site=site_id).order_by("-id")
            lunette=Client.objects.values("id","nom_client","sexe","sexe__libelle_sexe","age","ordonnance_lunette","ordonnance_lunette__dates_ordonnance","ordonnance_lunette__site__name").filter(ordonnance_lunette__site=site_id).order_by("-id")

        elif int(site_id)==0:
            Consultation=Client.objects.values("id","nom_client","sexe","sexe__libelle_sexe","age","consultation","consultation__site__name","consultation__dates_consultation").filter(consultation__site=site_id).order_by("-id")
            Prescription=Client.objects.values("id","nom_client","sexe","sexe__libelle_sexe","age","prescription","prescription__dates_prescription","prescription__site__name").filter(prescription__site=site_id).order_by("-id")
            lunette=Client.objects.values("id","nom_client","sexe","sexe__libelle_sexe","age","ordonnance_lunette","ordonnance_lunette__dates_ordonnance","ordonnance_lunette__site__name").filter(ordonnance_lunette__site=site_id).order_by("-id")
        return Response({"consultation":Consultation,"prescription":Prescription,"lunette":lunette })

    @action(detail=False, methods=['get'])
    def by_site(self, request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0 :
            clients =Client.objects.values("site__name","sexe__libelle_sexe","nom_client","numero_client","adresse","id").order_by('-id')
        elif int(site_id)==0:
            clients =Client.objects.values("site__name","sexe__libelle_sexe","nom_client","numero_client","adresse","id").order_by('-id')   
        return Response(clients)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def destroy(self,request,*args,**kwargs):
        return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    @action(detail=False, methods=['get'])
    def prix(self, request):
        article_id=request.query_params.get('article_id', None)
        articles =Article.objects.values("prix").filter(id=article_id)
        return Response(articles)
    @action(detail=False,methods=['get'])
    def categorie(self,request):
        categorie=Categorie.objects.values("id","libelle_categorie").exclude(libelle_categorie="verre")
        return Response(categorie)
    @action(detail=False,methods=['get'])
    def list_article(self,request):
        article=Article.objects.values("id",'categorie',"categorie__libelle_categorie","libelle_article","prix") #.exclude(categorie__libelle_categorie="consultation & examen")
        return Response(article)
        
class VenteViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def list(self,request, *args, **kwargs):
        Stocks=Stock.objects.values("dates_stock","numero_facture","client__nom_client","client__numero_client","article__libelle_article","montant_fixe","prix_convenu","remise","site__name").filter(Type_operation__libelle_type="vente")
        return Response(Stocks)
    @action(detail=False, methods=['get'])
    def by_site(self, request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            Stocks =Stock.objects.values("site__name","dates_stock","numero_facture","client__nom_client","article__libelle_article","montant_fixe","prix_convenu","quantite","remise").filter(site=site_id,Type_operation__libelle_type="vente").order_by('-id')
        elif int(site_id)==0:
            Stocks =Stock.objects.values("site__name","dates_stock","numero_facture","client__nom_client","article__libelle_article","montant_fixe","prix_convenu","quantite","remise").filter(Type_operation__libelle_type="vente").order_by('-id')
        return Response(Stocks)

    @action(detail=False, methods=['get'])
    def by_client(self, request):
        client_id=request.query_params.get('client_id', None)
        stock= Stock.objects.values("dates_stock","numero_facture","article__libelle_article","quantite","prix_convenu").filter(client=client_id,Type_operation__libelle_type="vente")
        return Response(stock)

    @action(detail=False, methods=['get'])
    def liste_facture_by_client(self, request):
        client_id=request.query_params.get('client_id', None)
        site_id=request.query_params.get('site_id', None)
        stock= Stock.objects.values("numero_facture","dates_stock").filter(client=client_id).annotate(totals=models.Sum("prix_convenu"))
        accompte=Paiement.objects.filter(client=client_id).aggregate(models.Sum('montant'))
        return Response({ "facture":stock,"accompte":accompte } )


    @action(detail=False, methods=['get'])
    def by_facture(self, request):
        numero_facture=request.query_params.get('numero_facture', None)
        stock= Stock.objects.values("id","dates_stock","client__nom_client","client","montant_fixe","remise","numero_facture","article__libelle_article","quantite","prix_convenu").filter(numero_facture=numero_facture,Type_operation__libelle_type="vente")
        return Response(stock)

    @action(detail=False, methods=['get'])
    def by_site_and_date(self, request):
        Stocks={}
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        site_id=request.query_params.get('site_id', None)
        print(start_date)
        try:    
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)
            print(end_date)
            site_id=request.query_params.get('site_id', None)
            if int(site_id)>0:
                Stocks =Stock.objects.values("site__name","dates_stock","numero_facture","client__nom_client","article__libelle_article","montant_fixe","prix_convenu","quantite","remise").order_by('-id').filter(dates_stock__range=(start_date, end_date)).filter(site=site_id,Type_operation__libelle_type="vente").order_by('-id')
            elif int(site_id)==0:
                Stocks =Stock.objects.values("site__name","dates_stock","numero_facture","client__nom_client","article__libelle_article","montant_fixe","prix_convenu","quantite","remise").order_by('-id').filter(dates_stock__range=(start_date, end_date),Type_operation__libelle_type="vente").order_by('-id')    
        except:
            print("erreur")
            pass
        return Response(Stocks)
             
    @action(detail=False, methods=['get'])
    def facture(self,request):
        site_id=request.query_params.get('site_id', None)
        facture=Stock.objects.values("numero_facture").filter(site=site_id).order_by("-id").distinct()
        return Response(facture)

    @action(detail=False, methods=['get'])
    def by_client(self,request):
        client_id=request.query_params.get("client_id",None)
        stock=Stock.objects.values("id","client","dates_stock","client__nom_client","article","article__libelle_article","quantite","montant_fixe","prix_convenu",'remise').filter(client=client_id)
        return Response(stock)
    @action(detail=False, methods=['get'])
    def etat_stock_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            entree_stock=Stock.objects.values("article","article__libelle_article","article__prix").filter(site=site_id,Type_operation__libelle_type="entree").exclude(article__categorie__libelle_categorie="consultation & examen").annotate(quantite_entree=models.Sum("quantite"))
            sortie_stock=Stock.objects.values("article","article__libelle_article","article__prix").filter(site=site_id).exclude(Type_operation__libelle_type="entree").exclude(article__categorie__libelle_categorie="consultation & examen").annotate(quantite_entree=models.Sum("quantite"))
        elif int(site_id)==0:
            entree_stock=Stock.objects.values("article","article__libelle_article","article__prix").filter(Type_operation__libelle_type="entree").exclude(article__categorie__libelle_categorie="consultation & examen").annotate(quantite_entree=models.Sum("quantite"))
            sortie_stock=Stock.objects.values("article","article__libelle_article","article__prix").exclude(Type_operation__libelle_type="entree").exclude(article__categorie__libelle_categorie="consultation & examen").annotate(quantite_entree=models.Sum("quantite"))
        etat_stock={ "entree": entree_stock,"sortie":sortie_stock }
        return Response(etat_stock)

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class Ordonnance_lunetteViewSet(viewsets.ModelViewSet):
    queryset = Ordonnance_lunette.objects.all()
    serializer_class = Ordonnance_lunetteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class PaiementViewSet(viewsets.ModelViewSet):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def list(self, request):
        paiement=Paiement.objects.values("id","dates_paiement","facture","client","client__nom_client","user","user__username","site","site__name","montant")
        return Response(paiement)
    @action(detail=False, methods=['get'])
    def accompte(self,request):
        client_id= request.query_params.get("client_id",None)
        total_montant=Paiement.objects.values("montant").filter(client=client_id).aggregate(total_montant=models.Sum("montant"))
        return Response(total_montant)
    @action(detail=False, methods=['get'])
    def accompte_by_facture(self,request):
        numero_facture= request.query_params.get("numero_facture",None)
        total_montant=Paiement.objects.values("montant").filter(facture=numero_facture).aggregate(total_montant=models.Sum("montant"))
        return Response(total_montant)
    @action(detail=False, methods=['get'])
    def by_site_and_date(self,request):
        paiement={}
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        site_id= request.query_params.get("site_id",None)
        try:
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)
            if int(site_id)>0:
                paiement=Paiement.objects.values("id","dates_paiement","facture","client","client__nom_client","user","user__username","site","site__name","montant").order_by('-id').filter(site=site_id).filter(dates_paiement__range=(start_date, end_date)).order_by('-id')
            elif int(site_id)==0:
                paiement=Paiement.objects.values("id","dates_paiement","facture","client","client__nom_client","user","user__username","site","site__name","montant").order_by('-id').filter(dates_paiement__range=(start_date, end_date)).order_by('-id')
        except:
            pass
        return Response(paiement)
    @action(detail=False, methods=['get'])
    def by_site(self,request):
        site_id= request.query_params.get("site_id",None)
        if int(site_id)>0:
            paiement=Paiement.objects.values("id","dates_paiement","facture","client","client__nom_client","user","user__username","site","site__name","montant").order_by('-id').filter(site=site_id)
        elif int(site_id)==0:
            paiement=Paiement.objects.values("id","dates_paiement","facture","client","client__nom_client","user","user__username","site","site__name","montant").order_by('-id')
        
        return Response(paiement)

class SexeViewSet(viewsets.ModelViewSet):
    queryset = Sexe.objects.all()
    serializer_class = SexeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class DepenseViewSet(viewsets.ModelViewSet):
    queryset = Depense.objects.all()
    serializer_class = DepenseSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    
class SortieViewSet(viewsets.ModelViewSet):
    queryset = Sortie.objects.all()
    serializer_class = SortieSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def list(self, request):
        sortie=Sortie.objects.values("id","dates_sortie","depense__initule_depense","montant_depense","user","site")
        return Response(sortie)
    
    @action(detail=False, methods=['get'])
    def by_site(self, request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            sortie=Sortie.objects.values("id","site__name","dates_sortie","depense__initule_depense","montant_depense","user","site").filter(site=site_id).order_by("-id")
        elif int(site_id)==0:
            sortie=Sortie.objects.values("id","site__name","dates_sortie","depense__initule_depense","montant_depense","user","site").order_by("-id")
        return Response(sortie)
    @action(detail=False, methods=['get'])
    def by_site_and_date(self, request):
        sortie={}
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        site_id=request.query_params.get('site_id', None)
        print(start_date)
        try:    
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)
            print(end_date)
            site_id=request.query_params.get('site_id', None)
            if int(site_id)>0:
                sortie=Sortie.objects.values("id","dates_sortie","depense__initule_depense","montant_depense","user","site").filter(site=site_id).order_by("-id").filter(dates_sortie__range=(start_date, end_date))
            elif int(site_id)==0:
                sortie=Sortie.objects.values("id","dates_sortie","depense__initule_depense","montant_depense","user","site").order_by("-id").filter(dates_sortie__range=(start_date, end_date))   
        except:
            print("erreur")
            pass
        
        return Response(sortie)
    
class AutreStockViewSet(viewsets.ModelViewSet):
    queryset = stock_autre.objects.all()
    serializer_class = StockAutreSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    @action(detail=False, methods=['get'])
    def by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        entree_stock={}
        if int(site_id)>0:
            entree_stock=Stock.objects.values("id","dates_stock","Type_operation__libelle_type","article__libelle_article","user__username","site","quantite","prix_convenu").filter(site=site_id).exclude(Type_operation__libelle_type="vente").order_by("-id")
        elif int(site_id)==0:
            entree_stock=Stock.objects.values("id","dates_stock","Type_operation__libelle_type","article__libelle_article","user__username","site","quantite","prix_convenu").exclude(Type_operation__libelle_type="vente").order_by("-id")
        return Response(entree_stock)
    @action(detail=False, methods=['get'])
    def by_site_and_and(self,request):
        entree_stock={}
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        site_id=request.query_params.get('site_id', None)
        print(start_date)
        try:    
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)
            print(end_date)
            site_id=request.query_params.get('site_id', None)
            if int(site_id)>0:
                entree_stock=stock_autre.objects.values("id","dates_entree","type_operation__libelle_type","article__libelle_article","user__username","site","quantite","prix_unitaire").filter(site=site_id).order_by("-id").filter(dates_sortie__range=(start_date, end_date))
            elif int(site_id)==0:
                entree_stock=stock_autre.objects.values("id","dates_entree","type_operation__libelle_type","article__libelle_article","user__username","site","quantite","prix_unitaire").order_by("-id").filter(dates_sortie__range=(start_date, end_date))
        except:
            print("erreur")
            pass
        return Response(entree_stock)

    @action(detail=False, methods=['get'])
    def etat_stock_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            entree_stock=stock_autre.objects.values("article","article__libelle_article","article__prix").filter(site=site_id,type_operation__libelle_type="entree").annotate(quantite_entree=models.Sum("quantite"))
            sortie_stock=stock_autre.objects.values("article","article__libelle_article","article__prix").filter(site=site_id,type_operation__libelle_type="sortie").annotate(quantite_entree=models.Sum("quantite"))
        elif int(site_id)==0:
            print("0 error")
            entree_stock=stock_autre.objects.values("article","article__libelle_article","article__prix").filter(type_operation__libelle_type="entree").annotate(quantite_entree=models.Sum("quantite"))
            sortie_stock=stock_autre.objects.values("article","article__libelle_article","article__prix").filter(type_operation__libelle_type="sortie").annotate(quantite_entree=models.Sum("quantite"))
        etat_stock={ "entree": entree_stock,"sortie":sortie_stock }
        return Response(etat_stock)
    @action(detail=False, methods=['get'])
    def liste_autre_stock(self,request):
        article=Article.objects.values("id",'categorie',"categorie__libelle_categorie","libelle_article","prix").exclude(categorie__libelle_categorie="verre")
        return Response(article)
        
class StockLunetteViewSet(viewsets.ModelViewSet):
    queryset = stock_lunette.objects.all()
    serializer_class = StockLunetteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    @action(detail=False, methods=['get'])
    def by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            entree_stock=stock_lunette.objects.values("id","dates","type_operation__libelle_type","Lunette__MatierePremiereLunette__MatierePremiereLunette","Lunette__PointFocalLunette__PointFocalLunette","Lunette__TeinteLunette__TeinteLunette","Lunette__TraitementLunette__TraitementLunette","user__username","site__name","quantites","prix_unitaire").filter(site=site_id).order_by("-id")
        elif int(site_id)==0:
            entree_stock=stock_lunette.objects.values("id","dates","type_operation__libelle_type","Lunette__MatierePremiereLunette__MatierePremiereLunette","Lunette__PointFocalLunette__PointFocalLunette","Lunette__TeinteLunette__TeinteLunette","Lunette__TraitementLunette__TraitementLunette","user__username","site__name","quantites","prix_unitaire").order_by("-id")
        return Response(entree_stock)
    @action(detail=False, methods=['get'])
    def by_site_and_and(self,request):
        entree_stock={}
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        site_id=request.query_params.get('site_id', None)
        print(start_date)
        try:    
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)
            print(end_date)
            site_id=request.query_params.get('site_id', None)
            if int(site_id)>0:
                entree_stock=stock_lunette.objects.values("id","dates","type_operation__libelle_type","Lunette__MatierePremiereLunette__MatierePremiereLunette","Lunette__PointFocalLunette__PointFocalLunette","Lunette__TeinteLunette__TeinteLunette","Lunette__TraitementLunette__TraitementLunette","user__username","site__name","quantites","prix_unitaire").filter(site=site_id).order_by("-id").filter(dates_sortie__range=(start_date, end_date))
            elif int(site_id)==0:
                entree_stock=stock_lunette.objects.values("id","dates","type_operation__libelle_type","Lunette__MatierePremiereLunette__MatierePremiereLunette","Lunette__PointFocalLunette__PointFocalLunette","Lunette__TeinteLunette__TeinteLunette","Lunette__TraitementLunette__TraitementLunette","user__username","site__name","quantites","prix_unitaire").order_by("-id").filter(dates_sortie__range=(start_date, end_date))
        except:
            print("erreur")
            pass
        return Response(entree_stock)

    @action(detail=False, methods=['get'])
    def etat_stock_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            entree_stock=stock_lunette.objects.values("Lunette","Lunette__MatierePremiereLunette__MatierePremiereLunette","Lunette__PointFocalLunette__PointFocalLunette","Lunette__TeinteLunette__TeinteLunette","Lunette__TraitementLunette__TraitementLunette","Lunette__prix_article").filter(site=site_id,type_operation__libelle_type="entree").annotate(quantite_entree=models.Sum("quantites"))
            sortie_stock=stock_lunette.objects.values("Lunette","Lunette__MatierePremiereLunette__MatierePremiereLunette","Lunette__PointFocalLunette__PointFocalLunette","Lunette__TeinteLunette__TeinteLunette","Lunette__TraitementLunette__TraitementLunette","Lunette__prix_article").filter(site=site_id,type_operation__libelle_type="sortie").annotate(quantite_entree=models.Sum("quantites"))
        elif int(site_id)==0:
            entree_stock=stock_lunette.objects.values("Lunette","Lunette__MatierePremiereLunette__MatierePremiereLunette","Lunette__PointFocalLunette__PointFocalLunette","Lunette__TeinteLunette__TeinteLunette","Lunette__TraitementLunette__TraitementLunette","Lunette__prix_article").filter(type_operation__libelle_type="entree").annotate(quantite_entree=models.Sum("quantites"))
            sortie_stock=stock_lunette.objects.values("Lunette","Lunette__MatierePremiereLunette__MatierePremiereLunette","Lunette__PointFocalLunette__PointFocalLunette","Lunette__TeinteLunette__TeinteLunette","Lunette__TraitementLunette__TraitementLunette","Lunette__prix_article").filter(type_operation__libelle_type="sortie").annotate(quantite_entree=models.Sum("quantites"))
        
        etat_stock={ "entree": entree_stock,"sortie":sortie_stock }
        return Response(etat_stock)
    @action(detail=False, methods=['get'])
    def liste_lunette(self,request):
        article=Lunette.objects.values("id","MatierePremiereLunette__MatierePremiereLunette","PointFocalLunette__PointFocalLunette","TeinteLunette__TeinteLunette","TraitementLunette__TraitementLunette","prix_article")
        return Response(article)
        
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user=User.objects.values("id","username","groups","groups__name").filter(id=user.pk)
        return Response({
            "user":user,
            'token': token.key
        })

class ManagementViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    # management  vente 
    
    @action(detail=False, methods=['get'])
    def vente_bysite(self,request):
        site_id=request.query_params.get('site_id', None)
        vente={}
        if site_id>0:
            vente=Article.objects.values("libelle_article").filter(stock__site=site_id).annotate(total_vente=models.Sum("stock__total"))
        elif site_id==0:
            vente=Article.objects.values("libelle_article").annotate(total_vente=models.Sum("stock__total"))    
        return Response(vente)
    @action(detail=False, methods=['get'])
    def vente_by_site_and_date(self,request):
        vente={}
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        site_id=request.query_params.get('site_id', None)
        try:    
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)
            print(end_date)
            site_id=request.query_params.get('site_id', None)
            if int(site_id)>0:
                vente=Article.objects.values("libelle_article").filter(stock__Type_operation__libelle_type="vente",stock__site=site_id,stock__dates_stock__range=(start_date, end_date)).annotate(total_vente=models.Sum("stock__total"))
            elif int(site_id)==0:
                vente=Article.objects.values("libelle_article").filter(stock__Type_operation__libelle_type="vente",stock__dates_stock__range=(start_date, end_date)).annotate(total_vente=models.Sum("stock__total"))        
        except:
            pass
        return Response(vente)

    # management perception
    @action(detail=False, methods=['get'])
    def perception_bysite(self,request):
        site_id=request.query_params.get('site_id', None)
        if site_id>0:
            vente = Client.objects.values("id","nom_client").filter(stock__site=site_id).annotate(total_ventes=models.Sum('stock__total'))
            paiement=Client.objects.values("id","nom_client").filter(paiement__site=site_id).annotate(total_paiements=models.Sum('paiement__montant'))
        elif site_id==0:
            vente= Client.objects.values("id","nom_client").annotate(total_ventes=models.Sum('stock__total'))
            paiement=Client.objects.values("id","nom_client").annotate(total_paiements=models.Sum('paiement__montant'))
        return Response( {"vente": vente, "paiement": paiement } )
    
    @action(detail=False, methods=['get'])
    def perception_bysite_and_date(self,request):
        vente={}
        paiement={}
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        site_id=request.query_params.get('site_id', None)
        try:  
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)
            site_id=request.query_params.get('site_id', None)
            if int(site_id)>0:
                vente= Client.objects.values("id","nom_client").filter(stock__site=site_id, stock__dates_stock__range=(start_date, end_date) ).annotate(total_ventes=models.Sum('stock__total'))
                paiement=Client.objects.values("id","nom_client").filter(paiement__site=site_id,paiement__dates_paiement__range=(start_date, end_date)).annotate(total_paiements=models.Sum('paiement__montant'))
            elif int(site_id)==0:
                vente= Client.objects.values("id","nom_client").filter(stock__dates_stock__range=(start_date, end_date) ).annotate(total_ventes=models.Sum('stock__total'))
                paiement=Client.objects.values("id","nom_client").filter(paiement__dates_paiement__range=(start_date, end_date)).annotate(total_paiements=models.Sum('paiement__montant'))
                
        except:
            pass 
        return Response({"vente": vente, "paiement": paiement })

    # management depense 
    @action(detail=False, methods=['get'])
    def Depense_bysite(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            paiement=Depense.objects.values("initule_depense").filter(sortie__site=site_id).annotate(total_depense=models.Sum("sortie__montant_depense"))
        elif int(site_id)==0:
            paiement=Depense.objects.values("initule_depense").annotate(total_depense=models.Sum("sortie__montant_depense"))
        return Response(paiement)
    
    @action(detail=False, methods=['get'])
    def Depense_by_site_and_date(self,request):
        vente={}
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        site_id=request.query_params.get('site_id', None)
        try:    
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)
            site_id=request.query_params.get('site_id', None)
            if int(site_id)>0:
                vente=Depense.objects.values("initule_depense").filter(sortie__site=site_id,sortie__dates_sortie__range=(start_date, end_date)).annotate(total_depense=models.Sum("sortie__montant_depense"))
            elif int(site_id)==0:
                vente=Depense.objects.values("initule_depense").filter(sortie__dates_sortie__range=(start_date, end_date)).annotate(total_depense=models.Sum("sortie__montant_depense"))
             
        except:
            pass
        return Response(vente)
        # management entree

    @action(detail=False,methods=['get'])
    def entree_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        entree=0
        if int(site_id)==0:
            entree=Paiement.objects.aggregate(total=models.Sum("montant"))
        elif int(site_id)>0:
            entree=Paiement.objects.filter(site=site_id).aggregate(total=models.Sum("montant"))
    
    @action(detail=False,methods=['get'])
    def entree_by_site_and_date(self,request):
        site_id=request.query_params.get('site_id', None)
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        entree=0
        try:    
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)
            site_id=request.query_params.get('site_id', None)
            if int(site_id)==0:
                entree=Paiement.objects.filter(dates_paiement__range=(start_date, end_date)).aggregate(total=models.Sum("montant"))
            elif int(site_id)>0:
                entree=Paiement.objects.filter(site=site_id,dates_paiement__range=(start_date, end_date)).aggregate(total=models.Sum("montant"))
        except:
            pass
        return Response(entree)

# management reste
    
    @action(detail=False, methods=['get'])
    def reste_bysite(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            vente= Client.objects.values("id","nom_client").filter(stock__site=site_id).aggregate(total_ventes=models.Sum('stock__total'))
            paiement=Client.objects.values("id","nom_client").filter(paiement__site=site_id).aggregate(total_paiements=models.Sum('paiement__montant'))
        elif int(site_id)==0:
            vente= Client.objects.values("id","nom_client").aggregate(total_ventes=models.Sum('stock__total'))
            paiement=Client.objects.values("id","nom_client").aggregate(total_paiements=models.Sum('paiement__montant'))
        return Response( {"vente": vente, "paiement": paiement } )
    
    @action(detail=False, methods=['get'])
    def History_client_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            historique = Client.history.all().filter(site=site_id)
            serializer = HistoryClientSerializer(historique, many=True)
        elif int(site_id)==0:
            historique = Client.history.all()
            serializer = HistoryClientSerializer(historique, many=True)
            
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def History_article_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            historique = Article.history.all().filter(site=site_id)
            serializer = HistoryArticleSerializer(historique, many=True)
        elif int(site_id)==0:
            historique = Article.history.all()
            serializer = HistoryArticleSerializer(historique, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def History_vente_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            historique = Stock.history.values("history_date","history_type","history_user__username","site__name","dates_stock","numero_facture","client__nom_client","article__libelle_article","montant_fixe","prix_convenu","quantite","remise").filter(site=site_id)
        elif int(site_id)==0:
            historique = Stock.history.values("history_date","history_type","history_user__username","site__name","dates_stock","numero_facture","client__nom_client","article__libelle_article","montant_fixe","prix_convenu","quantite","remise")  
        return Response(historique)
    
    @action(detail=False, methods=['get'])
    def History_paiement_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            historique = Paiement.history.all().filter(site=site_id)
            serializer = HistoryPaiementSerializer(historique, many=True)
        elif int(site_id)==0:
            historique = Paiement.history.all()
            serializer = HistoryPaiementSerializer(historique, many=True)
            
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def History_sortie_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        if int(site_id)>0:
            historique = Sortie.history.values("history_id","history_user__username","history_type","id","dates_sortie","montant_depense","history_date","site","depense__initule_depense").filter(site=site_id)
        elif int(site_id)==0:
            historique = Sortie.history.values("history_id","history_user__username","history_type","id","dates_sortie","montant_depense","history_date","site","depense__initule_depense")
        
        # serializer = HistorySortieSerializer(historique, many=True)
        return Response(historique)
    
    @action(detail=False, methods=['get'])
    def History_consultation_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        historique = Consultation.history.all().filter(site=site_id)
        serializer = HistoryConsultationSerializer(historique, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def History_prescription_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        historique = Consultation.history.all().filter(site=site_id)
        serializer = HistoryPrescriptionSerializer(historique, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def History_ordonnance_lunette_by_site(self,request):
        site_id=request.query_params.get('site_id', None)
        historique = Ordonnance_lunette.history.all().filter(site=site_id)
        serializer = HistoryOrdonnance_lunetteSerializer(historique, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def user_list(self,request):
        site_id=request.query_params.get('site_id',None)
        if int(site_id)>0:
            user=User.objects.values("id","username",'password',"groups__name","is_active").filter(groups=site_id,is_active=True).order_by('-is_active', 'username')
        elif int(site_id)==0:
            user=User.objects.values("id","username",'password',"groups__name","is_active").filter(is_active=True).order_by('-id','username')
        return Response(user)
    
class InformationViewSet(viewsets.ModelViewSet):
    queryset =Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def destroy(self,request,*args,**kwargs):
            return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    def create(self,request,*args,**kwargs):
        return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )

class LunetteViewSet(viewsets.ModelViewSet):
    queryset =Lunette.objects.all()
    serializer_class = LunetteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def destroy(self,request,*args,**kwargs):
            return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    def create(self,request,*args,**kwargs):
            return Response({"message":" cette methode n'est pas autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED )
    @action(detail=False,methods=['get'])
    def composition(self,request):
        MP=MatierePremiereLunette.objects.values("id","MatierePremiereLunette")
        PO=PointFocalLunette.objects.values("id","PointFocalLunette")
        TT=TeinteLunette.objects.values("id","TeinteLunette")
        TMT=TraitementLunette.objects.values("id","TraitementLunette")
        
        return Response({
            "matiere":MP,
            "pointfocal":PO,
            "Teinte":TT,
            "traiement":TMT
        })