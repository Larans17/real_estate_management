import requests
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from RealEstateAdmin.utils import *
from django.conf import settings
from RealEstateAdmin.allmessages import *

url = settings.API_URL
import json



def login(request):
    """
    Summary or Description of the Function:
        *  Admin Signin data and the bind data to input field.
    Method: ,'POST'
    """
    try:
        if request.method == "POST":
            email = request.POST.get("txtusername")
            password = request.POST.get("txtpassword")
            data = {'email':email,'password':password}

            login_data = requests.post('{url}/login/'.format(url=url),data=data)
            user_data = login_data.json()
            error_msg = user_data.get('message')
            if login_data.status_code == 200:
                request.session['Token']=user_data.get('Token')
                request.session['UserId']=user_data.get('user_id')
                request.session['User_name']=user_data.get('user_name')
                request.session['isSuperAdmin']= user_data.get('is_super_admin')
                messages.success(request,RealEstateMessages.login())
                return redirect('/create/property/')
                
            elif len(error_msg) == 1:
                context = data
                messages.error(request,LOGIN_VALIDATION)
                return render(request, "login/adminlogin.html")
            else:
                messages.error(request,error_msg)
                return redirect('login')
    
        return render(request, "login/adminlogin.html")

    except Exception as e:
        return RealEstateResponse.Response_errorhandler("login", str(e), request)


def admin_dashboard(request):

    """
    Summary or Description of the Function:
        *  Admin Dashboard data  and the bind data to Screen.
    Method: ,'GET'
    """
    # try:
    # user_id = request.session["UserId"]
    # headers = RealEstateResponse.Token_Authentication(request)

    # data = requests.get(
    #     "{url}/dashboard/admin-dashboard/".format(url=url), headers=headers,
    # ).json()

    context ={
        "data":'data'
    }
    return render(request,'dashboard.html',context=context)
    
    # except Exception as e:
    #     return RealEstateResponse.Response_errorhandler(
    #         "admin_dashboard", str(e), request
    #     )

def logout(request):
    request.session.flush()
    messages.success(request,LOGOUT)
    return redirect('login')

def render_page(request,page):
    try:
        headers = RealEstateResponse.Token_Authentication(request)
        context = {}
        if page == 'property':
            html_file = 'mypanel/property.html'
        elif page == 'unit':
            data_list = requests.get(
            "{url}/getall-property/".format(url=url), headers=headers).json()
            context['property']=data_list
            html_file = 'mypanel/unit.html'
        else:
            data_list = requests.get(
            "{url}/getall-unit/".format(url=url), headers=headers).json()
            context['tenant_list']=data_list
            html_file = 'mypanel/tenant.html'
        return render(request,html_file,context=context)
    
    except Exception as e:
        return RealEstateResponse.Response_errorhandler("render_page", str(e), request)

def create_property(request):
    """
    Summary or Description of the Function:
        * Create property
    """
    try:
        user_id = request.session["UserId"]
        headers = RealEstateResponse.Token_Authentication(request)
        if request.method =="POST":
            name = request.POST.get('txtpropertyname')
            location = request.POST.get('txtlocation')
            features = request.POST.get('hdFeature')
            address = request.POST.get('txtaddress')
            data={
                'name':name,
                'location':location,
                'features':features,
                'address':address,
                'created_by':user_id
                }
            print(data)
            post_data = requests.post(
            "{url}/post-property/".format(url=url), headers=headers,data=data).json()
            return JsonResponse(post_data,safe=False)
    
    except Exception as e:
        return RealEstateResponse.Response_errorhandler("create_property", str(e), request)
    
def get_object_list(request):
    """
    Summary or Description of the Function:
        * Create property
    """
    try:
        user_id = request.session["UserId"]
        headers = RealEstateResponse.Token_Authentication(request)
        obj_name = request.GET.get('obj_name')
        data_list = requests.get(
        "{url}/getall-{obj_name}/".format(url=url,obj_name=obj_name), headers=headers).json()
        return JsonResponse(data_list,safe=False)
    
    except Exception as e:
        return RealEstateResponse.Response_errorhandler("get_object_list", str(e), request)
    

def create_unit(request):
    """
    Summary or Description of the Function:
        * Create unit
    """
    try:
        user_id = request.session["UserId"]
        headers = RealEstateResponse.Token_Authentication(request)
        if request.method =="POST":
            property = request.POST.get('ddlproperty')
            unittype = request.POST.get('ddlunittype')
            rent_cost = request.POST.get('txtrentcost')
            data={
                'property':property,
                'unit_type':unittype,
                'rent_cost':rent_cost,
                'created_by':user_id
                }
            post_data = requests.post(
            "{url}/post-unit/".format(url=url), headers=headers,data=data).json()
            return JsonResponse(post_data,safe=False)
    
    except Exception as e:
        return RealEstateResponse.Response_errorhandler("create_unit", str(e), request)
    


def create_tenant(request):
    """
    Summary or Description of the Function:
        * Create tenant
    """
    try:
        user_id = request.session["UserId"]
        headers = RealEstateResponse.Token_Authentication(request)
        if request.method =="POST":
            name = request.POST.get('txtname')
            address = request.POST.get('txtaddress')
            unit = request.POST.get('ddlunit')
            agreement_end_date = request.POST.get('txtenddate')
            monthly_rent_date = request.POST.get('txtrentdate')
            documents = request.FILES.get('documents')
            data={
                'name':name,
                'address':address,
                'unit':unit,
                'agreement_end_date':agreement_end_date,
                'monthly_rent_date':monthly_rent_date,
                'created_by':user_id
                }
            file={'documents':documents}
            post_data = requests.post(
            "{url}/post-tenant/".format(url=url), headers=headers,data=data,files=file).json()
            return JsonResponse(post_data,safe=False)
    
    except Exception as e:
        return RealEstateResponse.Response_errorhandler("create_unit", str(e), request)
