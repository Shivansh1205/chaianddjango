from django.contrib import admin
from chai.models import *
# Register your models here.
class chai_review_Inline(admin.TabularInline):
    model = chai_reviews
    extra = 2
class chai_variety_admin(admin.ModelAdmin):
    list_display = ('name', 'date', 'type')
    inlines = [chai_review_Inline]

class store(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varity',)

class Chai_certificate_admin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')

class chai_reviews_admin(admin.ModelAdmin):
    list_display = ('chai','user', 'rating','date_added')

admin.site.register(chai_variety, chai_variety_admin)
admin.site.register(Store, store)
admin.site.register(certificate, Chai_certificate_admin)
admin.site.register(chai_reviews, chai_reviews_admin)