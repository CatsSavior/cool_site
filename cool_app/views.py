from django.shortcuts import render

def my_site(request):
    return render(request, "main.html", locals())

def about(request):
    return render(request, "about.html", locals())
