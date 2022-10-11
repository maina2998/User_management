from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from .models import User
from django.core.paginator import Paginator


def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user:user_list')
            
        else:
            print(form.errors)    
    else:
        form = UserRegistrationForm()
    return render(request,'register_user.html',{'form':form})


def edit_user(request,id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        form=UserRegistrationForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
    else:
        form=UserRegistrationForm(instance=user)
        return render(request,'edit_user.html',{'form':form})        
        
def user_profile(request,id):
    user=User.objects.get(id=id)
    return render(request,'user_profile.html',{'user':user})

def delete_user(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('user:user_list')

def user_list(request):
    user=User.objects.all()

    paginator = Paginator(user, 7) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'user_list.html', {'page_obj': page_obj})