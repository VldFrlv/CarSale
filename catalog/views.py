from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.db.models import F

from .models import Car
from .forms import CarForm


class Home(ListView):
    model = Car
    template_name = 'catalog/home.html'
    context_object_name = 'cars'
    paginate_by = 3


class ViewCar(DetailView):
    queryset = Car.objects.select_related('seller')
    context_object_name = 'car_item'
    template_name = 'catalog/car_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ViewCar, self).get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


@login_required
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.seller = request.user
            form.save()
            return redirect('personal_area')
    else:
        form = CarForm()
    context = {'form': form}
    return render(request, 'catalog/add.html', context)


@login_required
def user_personal_area(request):
    user_cars = Car.objects.select_related('seller').filter(seller=request.user)
    context = {'user_cars': user_cars}
    return render(request, 'catalog/personal_area.html', context)


class DeleteCar(LoginRequiredMixin, DeleteView):
    model = Car
    context_object_name = 'user_car'
    template_name = 'catalog/deleteconfirmation.html'
    success_url = '/personal_area'


class EditCarView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'catalog/edit_car.html'
