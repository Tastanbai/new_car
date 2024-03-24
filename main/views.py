from django.shortcuts import render, get_object_or_404, redirect 
from .models import Car, Rental
from .forms import RentalForm
from .forms import ContactForm
from django.contrib import messages 
from django.utils import timezone 
from .models import Feedback
from django.core.mail import send_mail
from django.conf import settings

def about(request):
    context={
        'title': 'About'
    }
    return render(request, 'main/about.html', context)


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance=form.save()
            send_mail(
                subject='New Contact Form Submission',
                message=f"New submission from {contact_instance.first_name} - {contact_instance.email}. \n\nMessage:\n{contact_instance.message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['tastanbay02@gmail.com'],  # замените на ваш email для получения сообщений
                fail_silently=False,
            )
            return redirect('main:success_page') 
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