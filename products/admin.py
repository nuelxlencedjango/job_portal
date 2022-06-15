
from django.contrib import admin

from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User

#admin.site.register(Carts)
#admin.site.register(Production)
#admin.site.register(Orders)
#admin.site.register(OrderItems)


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OurLocations)

#admin.site.register(Artisans)
