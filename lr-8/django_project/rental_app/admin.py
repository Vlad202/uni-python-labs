from django.contrib import admin
from .models import Tenant, Premise, RentalAgreement

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'manager_name', 'phone')
    search_fields = ('company_name', 'manager_name')
    list_filter = ('company_name',)

@admin.register(Premise)
class PremiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'area', 'rent_cost', 'floor', 'phone_in_premise', 'decoration_type')
    search_fields = ('decoration_type',)
    list_filter = ('floor', 'decoration_type', 'phone_in_premise')

@admin.register(RentalAgreement)
class RentalAgreementAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'duration_days', 'purpose', 'tenant', 'premise')
    search_fields = ('purpose',)
    list_filter = ('start_date', 'purpose', 'tenant', 'premise')
    date_hierarchy = 'start_date'  # Для фильтрации по дате