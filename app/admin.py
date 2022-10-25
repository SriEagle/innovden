import import_export
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin, ExportActionModelAdmin, ImportMixin

import_export.admin
class ImportExportActionModelAdmin(ImportMixin, ExportActionModelAdmin):
    pass


# Register your models here.



class what_you_learn_TabularInline(admin.TabularInline):
    model = What_you_learn


class Requirements_TabularInline(admin.TabularInline):
    model = Requirements


class Video_TabularInLine(admin.TabularInline):
    model = Video


class File_TabularInLine(admin.TabularInline):
    model = File


class course_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TabularInline,Requirements_TabularInline,Video_TabularInLine,File_TabularInLine)





admin.site.register(Categories)

admin.site.register(Author)

admin.site.register(Course,course_admin)

admin.site.register(Level)

admin.site.register(What_you_learn)

admin.site.register(Requirements)

admin.site.register(Lesson)

admin.site.register(ReviewRating)

admin.site.register(Language)

admin.site.register(UserCourse)

