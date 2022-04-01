from django.db import models

from django.urls import reverse

class Patient(models.Model):
    patient_id = models.AutoField("ID", primary_key=True)
    email = models.EmailField("E-mail", max_length=128)
    phone_number = models.IntegerField("Phone number", max_length=128)
    first_name = models.CharField("First Name", max_length=128)
    last_name = models.CharField("Last Name", max_length=128)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Record(models.Model):
    record_id = models.AutoField("ID", primary_key=True)
    doctor = models.CharField("Doctor", max_length=128)
    record_date = models.DateField("Record Date")
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s' % (self.record_id, self.doctor)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

class Doctor(models.Model):
    category = models.ForeignKey(Category, related_name='doctors')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='doctors/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:doctor_detail', args=[self.id, self.slug])

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name