from lib2to3.fixes.fix_input import context

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render, redirect

from app1.models import Movie
from app1.forms import MovieForm
#
# def home(request):
#     k=Movie.objects.all()
#     return render(request,'home.html',{'movie':k})

class Home(ListView):
    model=Movie
    template_name = 'home.html'
    context_object_name = 'movie'

    #get_queryset

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     queryset=qs.filter(title__icontains="h")  #lookups
    #     return queryset

    #get_context-data or extra_context

    # def get_context_data(self):
    #     context=super().get_context_data()
    #     context['name']="arun"
    #
    #     return context

    extra_context = {'name':'arun','age':23}


# def addmovie1(request):
#     if(request.method=="POST"):
#         form=MovieForm(request.POST,request.FILES) #creates a form object using values that are passed through request.POST
#         if form.is_valid():  #is_valid() built in function to check the values of form field
#             form.save()      #save the form object in Db table
#             return redirect('app1:home')  #redirect to home page
#
#     form=MovieForm()
#     context={'form':form}
#     return render(request,'add1.html',context)

# def addmovie(request):
#     if request.method == "POST":
#         t=request.POST['t']
#         d=request.POST['d']
#         y=request.POST['y']
#         l=request.POST['l']
#         i=request.FILES['i']
#
#         m=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
#         m.save()
#
#         return home(request)
#     return render(request,'add.html')

class Addmovie(CreateView):
    model=Movie
    fields = ['title','description','year','language','image']
    template_name = 'add1.html'
    success_url = reverse_lazy('app1:home')

# def details(request,m):
#     k=Movie.objects.get(id=m)
#     return render(request,'details.html',{'movie':k})


class Details(DetailView):
    model=Movie
    template_name = 'details.html'
    context_object_name = 'movie'
#
# def delete(request,m):
#     k=Movie.objects.get(id=m)
#     k.delete()
#     return home(request)

class Delete(DeleteView):
    template_name = 'delete.html'
    model=Movie
    success_url = reverse_lazy('app1:home')

# def edit(request,m):
#     k=Movie.objects.get(id=m)
#
#     if request.method == "POST":
#         k.title=request.POST['t']
#         k.description=request.POST['d']
#         k.year=request.POST['y']
#         k.language=request.POST['l']
#
#         if request.FILES.get('i')==None:
#             k.save()
#         else:
#             k.image=request.FILES.get('i')
#         k.save()
#         return home(request)
#
#     return render(request,'edit.html',{'movie':k})

class Edit(UpdateView):
    model=Movie
    fields = ['title','description','year','language','image']
    template_name = 'edit.html'
    success_url = reverse_lazy('app1:home')