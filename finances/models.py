from django.db import models

# Create your models here.
class Category(models.Model):
    TYPE_CHOICES = [
        ('RE', 'Receita'),
        ('DE', 'Despesa'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Transaction(models.Model):
    TYPE_CHOICES = [
        ('RE', 'Receita'),
        ('DE', 'Despesa'),
    ]
    
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    description = models.TextField(null = True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Trasaction'
        verbose_name_plural = 'Transactions'
    
    def __str__(self):
        return f"{self.category.name} - R${self.value}"


class Account(models.Model):
    name = models.CharField(max_length=100)
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        ordering = ['name']
    
    def __str__(self):
        return self.name
