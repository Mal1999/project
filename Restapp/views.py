from django.http import HttpResponse , HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .forms import RegisterForm, StudentForm, LoginForm
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
# from .models import Department, Course
# from .forms import CourseForm
def home_view(request):
    return render(request, 'home.html')

def department_view(request, department_name):
    # Assuming you have a function to generate Wikipedia links based on department names
    wikipedia_link = generate_wikipedia_link(department_name)

    context = {
        'department': department_name,
        'wikipedia_link': wikipedia_link,
    }

    return render(request, 'department_view.html', context)

def generate_wikipedia_link(department_name):
    # Implement your logic to generate Wikipedia link based on the department name
    # Example: Constructing a simple link with department name in the URL
    return f"https://en.wikipedia.org/wiki/{department_name}"

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request)
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid user or pass,"}
            return render(request, "login.html", context)
        login(request, user)
        return redirect("Restapp:dashboard")
    else:
        form = AuthenticationForm(request)
    return render(request, "login.html",{})

def dashboard(request):
    return render(request, 'dashboard.html')

def new_page(request):
    return render(request, 'new_page.html')

# def register(request):
#     form = UserCreationForm(request.POST or None)
#     if form.is_valid():
#         user_obj = form.save()
#         return redirect('Restapp:login_view')
#     context = {"form": form}
#     return render(request, 'register.html', context)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('Restapp:dashboard')  # Redirect to the dashboard after registration
        else:
            form = UserCreationForm()  # Return a clean form if it's not valid
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def form_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order Confirmed!')

            # Redirect to the form_confirm URL with a success message
            return redirect('Restapp:submit_form')
        else:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'form.html', {'form': form})
    else:
        # If the request method is not POST, render the form page
        form = StudentForm()
        return render(request, 'form.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("Restapp:home_view")
    return render(request, "logout.html", {})

def submit_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Restapp:form_confirm')
    else:
        form = StudentForm()
    return redirect('Restapp:form_page')


def form_confirm(request):
    # Your logic here
    return render(request, 'form_confirm.html')


# def single_template_view(request):
#     form = CourseForm()

#     if request.method == 'POST':
#         form = CourseForm(request.POST)
#         if form.is_valid():
#             form.save()

#     return render(request, 'Restapp/single_template.html', {'form': form})

# def get_courses(request):
#     department_id = request.GET.get('department_id')
#     courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    # return JsonResponse(list(courses), safe=False)
