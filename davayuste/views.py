from django.shortcuts import render 

def index(requests):
    context={
        'judul':'Welcome | Home',
        'subjudul':'Selamat Datang Di Home',
        'banner' : '/img/img1.jpg'

    }
    return render(requests, 'index.html', context)

