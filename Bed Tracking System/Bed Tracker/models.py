from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    patient_tag = models.CharField(max_length=20, null=False, unique=True,default=0)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    MALE = 'M'
    FEMALE = 'F'
    type_of_sex = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    )
    sex = models.CharField(max_length=10,
                                      choices=type_of_sex,
                                      default=MALE, blank=False)
    time_of_admission = models.DateTimeField(default=timezone.now, blank=True)
    Undetermined = 'Undetermined'
    Good = 'Good'
    Fair = 'Fair'
    Serious = 'Serious'
    Critical = 'Critical'
    Dead = 'Dead'
    cond_type =(
        (Undetermined,'Undetermined'),
        (Good,'Good'),
        (Fair,'Fair'),
        (Serious,'Serious'),
        (Critical,'Critical'),
        (Dead,'Dead')
    )
    condition = models.CharField(max_length=50,choices=cond_type,default=Undetermined)
    ICU_CC = 'ICU/CC'
    EU = 'EU'
    MED_SURG = 'MED/SURG'
    OB = 'OB'
    SICU = 'SICU'
    Neg_Pres_Iso = 'Neg-Pres/Iso'
    OR = 'OR'
    Peds = 'Peds'
    PICU = 'PICU'
    NICU = 'NICU'
    Burn = 'Burn'
    Mental_Health = 'Mental-Health'
    Other = 'Other'
    type_of_bed= (
        (ICU_CC,'ICU/CC'),
        (EU,'EU'),
        (MED_SURG,'MED/SURG'),
        (OB, 'OB'),
        (SICU, 'SICU'),
        (Neg_Pres_Iso, 'Neg-Pres/Iso'),
        (OR, 'OR'),
        (Peds, 'Peds'),
        (PICU, 'PICU'),
        (NICU,'NICU'),
        (Burn, 'Burn'),
        (Mental_Health,'Mental-Health'),
        (Other, 'Other'),
    )
    bed_type = models.CharField(max_length=50, choices=type_of_bed,default='ICU',blank=True)
    bed_id = models.CharField(max_length=50,null=False,unique=True)
    mode_of_arrival = models.CharField(max_length=50,blank=True)
    age = models.CharField(max_length=10,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20,null=True, blank=True)
    injuries = models.CharField(max_length=50,blank=True)
    deposition = models.CharField(max_length=50, blank=True)
    time_of_surgery = models.CharField(max_length=20,blank=True)
    kin_name = models.CharField(max_length=50,blank=True)
    relation = models.CharField(max_length=50,blank=True)
    time_of_death = models.CharField(max_length=20,blank=True)
    created_date = models.DateTimeField(default=timezone.now,blank=True)
    updated_date = models.DateTimeField(auto_now_add=True, null = True)
    nurse_id = models.ForeignKey("Nurse", on_delete=models.CASCADE, related_name='nurpatients', null = False,default=1)
    hospital_id = models.ForeignKey("Hospital", on_delete=models.CASCADE, related_name='hosppatients', null=True)
    Admitted = 'Admitted'
    Discharged = 'Discharged'
    status =( (Admitted,'Admitted'),(Discharged,'Discharged'),)
    patient_status = models.CharField(max_length=40, choices=status, default='Admitted',blank=True)

    def created(self):
        self.time_of_admission = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.patient_tag)


class Nurse(models.Model):
    nurse_id = models.AutoField(null=False, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=20)
    created_date = models.DateField(default=timezone.now, blank=True, null=True)
    username = models.CharField(max_length=20, null=False,blank=False)
    password = models.CharField(max_length=32, null=False,blank=False)
    hospital_id = models.ForeignKey('Hospital',on_delete=models.CASCADE, related_name='hosnurses')
    # admin_id = models.ForeignKey('Administrator', on_delete=models.CASCADE, related_name='admnurses')

    def __str__(self):
        return str(self.nurse_id)


class Bed(models.Model):
    bed_id = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    bed_type = models.CharField(max_length=50, choices=Patient.type_of_bed,default='ICU')
    created_date = models.DateField(default=timezone.now)
    bh = models.ForeignKey('Hospital', on_delete=models.CASCADE, related_name='hosbeds')
    status = models.CharField(max_length=20,default='VACANT')

    def __str__(self):
        self.save()
        return str(self.bed_id)


class Hospital(models.Model):
    hospital_id = models.CharField(primary_key=True,max_length=100)
    hospital_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=12)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        self.save()
        return str(self.hospital_id)


class Administrator(models.Model):
    admin_id = models.AutoField(null=False, primary_key=True)
    admin_name = models.CharField(max_length= 100)

    def __str__(self):
        self.save()
        return str(self.admin_id)

class ContactUs(models.Model):
    contactId = models.AutoField(null=False, primary_key=True)
    firstName = models.CharField(max_length= 100)
    lastName = models.CharField(max_length=100)
    emailId = models.CharField(max_length=50)
    question = models.TextField()
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        self.save()
        self.created_date = timezone.now()
        return str(self.contactId)
