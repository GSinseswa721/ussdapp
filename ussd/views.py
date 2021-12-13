from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .iteganya import *
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='tuganimana01@gmail.com'
api_key ='1526a36fc4c257d18d07bcfd53b0d18324ce969a5cd6981a35abfa6028b259ac'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        level = text.split('*')
        category = text[:3]
        response =""
        #  main menu for our application
        if text == '':
            response =  "CON Welcome in Kigali insight hospitals \n"
            response += "1. Registration \n"
            response += "2. Hospitals \n"
        elif text == '1':

            response = "CON Choose hospital \n"
            response += "1. CHUK \n"
            response += "2. King Faisal Hospital"
        elif text == '1*1':
            product="CHUK"
            response = "CON Specialized "+str(product)+"\n"
        elif category =='1*1' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON Symbols \n"
        elif category =='1*1' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "CON Date of the day \n"
        elif category =='1*1' and int(len(level)) == 5 and str(level[4]) in  str(level):
            # save the data into the database
            category='CHUK'
            sizeOfland=level[2]
            names= level[3]
            idnumber = level[4]
            insert = Idafarmuser(sessiondId=session_id,
            serviceCode = service_code,
            phoneNumber=phone_number,
            level=level,
            category=category,
            sizeOfland=sizeOfland,
            names=names,
            idnumber=idnumber,
            )
            insert.save()
            response = "END Thank you \n"


        elif text == '1*2':
            product ="King faisal hospital"
            response ="CON Specialized "+str(product)+"\n"
        elif category =='1*2' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON Symbols \n"
        elif category =='1*2' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "CON your names \n"
        elif category =='1*2' and int(len(level)) == 5 and str(level[4]) in  str(level):
            category='CHUK'
            sizeOfland=level[2]
            names= level[3]
            idnumber = level[4]
            insert = Idafarmuser(sessiondId=session_id,
            serviceCode = service_code,
            phoneNumber=phone_number,
            level=level,
            category=category,
            sizeOfland=sizeOfland,
            names=names,
            idnumber=idnumber,
            )
            insert.save()
            response = "END Thank you \n"
         
        #  ======================== INGENGABIHE==================
        elif text == '2':
            response = "CON  Dates\n "
            response += "1. Once in month \n"
            response += "2. Twice in month \n"
            response += "3. Daily"
        elif text == '2*1':
            # save the data
            insertData(
                category='One',
                sessionID=session_id,
                phoneNumber=phone_number
            )
            response ="END Thanks , we will be sending information once in month"
        elif text == '2*2':
            insertData(
                category='Two',
                sessionID=session_id,
                phoneNumber=phone_number
            )
            response ="END Thanks , we will be sending information twice in month"
        elif text == '2*3':
            insertData(
                category='Daily',
                sessionID=session_id,
                phoneNumber=phone_number
            )
            response ="END Thanks , we will be sending information daily"

        else:
            response = "END try again"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')
