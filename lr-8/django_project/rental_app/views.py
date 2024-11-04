# rental_app/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Tenant, Premise, RentalAgreement

def project_info(request):
    tenants = Tenant.objects.all()
    premises = Premise.objects.all()
    rental_agreements = RentalAgreement.objects.select_related('tenant', 'premise').all()

    tenant_paginator = Paginator(tenants, 10)
    premise_paginator = Paginator(premises, 10)
    rental_agreement_paginator = Paginator(rental_agreements, 10)

    tenant_page = request.GET.get('tenant_page')
    premise_page = request.GET.get('premise_page')
    rental_agreement_page = request.GET.get('rental_agreement_page')

    context = {
        'project_name': 'Проект оренди приміщень (лаба 8)',
        'student_name': 'Думанський Владлен Юрійович',
        'student_group': 'Група ІПЗ-22011бск',
        'tenants': tenant_paginator.get_page(tenant_page),
        'premises': premise_paginator.get_page(premise_page),
        'rental_agreements': rental_agreement_paginator.get_page(rental_agreement_page),
    }

    return render(request, 'rental_app/project_info.html', context)
