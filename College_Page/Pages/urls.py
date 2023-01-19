from django.urls import path
from .views import *
urlpatterns = [
     path("gnana-gangotri-hostel.html",HostelBoysPageView.as_view(), name="boys_hostel"),


     path("dept_of_english.html", DeptOfEnglishPageView.as_view(), name="dept_of_english"),



     path("scholarships.html", ScholarshipsPageView.as_view(), name="scholarships"),
     path("fee_structure.html", FeeStructurePageView.as_view(), name="fee-structure"),
     path("reservations.html", ReservationsPageView.as_view(), name
     ="reservations"),

     path("rules.html", RulesPageView.as_view(),
         name="rules"),

    path("procedure_for_admission.html", ProcedureForAdmissionPageView.as_view(),
         name="procedure_for_admission"),

    path("eligibility-for-admission.html",
         EligibilityForAdmissionPageView.as_view(), name="eligibility-for-admission"),

    path("courses-offered.html", CoursesOfferedPageView.as_view(),
         name="courses-offered"),


    path("administrative-staff/", AdministrativeStaffPageView.as_view(),
         name="administrative-staff"),
    path("administrative-structure/", AdministrativeStructurePageView.as_view(),
         name="administrative-structure"),



    path("college-profile/", CollegeProfilePageView.as_view(),
         name="college-profile"),

    path("university-profile/", UniversityProfilePageView.as_view(),
         name="university-profile"),
    path("", HomePageView.as_view(), name="home"),


]
