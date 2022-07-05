from django.contrib.auth import get_user_model
from .models import Employee,Department,Kin,Attendance, Leave, Recruitment
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.core import validators
from django.utils import timezone
from django.db.models import Q
import time
class RegistrationForm (UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email is required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    is_staff = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'emp ID'}))
    emp_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'employee ID'}))
    thumb = forms.ImageField(label='Attach a Passport Photograph',required=True,widget=forms.FileInput(attrs={'class':'form-control mt-2'}))
    class Meta:
        model = get_user_model()
        fields = ('username','email','password1', 'password2','emp_id','thumb','is_staff')

class LoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':True, 'placeholder':'Username Here', 'class':'form-control'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'********'}))

class EmployeeForm (forms.ModelForm):
    thumb = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    
    first_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    emp_id = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Employee ID'}))
    employee_type = forms.ChoiceField(choices=Employee.EMPLOYEE_TYPE,widget=forms.Select(attrs={'class':'form-control'}))
    mobile = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email'}))
    department = forms.ModelChoiceField(Department.objects.all(),required=True, empty_label='Select a department',widget=forms.Select(attrs={'class':'form-control'}))
    designation = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Designation'}))
    reporting_officer = forms.ModelChoiceField(Employee.objects.all(),required=True, empty_label='Select Reporting Officer',widget=forms.Select(attrs={'class':'form-control'}))
    #reporting_officer = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Reporting Officer'}))
    shift = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Shift'}))
    experience = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Experience'}))
    gender = forms.ChoiceField(choices=Employee.GENDER,widget=forms.Select(attrs={'class':'form-control'}))
    qualification = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Qualification'}))
    merital_status = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Merital Status'}))
    place_of_birth = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Place of Birth'}))
    blood_group = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Blood Group'}))
    emergency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    emergency_contact_person_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Emergency Contact Person Name'}))
    relationship = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relationship'}))
    personal_mail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email'}))
    current_address = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Current Address'}))
    #aadhar_address = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Aadhar Address'}))
    uan_number = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'UAN Number'}))
    member_id = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Member ID'}))
    esic_number = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ESIC Number'}))
    ifsc_code = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'IFSC Code'}))
    aadhar_number = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Aadhar Number'}))
    pan_number = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'PAN Number'}))
    status = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Status'}))
    language = forms.ChoiceField(choices=Employee.LANGUAGE,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'employee_type', 'joined','emp_id','email','mobile','designation','department','reporting_officer','shift','experience','dob','gender','qualification','merital_status','place_of_birth','blood_group','emergency','emergency_contact_person_name','relationship','personal_mail','current_address','aadhar_address','uan_number','member_id','esic_number','bank_account_number','bank_name','ifsc_code','aadhar_number','pan_number','status','language','thumb')
        widgets={
            'joined': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'dob': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'bank_acount_number':forms.TextInput(attrs={'class':'form-control'}),
            'bank_name':forms.TextInput(attrs={'class':'form-control'})
        }

class KinForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    employee = forms.ModelChoiceField(Employee.objects.filter(kin__employee=None),required=False,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Kin
        fields = '__all__'
    


class DepartmentForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department Name'}))
    history = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Brief Department History'}))
    
    class Meta:
        model = Department
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Attendance.STATUS,widget=forms.Select(attrs={'class':'form-control w-50'}))
    staff = forms.ModelChoiceField(Employee.objects.filter(Q(attendance__status=None) | ~Q(attendance__date = timezone.localdate())), widget=forms.Select(attrs={'class':'form-control w-50'}))
    
    class Meta:
        model = Attendance
        fields = ['status','staff'] 
        


class LeaveForm (forms.ModelForm):

    class Meta:
        model = Leave
        fields = '__all__'

        widgets={
            'start': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'end': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'employee':forms.Select(attrs={'class':'form-control'}),
        }
class RecruitmentForm(forms.ModelForm):
    class Meta:
        model=Recruitment
        fields = '__all__'
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
        }
    
        