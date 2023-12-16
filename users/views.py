from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from . import forms
from car.models import CarModel
from users.models import orderModel, ItemModel
 
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('user_login')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'register'})
 
 
class UserLoginView(LoginView):
    template_name = 'register.html'
 
    def get_success_url(self):
        return reverse_lazy('user_profile')
 
    def form_valid(self, form):
        messages.success(self.request, 'User login successfully')
        return super().form_valid(form)
 
    def form_invalid(self, form):
        messages.success(self.request, 'User login information is incorrect')
        return super().form_invalid(form)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
 
 
@login_required
def profileupdate(request):
    orders = orderModel.objects.filter(user=request.user)
    arr = []
    for order in orders:
        item = ItemModel.objects.get(order=order)
        arr.append(item)
        
    data = CarModel.objects.filter(users=request.user)
    return render(request, 'profile.html', {'data': data, 'order': arr})
 
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password updated successfully')
            return redirect('user_profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form': form})
 
@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.updateProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('user_profile')
    else:
        profile_form = forms.updateProfileForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': profile_form})
 
class CarDetailsView(DetailView):
    model = CarModel
    # pk_url_kwarg = 'id'
    template_name = 'details.html'
 
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        context['car'] = car
        return context
 

 
@login_required
def buy_now(request, id):
    car = CarModel.objects.get(pk=id)
    if (car.quantity > 0):
        car.quantity = car.quantity - 1

        if ItemModel.objects.all().exists():
            have_car = ItemModel.objects.filter(car=car).exists()

            if have_car:
                getCar = ItemModel.objects.get(car=car)
                getCar.save()
                car.save()
            else:
                order = orderModel()
                order.user = request.user
                car.save()
                order.save()
                order_item = ItemModel()
                order_item.order = order
                order_item.car = car
                order_item.save()
        else:
            order = orderModel()
            order.user = request.user
            car.save()
            order.save()
            order_item = ItemModel()
            order_item.order = order
            order_item.car = car
            order_item.save()

    return redirect(reverse("car_details_view", args=[car.id]))

 
 
 
# class base user logout
class user_logout_view(LogoutView):
    def get_success_url(self):
        return reverse_lazy('user_login')