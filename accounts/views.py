# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):           #To create a form
    model = User                                #Use the User model of django, allows to avoid SQL injection       
    form_class = UserCreationForm               #To specify that we want to create a new user
    success_url = reverse_lazy("login")         #If the registration succeed, we redirect the user to the login page
    template_name = "registration/signup.html"  #The html page to show for the registration

    def form_valid(self, form):
        # Save the user object and redirect to the success URL
        response = super().form_valid(form)
        user = form.save()
        return response