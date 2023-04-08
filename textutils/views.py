# I have created this file - Prakhar Bhatt
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('<h1>Hello World</h1>  <a href="https://www.youtube.com">Youtube</a>')

# def about(request):
#     return HttpResponse("About Prakhar bhaiii")


# code for day 7
# def index(request):
#     return HttpResponse("Home ")

def index(request):
    # params = {"name":"Prakhar", "place":"India"}
    # return render(request, 'index.html', params)
    return render(request, 'index.html')


def analyze(request):
    # djText = request.GET.get('text', 'default')
    # after video number 16  (why? see the video)
    djText = request.POST.get('text', 'default')
    # removepunc = request.GET.get('removepunc', 'off') # changed default value to off
    # fullcaps = request.GET.get('fullcaps', 'off')
    # newlineremover = request.GET.get('newlineremover', 'off')
    # spaceremover = request.GET.get('spaceremover', 'off')
    # charCounter = request.GET.get('charCounter', 'off')
    # changed default value to off
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charCounter = request.POST.get('charCounter', 'off')
    # print(djText)

    # works for only one check button
    """if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'remove Punctautions', 'analyze_text': analyzed}
    elif (fullcaps == 'on'):
        analyzed = ""
        for char in djText:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Changed to upper case', 'analyze_text': analyzed}
    elif (newlineremover == 'on'):
        analyzed = ""
        for char in djText:
            if char !="\n" and char!="\r":  # \r necessary at time stage
                analyzed = analyzed+char
        params = {'purpose': 'Removed new lines', 'analyze_text': analyzed}
    elif (spaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(djText):
            if not(djText[index] ==" " and djText[index+1]==" "):
                analyzed = analyzed+char
        params = {'purpose': 'Removed extra spaces', 'analyze_text': analyzed}
    elif (charCounter == 'on'):
        analyzed = f"The length of textarea is {len(djText)}."
        params = {'purpose': 'Char counter', 'analyze_text': analyzed}
    else:
        return HttpResponse("Error")"""

    # works for all chcek button or one or more than one button   -  after video no.17
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'remove Punctautions', 'analyze_text': analyzed}
        djText = analyzed
    if (fullcaps == 'on'):
        analyzed = ""
        for char in djText:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Changed to upper case', 'analyze_text': analyzed}
        djText = analyzed
    if (newlineremover == 'on'):
        analyzed = ""
        for char in djText:
            if char != "\n" and char != "\r":  # \r necessary at time stage
                analyzed = analyzed+char
        params = {'purpose': 'Removed new lines', 'analyze_text': analyzed}
        djText = analyzed
    if (spaceremover == 'on'):
        analyzed = ""
        # print(djText)
        for index, char in enumerate(djText):
            # print(index)
            if not (djText[index] == " " and djText[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Clear extra spaces', 'analyze_text': analyzed}
        djText = analyzed
    if (charCounter == 'on'):
        analyzed = f"The length of textarea is {len(djText)}."
        params = {'purpose': 'Char counter', 'analyze_text': analyzed}

    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and spaceremover != 'on' and charCounter != 'on'):
        return HttpResponse("Error")
    # analyze text
    # return HttpResponse("removepunc <br> <a href='/'><button>Back</button></a>")
    return render(request, "analyze.html", params)

# def removepunc(request):
#     djText = request.get.get('text', 'default')
#     print(djText)
#     # analyze text
#     return HttpResponse("removepunc <br> <a href='/'><button>Back</button></a>")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newlineremove")

# def spaceremove(request):
#     return HttpResponse("spaceremove")

# def charcount(request):
#     return HttpResponse("charcount")
