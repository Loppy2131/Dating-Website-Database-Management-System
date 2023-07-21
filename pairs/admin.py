from django.contrib import admin
from pairs import models
# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display =('id','name','userid','password','email','photo','gender','phone')
	ording=('-pub_time',)
class User_Pair_idAdmin(admin.ModelAdmin):
	list_display=('person','pairid')
	ording=('-pub_time',)
class NotpairAdmin(admin.ModelAdmin):
	list_display=('person','notpairid')
	ording=('-pub_time',)
admin.site.register(models.UserRigister, UserAdmin)
admin.site.register(models.Pairid, User_Pair_idAdmin)
admin.site.register(models.NotPairid, NotpairAdmin)
admin.site.register(models.Marriage)
admin.site.register(models.Inrelationship)