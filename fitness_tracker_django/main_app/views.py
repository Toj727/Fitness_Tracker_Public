from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import DeleteView
from .models import Profile, WeighIn, Sleep
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import datetime
class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

# @method_decorator(login_required, name='dispatch')
class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['weigh_ins'] = WeighIn.objects.filter(user=self.request.user)
        return context

class WeightCreate(CreateView):


        # def get(self, request):
        #       context = {'user': Profile.objects.all()}
        #       return render(request, 'weight_create.html', context)

        # def post(self, request, pk):
            
        #       date = request.POST.get("date")
        #       weight = request.POST.get("weight")
        #       user = User.objects.get(pk=pk)
        #       WeighIn.objects.create(
        #           date=date,
        #           weight=weight,
        #           users=user)

        #       return redirect("dashboard", pk=pk)
        model = WeighIn
        fields = ['date', 'weight']
        template_name = 'weight_create.html'
        success_url = '/dashboard/'
        
        def get_initial(self):
            """
            Set the initial data for the form.
            """
            return {'user': self.request.user, 'date': datetime.date.today()}

        def form_valid(self, form):

            form.instance.user = self.request.user  
            return super(WeightCreate, self).form_valid(form)
        
        def get_success_url(self):
            print(self.kwargs)
            return reverse('dashboard', kwargs={'pk': self.object.pk})


class WeightDelete(DeleteView):
    

    model = WeighIn
    template_name = 'weight_delete.html'
    success_url = '/dashboard/'
# class WeightPostUpdate(UpdateView):

#       def get(self, request, pk):
#             context = {'weigh_ins': WeighIn.objects.all(), 'weighIn': WeighIn.objects.get(pk=pk)}

#             return render(request, 'weight_update.html', context)

#       def post(self, request, pk):
#             date = request.POST.get("date")
#             weight = request.POST.get('weight')
#             weigh_ins = WeighIn.objects.get(pk=request.POST.get('weigh_ins'))
#             WeighIn.objects.filter(pk=pk).update(
#                 date=date,
#                 weight=weight)

#             return redirect(f"/dashboard/{pk}")

# class WeightPostDelete(View):
#       def get(self, request, pk):
#             context = {''}
# @method_decorator(login_required, name='dispatch')

class SleepCreate(CreateView):
    

        # def get(self, request):
        #       context = {'user': Profile.objects.all()}
        #       return render(request, 'weight_create.html', context)

        # def post(self, request, pk):
            
        #       date = request.POST.get("date")
        #       weight = request.POST.get("weight")
        #       user = User.objects.get(pk=pk)
        #       WeighIn.objects.create(
        #           date=date,
        #           weight=weight,
        #           users=user)

        #       return redirect("dashboard", pk=pk)
        model = Sleep
        fields = ['date', 'hours']
        template_name = 'sleep_create.html'
        success_url = '/dashboard/'
        
        def get_initial(self):
            """
            Set the initial data for the form.
            """
            return {'user': self.request.user, 'date': datetime.date.today()}

        def form_valid(self, form):

            form.instance.user = self.request.user  
            return super(SleepCreate, self).form_valid(form)
        
        def get_success_url(self):
            print(self.kwargs)
            return reverse('dashboard', kwargs={'pk': self.object.pk})
        
class ProfileView(View):
    template_name = 'profile.html'

    def get_(self, request):
        # if current user, render current user
        # else send error that this is not current users profile page
        return redirect(f"/profile/{request.user.id}")
        
class ProfileDetail(DetailView):
    model = User
    template_name = 'user_profile.html'

# @method_decorator(login_required, name='dispatch')
# class UpdateProfile(View):
    
#     def get(self, request):
#         return redirect(f"/profile/{request.user.id}/update")

# @method_decorator(login_required, name='dispatch')
# class ProfileUpdate(View):

class ProfileUpdate(UpdateView):
        # template_name = 'profile_update.html'
        # model = Profile
        # fields = ['date', 'weight']

        # def get_success_url(self):
        #     user_id = self.request.user.id
        #     return reverse('profile_detail', kwargs={'pk':user_id})
    
    def post(self, request, pk):
        
        profile = Profile.objects.get(pk=pk)
        profile.image = request.POST.get("image")
        profile.starting_weight = request.POST.get("starting_weight")
        profile.weight_goal = request.POST.get("weight_goal")
        profile.save()

        user = User.objects.get(pk=request.user.id)
        user.save()

        return redirect(f"/profile/{profile.pk}")
    
    def get(self, request, pk):
    
        return render(request, 'profile_update.html')

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse('user_profile', kwargs={'pk': user_id})
    

# @method_decorator(login_required, name='dispatch')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/signup.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            context = {'form': form}
            Profile.objects.create(user=request.user, starting_weight='150.00')
            return redirect(f'/profile/{user.profile.id}/')
        else:
            context = {'form': form}
            return render(request, "registration/signup.html", context)