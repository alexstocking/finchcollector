from django.db import models
from django.urls import reverse

from datetime import date

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name_species = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    habitat = models.CharField(max_length=250)
    diet = models.CharField(max_length=250)
    average_lifespan = models.CharField(max_length=50)
    image_url = models.URLField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name_species
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    
class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(
      max_length=1,
      choices=MEALS,
      default=MEALS[0][0]
    )
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
  
  def __str__(self):
      return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
      ordering = ['-date']