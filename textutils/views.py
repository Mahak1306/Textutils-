# i have creted thid
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    dic={'name':'mahak','age':'22','course':'mca'}
    return render(request,'index.html',dic)
    # return HttpResponse('''<h1>mahak</h1> <a href="https://www.facebook.com/" code with mahak </a>''')


# def about(request):
#     return HttpResponse("hello mahak jain")

def home(request):
    return HttpResponse("Home")


# def removepunc(request):
#     # get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     return HttpResponse("remove punc")
#

def capfirst(request):

    return HttpResponse("capitalize first  <a href='/'> back</a>")


def spaceremove(request):
    return HttpResponse("space remove")


def charcount(request):
    return HttpResponse("character count <a href='/'> back</a>")


def newlineremove(request):
    return HttpResponse("Nnew line remover")
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove= request.POST.get('newlineremove', 'off')
    spaceremove= request.POST.get('spaceremove', 'off')
    charcount= request.POST.get('charcount', 'off')
    print(removepunc)

    if (removepunc=="on"):

        analyzed=djtext
        punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char
        dic={'purpose':'remove punc','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',dic)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ char.upper()
        dic = {'purpose': 'changed to upper case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', dic)

    if (newlineremove=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char.upper()
        dic = {'purpose': 'REmoved new line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', dic)
    if (spaceremove=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if  djtext[index]==" " and djtext[index+1]==" ":
               pass
            else:
                analyzed = analyzed + char
        dic = {'purpose': 'REmoved new line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', dic)
    if (charcount=="on"):
        analyzed = ""
        c=0
        for char in djtext:
            if char!= "":
                c=c+1
                analyzed = analyzed + char
        counter ="No of character is: "+ str(c)
        dic = {'purpose': 'count number of character', 'analyzed_text': counter }

        # print("no of character is",c)
        #    return render(request, 'analyze.html', dic)

    if (removepunc!="on" and fullcaps!="on" and newlineremove!="on" and spaceremove!="on" and charcount!="on" ):
        return HttpResponse("Please select any operation")

    return render(request, 'analyze.html', dic)
