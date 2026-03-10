from django.db import models

class Member(models.Model):
    YEAR_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', 'Visitor'),
        ('6', 'Alumni'),
        ('7', 'Staff'),
    ]
    CLASS_CHOICES = [
        ('Vine branches', 'Vine branches'),
        ('Bible Scholars', 'Bible Scholars'),
        ('LightBearers', 'LightBearers'),
    ]

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    year_of_study = models.CharField(choices=YEAR_CHOICES,default='1')
    class_name = models.CharField(max_length=50, choices=CLASS_CHOICES, default='Bible Scholars')
    registration_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"
