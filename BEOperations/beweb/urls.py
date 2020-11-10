from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . forms import *
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
app_name = 'beweb'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('landing', views.landing, name='landing'),
    path('jobs',views.viewJobs,name='jobs'),
    path('listjobs/',ListJobs.as_view(),name='listjobs'),
    path('sjob',views.seejob,name='sjob'),
    path('editjob/',views.editjob,name='editjob'),
    path('changejob/',views.ChangeJob.as_view(),name='changejob'),
    path('job/',views.job,name='job'),
    path('mywork/', workorder, name='mywork'),
    path('api/login', views.login),
    path('addjob/', AddJob.as_view(), name='addjob'),
    path('getteam/', MyTeam.as_view(), name='getteam'),
    path('getmyteam/', MTeam.as_view(), name='getmyteam'),
    path('getasset/', MyAsset.as_view(), name='getasset'),
    path('updatejobasset/', MyjobAsset.as_view(), name='updatejobasset'),
    path('getwoid/', Mywo.as_view(), name='getwoid'),
    path('SaveJobandAddAsset/', SaveJobandAddAsset.as_view(), name='SaveJobandAddAsset'),
    path('SaveJob/', SaveJob.as_view(), name='SaveJob'),
    path('saveasset/', WoSaveAsset.as_view(), name='saveasset'),
    path('get_user/', views.get_user, name='get_user'),
    path('addteam/', views.addteam, name='addteam'),
    path('create/', views.create, name='create'),
    path('create_e117/',Create_E117_Job.as_view(),name='create_e117'),
    path('newteam/', views.create_team, name='newteam'),
    path('view_teams/',views.view_Teams,name='view_teams'),
    path('team/<ec_number>',views.view_Team,name='team'),
    path('editteam/',views.editTeam,name='editteam'),  
    path('orders/<ec_num>/', JobsViewSet.as_view(),name="orders"),
    path('openjobs/<username>/<section>/<status>/', JobsViewProcedure.as_view(),name="openjobs"),
    path('progressjobs/<username>/<section>/<status>/', ProgressJobs.as_view(), name="progressjobs"),
    path('supervisorjobs/<username>/<section>/<status>/', SuspendedJobs.as_view(),name="supervisorjobs"),
    path('workorders/<centre>/',WorkorderViewSet.as_view(),name='workorders'),
    path('saveworkorder/', OnlySaveWorkorder.as_view(), name='saveworkorder'),
    path('editwork/', editwork, name='editwork'),
    path('addjob/', AddJob.as_view(), name='addjob'),
    path('saveeditedworkorder/', SaveEditedWorkorder.as_view(), name='saveeditedworkorder'),
    path('form/<job_id>/', FormsView.as_view(), name='form'),
    path('Jobworkflow/', views.Job_workflow, name='Jobworkflow'),
    path('forms/', views.listForms, name='forms'),
    path('display/e84/',views.displayE84Form,name='e84-display'),
    path('e84/',e84Form,name='e84-view'),
    path('jobprogress/',views.jobprogress,name='jobprogress'),
    path('myjobs/',views.myjobs,name='myjobs'),
    path('<workorder_id>/jobs/',views.workorder_jobs,name='workorder-jobs'),
    path('reports/',views.reports,name='reports')
]
