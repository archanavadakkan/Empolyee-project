from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import EmployeeData
from .forms import ModeForm


# Create your views here.
# @login_required()
def employee(request):
    obj = EmployeeData.objects.all()
    return render(request, "home.html", {'obj': obj})


def employeeDetail(request, emp_id):
    detail = EmployeeData.objects.get(id=emp_id)
    return render(request, "detail.html", {'detail': detail})


def add_employee(request):
    if request.method == 'POST':
        emp_no = request.POST.get('emp_no')
        name = request.POST.get('name')
        address = request.POST.get('address')
        emp_start_date = request.POST.get('emp_start_date')
        emp_end_date = request.POST.get('emp_end_date')
        img = request.FILES['img']
        status = request.POST.get('status')
        e = EmployeeData(emp_no=emp_no, name=name, address=address, emp_start_date=emp_start_date,
                         emp_end_date=emp_end_date, img=img, status=status)
        e.save()
        print("Employee Added")
    return render(request, "add.html")


def update(request, id):
    obj1 = EmployeeData.objects.get(id=id)
    form = ModeForm(request.POST or None, request.FILES, instance=obj1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'obj1': obj1})


def delete(request, id):
    if request.method == 'POST':
        obj2 = EmployeeData.objects.get(id=id)
        obj2.delete()
        return redirect('/')
    return render(request, 'delete.html')
