from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'rating',
        'review_text',
        'product',
        'user',
        'date'
    )

    ordering = ('product', )


admin.site.register(Review, ReviewAdmin)
