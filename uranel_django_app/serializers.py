from dataclasses import field, fields
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User,Group
from simple_history.utils import update_change_reason

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Utiliser la méthode `create_user` pour s'assurer que le mot de passe est haché
        user = User.objects.create_user(**validated_data)
        return user
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields='__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields='__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields='__all__'


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Consultation
        fields='__all__'


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prescription
        fields='__all__'


class Ordonnance_lunetteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ordonnance_lunette
        fields='__all__'



class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paiement
        fields='__all__'
    
    


class SexeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sexe
        fields='__all__'
    
    
class SortieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sortie
        fields='__all__'
    
class StockAutreSerializer(serializers.ModelSerializer):
    class Meta:
        model=stock_autre
        fields='__all__'


class MatierePremiereLunetteSerializer(serializers.ModelSerializer):
    class Meta:
        model=MatierePremiereLunette
        fields='__all__'

class PointFocalLunetteSerializer(serializers.ModelSerializer):
    class Meta:
        model=PointFocalLunette
        fields='__all__'

class LunetteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lunette
        fields='__all__'




class StockLunetteSerializer(serializers.ModelSerializer):
    class Meta:
        model=stock_lunette
        fields='__all__'



class DepenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Depense
        fields='__all__'

class ClientSummarySerializer(serializers.ModelSerializer):
    total_ventes = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    total_paiements = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Client
        fields = ['nom_client', 'total_ventes', 'total_paiements']

# history

class HistoryClientSerializer(serializers.ModelSerializer):
    history_user = serializers.StringRelatedField()
    history_type = serializers.CharField(source='get_history_type_display')
    class Meta:
        model = Client.history.model
        fields ='__all__'


class HistoryArticleSerializer(serializers.ModelSerializer):
    history_user = serializers.StringRelatedField()
    history_type = serializers.CharField(source='get_history_type_display')
    class Meta:
        model = Article.history.model
        fields ='__all__'

class HistoryStockSerializer(serializers.ModelSerializer):
    history_user = serializers.StringRelatedField()
    history_type = serializers.CharField(source='get_history_type_display')
    class Meta:
        model = Stock.history.model
        fields ='__all__'

class HistoryPaiementSerializer(serializers.ModelSerializer):
    history_user = serializers.StringRelatedField()
    history_type = serializers.CharField(source='get_history_type_display')
    class Meta:
        model = Paiement.history.model
        fields ='__all__'


class HistorySortieSerializer(serializers.ModelSerializer):
    history_user = serializers.StringRelatedField()
    history_type = serializers.CharField(source='get_history_type_display')
    class Meta:
        model = Sortie.history.model
        fields ='__all__'

class HistoryConsultationSerializer(serializers.ModelSerializer):
    history_user = serializers.StringRelatedField()
    history_type = serializers.CharField(source='get_history_type_display')

    class Meta:
        model = Consultation.history.model
        fields ='__all__'

class HistorPrescriptionSerializer(serializers.ModelSerializer):
    history_user = serializers.StringRelatedField()
    history_type = serializers.CharField(source='get_history_type_display')
    class Meta:
        model = Prescription.history.model
        fields ='__all__'

class HistoryOrdonnance_lunetteSerializer(serializers.ModelSerializer):
    history_user = serializers.StringRelatedField()
    history_type = serializers.CharField(source='get_history_type_display')
    class Meta:
        model = Ordonnance_lunette.history.model
        fields ='__all__'


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Information
        fields='__all__'
