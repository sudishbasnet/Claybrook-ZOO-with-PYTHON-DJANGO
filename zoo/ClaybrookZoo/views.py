from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from ClaybrookZoo import forms,models
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone
import json
# for paypal
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm


def home(request):
    data ={
            'updates' : models.Update.objects.all(),
            'feedbacks' : models.Feedback.objects.filter(highlight=True)
        }
    return render(request,'index.html',data)


def site(request,location):
    if location == 'gallery':
        gallery = models.Animal.objects.all()
        return render(request, 'gallery.html',{'gallery':gallery})

    elif location == 'contact':
        return render(request, 'contact.html')
    return render(request, 'about.html')



def animal(request):
    if request.is_ajax():
        name = request.GET.get("a")
        species = request.GET.get("b")
        habitat = request.GET.get("c")
        diet = request.GET.get("d")
        classification = request.GET.get("e")
        condition = request.GET.get("g")
        animal = ''   
        if request.GET.get("a") == '':
            name = ''
        if request.GET.get("b") == '':
            species = ''
        if request.GET.get("c") == '':
            habitat = ''
        if request.GET.get("d") == '':
            diet = ''
        if request.GET.get("e") == '':
            classification = ''
        if request.GET.get("g") == '':
            condition = ''
        if request.GET.get("f") == 'Non sponsored':
            animal = models.Animal.objects.filter(name__icontains=name,species__icontains=species,natural_habitat__icontains=habitat,dietary_requirement__icontains=diet,classification__icontains=classification,visibility='visible',sponsored_animal=None,condition__icontains=condition)
        if request.GET.get("f") == 'Sponsored':
            animal = models.Animal.objects.filter(name__icontains=name,species__icontains=species,natural_habitat__icontains=habitat,dietary_requirement__icontains=diet,classification__icontains=classification,visibility='visible',sponsored_animal__name__icontains='',condition__icontains=condition)

        if request.GET.get("f") == '':
            animal = models.Animal.objects.filter(name__icontains=name,species__icontains=species,natural_habitat__icontains=habitat,dietary_requirement__icontains=diet,classification__icontains=classification,visibility='visible',condition__icontains=condition)
        
        html = render_to_string(template_name="animaldetails.html", context={"animals": animal})
        data = {"dataview": html}
        return JsonResponse(data=data, safe=False)
    else:
        animal = models.Animal.objects.filter(visibility='visible')
        return render(request, 'animal.html',{'animals':animal})




