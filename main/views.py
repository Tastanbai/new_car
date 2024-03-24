from django.shortcuts import render, get_object_or_404, redirect 
from .models import Car, Rental 
from .forms import RentalForm
from .forms import ContactForm
from django.contrib import messages 
from django.utils import timezone 
from .models import Feedback



def about(request):
    context={
        'title': 'About'
    }
    return render(request, 'main/about.html', context)


# def contact(request):
#     context = {'title': 'Contact'}

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Создаем объект Feedback и сохраняем его
#             feedback = Feedback(
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 email=form.cleaned_data['email'],
#                 phone_number=form.cleaned_data.get('phone_number', ''),
#                 message=form.cleaned_data['message'],
#             )
#             feedback.save()

#             # Теперь отправляем email
#             send_mail(
#                 subject=f'Message from {feedback.first_name} {feedback.last_name}',
#                 message=feedback.message,
#                 from_email=feedback.email,
#                 recipient_list=['tastan.bay@yandex.kz'],  
#                 fail_silently=False,
#             )
#             return redirect('main:success_page')  
#     else:
#         form = ContactForm()
    
#     context['form'] = form
#     return render(request, 'main/contact.html', context)


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:success_page')  # Укажите здесь имя URL вашей страницы успеха
        # Если форма не валидна, отобразим её снова с сообщениями об ошибках
        else:
            print("********* ERROR")
    else:
        form = ContactForm()
    context = {
        'form': form,
        'title': 'Contact'
        }
    return render(request, 'main/contact.html', context)


def show(request, car_id):
    car = Car.objects.get(pk=car_id)
    context={
        'title': 'Show', 
        'car': car
    }
    return render(request, 'main/show.html',context)



def success_page(request):
    context={
        'title': 'success_page',
    }
    return render(request, 'main/success_page.html', context)



def index(request):
    cars = Car.objects.all()
    for car in cars:
        # Находим последнюю аренду, где date_in еще не установлена
        rentals = Rental.objects.filter(car=car, date_in__isnull=True).order_by('-date_out')
        car.current_rental = rentals.first() if rentals.exists() else None

    context = {
        'title': 'Catalog',
        'cars': cars,
    }
    return render(request, 'main/index.html', context)


def return_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if not car.is_rented:
        messages.error(request, "This car has already been returned.")
        return redirect('main:index')
    
    car.is_rented = False
    car.save()

    rental = Rental.objects.filter(car=car, date_in__isnull=True, time_in__isnull=True).first()
    if rental:
        rental.date_in = timezone.now().date()
        rental.time_in = timezone.now().time()
        rental.save()
        messages.success(request, "The car has been returned successfully.")
    else:
        messages.error(request, "No active rental found for this car.")
    
    return redirect('main:index')

def rent_car(request, car_id, car_name):  # Добавьте car_name как параметр
    car = get_object_or_404(Car, pk=car_id, name=car_name)
    context = {'title': 'Rent'}
    if car.is_rented:
        messages.error(request, "This car is already rented.")
        return redirect('main:index')

    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.car = car
            car.is_rented = True
            car.save()
            rental.save()
            messages.success(request, "The car has been rented successfully.")
            return redirect('main:success_page')
    else:
        form = RentalForm(initial={'car': car})
    
    context['form'] = form
    context['car'] = car
    context['car_name']=car_name
    return render(request, 'main/rent.html', context)