from django.shortcuts import get_object_or_404, render
from .forms import ProfileForm,CustomUserForm
from profiles.models import Profile
from django.contrib import messages
import os
# Create your views here.


def profile_index(request):
    user = get_object_or_404(Profile,user_id=request.user.id)
    profile = Profile.objects.get(id=user.id)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES,instance=user)
        custom_form = CustomUserForm(request.POST,instance=request.user)
        if profile_form.is_valid() and custom_form.is_valid():
            if len(request.FILES) !=0:
                os.remove(profile.photo.path)
                profile_form.save()
                
            profile_form.save()
            custom_form.save()
            messages.success(request,'Your Profile Has Been Updated Successfully')
        
    else:
        profile_form = ProfileForm(instance=user)
        custom_form = CustomUserForm(instance=request.user)
    context = {'form': profile_form, 'user_form': custom_form, 'profile': user}
    return render(request, 'profiles/profile_index.html',context )
