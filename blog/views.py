from django.shortcuts import render 

def index(requests):
    context={
        'judul':'Welcome | Blog',
        'subjudul':'Selamat Datang Di Blog',
        'banner' : 'img/img3.jpg'

    }
    return render(requests, 'index.html', context)

