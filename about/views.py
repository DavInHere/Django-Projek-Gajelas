from django.shortcuts import render 

def index(requests):
    context={
        'judul':'Welcome | About',
        'subjudul':'Selamat Datang Di About',
        'banner' : 'img/img2.jpg'

    }
    return render(requests, 'index.html', context)

