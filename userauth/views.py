from django.shortcuts import render, get_object_or_404
from userauth.forms import UserForm, UserProfileForm, UserProfileRegistrationForm, UserLoginForm, ChangePWForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import UpdateView
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from models import UserProfile, User

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileRegistrationForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            # a bit of redundancy but it's for simplicity
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.save()
            registered = True
            return HttpResponseRedirect('/')
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
    return render(request,
                  'userauth/register.html',
                  {'user_form': user_form,  'registered': registered} )

def user_login(request):
    context = {}
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
        # because the request.POST.get('<variable>') returns None, if the value does not exist,
        # while the request.POST['<variable>'] will raise key error exception

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                context['user_id_tracking'] = True
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account has been disabled")
        else:
            # Bad login details provided
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        context['login_form'] = UserLoginForm()
        return render(request, 'userauth/login.html', context)



def profile(request, profile_id):
    user = get_object_or_404(UserProfile, user_id=profile_id)
    context = {}
    context['profile'] = user
    context['active_profile'] = True
    return render(request, 'userauth/profile.html', context)

@login_required
def user_logout(request):
    logout(request)
    # Take user back to homepage
    return HttpResponseRedirect('/')

@login_required
def user_edit(request):
    context = {}
    context['active_edit_profile'] = True
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        context['profile_form'] = form
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile details have been successfully updated.')
    else:
        profile_form = UserProfileForm(request.POST or None)
    return render(request, 'userauth/edit.html', {'profile_form':profile_form})

@login_required
def user_settings(request):
    context = {}
    context['active_settings'] = True
    user = get_object_or_404(User, id=request.user.id)

    if request.method == "POST":
        password = request.POST.get('password')
        new_pw = request.POST.get('new_pw')
        confirm_pw = request.POST.get('confirm_pw')
        username = request.user.username
        user = authenticate(username=username, password=password)
        if user:
            if confirm_pw == new_pw:
                user.set_password(confirm_pw)
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Your password has been updated.')
                login(request, user)

      #      else:
      #          raise ValidationError(_('New passwords do not match'), code='invalid')

    form = ChangePWForm(request.POST, instance=user)
    context['pw_form'] = ChangePWForm()
    return render(request, 'userauth/settings.html', context)
