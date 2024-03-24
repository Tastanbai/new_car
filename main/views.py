from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Rental 
from django.http import HttpResponse
from .forms import RentalForm
from django.core.mail import send_mail
from .forms import ContactForm


def index(request):
    cars = Car.objects.all()
    context={
        'title': 'Catalog',
        'cars': cars, 
    }
    return render(request, 'main/index.html',context)

def about(request):
    context={
        'title': 'About'
    }
    return render(request, 'main/about.html', context)



from .models import Feedback

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
    context = {'title': 'Contact'}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Создаем объект Feedback и сохраняем его
            feedback = Feedback(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data.get('phone_number', ''),
                message=form.cleaned_data['message'],
            )
            feedback.save()

            # Перенаправляем пользователя на страницу успеха после сохранения формы
            return redirect('main:success_page')  
    else:
        form = ContactForm()
    
    context['form'] = form
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



def rent_car(request, car_name):
    context = {'title': 'Rent'}
    car = get_object_or_404(Car, name=car_name)  

    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False) 
            rental.car = car  
            rental.save() 
            return redirect('main:success_page')
    else:
        form = RentalForm(initial={'car': car})  
        
    context['form'] = form
    context['car'] = car  
    context['car_name']= car_name 
    return render(request, 'main/rent.html', context)
