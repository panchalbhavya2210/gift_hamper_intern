from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect

from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)
from django.db.models import Count
from django.db.models import Q
from django.db.models import Sum
from django.contrib import messages
from django.db.models.functions import Random

# Create your views here.

def index(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)
        allprodsdata = product_detail.objects.filter(is_active=True).order_by(Random())

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'allprodsdata': allprodsdata,
        }
        return render(request, 'index.html', details)
    except:
        pass
    allprodsdata = product_detail.objects.filter(is_active=True).order_by(Random())
    details = {
        'allprodsdata': allprodsdata,
    }
    return render(request, 'index.html', details)

def signup(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
        }
        return render(request, 'signup.html', details)
    except:
        pass
    return render(request, 'signup.html')

def about(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
        }
        return render(request, 'about.html', details)
    except:
        pass
    return render(request, 'about.html')

def login(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
        }
        return render(request, 'login.html', details)
    except:
        pass
    return render(request, 'login.html')

def forgot(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
        }
        return render(request, 'forgot.html', details)
    except:
        pass
    return render(request, 'forgot.html')

def profile(request):
    try:
        uid = request.session['log_id']

        try:
            profiledata = login_table.objects.get(id=uid)
        except login_table.DoesNotExist:
            profiledata = None

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        details = {
            'profiledata': profiledata,
            'Vendor': Vendor,
        }
        return render(request, 'profile.html', details)
    except:
        pass
    return render(request, 'profile.html')

def editprofile(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
        }
        return render(request, 'editprofile.html', details)
    except:
        pass
    return render(request, 'editprofile.html')

def editpw(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
        }
        return render(request, 'editpw.html', details)
    except:
        pass
    return render(request, 'editpw.html')

def contactus(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
        }
        return render(request, 'contact.html', details)
    except:
        pass
    return render(request, 'contact.html')

def viewdata(request):
    print(request.FILES)
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        dob = request.POST.get("dob")
        role = request.POST.get("usertype")
        address = request.POST.get("address")
        print("form submitted1")
        filepicture = request.FILES['dp']
        print("form submitted")

        try:
            alllogins = login_table.objects.get(Email=email)
        except login_table.DoesNotExist:
            alllogins = None

        if alllogins is None:
            if role == "Vendor":
                logindata = login_table(Name=name,Email=email, Phone=phone, Password=password,dp=filepicture,Dob=dob,Address=address, usertype=role, comments="Account Created")
                logindata.save()
                messages.success(request, 'Account Created Successfully and Under Verification. You can login now. ')
            else:
                logindata = login_table(Name=name,Email=email, Phone=phone, Password=password,dp=filepicture,Dob=dob,Address=address, usertype=role, comments="Account Created")
                logindata.save()
                messages.success(request, 'Account Created Successfully. you can login now')
        else:
            messages.error(request, 'Account already exist with same email')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'error occured')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def checklogin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
            user = login_table.objects.get(Email=username, Password=password)
            request.session['log_user'] = user.Email
            request.session['log_id'] = user.id
            request.session.save()

        except login_table.DoesNotExist:
            user = None

        if user is not None:
            print("successfully logged in")
            messages.success(request, 'Successfully Logged In')

        else:
            print("not logged in")
            messages.error(request, 'Invalid USER ID')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect(index)

def logout(request):
    try:
        del request.session['log_user']
        del request.session['log_id']
    except:
        pass
    return redirect(index)

