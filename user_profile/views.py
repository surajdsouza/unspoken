from django.shortcuts import render

def profile(request):
    user = request.get_full_path()[3:]
    context_dict = {"title":'Unspoken',
                    "body":'<a href="/">Unspoken</a><br>'+user+'\'s profile</br>'}

    return render(request, "basic.html", context_dict)