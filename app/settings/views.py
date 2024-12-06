from django.shortcuts import render, redirect
from app.settings.models import SettingsBanner, Settings, GalleryMainPage, MainTours, VideoMainPage, Partners,\
ImageMainPage, DopInfo, AboutPage, AboutPercent, TeamAboutPage, ContactPage
from django.core.mail import send_mail

from app.settings.utils import send_contact_email

# Create your views here.
def index(request):
    settings_all = SettingsBanner.objects.all()
    settings_id = Settings.objects.latest('id')
    gallery_all = GalleryMainPage.objects.all()
    main_all = MainTours.objects.all()
    video_all = VideoMainPage.objects.all()
    partnews_all = Partners.objects.all()
    image_all = ImageMainPage.objects.all()
    dopinfo_all = DopInfo.objects.all()
    return render(request, 'base/index.html', locals())

def about(request):
    about_id = AboutPage.objects.latest("id")
    about_procent_all = AboutPercent.objects.all()[:2]
    about_all = AboutPercent.objects.all()[2:]
    team_about_all = TeamAboutPage.objects.all()
    return render(request, 'base/about.html', locals())

def contact(request):
    contact_id = ContactPage.objects.latest("id")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            'Ecoland',
            f"""Здравствуйте.
            Спасибо за обратную связь, мы скоро свами свяжемся.
            Ваше ФИО: {name}
            Ваш email: {email}
            Ваше сообщение: {message}...

            Если вы ошиблись при указании данных можете обратно зайти на сайт и оставить новый отзыв с исправленными
            данными! """,
            "noreply@somehost.local",
            ["nurlanuuulubeksultan@gmail.com"]
        )
        send_contact_email.delay(name, email, message)
        return redirect('index')

    return render(request, "base/contact.html", locals())