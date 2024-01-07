'''View Functions related to Accounts functionality'''
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from accounts.forms import AccountCreationForm
# Create your views here.
def register_user(request):
    '''Handles User registration'''
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User registration successful")
            return redirect('accounts:login')
        else:
            messages.error(request,"User registration failed")
            return redirect('accounts:register')
    form = AccountCreationForm()
    context = {'form':form}
    return render(request,'accounts/register.html',context=context)

def login_user(request):
    '''This function logs in the user'''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged In Successfully')
            return redirect('store:homepage')
        else:
            messages.error(request,'Logged In Failed')
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')
    

def logout_user(request):
    '''This Function logs out the user'''
    logout(request=request)
    return redirect('accounts:login')