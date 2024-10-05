from re import A
from django.contrib import admin
from .models import *
from django.contrib.admin.models import LogEntry


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'user', 'content_type', 'object_id', 'action_flag', 'change_message')
    list_filter = ('action_time', 'user', 'content_type', 'action_flag')
    search_fields = ('change_message', 'user__username')
# Register your models here.
admin.site.register(Sexe)
admin.site.register(Client)
admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(Type_operation)
admin.site.register(Stock)
admin.site.register(stock_autre)
admin.site.register(Consultation)
admin.site.register(Paiement)
admin.site.register(Depense)
admin.site.register(Sortie)
admin.site.register(Prescription)
admin.site.register(Ordonnance_lunette)
admin.site.register(type_verre)
admin.site.register(Information)

admin.site.register(MatierePremiereLunette)
admin.site.register(PointFocalLunette)
admin.site.register(TeinteLunette)
admin.site.register(TraitementLunette)
admin.site.register(Lunette)
admin.site.register(stock_lunette)

