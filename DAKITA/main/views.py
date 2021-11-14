from .funcs import pic_download, ttss, langs
from django.shortcuts import render

def home(request):
    info = None
    tcuser = request.GET.get("tcname")
    submit = request.GET.get('name')

    if submit == "search":
        try:
            pic_download(tcuser)
        except:
            info = "Can't find the user"

    context = {
        "result": info,
        "tcuser": tcuser,
    }
    return render(request, "main/home.html", context)

def tts(request):
    tex = request.GET.get("text")
    lan = request.GET.get("l")
    b = request.GET.get("submit")
    
    if b == "submit":
       ttss(t=tex, l=lan)
            
    context = {
        "langs": langs,
        "text": tex,
        "lan": lan,
    }
    return render(request, "main/tts.html", context)