def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST['email']
        try:
            user = login_table.objects.get(Email=username)

        except login_table.DoesNotExist:
            user = None
        #if user exist then only below condition will run otherwise it will give error as described in else condition.
        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = "hello here it is your new password  "+password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'krushanuinfolabz@gmail.com',
                [username],
                fail_silently=False,
            )
            # NOTE: must include below details in settings.py
            # detail tutorial - https://www.geeksforgeeks.org/setup-sending-email-in-django-project/
            # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            # EMAIL_HOST = 'smtp.gmail.com'
            # EMAIL_USE_TLS = True
            # EMAIL_PORT = 587
            # EMAIL_HOST_USER = 'mail from which email will be sent'
            # EMAIL_HOST_PASSWORD = 'pjobvjckluqrtpkl'   #turn on 2 step verification and then generate app password which will be 16 digit code and past it here

            #############################################

            #now update the password in model
            cuser = login_table.objects.get(Email=username)
            cuser.Password = password
            cuser.save(update_fields=['Password'])

            print('Mail sent')
            messages.info(request, 'mail is sent')
            return redirect(login)

        else:
            messages.error(request, 'This account does not exist')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def updateprofile(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)

        uname = request.POST.get("name")
        uemail = request.POST.get("email")
        uphone = request.POST.get("phone")
        uaddress = request.POST.get("address")
        udob = request.POST.get("dob")

        userdata.Name = uname
        userdata.Phone = uphone
        userdata.Email = uemail
        userdata.Address = uaddress
        userdata.Dob = udob

        if 'profile' in request.FILES:
            profile = request.FILES["profile"]
            userdata.dp = profile

        userdata.save()


        messages.success(request, 'Your profile has been updated successfully.')
        return redirect(profile)  # Redirect to the user's profile page after update

    except:
        pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def updatepw(request):
    try:
        uid = request.session['log_id']
        userdata = login_table.objects.get(id=uid)
        cpassword = request.POST.get("cpassword")
        password = request.POST.get("password")

        current_password = userdata.Password

        if current_password == cpassword:
            cuser = login_table.objects.get(id=uid)
            cuser.Password = password
            cuser.save(update_fields=['Password'])
            messages.success(request, 'Your password updated successfully.')
        else:
            messages.error(request, 'Current password does not match.')


        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except:
        pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def addproducthamper(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        productcatdata = product_category.objects.all()
        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'productcatdata': productcatdata,
        }
        return render(request, 'addproducthamper.html', details)
    except:
        pass
    return render(request, 'addproducthamper.html')


def addproduct(request):
    print(request.FILES)
    if request.method == 'POST':
        uid = request.session['log_id']
        name = request.POST.get("name")
        price = request.POST.get("price")
        pdesc = request.POST.get("pdesc")
        pcat = request.POST.get("pcat")
        filepicture = request.FILES['photo']

        productdata = product_detail(vendor_id=login_table(id=uid),Pro_name=name, Pro_image=filepicture, Pro_description=pdesc,Pro_price=price,Pro_Cat=product_category(id=pcat))
        productdata.save()
        messages.success(request, 'Product Added')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'error occured while adding product')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def addhamper(request):
    print(request.FILES)
    if request.method == 'POST':
        uid = request.session['log_id']
        name = request.POST.get("name")
        price = request.POST.get("price")
        filepicture = request.FILES['photo']

        hamperdata = hamper_details(vendor_id=login_table(id=uid),hamper_name=name, hamper_price=price, hamper_image=filepicture)
        hamperdata.save()
        messages.success(request, 'Hamper Added')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'error occured while adding product')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def manageproduct(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        productcatdata = product_category.objects.all()
        myproducts = product_detail.objects.filter(vendor_id=login_table(id=uid),is_active=True)
        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'productcatdata': productcatdata,
            'myproducts': myproducts,
        }
        return render(request, 'manageproduct.html', details)
    except:
        pass
    return render(request, 'manageproduct.html')

def removeproduct(request, rpid):
    prod = product_detail.objects.get(id=rpid)
    prod.is_active = False
    prod.save(update_fields=['is_active'])

    messages.error(request, 'Product Removed')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def managehamper(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        productcatdata = product_category.objects.all()
        myhampers = hamper_details.objects.filter(vendor_id=login_table(id=uid),is_active=True)
        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'productcatdata': productcatdata,
            'myhampers': myhampers,
        }
        return render(request, 'managehamper.html', details)
    except:
        pass
    return render(request, 'managehamper.html')

