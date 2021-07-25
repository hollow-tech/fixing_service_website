from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from .forms import OrderForm, ConsultationForm
from .models import Worker, Order, Consultation
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required
def AddOrder(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            phone_number = form.cleaned_data["phone_number"]
            workers = form.cleaned_data["workers"]
            t = Order(name=name, phone_number=phone_number, workers=workers)
            t.save()
    else:
        form = OrderForm()
    return render(request, "client.html", {"form": form})


@login_required
def AddConsultation(request):
    if request.method == "POST":
        form = ConsultationForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            phone_number = form.cleaned_data["phone_number"]
            workers = form.cleaned_data["workers"]
            t = Consultation(name=name, phone_number=phone_number, workers=workers)
            t.save()
    else:
        form = ConsultationForm()
    return render(request, "consultation.html", {"form": form})



