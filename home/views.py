from django.shortcuts import render

def home(request):
    context_dict = {"title":'Welcome to Unspoken',
                    "body":'<h1>Login</h1>'}

    return render(request, "basic.html", context_dict)