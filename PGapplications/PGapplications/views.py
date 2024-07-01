# i have created this file- ANkit
from django.http import HttpResponse
from django.shortcuts import render
'''def index(request):
    return HttpResponse ("hello Mummmy aap kaise ho MAA")

def About(request):
    return HttpResponse ("this is a about page")'''
#def fun(request):
   # return HttpResponse ('''<h1>this is my website</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Django code with Harrya</a>''')'''

def index(request):
  # Pars={'name':'Ankit','Age':'26'}
   return render(request, 'index.HTML')


    #return HttpResponse("home page")   
def Analyze(request):
    # get the text
    djtext= request.POST.get('Text','default')
    # check checkbox values
    pucne=request.POST.get('remove','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    Extraspaceremove=request.POST.get('Extraspaceremove','off')

    
    #anlayze=djtext
    # check which checkbox is on
    if pucne=="on":
        punctuatins ='''!()-[]{};:'"\,<>./?@#$%^&*_-'''
        anlayze=""
        for char in djtext:
            if char not in punctuatins:
                anlayze=anlayze+char 

        Param={'purpose':'Removed Punctuations','Analyze_text':anlayze}
        return render(request, 'Analyze.HTML',Param)
    if(fullcaps=="on"):
        anlayze=""
        for char in djtext:
            anlayze=anlayze+char.upper()
        Param={'purpose':'change to Upparcase','Analyze_text':anlayze}
        djtext=Analyze
        #return render(request, 'Analyze.HTML',Param)
    if(newlineremove=="on"):
        anlayze=""
        for char in djtext:
            if char !="\n" and char !="\r":
                anlayze=anlayze+char
        Param={'purpose':'Remove new Line','Analyze_text':anlayze}
        djtext=Analyze
       # return render(request, 'Analyze.HTML',Param)
    if(Extraspaceremove=="on"):
        anlayze=""
        for index ,char in enumerate(djtext):
            if not( djtext[index] ==" " and djtext[index+1]==" "):
                anlayze=anlayze+char
        Param={'purpose':'Remove new Line','Analyze_text':anlayze}
        djtext=Analyze
        #return render(request, 'Analyze.HTML',Param)     
    if(pucne=="on" and Extraspaceremove!="on" and newlineremove!="on" and fullcaps!="on"):
         return HttpResponse("Plz Select taype the words") 

     #else:
        
    return render(request, 'Analyze.HTML',Param)   
'''def remove(request):
    return HttpResponse("Remove details")  
def newlineadd(request):
    return HttpResponse("Add the new line") 
def space(request):
    return HttpResponse("give the space <a href='/'> back</a>") '''