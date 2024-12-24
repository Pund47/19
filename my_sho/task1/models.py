from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=50)     #- имя покупателя (username аккаунта)
    balance = models.DecimalField(max_digits=10, decimal_places=2)  #- баланс(DecimalField)
    age = models.IntegerField()      #- возраст.

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=50)#- название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  #- цена(DecimalField)
    size = models.DecimalField(max_digits=10, decimal_places=2) #- размер файлов игры(DecimalField)
    description = models.TextField() #- описание(неограниченное кол - во текста)
    age_limited = models.BooleanField(default=False)#- ограничение возраста 18 + (BooleanField, по умолчанию False)
    buyer = models.ManyToManyField(Buyer,related_name='games') #- покупатель обладающий игрой(ManyToManyField).
                                                          # У каждого покупателя может быть игра и у каждой игры
                                                          #может быть несколько обладателей.
    DecimalField = models.FloatField()#- поле для дробных чисел.
    BooleanField = models.BooleanField()#- поле для булевых значений.

    def __str__(self):
        return self.title