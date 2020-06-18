from django.contrib import admin
from .models import Patient, Nurse, Hospital, Administrator, Bed, ContactUs
# Register your models here.


class PatientList(admin.ModelAdmin):
    list_display = ('patient_tag', 'first_name', 'last_name', 'sex', 'time_of_admission', 'condition', 'bed_type')
    list_filter = ('patient_tag','hospital_id','first_name', 'last_name','bed_id')
    search_fields = ('first_name', 'last_name','bed_id')
    ordering = ['first_name', 'last_name']


class HospitalList(admin.ModelAdmin):
    list_display = ('hospital_id','hospital_name', 'address', 'phone_no')
    list_filter = ('hospital_name', 'phone_no')
    search_fields = ('hospital_name', 'address')
    ordering = ['hospital_name']


class NurseList(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')
    search_fields = ('nurse_id', 'first_name', 'last_name')
    ordering = ['first_name', 'last_name']


class BedList(admin.ModelAdmin):
    list_display = ('bed_id', 'bed_type')
    list_filter = ('bed_id', 'bed_type', 'bh')
    search_fields = ('bed_id', 'bed_type','bed_count')
    ordering = ['bed_type']


class AdminList(admin.ModelAdmin):
    list_display = ('admin_id', 'admin_name')
    list_filter = ('admin_id', 'admin_name')
    search_fields = ('admin_id', 'admin_name')
    ordering = ['admin_name']

class ContactUsList(admin.ModelAdmin):
    list_display = ('contactId', 'firstName','lastName','emailId','question','created_date')
    list_filter = ('contactId', 'firstName','lastName','emailId','question','created_date')
    search_fields = ('contactId', 'firstName','lastName','emailId','question','created_date')
    ordering = ['contactId']


admin.site.register(Patient, PatientList)
admin.site.register(Nurse, NurseList)
admin.site.register(Hospital, HospitalList)
admin.site.register(Administrator,AdminList)
admin.site.register(Bed, BedList)
admin.site.register(ContactUs, ContactUsList)


