from django.contrib import admin
from .models import *
class Expertise_Info(admin.TabularInline):
    model = Expertise

class Skills_Info(admin.TabularInline):
    model = Skills

class Languages_Info(admin.TabularInline):
    model = Languages

class Projects_Info(admin.TabularInline):
    model = Projects


class Education_Info(admin.TabularInline):
    model = Education

class Certificates_Info(admin.TabularInline):
    model = Certificates

class MoreDetails_Info(admin.TabularInline):
    model = MoreDetails

class SocialLinks_Info(admin.TabularInline):
    model = SocialLinks

class PersonalDetails_Admin(admin.ModelAdmin):
    inlines = [Expertise_Info, Skills_Info, Languages_Info, Projects_Info, Education_Info, Certificates_Info, MoreDetails_Info, SocialLinks_Info]
class ProjectTechnologies_Info(admin.TabularInline):
    model = ProjectTechnologies

class ProjectDetails_Admin(admin.ModelAdmin):
    inlines = [ProjectTechnologies_Info]

admin.site.register(PersonalDetails, PersonalDetails_Admin)
admin.site.register(Expertise)
admin.site.register(Skills)
admin.site.register(Languages)
admin.site.register(Projects, ProjectDetails_Admin)
admin.site.register(ProjectTechnologies)
admin.site.register(Education)
admin.site.register(Certificates)
admin.site.register(MoreDetails)
admin.site.register(SocialLinks)
admin.site.register(NewMessages)


