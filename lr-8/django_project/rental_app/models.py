from django.db import models

class Tenant(models.Model):
    company_name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name

class Premise(models.Model):
    area = models.DecimalField(max_digits=5, decimal_places=2)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    floor = models.IntegerField()
    phone_in_premise = models.BooleanField(default=False)
    decoration_type = models.CharField(max_length=20, choices=[('звичайне', 'Звичайне'), ('поліпшене', 'Поліпшене'), ('євро', 'Євро')])

    def __str__(self):
        return f"Premise {self.id}"

class RentalAgreement(models.Model):
    start_date = models.DateField()
    duration_days = models.IntegerField()
    purpose = models.CharField(max_length=20, choices=[('офіс', 'Офіс'), ('кіоск', 'Кіоск'), ('склад', 'Склад')])
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    premise = models.ForeignKey(Premise, on_delete=models.CASCADE)

    def __str__(self):
        return f"Agreement {self.id}"
