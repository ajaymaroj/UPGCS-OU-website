from django.shortcuts import render

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    
class UniversityProfilePageView(TemplateView):
    template_name = "ABOUT_US/university_profile.html"

class CollegeProfilePageView(TemplateView):
    template_name = "ABOUT_US/college_profile.html"

# class InchargeHeadsPageView(TemplateView):
#     template_name = "ABOUT_US/incharge_heads.html"


class AdministrativeStaffPageView(TemplateView):
    template_name = "ABOUT_US/administrative_staff.html"


class AdministrativeStructurePageView(TemplateView):
    template_name = "ABOUT_US/administrative_structure.html"


class CoursesOfferedPageView(TemplateView):
    template_name = "ADMISSIONS/courses_offered.html"

class  EligibilityForAdmissionPageView(TemplateView):
    template_name = "ADMISSIONS/eligibility_for_admission.html"

class ProcedureForAdmissionPageView(TemplateView):
    template_name = "ADMISSIONS/procedure_for_admission.html"

class ReservationsPageView(TemplateView):
    template_name = "ADMISSIONS/reservations.html"

class FeeStructurePageView(TemplateView):
    template_name = "ADMISSIONS/fee_structure.html"

class ScholarshipsPageView(TemplateView):
    template_name = "ADMISSIONS/scholarships.html"


class RulesPageView(TemplateView):
    template_name= "ADMISSIONS/rules.html"



class DeptOfEnglishPageView(TemplateView):
    template_name = "DEPARTMENTS/dept_of_english.html"


class HostelBoysPageView(TemplateView):
    template_name= "HOSTEL/gnana-gangotri-hostel.html"
# Create your views here.
