from django.db import models

# Create your models here.

sex_choices = (("m", "male"), ("f","female"))
choices = (('y', "yes"), ("n", "no"))
smoke_choice = (("N", "Never Smoked"), ("F", "Former Smoker"), ("C", "Current Smoker"))
tem_choices = (("34.0","Normal"),("37.5 - 38.0°C", "Low Fever" ), ("38.1-39.0°C", "High Fever"), (">39.0°C", "Very High Fever"))

class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=20, )
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=sex_choices)
    country = models.CharField(max_length=20)
    postal_code = models.IntegerField()

    smoking_history = models.CharField(max_length=20, choices=smoke_choice)

    #### health data
    chronic_opd = models.CharField(max_length=10, choices=choices)
    diabetes = models.CharField(max_length=10, choices=choices)
    hypertension = models.CharField(max_length=10, choices=choices)
    coronary_hd = models.CharField(max_length=10, choices=choices)
    cerebrovascular = models.CharField(max_length=10, choices=choices)
    hepatitis_b = models.CharField(max_length=10, choices=choices)
    cancer = models.CharField(max_length=10, choices=choices)
    chronic_renal = models.CharField(max_length=10, choices=choices)
    immunodeficiency = models.CharField(max_length=10, choices=choices)

    #### selftest
    screening_test = models.CharField(max_length=10, choices=choices)

    ####
    current_location = models.CharField(max_length=20)
    current_postalcode = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    temperature_pills = models.CharField(max_length=20, choices=tem_choices, default=None)


    def __str__(self):
        return f'{self.username} Profile'