def removehamper(request, rhid):
    hamperobj = hamper_details.objects.get(id=rhid)
    hamperobj.is_active = False
    hamperobj.save(update_fields=['is_active'])

    messages.error(request, 'Hamper Removed')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def allcats(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        productcatdata = product_category.objects.all()
        myhampers = hamper_details.objects.filter(vendor_id=login_table(id=uid),is_active=True)

        # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(productcatdata, 3)  # Set the number of items per page

        try:
            productcatdata = paginator.page(page)
        except PageNotAnInteger:
            productcatdata = paginator.page(1)
        except EmptyPage:
            productcatdata = paginator.page(paginator.num_pages)



        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'productcatdata': productcatdata,
            'myhampers': myhampers,
        }
        return render(request, 'allcats.html', details)
    except:
        pass
    productcatdata = product_category.objects.all()

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(productcatdata, 3)  # Set the number of items per page

    try:
        productcatdata = paginator.page(page)
    except PageNotAnInteger:
        productcatdata = paginator.page(1)
    except EmptyPage:
        productcatdata = paginator.page(paginator.num_pages)

    details = {
        'productcatdata': productcatdata,
    }
    return render(request, 'allcats.html', details)

def catwiseprods(request, cwpid):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        catwiseprodsdata = product_detail.objects.filter(Pro_Cat=product_category(id=cwpid),is_active=True)

        # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(catwiseprodsdata, 3)  # Set the number of items per page

        try:
            catwiseprodsdata = paginator.page(page)
        except PageNotAnInteger:
            catwiseprodsdata = paginator.page(1)
        except EmptyPage:
            catwiseprodsdata = paginator.page(paginator.num_pages)



        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'catwiseprodsdata': catwiseprodsdata,
        }
        return render(request, 'catwiseprods.html', details)
    except:
        pass
    catwiseprodsdata = product_detail.objects.filter(Pro_Cat=product_category(id=cwpid), is_active=True)

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(catwiseprodsdata, 3)  # Set the number of items per page

    try:
        catwiseprodsdata = paginator.page(page)
    except PageNotAnInteger:
        catwiseprodsdata = paginator.page(1)
    except EmptyPage:
        catwiseprodsdata = paginator.page(paginator.num_pages)

    details = {
        'catwiseprodsdata': catwiseprodsdata,
    }
    return render(request, 'catwiseprods.html', details)


def allprods(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        allprodsdata = product_detail.objects.filter(is_active=True).order_by(Random())

        # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(allprodsdata, 3)  # Set the number of items per page

        try:
            allprodsdata = paginator.page(page)
        except PageNotAnInteger:
            allprodsdata = paginator.page(1)
        except EmptyPage:
            allprodsdata = paginator.page(paginator.num_pages)



        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'allprodsdata': allprodsdata,
        }
        return render(request, 'allprods.html', details)
    except:
        pass
    allprodsdata = product_detail.objects.filter(is_active=True).order_by(Random())

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(allprodsdata, 3)  # Set the number of items per page

    try:
        allprodsdata = paginator.page(page)
    except PageNotAnInteger:
        allprodsdata = paginator.page(1)
    except EmptyPage:
        allprodsdata = paginator.page(paginator.num_pages)

    details = {
        'allprodsdata': allprodsdata,
    }
    return render(request, 'allprods.html', details)

def searchresult(request):
    try:
        uid = request.session['log_id']

        search = request.POST.get("search")


        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        allprodsdata = product_detail.objects.all().filter(Pro_name__icontains=search,is_active=True)

        # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(allprodsdata, 3)  # Set the number of items per page

        try:
            allprodsdata = paginator.page(page)
        except PageNotAnInteger:
            allprodsdata = paginator.page(1)
        except EmptyPage:
            allprodsdata = paginator.page(paginator.num_pages)



        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'allprodsdata': allprodsdata,
        }
        return render(request, 'searchresult.html', details)
    except:
        pass

    search = request.POST.get("search")

    allprodsdata = product_detail.objects.all().filter(Pro_name__icontains=search,is_active=True)

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(allprodsdata, 3)  # Set the number of items per page

    try:
        allprodsdata = paginator.page(page)
    except PageNotAnInteger:
        allprodsdata = paginator.page(1)
    except EmptyPage:
        allprodsdata = paginator.page(paginator.num_pages)

    details = {
        'allprodsdata': allprodsdata,
    }
    return render(request, 'searchresult.html', details)


