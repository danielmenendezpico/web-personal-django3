from django import http
from django.shortcuts import render, HttpResponse

html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/portfolio/">Portafolio</a></li>
        <li><a href="/contact/">contacto</a></li>
    </ul>
"""

# Create your views here.
def home (resquest):
    return render(resquest, "core/home.html")
       
def about(resquest):
    return render(resquest, "core/about.html")



def contact(resquest):
    return render(resquest, "core/contact.html")


    # <>