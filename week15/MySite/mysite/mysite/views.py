from django.http import HttpResponse
from django.shortcuts import render

from mysite.helpers import *


def index(request):
    return render(request, 'index.html', locals())


def fact(request):
    result = 0
    if request.method == 'POST':
        num = int(request.POST['factorial'])
        result = factorial(num)
    return render(request, 'index.html', locals())


def fibo(request):
    fibo_result = 0
    if request.method == 'POST':
        num = int(request.POST['fibonacci'])
        fibo_result = nth_fibonacci(num)
    return render(request, 'index.html', locals())


def prime(request):
    prime_result = []
    if request.method == 'POST':
        num = int(request.POST['primes'])
        prime_result = ','.join([str(i) for i in n_prime_numbers(num)])

    return render(request, 'index.html', locals())


def rle(request):
    rle_result = []
    if request.method == 'POST':
        string = request.POST['rle']
        rle_result = RLE(string)

    return render(request, 'index.html', locals())


def drle(request):
    drle_result = ""
    if request.method == 'POST':
        string = request.POST['drle']
        drle_result = DRLE(string)

    return render(request, 'index.html', locals())
