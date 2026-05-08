from django.shortcuts import render, redirect
from .models import Employee


# HOME PAGE
def home(request):

    query = request.GET.get('q')
    status = request.GET.get('status')

    employees = Employee.objects.all()

    
    if query:
        employees = employees.filter(id=query)

    
    if status == "Active":
        employees = employees.filter(status='Active')
        

    return render(request, 'emp/home.html', {'employees': employees})


# ADD EMPLOYEE
def add_employee(request):

    message = ""

    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        department = request.POST['department']
        salary = request.POST['salary']
        status = request.POST['status']

        # CHECK UNIQUE EMAIL
        if Employee.objects.filter(email=email).exists():

            message = "Email already exists!"

            return render(
                request,
                'emp/add.html',
                {'message': message}
            )

        Employee.objects.create(
            name=name,
            email=email,
            department=department,
            salary=salary,
            status=status
        )

        return redirect('/')

    return render(request, 'emp/add.html')


# EDIT EMPLOYEE
def edit_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == 'POST':

        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']
        employee.status = request.POST['status']

        employee.save()

        return redirect('/')

    return render(
        request,
        'emp/edit.html',
        {'employee': employee}
    )


# SOFT DELETE (INACTIVE)
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.status = "Inactive"

    employee.save()

    return redirect('/')