@login_required(login_url='/auth/login')
@csrf_exempt
def adminpanel(request,display,action,id):
    data = {}
    
    if request.user.role  == 'visitors':
        return redirect('/Claybrook-Zoo/visitorpanel/dashboard/none/0')
    
    
    
    elif display == 'user':
        title = 'user'
        form = forms.StaffSignUpForm
        if (request.user.role == 'admin' ):
            actionname = 'Add New User'
        else :
            actionname = ''
        user = models.User.objects.all()
        if action == "update":
            actionname = 'Update Information'
            details =models.User.objects.get(pk=id)
            form = forms.StaffSignUpFormUpdate(request.POST or None, instance=details)
            title ="Update Information"
            if form.is_valid():
                form.save()
                return redirect('/Claybrook-Zoo/adminpanel/user/none/0')
                
        elif action == 'delete':
            user = models.User.objects.get(pk=request.POST.get('id'))
            models.Feedback.objects.filter(sender=user).delete()
            models.Message.objects.filter(sender=user).delete()
            models.Message.objects.filter(receiver=user).delete()
            models.Update.objects.filter(uploaded_by=user).delete()
            models.Sponsor.objects.filter(sponsored_user=user).delete()
            user.delete()
            response_data = {}
            return HttpResponse(json.dumps(response_data),content_type="application/json")

        elif action == 'staff':
            title = 'Staff'
            user = models.User.objects.exclude(role='visitor')
            
        elif action == 'visitor':
            title = 'visitors'
            user = models.User.objects.filter(role='visitor')
        
        elif action == 'add':
            title = 'Add New User'
            if request.method == 'POST':
                form = forms.StaffSignUpForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/Claybrook-Zoo/adminpanel/user/none/0')
        

        elif request.is_ajax():
            username = request.GET.get("a")              
            if request.GET.get("a") == '':
                username = ''
            user = models.User.objects.filter(username__icontains=username)
            html = render_to_string(template_name="adminpanelfilterlist.html", context={"users": user,"role":request.user.role})
            data = {"dataview": html}
            return JsonResponse(data=data, safe=False)


        data={
            'location' : 'user',
            'title' : title,
            'users' : user,
            'adminaction' : actionname,
            'form' : form,
            'action' : action            
        }



    elif display == 'booking':
        title = 'booking'
        booking = models.Booking.objects.all()
        if (request.user.role == 'admin' or request.user.role == 'manager' or request.user.role == 'temporary staff'):
            actionname = 'Add new ticket'
        form = forms.OfficialBooking
        if action == 'yes' or action == 'no':
            booking = models.Booking.objects.filter(payment=action)

        elif action == "update":
            details =models.Booking.objects.get(pk=id)
            form = forms.Booking(request.POST or None, instance=details)
            title ="Update Information"
            if form.is_valid():
                form.save()
                return redirect('/Claybrook-Zoo/adminpanel/booking/none/0')
            actionname = 'Update Information'
                
        elif action == 'delete':
            models.Booking.objects.get(pk=request.POST.get('id')).delete()
            response_data = {}
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        

        elif action == 'add':
            title = "Book New Tickets"
            if request.method == 'POST':
                form = forms.OfficialBooking(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/Claybrook-Zoo/adminpanel/booking/none/0')

        elif request.is_ajax():
            username = request.GET.get("a")              
            if request.GET.get("a") == '':
                username = ''
            booking = models.Booking.objects.filter(booked_by__username__icontains=username)
            html = render_to_string(template_name="adminpanelfilterlist.html", context={"bookings": booking,"role":request.user.role})
            data = {"dataview": html}
            return JsonResponse(data=data, safe=False)
        
        data={
            'location' : 'booking',
            'adminaction' : actionname,
            'form' : form,
            'title' : title,
            'bookings' : booking,
            'action' : action            
        }




    elif display == 'animal':
        title = 'animal'
        form = forms.AnimalForm
        form1 =''
        if (request.user.role == 'admin' or request.user.role == 'manager' ):
            actionname = 'Add New Animal'
        else:
            actionname = ''
        animal = models.Animal.objects.all()
        if action == "update":
            actionname = 'Update Information'
            animal =models.Animal.objects.get(pk=id)  
            if animal.mammal.all() :
                details =models.Mammal.objects.get(animal=animal)
                form1 = forms.Mammal(request.POST or None, instance=details)
            elif animal.bird.all() :
                details =models.Bird.objects.get(animal=animal)
                form1 = forms.Bird(request.POST or None, instance=details)
            elif animal.fish.all() :
                details1 =models.Fish.objects.get(animal=animal)
                form1 = forms.Fish(request.POST or None, instance=details)
            elif animal.reptile.all() :
                details =models.Reptile.objects.get(animal=animal)
                form1 = forms.Reptile(request.POST or None, instance=details)
            form = forms.AnimalForm(request.POST or None, instance=animal)
            files = request.FILES.getlist('photo')
            title ="Update Information"
            if form.is_valid():
                form.save()
                form1.save()   
                for f in files:
                    uFile = models.AnimalPhoto(animal=animal, photo=f)
                    uFile.save()
                return redirect('/Claybrook-Zoo/adminpanel/animal/none/0')
                
        elif action == 'archive':
            response_data = {}
            data = models.Animal.objects.get(pk=request.POST.get('id'))
            animal = models.Animal.objects.filter(pk=request.POST.get('id'))
            if data.visibility == 'archive':
                animal.update(visibility='visible')
                response_data['action'] = 'archive'
                response_data['response'] = 'danger'
            else:
                animal.update(visibility='archive')
                response_data['action'] = 'visible'
                response_data['response'] = 'success'
            return HttpResponse(json.dumps(response_data),content_type="application/json")




        elif action == 'delete':
            if request.POST.get('image'):
                models.AnimalPhoto.objects.filter(pk=request.POST.get('id')).delete()
            else:
                animal = models.Animal.objects.get(pk=request.POST.get('id'))
                models.Mammal.objects.filter(animal=animal).delete()
                models.Bird.objects.filter(animal=animal).delete()
                models.Reptile.objects.filter(animal=animal).delete()
                models.Fish.objects.filter(animal=animal).delete()
                models.Sponsor.objects.filter(animal=animal).delete()
                models.AnimalPhoto.objects.filter(animal=animal).delete()
                animal.delete()
            response_data = {}
            return HttpResponse(json.dumps(response_data),content_type="application/json")



        elif action == 'filter':
            animal = ''
            visibility = request.GET.get("a")
            species = request.GET.get("b")
            name = request.GET.get("c")
            classification = request.GET.get("d")
            condition = request.GET.get("f")
            if request.GET.get("a") == 'None':
                visibility = ''
            if request.GET.get("b") == 'None':
                species = ''
            if request.GET.get("c") == 'None':
                name = ''
            if request.GET.get("d") == 'None':
                classification = ''
            if request.GET.get("f") == 'None':
                condition = ''
            if request.GET.get("e") == 'Non sponsored':
                animal = models.Animal.objects.filter(name__icontains=name,species__icontains=species,visibility__icontains=visibility,classification__icontains=classification,sponsored_animal=None,condition__icontains=condition)
            if request.GET.get("e") == 'Sponsored':
                animal = models.Animal.objects.filter(name__icontains=name,species__icontains=species,visibility__icontains=visibility,classification__icontains=classification,sponsored_animal__name__icontains='',condition__icontains=condition)
            if request.GET.get("e") == '':
                animal = models.Animal.objects.filter(name__icontains=name,species__icontains=species,visibility__icontains=visibility,classification__icontains=classification,condition__icontains=condition)
            
            html = render_to_string(template_name="adminpanelfilterlist.html", context={"animals": animal,"role":request.user.role})
            data = {"dataview": html}
            return JsonResponse(data=data, safe=False)




        elif action == 'classification':
            if request.is_ajax():
                name = request.GET.get("a")
                if name == 'Mammal':
                    form1 = forms.Mammal
                elif name == 'Bird':
                    form1 = forms.Bird
                elif name == 'Fish':
                    form1 = forms.Fish
                elif name == 'Reptile':
                    form1 = forms.Reptile
                html = render_to_string(template_name="classificationform.html", context={"form1": form1})
                data = {"dataview": html}
                return JsonResponse(data=data, safe=False)
            Animal = models.Animal.objects.get(id=id)
            models.Mammal.objects.filter(animal=Animal).delete()
            models.Bird.objects.filter(animal=Animal).delete()
            models.Reptile.objects.filter(animal=Animal).delete()
            models.Fish.objects.filter(animal=Animal).delete()
            actionname = 'Update Information'
            title = 'Change Animal Classification Details'
            form = ''
            if request.method == 'POST':
                if request.POST.get('classification') == 'Mammal':
                    form1 = forms.Mammal(request.POST)
                elif request.POST.get('classification') == 'Bird':
                    form1 = forms.Bird(request.POST)
                elif request.POST.get('classification') == 'Fish':
                    form1 = forms.Fish(request.POST)
                elif request.POST.get('classification') == 'Reptile':
                    form1 = forms.Reptile(request.POST)
                if form1.is_valid():
                    form1.save()
                    if request.POST.get('classification') == 'Mammal':
                        model = models.Mammal.objects.latest('id')
                        category = models.Mammal.objects.filter(id=model.id)
                    elif request.POST.get('classification') == 'Bird':
                        model = models.Bird.objects.latest('id')
                        category = models.Bird.objects.filter(id=model.id)
                    elif request.POST.get('classification') == 'Fish':
                        model = models.Fish.objects.latest('id')
                        category = models.Fish.objects.filter(id=model.id)
                    elif request.POST.get('classification') == 'Reptile':
                        model = models.Reptile.objects.latest('id')
                        category = models.Reptile.objects.filter(id=model.id)
                    category.update(animal=Animal)
                    models.Animal.objects.filter(id=id).update(classification=request.POST.get('classification'))
                    return redirect('/Claybrook-Zoo/adminpanel/animal/none/0')


        elif action == 'add':
            title = 'Add New Animal'
            if request.POST.get('classification') == 'Mammal':
                form1 = forms.Mammal(request.POST)
            elif request.POST.get('classification') == 'Bird':
                form1 = forms.Bird(request.POST)
            elif request.POST.get('classification') == 'Fish':
                form1 = forms.Fish(request.POST)
            elif request.POST.get('classification') == 'Reptile':
                form1 = forms.Reptile(request.POST)
            if request.method == 'POST':
                form = forms.AnimalForm(request.POST)
                files = request.FILES.getlist('photo')
                if form.is_valid():
                    form.save()
                    animal=models.Animal.objects.latest('id')
                    Animal = models.Animal.objects.get(id=animal.id)
                    form1.save()
                    if request.POST.get('classification') == 'Mammal':
                        model = models.Mammal.objects.latest('id')
                        category = models.Mammal.objects.filter(id=model.id)
                    elif request.POST.get('classification') == 'Bird':
                        model = models.Bird.objects.latest(id=model.id)
                        category = models.Bird.objects.filter(id=id)
                    elif request.POST.get('classification') == 'Fish':
                        model = models.Fish.objects.latest('id')
                        category = models.Fish.objects.filter(id=model.id)
                    elif request.POST.get('classification') == 'Reptile':
                        model = models.Reptile.objects.latest('id')
                        category = models.Reptile.objects.filter(id=model.id)
                    category.update(animal=Animal)
                    models.Animal.objects.filter(id=Animal.id).update(classification=request.POST.get('classification'))
                    for f in files:
                        uFile = models.AnimalPhoto(animal=Animal, photo=f)
                        uFile.save()
                    return redirect('/Claybrook-Zoo/adminpanel/animal/none/0')
        data={
            'location' : 'animal',
            'title' : title,
            'animals' : animal,
            'adminaction' : actionname,
            'form' : form,
            'action' : action, 
            'form1'  : form1 
        }




    

    elif display == 'watchlist':
        title = 'watchlist'
        form = forms.Watchlist
        if (request.user.role == 'admin' or request.user.role == 'manager'  or request.user.role == 'zoo keeper'):
            actionname = 'Add watchlist'
        else :
            actionname = ''
        watchlist = models.WatchList.objects.all()
        if action == "update":
            actionname = 'Update Information'
            watchlist =models.WatchList.objects.get(pk=id)  
            form = forms.Watchlist(request.POST or None, instance=watchlist)
            title ="Update Information"
            if form.is_valid():
                form.save()
                models.Animal.objects.filter(id=watchlist.animal.id).update(condition=watchlist.condition)
                return redirect('/Claybrook-Zoo/adminpanel/watchlist/none/0')

        elif action == 'delete':
            watchlist = models.WatchList.objects.get(pk=id)
            watchlist.delete()
            response_data = {}
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        

        elif request.is_ajax():
            name = request.GET.get("a")              
            if request.GET.get("a") == '':
                name = ''
            watchlist = models.WatchList.objects.filter(animal__name__icontains=name)
            html = render_to_string(template_name="adminpanelfilterlist.html", context={"watchlist": watchlist,"role":request.user.role})
            data = {"dataview": html}
            return JsonResponse(data=data, safe=False)


        elif action == 'add':
            title = 'Add New Watchlist'
            if request.method == 'POST':
                form = forms.Watchlist(request.POST)
                if form.is_valid():
                    form.save()
                    watchlist=models.WatchList.objects.latest('id')
                    models.Animal.objects.filter(id=watchlist.animal.id).update(condition=watchlist.condition)
                    return redirect('/Claybrook-Zoo/adminpanel/watchlist/none/0')
        data={
            'location' : 'watchlist',
            'title' : title,
            'watchlist' : watchlist,
            'adminaction' : actionname,
            'form' : form,
            'action' : action, 
        }






    elif display == 'sponsor':
        title = 'sponsor'
        form = forms.AdminSponsorForm
        if request.user.role == 'admin':
            actionname = 'Add New Sponsor'
        else:
            actionname = ''
        sponsor = models.Sponsor.objects.all()
        if action == "update":
            actionname = 'Update Information'
            details =models.Sponsor.objects.get(pk=id)
            form = forms.AdminSponsorForm(request.POST or None, instance=details)
            title ="Update Information"
            if form.is_valid():
                form.save()
                return redirect('/Claybrook-Zoo/adminpanel/sponsor/none/0')
                
        elif action == 'delete':
            models.Sponsor.objects.get(pk=request.POST.get('id')).delete()
            response_data = {}
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        
        elif action == 'filter':
            sponsor = request.GET.get("a")              
            if request.GET.get("a") == '':
                sponsor = ''
            if(sponsor == ''):
                sponsor = models.Sponsor.objects.all()
            else:
                sponsor = models.Sponsor.objects.filter(payment_received__icontains=sponsor)
            html = render_to_string(template_name="adminpanelfilterlist.html", context={"sponsors": sponsor,"role":request.user.role})
            data = {"dataview": html}
            return JsonResponse(data=data, safe=False)

        elif request.is_ajax():
            name = request.GET.get("a")              
            if request.GET.get("a") == '':
                name = ''
            sponsor = models.Sponsor.objects.filter(name__icontains=name)
            html = render_to_string(template_name="adminpanelfilterlist.html", context={"sponsors": sponsor})
            data = {"dataview": html}
            return JsonResponse(data=data, safe=False)

        elif action == 'add':
            title = 'Add New Sponsor'
            if request.method == 'POST':
                form = forms.AdminSponsorForm(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('/Claybrook-Zoo/adminpanel/sponsor/none/0')
        data={
            'location' : 'sponsor',
            'title' : title,
            'sponsors' : sponsor,
            'adminaction' : actionname,
            'form' : form,
            'action' : action            
        }


    elif display == 'message':
        title = 'message'
        content = models.Message.objects.all()
        message = models.Message.objects.filter(seen=False,receiver=request.user)
        data={
            'location' :'message',
            'messages' : message,
            'content' : content,
            'title' : title ,
            'action' : action
            
        }



    
    elif display == 'feedback':
        title = 'feedback'
        feedback = models.Feedback.objects.all()
                
        if action == 'delete':
            models.Feedback.objects.get(pk=request.POST.get('id')).delete()
            response_data = {}
            return HttpResponse(json.dumps(response_data),content_type="application/json")


        elif action == 'highlight':
            response_data = {}
            feedback = models.Feedback.objects.filter(id=id)
            for feed in feedback:
                if feed.highlight == True:
                    feedback.update(highlight=False)
                    response_data['action'] = ''
                    response_data['response'] = 'success'
                else:
                    feedback.update(highlight=True)
                    response_data['action'] = 'Cancel'
                    response_data['response'] = 'danger'
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        
        data={
            'location' : 'feedback',
            'title' : title,
            'feedbacks' : feedback,
            'action' : action            
        }





    elif display == 'dashboard' :
        title = 'dashboard'
        form = forms.UpdateForm
        if (request.user.role == 'admin' or request.user.role == 'manager' ):
            actionname = 'Add New Updates'
        else:
            actionname = ''
        update = models.Update.objects.all()
        if action == "update":
            actionname = 'Update Information'
            details =models.Update.objects.get(pk=id)
            form = forms.UpdateForm(request.POST or None, instance=details)
            title ="Update Information"
            if form.is_valid():
                form.save()
                return redirect('/Claybrook-Zoo/adminpanel/dashboard/none/0')
                
        elif request.is_ajax():
            models.Update.objects.get(pk=request.POST.get('id')).delete()
            response_data = {}
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        
        elif action == 'add':                
            title = 'Add New Update'
            if request.method == 'POST':
                models.Update(heading=request.POST.get("heading"),description=request.POST.get("description"),uploaded_by=request.user).save()
                return redirect('/Claybrook-Zoo/adminpanel/dashboard/none/0')
        
        use = models.User.objects.all()
        vis = models.User.objects.filter(role='visitor')
        sta = models.User.objects.exclude(role='visitor')
        anim = models.Animal.objects.all()
        spon = models.User.objects.filter(sponsored_user=True)
        book = models.Booking.objects.all()

        
        visitorper = (vis.count()/use.count())*100
        bookingper = (book.count()/vis.count())*100
        animalper = (anim.count()/use.count())*100
        staffper = (sta.count()/use.count())*100
        sponsorper = (sta.count()/use.count())*100

        sa = models.Sponsor.objects.all().count()
        ca = models.Animal.objects.filter(condition='Critical').count()
        na = models.Animal.objects.filter(condition='Normal').count()
        da = models.Animal.objects.filter(condition='Dead').count()

        data={
            'location' : 'dashboard',
            'title' : title,
            'updates' : update,
            'adminaction' : actionname,
            'form' : form,
            'action' : action, 
            'visitorper':visitorper,
            'bookingper':bookingper,
            'animalper':animalper,
            'staffper':staffper,
            'sponsorper':sponsorper,  
            'sa' : sa,
            'ca' : ca,
            'na' : na,
            'da' : da,
        }
        
    return render(request, 'adminpanel.html',data)



@login_required(login_url='/auth/login')
def message(request):
    if request.POST.get('content'):
        user = models.User.objects.filter(id=request.POST.get('userid'))
        if user:
            pass
        else:
            user = models.User.objects.exclude(role='visitor')
            for use in user:
                messages = models.Message.objects.filter(sender=request.user,receiver=use)
                messages.update(seen=True)
        msg = models.Message(content=request.POST.get('content'),sender=request.user)
        msg.save()
        for user in user:
            msg.receiver.add(user)
        response_data = {}
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        return redirect('/Claybrook-Zoo')




def signup(request,action):
    name="Create Account"
    if action=="update":
        details =models.User.objects.get(username=request.user)
        form = forms.SignUpFormUpdate(request.POST or None, instance=details)
        name ="Update Information"
        if form.is_valid():
            form.save()
            return redirect('/Claybrook-Zoo')
    elif request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/Claybrook-Zoo')
    else:
        form = forms.SignUpForm()
    data ={
        'form' :form,
        'name' :name
        }
    return render(request,'signup.html',data)











@login_required(login_url='/auth/login')
@csrf_exempt
def visitorpanel(request,display,action,id):
    data = {}

    if request.user.role != 'visitor':
        return redirect('/Claybrook-Zoo/adminpanel/dashboard/none/0')

    elif display == 'message':
        title = 'message'
        content = models.Message.objects.all()
        message = models.Message.objects.filter(sender=request.user)
        data={
            'location' :'message',
            'title' : title,
            'messages' : message,
            'action' : action,
            'content' : content
            
        }



    elif display == 'booking':
        title = 'booking'
        form = forms.Booking
        actionname = 'Book New Ticket'
        booking = models.Booking.objects.filter(booked_by=request.user)
        if action == "update":
            actionname = 'Update Information'
            details =models.Booking.objects.get(pk=id)
            form = forms.Booking(request.POST or None, instance=details)
            title ="Update Information"
            if form.is_valid():
                form.save()
                return redirect('/Claybrook-Zoo/visitorpanel/booking/none/0')
                
        elif action == 'delete':
            models.Booking.objects.get(pk=request.POST.get('id')).delete()
            response_data = {}
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        
        elif action == 'add':
            title = 'Book New Ticket'
            if request.method == 'POST':
                booking =models.Booking(entry_date=request.POST.get('entry_date'),no_of_entries=request.POST.get('no_of_entries'),booked_by=request.user,total_cost=request.POST.get('total_cost'))
                booking.save()
                request.session['booking_id'] = booking.id
                return redirect('/Claybrook-Zoo/payment/process')
        elif action == 'pay':
            request.session['booking_id'] = id
            return redirect('/Claybrook-Zoo/payment/process')
        data={
            'location' : 'booking',
            'title' : title,
            'bookings' : booking,
            'visitoraction' : actionname,
            'form' : form,
            'action' : action            
        }




    elif display == 'feedback':
        title = 'feedback'
        form = forms.Feedback
        actionname = 'Give Feedback to zoo'
        feedback = models.Feedback.objects.filter(sender=request.user)
                
        if action == 'delete':
            models.Feedback.objects.get(pk=request.POST.get('id')).delete()
            response_data = {}
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        
        elif action == 'add':
            title = 'Give feedback to zoo'
            if request.method == 'POST':
                models.Feedback(description=request.POST.get('description'),sender=request.user).save()
                return redirect('/Claybrook-Zoo/visitorpanel/feedback/none/0')
        data={
            'location' : 'feedback',
            'title' : title,
            'feedbacks' : feedback,
            'visitoraction' : actionname,
            'form' : form,
            'action' : action            
        }



    

    elif display == 'sponsor':
        title = 'sponsor'
        form = forms.VisitorSponsorForm
        actionname = 'Sponsor New Animal'
        sponsor = models.Sponsor.objects.filter(sponsored_user=request.user)
        if action == "update":
            actionname = 'Update Information'
            details =models.Sponsor.objects.get(pk=id)
            form = forms.VisitorSponsorForm(request.POST or None, instance=details)
            title ="Update Information"
            if form.is_valid():
                form.save()
                return redirect('/Claybrook-Zoo/visitorpanel/sponsor/none/0')
                
        elif action == 'delete':
            models.Sponsor.objects.get(pk=request.POST.get('id')).delete()
            response_data = {}
            return HttpResponse(json.dumps(response_data),content_type="application/json")

        elif action == 'add':
            title = 'Sponsor New Animal'

            if request.method == 'POST':
                form = forms.VisitorSponsorForm(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    if request.user.role == 'visitor':
                        ani = models.Animal.objects.get(id=id)
                        model = models.Sponsor.objects.latest('id')
                        sponsor = models.Sponsor.objects.get(pk=model.id)
                        if id != 0:
                            sponsor.animal.add(ani)
                        sponsor.sponsored_user.add(request.user)
                        request.session['sponsor_id'] = sponsor.id
                        return redirect('/Claybrook-Zoo/payment/process')
                    return redirect('/Claybrook-Zoo/visitorpanel/sponsor/none/0')
                
        elif action == 'pay':
            request.session['sponsor_id'] = id
            return redirect('/Claybrook-Zoo/payment/process')
                    
        data={
            'location' : 'sponsor',
            'title' : title,
            'sponsors' : sponsor,
            'visitoraction' : actionname,
            'form' : form,
            'action' : action,
            'id' : id,      
        }
    
    return render(request, 'visitorpanel.html',data)





def payment(request,action):
    booking = ''
    sponsor = ''
    name = ''
    if request.session.get('booking_id'):
        name = 'Ticket'
        booking_id = request.session.get('booking_id')
        booking = get_object_or_404(models.Booking, id=booking_id)
        form = ''
        if action == 'process':
            host = request.get_host()

            paypal_dict = {
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'amount': '%.2f' % int(booking.total_cost),
                'item_name': 'Booking {}'.format(booking.id),
                'invoice': str(booking.id),
                'currency_code': 'USD',
                'notify_url': 'http://{}{}'.format(host, ('paypal-ipn')),
                'return_url': 'http://{}{}'.format(host, ('/Claybrook-Zoo/payment/done')),
                'cancel_return': 'http://{}{}'.format(host, ('/Claybrook-Zoo/payment/canceled')),
            }
            form = PayPalPaymentsForm(initial=paypal_dict)
        elif action == 'done':
            update = models.Booking.objects.filter(id=booking.id)
            update.update(payment='yes')
    elif request.session.get('sponsor_id'):
        name = 'Sponsorship'
        sponsor_id = request.session.get('sponsor_id')
        sponsor = get_object_or_404(models.Sponsor, id=sponsor_id)
        form = ''
        if action == 'process':
            host = request.get_host()

            paypal_dict = {
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'amount': '%.2f' % int(sponsor.total_fee),
                'item_name': 'Sponsor {}'.format(sponsor.id),
                'invoice': str(sponsor.id),
                'currency_code': 'USD',
                'notify_url': 'http://{}{}'.format(host, ('paypal-ipn')),
                'return_url': 'http://{}{}'.format(host, ('/Claybrook-Zoo/payment/done')),
                'cancel_return': 'http://{}{}'.format(host, ('/Claybrook-Zoo/payment/canceled')),
            }
            form = PayPalPaymentsForm(initial=paypal_dict)
        elif action == 'done':
            update = models.Sponsor.objects.filter(id=sponsor.id)
            update.update(payment_received='yes')
    data = {
        'booking': booking,
        'form':form,
        'action':action,
        'sponsor':sponsor,
        'name' : name

    }

    return render(request, 'payment.html',data)



   