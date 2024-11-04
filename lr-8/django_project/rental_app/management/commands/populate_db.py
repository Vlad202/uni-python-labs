from django.core.management.base import BaseCommand
from rental_app.models import Tenant, Premise, RentalAgreement
from faker import Faker
import random
from datetime import timedelta, date

fake = Faker('uk_UA')

class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **kwargs):
        # Создание арендаторов
        tenants = []
        for _ in range(10):
            tenant = Tenant.objects.create(
                company_name=fake.company(),
                manager_name=fake.name(),
                phone=fake.phone_number()
            )
            tenants.append(tenant)

        # Создание помещений
        premises = []
        for _ in range(20):
            premise = Premise.objects.create(
                area=round(random.uniform(20, 100), 2),
                rent_cost=round(random.uniform(5000, 20000), 2),
                floor=random.randint(1, 10),
                phone_in_premise=fake.boolean(),
                decoration_type=random.choice(['звичайне', 'поліпшене', 'євро'])
            )
            premises.append(premise)

        # Создание договоров аренды
        for _ in range(15):
            RentalAgreement.objects.create(
                start_date=fake.date_this_decade(),
                duration_days=random.randint(30, 365),
                purpose=random.choice(['офіс', 'кіоск', 'склад']),
                tenant=random.choice(tenants),
                premise=random.choice(premises)
            )

        self.stdout.write(self.style.SUCCESS('Database populated with fake data'))
