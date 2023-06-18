from django.contrib import admin
from .models import Region, Settlement, ClubMember, MarriedCouple


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)
    search_fields = ('title',)

class SettlementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'region')
    list_filter = ('title', 'region')
    search_fields = ('title',)


class ClubMemberAdmin(admin.ModelAdmin):
    list_display = ('is_accepted', 'id', 'get_last_name', 'get_first_name', 'patronymic', 'birthday', 'gender',
                    'nationality', 'get_region',
                    'settlement', 'get_email', 'phone_number', 'education', 'activity_field', 'hobby', 'pets',
                    'favorite_holiday',
                    'favorite_color', 'favorite_dish', 'favorite_drink', 'favorite_musician', 'favorite_actor',
                    'favorite_book', 'favorite_movie', 'appreciate_in_people', 'repulsive_in_people')
    list_filter = ('id', 'user__first_name', 'user__last_name')
    search_fields = ('id', 'user__first_name', 'user__last_name')

    def get_first_name(self, obj):
        return obj.user.first_name

    get_first_name.short_description = 'first_name'

    def get_last_name(self, obj):
        return obj.user.last_name

    get_last_name.short_description = 'last_name'

    def get_email(self, obj):
        return obj.user.email

    get_email.short_description = 'email'

    def get_region(self, obj):
        return obj.settlement.region

    get_region.short_description = 'region'
    '''def save_model(self, request, obj, form, change):
        if not change:  # Создание нового объекта
            obj.user.first_name = obj.user.first_name
            obj.user.last_name = obj.user.last_name
            obj.user.email = obj.user.email
            obj.user.save()
        obj.save()'''

class MarriedCoupleAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_husband_full_name', 'get_wife_full_name', 'date_marriage')
    list_filter = ('id',)
    search_fields = ('id',)

    raw_id_fields = ('husband', 'wife')

    def get_husband_full_name(self, obj):
        return f"{obj.husband.user.first_name} {obj.husband.user.last_name}"
    get_husband_full_name.short_description = 'husband'

    def get_wife_full_name(self, obj):
        return f"{obj.wife.user.first_name} {obj.wife.user.last_name}"
    get_wife_full_name.short_description = 'wife'


admin.site.register(Region, RegionAdmin)
admin.site.register(Settlement, SettlementAdmin)
admin.site.register(ClubMember, ClubMemberAdmin)
admin.site.register(MarriedCouple, MarriedCoupleAdmin)

