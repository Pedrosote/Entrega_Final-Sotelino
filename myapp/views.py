from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "q ona bienvenio a la pagina"}
    return render(request,"myapp/index.html", context)