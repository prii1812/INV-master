from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model




from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, userupdateform, profileupdateform
from django.contrib import messages
# Create your views here.

User = get_user_model()


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            username = form.save(commit=False)
            username.is_active = False  # Set the user as inactive until they confirm their email address
            username.save()
            # Generate the confirmation token and send the email
            token_generator = default_token_generator
            email_subject = 'Confirm Your Email Address'
            email_message = f'Please click the link below to confirm your email address:\n\n{request.build_absolute_uri("/confirm-email/" + str(username.pk) + "/" + token_generator.make_token(username))}/'
            send_mail(email_subject, email_message, settings.DEFAULT_FROM_EMAIL, [username.email], fail_silently=True)

            messages.success(request, f'An email has been sent to {username.email} with instructions to confirm your email address.')
            return redirect('user-login')
            #username = form.save()
            #username=form.cleaned_data.get('username')
            #messages.success(request,f'Account has been created for {username}.')
            #return redirect('user-login')
    else:
        form=CreateUserForm()
    context={
        'form':form,
    }
    return render(request,'user/register.html',context)

def confirm_email(request, user_id, token):
    user = User.objects.filter(pk=user_id, is_active=False).first()
    if user is None:
        messages.error(request, 'Invalid confirmation link.')
        return redirect('user-login')

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your email address has been confirmed. You can now log in.')
    else:
        messages.error(request, 'Invalid confirmation link.')

    return redirect('user-login')



def profile(request):
    return render(request,'user/profile.html')

def profile_update(request):
    if request.method=='POST':
        user_form=userupdateform(request.POST,instance=request.user)
        profile_form=profileupdateform(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form=userupdateform(instance=request.user)
        profile_form=profileupdateform(instance=request.user.profile)


    context={
        'user_form':user_form,
        'profile_form':profile_form,

    }
    return render(request,'user/profile_update.html',context)