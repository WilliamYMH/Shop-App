from .forms import ProductForm
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.template import loader
from django.shortcuts import get_object_or_404, render_to_response, render
from django.views.generic import ListView, FormView, CreateView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


class AddProduct(LoginRequiredMixin, FormView):

    model = Product
    #redirect_field_name = 'login'
    template_name = 'new_product.html'
    form_class = ProductForm

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})


class CreateUser(CreateView):
    model = User
    fields = ('username', 'email', 'password')
    success_url = '/'

    def form_valid(self, form):
        form.save(commit=False)
        self.object = User.objects._create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'])
        self.object.save()
        return HttpResponseRedirect('/')


# Esta funcion se ha eliminado debido a la implementacion de la clase 'CreateUser' y 'LoginView'
'''
def auth_login(request):
    if(request.method == 'POST'):
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        if(action == 'signup'):
            user = User.objects._create_user(
                username=username, email=email, password=password)
            user.save()
            # print("Sing Up: %s" % user.username)
        elif(action == 'login'):
            user = authenticate(username=username, password=password)
           # print(user.username)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    return render(request, 'login/login.html', {})
'''

# esta funcion se ha eliminado debido a la implementacion de 'ProductList'
'''
def hello_world(request):
    # return HttpResponse("<h1>hello world!!</h1>")
    # return render(request, "index.html")
    product = Product.objects.order_by("id")
    template = loader.get_template("index.html")
    context = {
        "product": product
    }
    return HttpResponse(template.render(context, request))
'''

# Esta funcion se ha eliminado debido a la implementacion de 'ProductDetail'
'''
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # template = loader.get_template("product_detail.html")
    context = {
        "product": product
    }
    # render_to_response, mas facil y sin tanto condigo como el loader.
    return render_to_response('product_detail.html', context)
'''

# Esta funcion se ha eliminado debido a la implementacion de 'AddProduct'
'''
def new_product(request):

    if(request.method == 'POST'):
        form = ProductForm(request.POST, request.FILES)
        # print("que se iceceee")
        if(form.is_valid):

            form.save()
            # product.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()
    template = loader.get_template("new_product.html")
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))
'''
