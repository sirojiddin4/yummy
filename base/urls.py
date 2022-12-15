
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("logout/", views.log_out, name="logout"),
    path('accounts/login', auth_views.LoginView.as_view(), name="login"),
    
    
    path('', views.HomeView.as_view(), name='home'),
    path('menuitem/', views.MenuItemList.as_view(), name='menuitemlist'),
    path('menuitem/create', views.MenuItemCreate.as_view(), name='menuitemcreate'),
    path('menuitem/<slug:pk>/update', views.MenuItemUpdate.as_view(), name='menuitemupdate'),
    path('menuitem/<slug:pk>/delete', views.MenuDelete.as_view(), name='menudelete'),
    
    path('ingredient/', views.IngredientList.as_view(), name='ingredientlist'),
    path('ingredient/create', views.IngredientCreate.as_view(), name='ingredientcreate'),
    path('ingredient/<slug:pk>/update', views.IngredientUpdate.as_view(), name='ingredientupdate'),
    path('ingredient/<slug:pk>/delete', views.IngredientDelete.as_view(), name='ingredientdelete'),

    path('purchase/', views.PurchaseList.as_view(), name='purchaselist'),
    path('purchase/create', views.PurchaseCreate.as_view(), name='purchasecreate'),
    path('purchase/<slug:pk>/delete', views.PurchaseDelete.as_view(), name='purchasedelete'),


    path('recipe/create', views.NewRecipeRequirementView.as_view(), name='recipecreate'),
    path('report/', views.ReportView.as_view(), name='report'),
    
]
