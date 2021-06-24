from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from EmployeeApp.models import Department,Employee
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def DepartmentAPI(request,id=0):
    if request.method == 'GET':
        if id == 0:
            departments = Department.objects.all()
            department_serializer = DepartmentSerializer(departments,many=True)
            return JsonResponse(department_serializer.data,safe=False)
        else:
            try:
                departments = Department.objects.get(DepartmentId=id)
                department_serializer = DepartmentSerializer(departments)
                return JsonResponse(department_serializer.data,safe=False)
            except Department.DoesNotExist:
                return JsonResponse("Invallid DepartmentId!!",safe=False)
            
            
    elif request.method == 'POST':

        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Inserted Successfully!!",safe=False)
        return JsonResponse("Insert Unsuccessfull!!",safe=False)
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        departments = Department.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(departments, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!",safe=False)
        return JsonResponse("Update Unsuccessfull!!",safe=False)
    
    elif request.method == 'DELETE':
        department = Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("deleted Successfully!!")


@csrf_exempt
def EmployeeAPI(request,id=0):

    if request.method == 'GET':
        if id == 0:
            employee = Employee.objects.all()
            employee_serializer = EmployeeSerializer(employee,many=True)
            return JsonResponse(employee_serializer.data,safe=False)
        else:
            try:
                employee = Employee.objects.get(EmployeeId=id)
                employee_serializer=EmployeeSerializer(employee)
                return JsonResponse(employee_serializer.data,safe=False)
            except Employee.DoesNotExist:
                return JsonResponse("Invalid Employee ID!!",safe=False)
    
    elif request.method == 'POST':
        
        employee = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Inserted Successfully!!",safe=False)
        return JsonResponse("Insert Unsuccess!!",safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        try:
            employee = Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
            employee_serializer = EmployeeSerializer(employee,data=employee_data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return JsonResponse("Updated Successfully!!",safe=False)
            return JsonResponse("Update Unsuccessfull!!",safe=False)
        except Employee.DoesNotExist:
            return JsonResponse("Invalid Employee Id!!",safe=False)
    

    elif request.method == 'DELETE':
        try:
            employee = Employee.objects.get(EmployeeId=id)
            employee.delete()
            return JsonResponse('Deleted Successfully!!',safe=False)
        except Employee.DoesNotExist:
            return JsonResponse('Invalid Employee Id!!',safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['myFile']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)