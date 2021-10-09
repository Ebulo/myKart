from django.db import models


class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=60, default="")
    SubCategory = models.CharField(max_length=60, default="")
    price = models.IntegerField(default=0)
    desc = models.TextField(max_length=40000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")
    special_offer = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    Email = models.CharField(max_length=60, default="")
    phone = models.CharField(max_length=20, default="")
    desc = models.TextField(max_length=10000)

    def __str__(self):
        return self.name
