from django.contrib import admin

from main_page.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Accounts)
admin.site.register(DeveloperMessage)
admin.site.register(SearchHistory)
admin.site.register(WordHistory)
admin.site.register(WordOfTheDay)