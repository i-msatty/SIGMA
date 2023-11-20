from django.db import models
from django.contrib.auth.models import User

class counsellors(models.Model):
    counsellor_id =  models.ForeignKey(User,primary_key=True,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=100)
    email = models.EmailField()
    gender_choices = (
        ("1", "MALE"),
        ("2", "FEMALE"),
        ("3", "Any other"),
    )
    gender = models.CharField(max_length=20, choices=gender_choices, default="1")
    profile_picture = models.ImageField(
        upload_to="Counsellorsphotos/%Y/%m/%d/", blank=True
    )

    def __str__(self):
        return self.firstName + " " + self.lastName
