# from http.client import HTTPResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .formvalidation import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import json

# Create your views here.

def homePage(request):
    product_trend = Product.objects.filter(trending = 1)
    return render(request, 'Home.html',{"product_trend":product_trend})

def aboutPage(request):
    return render(request, 'About.html')

def categoryPage(request):
    category = Category.objects.filter(status=0)
    return render(request, 'Category.html',{"category" : category})

def subCategoryPage(request,name):
    if(Category.objects.filter(name=name,status=0)):
        subcategory =SubCategory.objects.filter(category__name = name)
        return render (request, 'SubCategory.html',{ "cname":name, "subcategory":subcategory})

def productPage(request,cname,name):
    if(Category.objects.filter(name=cname,status=0)):
        if(SubCategory.objects.filter(name=name,status=0)):
            product = Product.objects.filter(subcategory__name=name,status=0)
            return render(request,'Products.html',{"product":product, "cname":cname, "pname":name})
                
def singleProductPage(request, cname,pname, name):
        if(Category.objects.filter(name=cname,status=0)):
            if(SubCategory.objects.filter(name=pname,status=0)):
                if(Product.objects.filter(name=name,status=0)):
                    product = Product.objects.filter(name=name,status=0).first()
                    FavProduct=fav_items.objects.filter(user=request.user)
                    highlights = product.highlight.split(',')
                    # description = product.description.strip().split('.')
                    return render(request, 'SingleProduct.html',{"product":product, "cname":cname, "pname":pname, "name":name, "highlights": highlights, "favProduct" :FavProduct})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomUserForm()
        if request.method == 'POST':
            form = CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'completed')
                return redirect('loginpage')
    return render(request, 'Register.html', {"form": form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username = name, password = pwd)
            if user is not None:
                login(request,user)
                messages.success(request,'Super')
                return redirect('home')
            else:
                messages.error(request,'NO')
                return redirect('loginpage')
    return render(request, 'Login.html')

def logoutRequest(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'logout')
    return redirect('home')

def cartPage(request):
    if request.user.is_authenticated:
        cart=Cart_Items.objects.filter(user=request.user)
        if (cart):
            return render(request, 'Cart.html',{'cart':cart})
        else:
            return redirect('home')
    else:
        return redirect('home')
    
def add_to_cart(request):
    if(request.headers.get('X-requested-with') == 'XMLHttpRequest'):
        data = json.load(request)
        productId = data['productId']
        productCount = data['productCount']
        productSize = data['productSize']
        product_status = Product.objects.get(id = productId)
        if(product_status):
            if(Cart_Items.objects.filter(user = request.user.id, product_id = productId, product_size= productSize,product_qty = productCount)):
                return JsonResponse({'status': "Already"}, status = 200)
            else:
                if(11>=productCount):
                    Cart_Items.objects.create(user=request.user, product_id = productId, product_qty = productCount, product_size= productSize)
                    return JsonResponse({'status': "added"}, status = 200)
                else:
                    return JsonResponse({'status': "Not Available"}, status = 200)
        else:
            return JsonResponse({'status': "Login"}, status = 200)
    else:
        return JsonResponse({"status": "Invalid"}, status = 200)

# def updateCart(request):
#     if(request.headers.get('X-requested-with') == 'XMLHttpRequest'):
#         data = json.load(request)
#         productId = data['productId']
#         productCount = data['productCount']
#         print(productId, productCount)
#         product_status = Product.objects.get(id = productId)
#         if(product_status):
#             if(Cart_Items.objects.filter(user = request.user.id, product_id = productId)):
#                 if(product_status.quantity>=productCount):
#                     if(request.user.id == productId):
#                         Cart_Items.objects.update(product_id = productId, product_qty = productCount)
#                         return JsonResponse({'status': "Update"}, status = 200)
#                     else:
#                         return JsonResponse({'status': "Not There"}, status = 200)
#                 else:
#                     return JsonResponse({'status': "Not Available"}, status = 200)
#             else:
#                 return JsonResponse({'status': "Not Updated"}, status = 200)
#         else:
#             return JsonResponse({'status': "Not Available"}, status = 200)
#     else:
#         return JsonResponse({"status": "Invalid"}, status = 200)

def remove_cart(request, cid):
    cartItems = Cart_Items.objects.get(id=cid)
    cartItems.delete()
    return redirect('cartpage')

def addfav(request):
        if request.headers.get('x-requested-with')=='XMLHttpRequest':
            if request.user.is_authenticated:
                data = json.load(request)
                productId = data['productId']
                product_status = Product.objects.get(id = productId)
                if product_status:
                    if fav_items.objects.filter(user=request.user.id,product_id=productId):
                        return JsonResponse({'status':'Already'},status=200)
                    else:
                        fav_items.objects.create(user=request.user,product_id=productId)
                        return JsonResponse({'status':'fav added'},status=200)
            else:
                return JsonResponse({'status':'Login'},status=200)
        else:
            return JsonResponse({'status':'Invalid Access'},status=200)

def FavPage(request):
    if request.user.is_authenticated:
        FavProduct=fav_items.objects.filter(user=request.user)
        if(FavProduct):
            return render(request, 'Fav.html',{'favproduct':FavProduct})
        else: 
            return redirect('home')
    else:
        return redirect('home')
    
def remove_fav(request,fid):
    favItems = fav_items.objects.get(id=fid)
    favItems.delete()
    return redirect(request.META.get('HTTP_REFERER'))
    # print(request.META.get('HTTP_REFERER'))
