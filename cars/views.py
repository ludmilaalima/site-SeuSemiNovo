from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.views import View

# Create your views here.

class CarsView(View):
    def get(self, request):
        cars = Car.objects.all()
        search = request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search).order_by('model')

        return render(
            request,
            'cars.html',
            {'cars': cars})
    


class AddNewCarView(View):

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
    )



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
