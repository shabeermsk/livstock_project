from django.shortcuts import render,get_object_or_404

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.utils import timezone
from .models import Stock
from .forms import StockForm
from django.contrib.auth.models import User


class StockListView(ListView):
    model = Stock
    paginate_by = 32

    def get_queryset(self):
        return Stock.objects.filter(posted_date__lte=timezone.now())#.order_by('-name'))



class StockDetailView(DetailView):
    model = Stock

class UserStockListView(LoginRequiredMixin,ListView):
    model = Stock
    template_name = 'stock/user_stock_list.html'
    context_object_name = 'stocks'


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Stock.objects.filter(user=user).order_by('-posted_date')


class StockCreateView(LoginRequiredMixin,CreateView):
    redirect_field_name = 'stock/stock_detail.html'
    form_class = StockForm
    model = Stock


    def clean(self):
        cleaned_data = super(StockForm, self).clean()
        location = cleaned_data['location']
        cleaned_data['location'] = ",".join(location)
        return cleaned_data


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




class StockUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    login_url = 'seller/login/'
    redirect_field_name = 'stock/stock_detail.html'

    
    form_class = StockForm
    exclude= {'user','slug','posted_date'}
    model = Stock

    def test_func(self):
        stock=self.get_object()
        if self.request.user == stock.user:
            return True
        return False

class StockDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    login_url = 'seller/login/'
    redirect_field_name = 'stock/stock_detail.html'
    model = Stock
    success_url = reverse_lazy('stock:home')

    def test_func(self):
        stock=self.get_object()
        if self.request.user == stock.user:
            return True
        return False

class UserStockDetailView(LoginRequiredMixin,DetailView):
    model = Stock
    template_name = 'stock/user_stock_detail.html'
