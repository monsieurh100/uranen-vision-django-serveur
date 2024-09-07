from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter()

router.register('user',UserViewSet,'user')
router.register('group',GroupViewSet,'group')


router.register('client',ClientViewSet,'client')
router.register('article',ArticleViewSet,'article')
router.register('vente',VenteViewSet,'vente')
router.register('consultation',ConsultationViewSet,'consultation')
router.register('paiement',PaiementViewSet,'paiement')
router.register('sexe',SexeViewSet,'sexe')
router.register('Sortie',SortieViewSet,'sortie')
router.register('Prescription',PrescriptionViewSet,'Prescription')
router.register('Ordonnance_lunette',Ordonnance_lunetteViewSet,'Ordonnance_lunette')
router.register('Depense',DepenseViewSet,'Depense')
router.register("Management",ManagementViewSet,"Management")
router.register('AutreStock',AutreStockViewSet,'AutreStock')
router.register('StockLunette',StockLunetteViewSet,'StockLunette')
router.register("Information",InformationViewSet,"Information")
router.register("Lunette",LunetteViewSet,"Lunette")


urlpatterns = [
    path('',include(router.urls)),
    #  path('api/logs/', LogEntryListView.as_view(), name='logentry-list'),
    # path('votre-modele/<int:pk>/history/', HistoryView.as_view(), name='history-view'),
    # path('votre-modele/<int:pk>/history/', HistoryAPIView.as_view(), name='history-view'),

    
]
