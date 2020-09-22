from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from hierarchyapp.models import FileFolder

admin.site.register(FileFolder, DraggableMPTTAdmin)