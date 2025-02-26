from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from .models import Product
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string  # For rendering HTML template
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate,login
from .forms import CustomLoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout

#decorator used for change_password
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request,"app/base.html")

def index(request):
    return render(request,"app/index.html")

def about(request):
    return render(request,"app/about.html")
 
# def contactus(request):
#     return render(request,'app/contactus.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():


            #check country code and valid phone number
            
            phone_number = form.cleaned_data['phone_number']
    
            # Process the form data, e.g., send an email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'Contact Us - {name}'
            from_email = email
            to_email = settings.CONTACT_EMAIL


            # Send email (adjust this to your needs)
           
              # Render HTML message using Django template
            html_message = render_to_string('app/contact_email.html', {
                'name': name,
                'email': email,
                'message': message,
            })
           
             # Send the email with HTML content
            send_mail(
                subject,
                message,  # This is the plain text version (for clients that don't support HTML)
                from_email,
                [to_email],
                fail_silently=False,
                html_message=html_message,  # This is the HTML version of the email
            )
            contact = form.save(commit=False)
           
            contact.save()
            # Redirect to a thank you page or success message
            return HttpResponse('Thank u for contacting')
    else:
        form = ContactForm()

    return render(request,'app/contactus.html',{'form': form})


class categoryview(View):
    def get(self, request,val):

        product=Product.objects.filter(category=val)
        image=Product.objects.filter(category=val).values('product_image')
        title=Product.objects.filter(category=val).values('title')
        price=Product.objects.filter(category=val).values('selling_price')
        discount=Product.objects.filter(category=val).values('discounted_price')
    
        # passing value to the request function to the html page using the locals
        # locals is built-in  used to pass all the local variables from the request function to the html page
        return render(request,"app/category.html",locals())

class Categorytitle(View):
    def get(self, request,val):
        
    #     checks for the title that mayches the value.suppose the user has selected the buffalow milk or cow milk or mix milk 
    #     from the category.
    #     val="buffalow milk"
    #     title=list of all the product title in database
    #     now val is compared with the title
    #     and product detail where title=val(buffalowmilk) is fetched
        product=Product.objects.filter(title=val)      
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html", locals())

class productdetail(View):
    def get(self,request,pk):
         product=Product.objects.get(pk=pk)
         return render(request,"app/productdetail.html",{'product':product})
    


def signup(request):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                messages.success(request,"You Have been Registed Now")
                return redirect('login')  # Redirect to login page after successful registration
            else:
                messages.warning(request,"Inavlid Input Data")
                
        else:
            form = UserRegistrationForm()

        return render(request, 'app/signup.html', {'form': form})



def CustomLoginView(request):
    form = CustomLoginForm(request=request)
    if request.method=='POST':
        form =CustomLoginForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user) # for creating session of a curent user
                return redirect('index')
            else:
                form = CustomLoginForm()
    return render(request, 'app/login.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            # Save the new password
            form.save()

            # Update the session hash to avoid logging the user out
            update_session_auth_hash(request, form.user)

            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')  # Redirect to the profile page or wherever you want
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'app/change_password.html', {'form': form})

def password_change_done(request):
    return render(request,'password_change_done.html')

def Logout_View(request):
    logout(request)
    return redirect('index')



    
     




    