def proddetails(request, pdid):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        proddetaildata = product_detail.objects.get(id=pdid)

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'proddetaildata': proddetaildata,
        }
        return render(request, 'proddetails.html', details)
    except:
        pass
    proddetaildata = product_detail.objects.get(id=pdid)

    details = {
        'proddetaildata': proddetaildata,
    }
    return render(request, 'proddetails.html', details)


def addtocart(request):
    try:
        uid = request.session['log_id']

        if request.method == 'POST':
            qtybox = request.POST.get("qtybox")
            proid = request.POST.get("pid")
            proname = request.POST.get("pname")
            prodprice = request.POST.get("price")
            print(qtybox)

            iproprice = int(prodprice)
            iquan = int(qtybox)
            finalproprice = iproprice * iquan
            print("check1")

            cartdata = product_cart(Product_id=product_detail(id=proid), L_id=login_table(id=uid),
                                    Product_name=proname,
                                    Price=iproprice, Quantity=iquan, Final_price=finalproprice)
            print("check2")
            cartdata.save()

            messages.success(request, 'Product added to cart')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'error occured while adding product')
    except:
        pass
    messages.error(request, 'Please login to add product to cart.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def mycart(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        cartitems = product_cart.objects.filter(L_id=login_table(id=uid), Order_status=0)

        carttotal = product_cart.objects.filter(L_id=login_table(id=uid), Order_status=0).aggregate(Sum("Final_price"))
        carttotal = carttotal.get("Final_price__sum")

        hamperdata = hamper_details.objects.filter(is_active=True)

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'cartitems': cartitems,
            'carttotal': carttotal,
            'hamperdata': hamperdata,
        }
        return render(request, 'mycart.html', details)
    except:
        pass
    cartitems = product_cart.objects.filter(L_id=login_table(id=uid), Order_status=0)

    carttotal = product_cart.objects.filter(L_id=login_table(id=uid), Order_status=0).aggregate(Sum("Final_price"))
    carttotal = carttotal.get("Final_price__sum")

    details = {
        'cartitems': cartitems,
        'carttotal': carttotal,
    }
    return render(request, 'mycart.html', details)


def checkout(request):
    try:
        uid = request.session['log_id']

        if request.method == 'POST':
            subtotal = request.POST.get("subtotal")
            grandTotal = request.POST.get("grandTotal")
            selectedHamperId = request.POST.get("selectedHamperId")
            hamperPrice = request.POST.get("hamperPrice")

        print(subtotal)
        print(grandTotal)
        print(selectedHamperId)
        print(hamperPrice)

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        cartitems = product_cart.objects.filter(L_id=login_table(id=uid), Order_status=0)

        carttotal = product_cart.objects.filter(L_id=login_table(id=uid), Order_status=0).aggregate(Sum("Final_price"))
        carttotal = carttotal.get("Final_price__sum")

        hamperdata = hamper_details.objects.filter(is_active=True)

        details = {
            'subtotal': subtotal,
            'grandTotal': grandTotal,
            'userdata': userdata,
            'selectedHamperId': selectedHamperId,
            'Vendor': Vendor,
            'cartitems': cartitems,
            'carttotal': carttotal,
            'hamperdata': hamperdata,
        }
        return render(request, 'checkout.html', details)
    except:
        pass

    return render(request, 'checkout.html')


