from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase
from .forms import MenuItemForm, IngredientForm, RecipeForm
from django.views.generic import TemplateView
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import redirect
from django.db.models import Sum, F
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'base/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = MenuItem.objects.all()
        context['ingredient'] = Ingredient.objects.all()
        context['purchase'] = Purchase.objects.all()
        return context

class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'base/menu_list.html'

class MenuItemCreate(LoginRequiredMixin, CreateView):
    template_name="base/menuitem_create.html"
    model = MenuItem
    form_class  = MenuItemForm

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    template_name="base/menuitem_update.html"
    model = MenuItem
    form_class  = MenuItemForm
# Ingredient section


class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'base/ingredient_list.html'

class IngredientCreate(LoginRequiredMixin, CreateView):
    template_name="base/ingredient_create.html"
    model = Ingredient
    form_class  = IngredientForm

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    template_name="base/ingredient_update.html"
    model = Ingredient
    form_class  = IngredientForm

# Purchase section

class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'base/purchase_list.html'

class PurchaseCreate(LoginRequiredMixin, TemplateView):
    template_name="base/purchase_create.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = MenuItem.objects.all()
        return context

    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient=requirement.ingredient
            required_ingredient.quantity-=requirement.quantity
            required_ingredient.save()

        purchase.save()
        return redirect('/purchase')
# New Recipe

class NewRecipeRequirementView( LoginRequiredMixin, CreateView):
    template_name = "base/recipe_create.html"
    model = RecipeRequirement
    form_class = RecipeForm

class PurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "base/purchase_delete.html"
    success_url = '/purchase'


class MenuDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "base/menu_delete.html"
    success_url = '/menuitem'


class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "base/ingredient_delete.html"
    success_url = '/ingredient'

class ReportView(LoginRequiredMixin, TemplateView):
    template_name='base/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price")
        )["revenue"]
        total_cost = 0

        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost +=recipe_requirement.ingredient.price_per_unit *\
                    recipe_requirement.quantity
        
        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context
    

def log_out(request):
    logout(request)
    return redirect('/')



