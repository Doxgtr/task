from django.db import models

class Employee(models.Model):

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    department = models.CharField(max_length=100)

    salary = models.IntegerField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Active'
    )

    def __str__(self):
        return self.name