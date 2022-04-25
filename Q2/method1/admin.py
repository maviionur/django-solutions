from django.contrib import admin
from method1.models import Bin, Operation, BinOperation

# Register your models here.
admin.site.register(Bin)
admin.site.register(Operation)
admin.site.register(BinOperation)