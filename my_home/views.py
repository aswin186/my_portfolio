from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.
def index(request):
    personalDetails = PersonalDetails.objects.get(first_name="Aswin", active=PersonalDetails.live)
    person_id = personalDetails.id
    moreDetails = MoreDetails.objects.get(person_id=person_id)
    socialLinks = SocialLinks.objects.get(person_id=person_id)
    context = {"personalDetails": personalDetails, "moreDetails": moreDetails, "socialLinks": socialLinks}
    return render(request, 'index.html', context)

def dwonloadResume(request):
    personalDetails = get_object_or_404(PersonalDetails, active=PersonalDetails.live)
    if personalDetails.resume:
        response = HttpResponse(personalDetails.resume, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{personalDetails.first_name}_{personalDetails.second_name}_{personalDetails.profession}.pdf"'
        return response
    else:
        return HttpResponse("No resume available.", status=404)


def newMessageSaving(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']

        message_info = NewMessages(name=name, email_id=email, mobile_no=mobile, message=message)
        message_info.save()

        send_mail(
                subject=f"Message from {name}",
                message=f"Email Id:- {email} "+f"Phone Number:- {mobile} "+f"Name:- {name} "+f"Message:- {message} ",
                from_email=email,
                recipient_list=['aswinachu1812@gmail.com'],
        )

        messages.success(request,"Your Resopnse Is Recived")
        return redirect('index')
    else:
        messages.error(request,"error")
        return redirect('index')