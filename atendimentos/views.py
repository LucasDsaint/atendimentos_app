from django.shortcuts import render

# Create your views here.
def atendimentos_list(request):
    return render(request, 'atendimentos/atendimentos_list.html', {})