from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class AddNewCarCreateView(CreateView):
    model = Car
    template_name = 'new_car.html'
    form_class = CarForm
    success_url = reverse_lazy('cars_list')

class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search)

        return queryset
    

class CarDetailView(DetailView):
    model = Car
    template_name = 'cars_detail.html'
    context_object_name = 'car'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'update_car.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = reverse_lazy('cars_list')











'''class CarsView(View):
    def get(self, request):
        cars = Car.objects.all()
        search = request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search).order_by('model')

        return render(
            request,
            'cars.html',
            {'cars': cars})'''
    



'''class AddNewCarView(View):

    def get(self, request):
        add_new_car = CarForm()

        return render(
        request,
        'new_car.html',
        {'add_new_car': add_new_car}  
    )

    def post(self, request):
        add_new_car = CarForm(request.POST, request.FILES)
        print(request.FILES)
 
        if add_new_car.is_valid():
            
            add_new_car.save()
            return redirect('cars_list')
        return render(
        request,
        'new_car.html',
        {'add_new_car': add_new_car}  
    )'''



'''def add_new_car(request):

    add_new_car = CarForm()
    
    if request.method == 'POST':
        # Instancia o formulário com os dados enviados pelo usuário
        add_new_car = CarForm(request.POST, request.FILES)
     
        if add_new_car.is_valid():
            add_new_car.save()
            return redirect('cars_list')
  
    return render(
        request,
        'new_car.html',
        {'add_new_car': add_new_car}  # Certifique-se de usar o mesmo nome aqui
    )
'''
