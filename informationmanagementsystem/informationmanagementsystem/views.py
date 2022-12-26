from django.http import HttpResponse
from django.shortcuts import render


def HomePage(request):
    data ={
        'title': "New page",
        'bdata': "I want to be a developer",
        'clist': ["Bengali","English","Math"],
        'student_details': [
            {'name': 'Robin', 'phone': 1815339876,'District':'Chandpur','Country':'Bangladesh'},
            {'name': 'Samad', 'phone': 1815338040,'District':'Sylhet','Country':'Bangladesh'},
            {'name': 'Karim', 'phone': 1815338642,'District':'Khulna','Country':'Bangladesh'},
            {'name': 'Jibon', 'phone': 1815334045,'District':'Rangpur','Country':'Bangladesh'}
        ]

    }
    return render(request,'index.html',data)


def about(request):
     return HttpResponse('I am not understanding well')


def contact(request):
     return HttpResponse("<b>We don't have contact details yet<b>")


def coursedetails(request,courseid):
     return HttpResponse(courseid)

