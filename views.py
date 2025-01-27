from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect,FileResponse


from .models import Category,Post,Cv

from .forms import SignupForm,PostForm,PostSearchForm,PostFilterForm,CvForm
# Create your views here.

def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    form = PostSearchForm()
    return render(request,'core/index.html',{
        'posts' : posts,
        'categories' : categories,
        'form':form
    })

def login(request):
    username = UserLoggedIn(request)
    if username != None:
        return redirect('/')
    else :
        return render(request,'core/login.html')

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return redirect('/')
    else :
        return redirect('/')


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
       
            return redirect('/login/')
            
        else:
            context = {
                'form':form
                }
            return render(request, 'core/signup.html', context)
    form = SignupForm()
    context = {
            'form':form
        }
    return render(request, 'core/signup.html', context)


def jobpost(request):
    form = PostSearchForm()
    categories = Category.objects.all()
    posts = Post.objects.all()
    form1 = PostFilterForm()
    

    if 'category' in request.GET:
        form1 = PostFilterForm(request.GET)
        if form1.is_valid():
            category = form1.cleaned_data['category']
            if category:
                posts = posts.filter(category=category)


    return render(request,'core/jobpost.html',{'posts':posts,'categories':categories,'form':form,'filterForm':form1})

def profile(request):
    username = UserLoggedIn(request)
    if username != None:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.created_by = request.user
                post.save()
                return redirect('jobdetails', pk=post.id)
        else:
            form = PostForm()

        user = request.user  
        posts = Post.objects.filter(created_by=user)
        return render(request,'core/profile.html',{'form':form,'posts':posts})
    else :
        return redirect('/')

    

def jobdetails(request,pk):
    job = get_object_or_404(Post,pk=pk)
    related_jobs = Post.objects.filter(category=job.category).exclude(pk=pk)[0:3]
    form=CvForm()
    return render(request,'core/jobdetails.html',{
        'job':job,
        'related_items':related_jobs,
        'form':form

    })

def post_search(request):
    form = PostSearchForm()
    results = []

    if 'search_query' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            posts = Post.objects.filter(name__icontains=search_query)

    return render(request, 'core/search.html', {'form': form, 'posts': posts})



def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    username = UserLoggedIn(request)
    if username != None:
        if request.method == 'POST':
            post.delete()
            return redirect('/profile')
    else:
        return redirect('/login')
    return render(request, 'core/login.html')

def upload_document(request):
 
    if request.method == 'POST':
       
        form = CvForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            return redirect('/jobs')
    else:
        form = CvForm()

    return redirect( 'index')

def job_cv(request,pk):
    document = Cv.objects.filter(job=pk)
    return render(request,'core/cv.html',{'cv':document})

def fetch_document(request):
    document = Cv.objects.latest('id')
    file_path = document.cv.path
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
