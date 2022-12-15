from django.db import models
import datetime


# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/menuitem"
    
    def __str__(self):
        return f"{self.title}"    

class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    price_per_unit = models.FloatField(default=0)

    def get_absolute_url(self):
        return "/ingredient"
    
    def __str__(self):
        return f"""
        {self.name} 
        qty: {self.quantity} {self.unit};
        price: {self.price_per_unit}
        """



class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def get_absolute_url(self):
        return "/menuitem"
    
    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"

class Purchase(models.Model):

    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/purchases"
    
    def __str__(self):
        return f"{self.menu_item.__str__()} sold at {self.timestamp}"