def placeorder(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        paymentMethod = request.POST.get("paymentMethod")
        saddress = request.POST.get("saddress")

        hamperid = request.POST.get("hamperid")
        grandtotal = request.POST.get("grandtotal")
        number_int = int(float(grandtotal))

        if paymentMethod == "creditDebitCard":
            orderdata = product_order(L_id=login_table(id=uid), Address=saddress, Total_amount=number_int, Hamper_id=hamper_details(id=hamperid),
                                      Payment_status="online", order_status="Placed")
            orderdata.save()

            lasstid = product_order.objects.latest('id')

            print(lasstid)

            objid = lasstid.id
            print(objid)

            obj = product_cart.objects.filter(L_id=login_table(id=uid), Order_status=0)
            for object in obj:
                object.Order_id = objid
                object.Order_status = 1
                object.save()

            messages.success(request, 'Payment Successfull. Order Placed Successfully.')
            return redirect(placeorders)

        else:
            orderdata = product_order(L_id=login_table(id=uid), Address=saddress, Total_amount=number_int,
                                      Hamper_id=hamper_details(id=hamperid),
                                      Payment_status="Cash On Delivery", order_status="Placed")
            orderdata.save()

            lasstid = product_order.objects.latest('id')

            print(lasstid)

            objid = lasstid.id
            print(objid)

            obj = product_cart.objects.filter(L_id=login_table(id=uid), Order_status=0)
            for object in obj:
                object.Order_id = objid
                object.Order_status = 1
                object.save()


            messages.success(request, 'Order Placed Successfully.')
            return redirect(placeorders)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def placeorders(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
        }
        return render(request, 'placeorder.html', details)
    except:
        pass
    return render(request, 'placeorder.html')

def SubmitReview(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        ratings = request.POST.get("input-1")
        feedback = request.POST.get("feedback")
        print(ratings)
        print(feedback)
        subreview = FEEDBACK_TABLE(L_ID=login_table(id=uid), RATINGS=ratings, COMMENT=feedback)
        subreview.save()
        messages.success(request, 'Review Submitted Successfully.')

    return redirect(index)

def removefromcart(request, rcid):
    product_cart.objects.get(id=rcid).delete()
    messages.error(request, 'Product Removed from Cart.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def myorders(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        orderdata = product_order.objects.filter(L_id=login_table(id=uid))

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'orderdata': orderdata,
        }
        return render(request, 'myorders.html', details)
    except:
        pass

    return render(request, 'myorders.html')

def yourordersingle(request, yoid):
    try:
        uid = request.session['log_id']

        cartdetail = product_cart.objects.filter(Order_id=yoid)
        cartEntries = product_cart.objects.filter(L_id=uid, Order_status=0)

        details = {

            'cartEntries': cartEntries,
            'cartdetail': cartdetail,

        }
        return render(request, 'yourordersingle.html', details)
    except:
        pass
    return render(request, 'yourordersingle.html')

def vendororders(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        from django.db.models import Q

        # Assuming uid is the specific vendor_id you are interested in

        result = product_cart.objects.filter(
            Q(Order_id__gt=0) &  # Order_id not equal to 0
            Q(Product_id__vendor_id=login_table(id=uid))  # Product_id linked to product_detail with vendor_id equal to uid
        )
        print(result)

        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'result': result,
        }
        return render(request, 'vendororders.html', details)
    except:
        pass

    return render(request, 'vendororders.html')

def hamperorders(request):
    try:
        uid = request.session['log_id']

        userdata = login_table.objects.get(id=uid)
        Vendor = False
        if userdata.usertype == "Vendor":
            Vendor = True
            print(userdata.usertype)

        from django.db.models import Q
        from itertools import chain
        # Assuming uid is the specific vendor_id you are interested in


        # Step 1: Filter product_order objects
        product_order_hampers = product_order.objects.filter(Hamper_id__vendor_id=uid)
        product_order_ids = product_order.objects.filter(Hamper_id__vendor_id=uid).values_list('id', flat=True)

        # Step 2: Filter product_cart using the obtained ids
        hamper_orders = product_cart.objects.filter(Q(Order_id__in=product_order_ids) & ~Q(Order_id=0))

        # Now hamper_orders contains the product_cart objects associated with hamper orders from the specified vendor
        print(hamper_orders)
        print(product_order_ids)



        details = {
            'userdata': userdata,
            'Vendor': Vendor,
            'hamper_orders': hamper_orders,
            'product_order_hampers': product_order_hampers,
        }
        return render(request, 'hamperorders.html', details)
    except:
        pass

    return render(request, 'hamperorders.html')

def contactwithus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        insert = contact(Name=name, Email=email, Comment=message)
        insert.save()
        messages.info(request, 'Message Submited Successfully.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def hamperfeedback(request):
    if request.method == "POST":
        uid = request.session['log_id']
        hamperfeedback = request.POST.get("hamperfeedback")
        hamperid = request.POST.get("hamperid")

        hfeedback = hamper_feedback(L_id=login_table(id=uid), Hamper_id=hamper_details(id=hamperid), COMMENT=hamperfeedback)
        hfeedback.save()
        messages.info(request, 'Feedback Received Successfully.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))