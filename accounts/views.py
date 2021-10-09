from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        # male = request.POST['male', 'off']
        # female = request.POST['female', 'off']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Name Is Already Taken!‼')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Check The Email Again!⁉')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect("login")
        else:
            messages.info(request, 'Passwords Are not Matching!🤣🤔❌')
            return redirect('register')
        return redirect('login')
    else:
        return render(request, 'shop/Account.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/shop')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'shop/Account.html')


def logout(request):
    auth.logout(request)
    return redirect("/shop")


def account(request):

    return render(request, 'shop/Account.html')
