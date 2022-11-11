from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseServerError
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .decorators import unauthenticate_user
from assignment.models import Dataset
from django.db.models.functions import Cast
from django.db.models import TextField
import json

User = get_user_model()
def sorting(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = count = [0 for i in range(256)]

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]
    array= array[::-1]
    str_array=','.join(str(item) for item in array)
    return str_array

@unauthenticate_user
def signup(request):
    #getting form data
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["pass1"]
        #check user has already exists or not
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already taken')
            return redirect('signup')
        #save data for user signup
        user=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()
        return redirect('login')
    return render(request,'signup.html')
@unauthenticate_user
def user_login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        user=authenticate(request,username=email,password=password)
        print(user)
        if user:
            # return HttpResponse("working")
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Email or Password is incorrect')
    return render(request,'login.html')
    
@login_required(login_url='login')
def dashboard(request):
    output=None
    if request.method=="POST":        
        inupt_data=request.POST['input_data']
        search_data=request.POST['search_data']
        if str(search_data) in inupt_data:
            output=True
        else:
            output=False          
        # return HttpResponse(output)
        my_list = [int(data) for data in inupt_data.split(',') if data.isdigit()]
        # print(countingSort(my_list))
        # return HttpResponse(inupt_data)
        sorted_data=sorting(my_list)
        data=Dataset(input_values=sorted_data,user=request.user)
        data.save()
        # return render(request,'dashboard.html',{'output':output})
    return render(request,'dashboard.html',{'output':output})

def logoutuser(request):
    logout(request)
    return redirect('login')

def api_data(request):
    if request.method=="GET":
        response={}
        json_data = json.loads(request.body)
        print(json_data)
        try:
            start_date=json_data['start_datetime']
            end_date=json_data['end_datetime']
            qs=Dataset.objects.filter(created_at__range=(start_date,end_date),user=json_data['user_id']).values('input_values',
            timestamps=Cast('created_at', TextField()))
            if qs:

                response['status']='success'
                response['user_id']=json_data['user_id']
                response['payload']=list(qs)
                print(response)
                return HttpResponse(json.dumps(response))
            return HttpResponse("None")

        except KeyError:
          return  HttpResponseServerError("Malformed data!")
        return HttpResponse("Got json data")
