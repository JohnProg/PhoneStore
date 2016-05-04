# coding=utf-8
from django.contrib import messages
from django.contrib.auth import login, REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url
from django.shortcuts import render, resolve_url


def login_author_user(request,
                      redirect_field_name=REDIRECT_FIELD_NAME,
                      authentication_form=AuthenticationForm):
    """
    Displays the login form and handles the login action.
    :param authentication_form:
    :param redirect_field_name:
    :param request:
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url('/')

            # Okay, security check complete. Log the user in.
            login(request, form.get_user())
            messages.success(request, "Se inicio sesión exitosamente.")
            return HttpResponseRedirect(redirect_to)
        else:
            messages.error(request, "Ingresar correctamente los datos.")
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect("/")
        form = authentication_form(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to
    }
    return render(request, "public/login.html", context)