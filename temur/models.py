from django.db import models

class Car(models.Model):
    model_car = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    number_engine = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.model_car}-{self.number_engine}'
    
class NummerCar(models.Model):
    chance_car = models.OneToOneField(Car, on_delete=models.CASCADE)
    nummer = models.CharField(max_length=100, default='0 KG ')

    def __str__(self):
        return f'{self.chance_car}-{self.nummer}'









class CustomerName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductTemur(models.Model):
    name_product = models.CharField(max_length=100)
    image = models.ImageField(upload_to='temur/')
    customers = models.ManyToManyField(CustomerName)
    STATUS = (
        ('Собран на складе', 'Собран на складе'),
        ('Отправлен', 'Отправлен'),
        ('Получен', 'Получен')
    )

    status = models.CharField(max_length=100, choices=STATUS, default='Собран на складе')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name_product}-----{', '.join(i.name for i in self.customers.all() )}'