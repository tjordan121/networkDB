from django.shortcuts import render, redirect
from .models import Device
from .forms import deviceForm
from django.contrib import messages

def dashboard(request):
    return render(request, 'dashboard.html', {})

def devices(request):
    all_devices = Device.objects.all
    return render(request, 'devices.html', {'all':all_devices})

def addDevice(request):
    if request.method == "POST":
        form = deviceForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            hostname = request.POST['hostname']
            IPAddress = request.POST['IPAddress']
            deviceType = request.POST['deviceType']
            family = request.POST['family']
            model = request.POST['model']
            
            messages.success(request, ('There was an error in your form. Try again'))
            return render(request, 'addDevice.html', {'hostname':hostname,'IPAddress':IPAddress,
                'deviceType':deviceType,
                'family':family,
                'model':model,
                }) 

        messages.success(request, ('Your form has been submitted successfully!!'))
        return redirect('devices')
    else:
        return render(request, 'addDevice.html', {})

def groups(request):
    return render(request, 'groups.html', {})

def configs(request):
    return render(request, 'configs.html', {})

def tools(request):
    return render(request, 'tools.html', {})

def settings(request):
    return render(request, 'settings.html', {})