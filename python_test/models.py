from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator

AU_STATES = (
    (1, "New South Wales"),
    (2, "Victoria"),
    (3, "Queensland"),
    (4, "Western Australia"),
    (5, "South Australia"),
    (6, "Tasmania"),
    (7, "Australian Capital Territory"),
    (8, "Northern Territory"),
    (9, "Norfolk Island"),
    (10, "Christmas Island"),
    (11, "Australian Antarctic Territory"),
    (12, "Cocos (Keeling) Islands"),
    (13, "Jervis Bay Territory"),
    (14, "Coral Sea Islands"),
    (15, "Ashmore and Cartier Islands"),
    (16, "Heard Island and McDonald Islands"),
)


# Im not using here the Django User model, if login would be required we would have to create models in a different
# way by extending the User model => you can see the fotoPX application (github) as reference
# client_name, email, phone, suburb are required, the other fields are optional
# I assume that Client name is some company name, contact name is a person within the company

class Client(models.Model):
    client_name = models.CharField(max_length=128, unique=True, null=False, blank=False)
    email = models.CharField(max_length=128, null=False, blank=False)
    # phone as charfield as they may start with 0 and contain "+" etc.
    phone = models.CharField(max_length=24, null=False, blank=False)
    contact_name = models.CharField(max_length=128, null=True, blank=True)
    street = models.CharField(max_length=128, null=True, blank=True)
    # house number as CharField as numbers may contain letters and "/" etc
    house_number = models.CharField(max_length=10, null=True, blank=True)
    suburb = models.CharField(max_length=128, null=False, blank=False)
    post_code = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(9999)])
    state = models.SmallIntegerField(choices=AU_STATES, null=True, blank=True)
