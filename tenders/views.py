from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponse
from .models import tenders
import datetime
from django.core.paginator import Paginator
#from .forms import AddPost
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,DeleteView)

#from django.views.generic import ListView, DetailView


posts = [

    {
        'company' : 'Anahom',
        'title' : 'Tender Post 1',
        'content': 'First post content',
        'category': 'agri',
        'date_posted': 'August 27, 2019'
    },
    {
        'company' : 'Tsegawu',
        'title' : 'Tender Post 2',
        'content': 'secnod post content',
        'category': 'tect',
        'date_posted': 'August 28, 2019',
    }
]
 
def index(request):
        
    context = {
         'posts':tenders.objects.all()
    }
    return render (request,'tenders/tenders.html', context,{'title':'tenders'})      




class PostListView(ListView):
    model = tenders
    template_name = 'tenders/tenders.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4



class CategoryPostListView(ListView):
    model = tenders
    template_name = 'tenders/catagory.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
       self.category = get_object_or_404(catagory, pk=self.kwargs.get('pk'))
       return tenders.objects.filter(category=self.category).order_by('-date_posted')
    
    def get_context_data(self, **kwargs):
        context = super(CategoryPostListView, self.category).get_context_data(**kwargs)
        context['catagory'] = self.catagory
        return context



class UserPostListView(ListView):
    model = tenders
    template_name = 'tenders/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return tenders.objects.filter(company=user).order_by('-date_posted')

class SearchPostListView(ListView):
    model = tenders
    template_name = 'tenders/search.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')  
        results = tenders.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).order_by('-date_posted')
        return results
       





class PostDetailView(DetailView):
    model = tenders



class PostCreateView(LoginRequiredMixin,CreateView):
    model = tenders
    fields = ['title','body','company' 'category']
    success_url = '../tenders'
    
  


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = tenders
    fields = ['title','body','company' ]
    success_url = '../'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.company:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = tenders
    success_url = '../'
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.company:
            return True
        return False


 
'''
def search(request):
    template = 'tenders/tenders.html'
    query = request.GET.get('q')  

    #pages = pagination(request, results, num = 1)

    context = {
        'results' : tenders.objects.filter(Q(title_icontains=query) | Q(body_icontains=query))
    }
    return render(request, template, context) 


'''





















'''



def detail(request):
    return render (request, 'tenders/detail.html', {
                                            'object': title,
                                           'object': content,
                                           'object': date_posted,
                                           'object': content})
'''



'''
def addtender(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_posted = request.user
            form.save()
            form = AddPost()

    else:
        form = AddPost()  
    context = {'form':form}
    return render(request,'tenders/addtenders.html',context)
'''





'''

def detail(request, pk):

    post = tenders.objects.get(id = pk ) 
    return render (request, 'tenders/detail.html',{ 'post' : post})
'''
