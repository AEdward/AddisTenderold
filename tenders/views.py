from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponse
from .models import tenders, Catagory
import datetime
from django.core.paginator import Paginator
#from .forms import TendersSearchForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,DeleteView)
from django import forms
from .forms import TendersForm
from django.core.files.storage import FileSystemStorage 

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file



class PostCreateView(LoginRequiredMixin,CreateView):
    model = tenders
    form_class = TendersForm   
    success_url = '../tenders'
    context={'file':tenders.objects.all()}

def download(request,path):
	file_path=os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,'rb')as fh:
			response=HttpResponse(fh.read(),content_type="application/document")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response

	raise Http404		








'''
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'tenders_form.html', {'form': form})
'''







class PostListView(ListView):
    model = tenders
    template_name = 'tenders/tenders.html'
    context_object_name = 'posts'
    cats = Catagory.objects.all()
    ordering = ['-date_posted']
    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        cat_menu = Catagory.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
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
    paginate_by = 5


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = tenders.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
       # users = User.objects.filter(Q(username__icontains=query))

        return object_list



class PostDetailView(DetailView):
    model = tenders


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = tenders
    fields = ['title','company','body','open_date','close_date' ]
            
    widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'open_date':forms.DateTimeInput(attrs={'class': 'form-control','data-target': 'datetimepicker'}),
            'close_date':forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}),
            
        }
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

 

def CategoryView (request, cats):
    
    category_tenders = tenders.objects.filter(category = cats)  

    return render(request, 'tenders/categories.html', {'cats': cats, 'category_tenders':category_tenders})












