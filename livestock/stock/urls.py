from django.urls import path,re_path
from . import views

app_name = 'stock'

urlpatterns = [
    path('',views.StockListView.as_view(),name='home'),
    path('<slug:slug>/',views.StockDetailView.as_view(),name='detail'),
    path('update/<slug:slug>/',views.StockUpdateView.as_view(),name='update'),
    path('delete/<slug:slug>/',views.StockDeleteView.as_view(),name='delete'),
    path('user/<str:username>',views.UserStockListView.as_view(), name='user-stocks'),
    path('user/<str:username>/<slug:slug>',views.UserStockDetailView.as_view(),name='user-stock-detail'),


]
