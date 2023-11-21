from django.shortcuts import render, redirect, get_object_or_404
from .forms import addStaff, EmployeeEditForm, PositionForm
from .models import Staff, Position
from django.db.models import Q

def search(request):
    query = request.GET.get('q')
    employees = Staff.objects.filter(
        Q(name__icontains=query) | Q(surname__icontains=query) | Q(last_name__icontains=query) | Q(
            position__title__icontains=query)
    )
    positions = Position.objects.filter(title__icontains=query)

    return render(request, 'search_results.html', {'employees': employees, 'positions': positions, 'query': query})
def delete_employee(request, employee_id):
    employee = get_object_or_404(Staff, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('view_all')
def add_employee(request):
    if request.method == 'POST':
        form = addStaff(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_all')  # Перенаправление на страницу со списком сотрудников
    else:
        form = addStaff()

    return render(request, 'add_staff.html', {'form': form})


def views_staff(request):
    context = Staff.objects.all()
    return render(request, 'view_all.html', {'context': context})


def edit_employee(request, employee_id):
    employee = get_object_or_404(Staff, id=employee_id)

    if request.method == 'POST':
        form = EmployeeEditForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('view_all')
    else:
        form = EmployeeEditForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form})


# Position

def add_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('positions_list')  # Перенаправление на страницу со списком должностей
    else:
        form = PositionForm()

    return render(request, 'add_position.html', {'form': form})

def positions_list(request):
    positions = Position.objects.all()
    return render(request, 'positions_list.html', {'positions': positions})

def edit_position(request, position_id):
    position = get_object_or_404(Position, id=position_id)

    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('positions_list')  # Перенаправление на страницу со списком должностей
    else:
        form = PositionForm(instance=position)

    return render(request, 'edit_position.html', {'form': form})

def delete_position(request, position_id):
    position = get_object_or_404(Position, id=position_id)
    if request.method == 'POST':
        position.delete()
        return redirect('positions_list')