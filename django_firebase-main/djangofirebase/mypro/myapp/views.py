import requests
from django.conf import settings
from django.shortcuts import  render, redirect
from mypro.firebase_config import db
from django.contrib import messages

FIREBASE_KEY="AIzaSyA_sHnvQ0-Do7w7cct8DSqXRIk4h7z-fOo"
def Contacts(request):
    if request.method=="POST":
        a = request.POST.get("name")
        b = request.POST.get("email")
        c = request.POST.get("message")

        db.collection("contact").add({
            "Name": a,
            "Email" :b,
            "Msgs": c
        })
        messages.success(request,"query has been submitted")
        return redirect("con")

    return render(request,"myapp/Contact.html")

def ShowData(request):
    mydata = db.collection("contact").stream()
    contact=[]
    for a in mydata:
       convert_dict =  a.to_dict()
       convert_dict["id"] = a.id
       contact.append(convert_dict)
    return render(request,"myapp/Showdata.html",{"con":contact})

def Delete(req,id):
    db.collection("contact").document(id).delete()
    return redirect("show")

def register(req):
    if req.method == "POST":
        n = req.POST.get("name")
        e = req.POST.get("email")
        p = req.POST.get("password")

        if not n or not e or not p:
            messages.error(req,"All Fields are required")
            return redirect("reg")
        if len(p) < 8:
            messages.error(req,"Password must be 8 characters")
            return redirect("reg")
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={settings.FIRE}"
        payload = {
            "email":e,
            "password":p,
            "returnSecureToken":True
        }
        response = requests.post(url,payload)

        if response.status_code == 200:
            errorMsg=response.json()
            db.collection("User").add({
                "Name":n,
                "Email":e,
                "Pswd":p,
                "Role":"User",
            })
            messages.success(req,"User Register Successfully")
            return redirect("reg")

    return render(req,"myapp/Register.html")

def login(req):
    if req.method == "POST":
        e = req.POST.get("email")
        p = req.POST.get("password")

        if not e or not p:
            messages.error(req,"All fields are required")
            return redirect("log")

        url= f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={settings.FIRE}"
        payload={
            "email":e,
            "password":p,
            "returnSecureToken":True
        }
        res = requests.post(url,json=payload)

        if res.status_code == 200:
            userinfo = res.json()
            req.session["email"]=userinfo.get("email")
            return redirect("d")
        else:
            error= res.json().get("error",{}).get("message","Message not found")
            print(error)
            if error =="INVALID_LOGIN_CREDENTIALS":
                messages.error(req,"Invalid Credentials, login Again")
            elif error == "INVALID_PASSWORD":
                messages.error(req,"Password is incorrect")
            return redirect("log")
    return render(req,"myapp/login.html")

def dashboard(req):
    uemail = req.session["email"]
    return render(req,"myapp/dashboard.html",{"e":uemail})
