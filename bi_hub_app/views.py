from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'index.html', {})

def Analytic(request):
    return render(request, 'analytics-dashboards.html', {})