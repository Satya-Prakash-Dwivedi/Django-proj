from django.contrib import admin
from .models import chaiVariety, chaiCertificate, ChaiReview, Store

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1

class chaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type' )
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ['chai_varieties',]

class chaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issued_date', 'valid_until')


admin.site.register(chaiVariety, chaiVarietyAdmin)
admin.site.register(chaiCertificate, chaiCertificateAdmin)
admin.site.register(Store, StoreAdmin)
