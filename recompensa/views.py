from django.shortcuts import render


def recompensa(request):
    return render(request, 'recompensa/recompensas.html')
