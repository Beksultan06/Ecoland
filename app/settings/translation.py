from modeltranslation.translator import register, TranslationOptions
from app.settings.models import *

@register(SettingsBanner)
class SettingsBannerTranslation(TranslationOptions):
    fields = ("title", "descriptions")

@register(Settings)
class SettingsTranslation(TranslationOptions):
    fields = (
        "title", "title2", "title_plan_1", "title_plan_2", "descriptions_plan",
        "title_tours", "title_tours2", "title_tevily", "title_tevily2", 
        "title_partners", "title_testimonials", "title_testimonials2", 
        "title_choices", "title_choices2", "descriptions_choices", "title_news", "title_news2"
    )

@register(GalleryMainPage)
class GalleryMainPageTranslation(TranslationOptions):
    fields = ("title", "advantages_main_page")

@register(MainTours)
class MainToursTranslation(TranslationOptions):
    fields = ("superb", "title", "name_city")

@register(VideoMainPage)
class VideoMainPageTranslation(TranslationOptions):
    fields = ("title",)

@register(DopInfo)
class DopInfoTranslation(TranslationOptions):
    fields = ("title", "descriptions")

@register(AboutPage)
class AboutPageTranslation(TranslationOptions):
    fields = (
        "title", "title_tevily", "title_tevily2", "title_tevily3", "descriptions",
        "title_ready", "title_ready2", "title_saying", "title_saying2", 
        "title_video", "title_video2", "title_team", "title_team2"
    )

@register(TeamAboutPage)
class TeamAboutPageTranslation(TranslationOptions):
    fields = ("title", "job_title")

@register(ContactPage)
class ContactPageTranslation(TranslationOptions):
    fields = ("title", "title_form", "title_form2")

@register(AboutPercent)
class AboutPercentTranslation(TranslationOptions):
    fields = ("title",)