from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'index.html', {})

def Analytic(request):
    return render(request, 'analytics-dashboards.html', {})

def reconciliation(request):
    return render(request, 'Reconciliation.html', {})


def CrosslingApp(request):
    return render(request, 'cross-selling.html', {})