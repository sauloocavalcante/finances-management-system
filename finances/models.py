from django.db import models

# Create your models here.
class Category(models.Model):
    TYPE_CHOICES = [
        ('RE', 'Receita'),
        ('DE', 'Despesa'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    color = models.CharField(max_length=7, default='#000000')
    icon = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Transaction(models.Model):
    TYPE_CHOICES = [
        ('RE', 'Receita'),
        ('DE', 'Despesa'),
    ]
    
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    
    class Meta:
        verbose_name = 'Trasaction'
        verbose_name_plural = 'Transactions'
    
    def __str__(self):
        return f"{self.description[:50]} - R${self.value}"


class Account(models.Model):
    name = models.CharField(max_length=100)
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=7, default='#000000')
    
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
    
    def __str__(self):
        return self.name
