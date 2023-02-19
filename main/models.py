from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Manufaturer(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Item(models.Model):
    inventory_number = models.IntegerField()
    manufacturer = models.ForeignKey(Manufaturer, on_delete=models.PROTECT)
    country = models.CharField(max_length=32)
    model = models.CharField(max_length=64)

    def __str__(self):
        return self.model


class Supply(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name='supplies')
    storage = models.ForeignKey('Storage', on_delete=models.PROTECT, related_name='supplies')
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Storage(models.Model):
    name = models.CharField(max_length=32)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.name