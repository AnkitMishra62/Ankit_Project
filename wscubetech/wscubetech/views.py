from django.http import HttpResponse
# html file ko render karane ke liye ese import karate hai
from django.shortcuts import render
from .forms import usersFroms

def Home(request):
    # Django ke date ko Html page pe aise send karate hai 
    date={
        't':"home new",
        'bdate': "hellow Ankit Mishra",
        'clist':['php','java','python'],
        'number':[10,20,30,40,50],
        'student_details':[
            {'name':'Ankit','phone':9752526235},
            {'name':'shiva','phone':9229611633}
        ]
    }
    return render(request,"Home.HTML",date)

def aboutUs(request):
    return HttpResponse("welcome to my first website thanku kanha Ji")
def contect(request):
    return HttpResponse("my number is <h1> 9752526235 </h1>")
# dynamic route Exmaple
def coursedetails(request,courseid):
    return HttpResponse(courseid)
'''def userForm(request):
      finalans=0
      fn=usersFroms()
      data={'form':fn}
        try:
          if request.method=="post":
              n1=int(request.post.get('num1'))
              n2=int(request.post.get('num2'))
              finalans=n1+n2
              data={
                  'form':fn,
                  'output':finalans
                  
              }
              url="".format(finalans)
              return redirect(url)
       except:
             pass
       return render(request,"useform.html") '''