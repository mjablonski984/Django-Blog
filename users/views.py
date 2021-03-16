from django.shortcuts import render, redirect
from django.contrib import messages # default flash msg
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # instantiate user creation form with user data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# use login required decorator to protect the route
@login_required
def profile(request):
    if request.method == 'POST': # updating form (POST request)
        u_form = UserUpdateForm(request.POST, instance=request.user) # pass request.post data 
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user) #  populate form fields with instance of a user
        p_form = ProfileUpdateForm(instance=request.user.profile) #  populate form fields with instance of a profile

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)