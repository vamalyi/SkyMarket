from django.db import models

# Create your models here.


class Pilot(models.Model):
    name = models.CharField()
    email = models.CharField()
    photo = models.ImageField()
    address = models.CharField()
    contact_info = models.CharField()
    area = models.CharField()
    description = models.CharField()
    date_on_add = models.CharField()
    # SCOUTING_TYPES = []
    scout_type = models.CharField()
    drone_type = models.CharField()
    sensor_type = models.CharField()
    category = models.ManyToManyField(Category)
    price = models.CharField()

    status = models.CharField()



class Client(models.Model):
    name = models.CharField()
    email = models.CharField()

    address = models.CharField()
    contact_info = models.CharField()
    photo = models.ImageField()

    # status = models.CharField()



class Order(models.Model):
    name = models.CharField()
    description = models.CharField()
    budget = models.CharField()
    status = models.CharField()
    sensor_type = models.CharField()
    address = models.CharField()
    shape_on_map = models.CharField()

    date_on_add = models.DateField()
    date_start = models.DateField()
    date_finish = models.DateField()

    category = models.ManyToManyField(Category)

    pilot = models.ForeignKey(Pilot)
    client = models.ForeignKey(Client)


class Delivery(models.Model):
    description = models.CharField()

    pilot = models.ForeignKey(Pilot)
    client = models.ForeignKey(Client)
    order = models.ForeignKey(Order)

    data = models.CharField()
    date_on_add = models.DateField()
    status = models.CharField()
    # status = models.CharField()


class Category(models.Model):
    name = models.CharField()
    description = models.CharField()
