from django.db import models

class Employee(models.Model):
    id_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=20)
    details = models.TextField(blank=True, null=True)  # New field for details

    def __str__(self):
        return self.name