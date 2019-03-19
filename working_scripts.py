import random
from python_test.models import Client
from faker import Faker

# Generate 30 fake Clients
fake = Faker('en_AU')

for x in range(1, 31):
    client = fake.company()
    first_name = fake.first_name()
    last_name = fake.last_name()
    contact_name = first_name + " " + last_name
    email = fake.email()
    phone = fake.phone_number()
    street = fake.street_name()
    post_code = fake.postcode()
    suburb = fake.city()
    number = random.randint(1, 1000)
    state = random.randint(1, 15)

    Client.objects.create(
        client_name=client,
        email=email,
        phone=phone,
        contact_name=contact_name,
        street=street,
        house_number=number,
        suburb=suburb,
        post_code=post_code,
        state=state
    )

# python3 manage.py shell < working_scripts.py
