from django.views import generic
from .models import Product
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import logout
from datetime import datetime, date, time
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse


class IndexView(generic.ListView):
    template_name = "product/index.html"
    context_object_name = "latest_product_list"

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name = "product/detail.html"

class BaseView(generic.DetailView):
    model = Product
    template_name = "product/base.html"

class DeliveryCreate(LoginRequiredMixin, generic.CreateView):
    model = Product
    fields = ['name_product','count_product','destination_adress','date_delivery','status']

class DeliveryUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Product
    fields = ['name_product', 'count_product', 'destination_adress', 'date_delivery', 'status']

class DeliveryDelete(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('product:index')

class UserFormView(generic.View):
    form_class = UserForm
    template_name = 'product/registration_form.html'

    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('product:index')

        return render(request, self.template_name, {'form': form})

class LoginView(generic.View):
    form_class = UserForm
    template_name = 'product/login_form.html'
    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponse("ОК")
            else:
                return HttpResponse("Inactive user.")
        else:
            return render(request, self.template_name, {'form': form})

        return redirect('product:index')

class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(generic.settings.LOGIN_REDIRECT_URL)