import requests
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponseRedirect
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
import operator
from beapi.models import *
from .forms import *
import json
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK)
from rest_framework.response import Response
from django.contrib.auth.models import User
import posixpath
import os
import random
from . forms import NameForm, WorkOrderForm, JobForm, GeneralForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django_tables2 import RequestConfig
from .tables import *
from rest_framework import viewsets
from beapi.serializers import *
from django.db.models import Q


def user_authenticate(username):
    users = User.objects.all()
    for user in users:
        if user.username == username:
            token, created = Token.objects.get_or_create(user=user)
            return user.username, token.key
    return None


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)



def execsys(ecnum):
    URL = "http://172.20.0.70:8082/users/username/" + ecnum
    PARAMS = {'username': ecnum}
    r = requests.get(url=URL)
    data = r.json()
    return data


def get_center(centre_code):
    if centre_code == "ER":
        centre = "Regional Office (ER)"
        return centre, centre_code
    if centre_code == "ERM":
        centre = "Eastern Maintenance"
        return centre, centre_code
    if centre_code == "END":
        centre = "Network Development"
        return centre, centre_code
    if centre_code == "MTD":
        centre = "Mutare District"
        return centre, centre_code
    if centre_code == "URB":
        centre = "Mutare Urban"
        return centre, centre_code
    if centre_code == "ENV":
        centre = "Mutare Environs"
        return centre, centre_code
    if centre_code == "MTG":
        centre = "Mutare Garage"
        return centre, centre_code
    if centre_code == "MND":
        centre = "Manicaland District"
        return centre, centre_code
    if centre_code == "NYA":
        centre = "Nyanga"
        return centre, centre_code
    if centre_code == "RSP":
        centre = "Rusape"
        return centre, centre_code
    if centre_code == "CHP":
        centre = "Chipinge"
        return centre, centre_code
    if centre_code == "CHM":
        centre = "Chimanimani"
        return centre, centre_code
    if centre_code == "MSB":
        centre = "Middle Sabi"
        return centre, centre_code
    if centre_code == "MSD":
        centre = "Masvingo District"
        return centre, centre_code
    if centre_code == "MSV":
        centre = "Masvingo Urban"
        return centre, centre_code
    if centre_code == "GUT":
        centre = "Gutu"
        return centre, centre_code
    if centre_code == "MAS":
        centre = "Mashava"
        return centre, centre_code
    if centre_code == "RUT":
        centre = "Rutenga"
        return centre, centre_code
    if centre_code == "CHR":
        centre = "Chiredzi"
        return centre, centre_code
    if centre_code == "MSG":
        centre = "Masvingo Garage"
        return centre, centre_code
    centre = "No Centre"
    centre_code = "No Centre Code"
    return centre, centre_code


class MyTeam(View):
    def get(self, request, *args, **kwargs):
        team_leaders = request.GET['leader']
        myteam, teams = artisan_team(team_leaders)
        data = ""
        team_leaders = []
        Teams = Team.objects.all()
        my_teams = dict()

        for teamleader in Teams:
            if teamleader.team_leader not in [member.team_leader for member in team_leaders]:
                team_leaders.append(teamleader)
                my_teams[teamleader.team_leader] = []

        for teamleader in team_leaders:
            teammembers = Team.objects.filter(team_leader=teamleader)
            if teammembers:
                for teammember in teammembers:
                    my_teams[teamleader.team_leader].append(
                        teammember.team_member)
        return render(request, 'beweb/wo.html', {
            'data': data, 'myteam': myteam, 'my_teams': my_teams, 'teams': teams, 'team_leaders': team_leaders
        })

    def post(self, request, *args, **kwargs):
        members = []
        members = request.POST.getlist('members')
        return HttpResponse('Are you sure you want to save data')


class MTeam(View):
    def get(self, request, *args, **kwargs):
        data = execsys(request.user.username)
        centre_code = data['section']
        username = data['username']
        centre, centre_code = get_center(centre_code)
        centre = request.GET['centre']
        date = datetime.now().strftime("%Y%m%d%H%M")
        centre_code = request.GET['centre_code']
        team_leaders = request.GET['leader']
        myteam = artisan_team(team_leaders)
        data = ""
        return render(request, 'beweb/job/create.html', {
            'data': data, 'myteam': myteam,  'team_leaders': team_leaders
        })




class MyAssets(View):
    def get(self, request, *args, **kwargs):
        data = execsys(request.user.username)
        centre = data['section']
        return render(request, 'beweb/assets.html', {'centre': centre
                                                     })


class WoSaveAsset(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'beweb/assets/create.html', {
            'year': datetime.now(), 'wo': wo,
        })

    def get(self, request, *args, **kwargs):
        if not request.session['workorder_number']:
            username=request.session['username'] 
            description=request.session['description']
            supervisor=request.session['username']
            data = execsys(request.user.username)
            centre = data['section']
            section=request.session['section']
            centre_code=data['section']
            work_order_id=request.session['work_order']  
            date=datetime.now().strftime("%Y%m%d%H%M") 
            createdby=request.session['username'] 
            assignee=request.session['assignee']
            wo=request.session['work_order']
            job_description=request.session['job_description']
            expected_end_dt=request.session['expected_end_dt']
            section=request.session['section']  
            job_number=request.session['job_number']  
            trigger=request.session['trigger']  
            start_date=request.session['start_date']  
            asset_type=request.session['asset_type'] 
            job_type=request.session['job_type_id'] 
            fleet=request.session['fleet'] 
            team_members=request.session['team_members']       
            wo = save_wo(username, description, supervisor,
                        centre, date, centre_code, work_order_id)
            joid = Save_Job(createdby,assignee, job_type ,wo,job_description,expected_end_dt,centre,section,job_number,trigger,start_date,asset_type)
            jp = job_progress(job_number ,createdby,fleet)
            a=save_team(username ,assignee , jp,team_members)
            del request.session['description']
            del request.session['work_order']        
            del request.session['assignee']
            del request.session['job_description']
            del request.session['expected_end_dt']
            del request.session['section']  
            del request.session['job_number']  
            del request.session['trigger']  
            del request.session['start_date']  
            del request.session['asset_type'] 
            del request.session['job_type_id'] 
            del request.session['fleet'] 
            del request.session['team_members']
        else:
            wo=request.session['workorder_number']
            createdby=request.user.username
            username=request.user.username
            assignee=request.session['assignee']
            job_type=request.session['job_type_id']
            job_description=request.session['job_description']
            expected_end_dt=request.session['expected_end_dt']
            data = execsys(request.user.username)
            centre = data['section']
            section=request.session['section']  
            job_number=request.session['job_number']  
            trigger=request.session['trigger']  
            start_date=request.session['start_date']  
            asset_type=request.session['asset_type'] 
            fleet=request.session['fleet']  
            team_members=request.session['team_members']                     
            joid = Save_Job(createdby,assignee, job_type ,wo,job_description,expected_end_dt,centre,section,job_number,trigger,start_date,asset_type)
            jp = job_progress(job_number ,createdby,fleet)
            a=save_team(username ,assignee , jp,team_members) 
            del request.session['workorder_number']
            del request.session['assignee']
            del request.session['job_type_id'] 
            del request.session['job_description']
            del request.session['expected_end_dt']
            del request.session['section']  
            del request.session['job_number']  
            del request.session['trigger']  
            del request.session['start_date']  
            del request.session['asset_type']             
            del request.session['fleet']
            del request.session['team_members'] 

        joid = request.GET['joid']
        wo = request.GET['wo']
        url = 'http://172.20.0.70:8087/beapi/jobupdate/' + joid
        asset_sel = request.GET['asset_type']
        username = request.user.username
        selection = request.GET['asset_code_pk']
        usr, tkn = user_authenticate(username)
        data = {}
        if asset_sel == "transformer":
            t_pk = selection
            headers = {'Authorization': "Token "+tkn +
                       "", "Content-Type": "application/json"}
            URL = 'http://172.20.0.70:8089/gis/gistransformer/' + t_pk
            response = requests.get(url=URL, headers=headers)
            transformer = (response.json())[0]
            asset_id = transformer['transformerid']
            asset_name = transformer['name']
            asset_type = asset_sel
            asset_serial = transformer['serialno']
            asset_number = transformer['assetno']
            geom = transformer['geom2d']
            data = {
                "asset_id": asset_id,
                "asset_name": asset_name,
                "asset_type": asset_type,
                "asset_number": asset_number,
                "asset_serial": asset_serial,
                "geom":geom
            }
            data = json.dumps(data)
            r = requests.patch(url=url, data=data, headers=headers)
        if asset_sel == "switchgear":
            swt_pk = selection
            headers = {'Authorization': "Token "+tkn +
                       "", "Content-Type": "application/json"}
            URL = 'http://172.20.0.70:8089/gis/gisswitchgear/' + swt_pk
            response = requests.get(url=URL, headers=headers)
            switchgear = (response.json())[0]
            asset_id = switchgear['switchgearid']
            asset_name = asset_sel
            asset_type = asset_sel
            asset_serial = switchgear['serialno']
            asset_number = switchgear['assetno']
            geom = switchgear['geom2d']
            data = {
                "asset_id": asset_id,
                "asset_name": asset_name,
                "asset_type": asset_type,
                "asset_number": asset_number,
                "asset_serial": asset_serial,
                "geom":geom
            }
            data = json.dumps(data)
            r = requests.patch(url=url, data=data, headers=headers)
        if asset_sel == "meter":
            m_pk = selection
            headers = {'Authorization': "Token "+tkn +
                       "", "Content-Type": "application/json"}
            URL = 'http://172.20.0.70:8089/gis/gismeter/' + m_pk
            response = requests.get(url=URL, headers=headers)
            meter = (response.json())[0]
            asset_id = meter['meterid']
            asset_name = meter['make']
            asset_type = asset_sel
            asset_serial = ''
            asset_number = meter['meterno']
            geom = meter['geom2d']
            data = {
                "asset_id": asset_id,
                "asset_name": asset_name,
                "asset_type": asset_type,
                "asset_number": asset_number,
                "asset_serial": asset_serial,
                "geom":geom
            }
            data = json.dumps(data)
            r = requests.patch(url=url, data=data, headers=headers)
        if asset_sel == "feeder":
            f_pk = selection
            headers = {'Authorization': "Token "+tkn +
                       "", "Content-Type": "application/json"}
            URL = 'http://172.20.0.70:8089/gis/gisfeeder/' + f_pk
            response = requests.get(url=URL, headers=headers)
            feeder = (response.json())[0]
            asset_id = feeder['feedercode']
            asset_name = feeder['name']
            asset_type = asset_sel
            asset_serial = ''
            asset_number = feeder['assetno']
            geom = feeder['geom2d']
            data = {
                "asset_id": asset_id,
                "asset_name": asset_name,
                "asset_type": asset_type,
                "asset_number": asset_number,
                "asset_serial": asset_serial,
                "geom":geom
            }
            data = json.dumps(data)
            r = requests.patch(url=url, data=data, headers=headers)

        if asset_sel == "station":
            station_pk = selection
            headers = {'Authorization': "Token "+tkn +
                       "", "Content-Type": "application/json"}
            URL = 'http://172.20.0.70:8089/gis/gisstation/' + station_pk
            response = requests.get(url=URL, headers=headers)
            station = (response.json())[0]
            asset_id = station['stationid']
            asset_name = station['name']
            asset_type = asset_sel
            asset_serial = ''
            asset_number = station['assetno']
            geom=station['geom2d']
            data = {
                "asset_id": asset_id,
                "asset_name": asset_name,
                "asset_type": asset_type,
                "asset_number": asset_number,
                "asset_serial": asset_serial,
            }
            data = json.dumps(data)
            r = requests.patch(url=url, data=data, headers=headers)

        if asset_sel == "pole":
            p_pk = selection
            headers = {'Authorization': "Token "+tkn +
                       "", "Content-Type": "application/json"}
            URL = 'http://172.20.0.70:8089/gis/gistransformer/' + p_pk
            response = requests.get(url=URL, headers=headers)
            pole = (response.json())[0]
            asset_id = pole['poleid']
            asset_name = asset_sel
            asset_type = asset_sel
            asset_serial = ''
            asset_number = pole['assetno']
            geom = pole['geom2d']
            data = {
                "asset_id": asset_id,
                "asset_name": asset_name,
                "asset_type": asset_type,
                "asset_number": asset_number,
                "asset_serial": asset_serial,
            }
            data = json.dumps(data)
            r = requests.patch(url=url, data=data, headers=headers)
        my_work = Workorder.objects.filter(work_order_id=wo)
        my_jobs = Job.objects.filter(job_id=joid)
        my_progress = Jobprogress.objects.filter(job=joid)
        for jp in my_progress:
            my_team = Jobteam.objects.filter(job_progress=jp)

        return render(request, 'beweb/job/notification.html')


def workorder(request):
    work_order_id = request.GET.get('q', '')
    username = request.user.username
    usr, tkn = user_authenticate(username)
    headers = {'Authorization': "Token "+tkn +
               "", "Content-Type": "application/json"}

    url = "http://172.20.0.70:8087/beapi/single/workorder/" + work_order_id+"/"
    r = requests.get(url=url, headers=headers)
    data = r.json()
    num_jobs = len(data[0]['jobs'])
    employee_data = execsys(data[0]['created_by'])
    fullname = employee_data['firstname'] + " " + employee_data['surname']


    if data[0]['centre'] == "URB":
        data[0]['centre'] = "Mutare Urban"
    elif data[0]['centre'] == "ENV":
        data[0]['centre'] = "Mutare Environs"
    elif data[0]['centre'] == "RSP":
        data[0]['centre'] = "Rusape"
    elif data[0]['centre'] == "NYA":
        data[0]['centre'] = "Nyanga"
    elif data[0]['centre'] == "CHP":
        data[0]['centre'] = "Chipinge"
    elif data[0]['centre'] == "CHM":
        data[0]['centre'] = "Chimanimani"
    elif data[0]['centre'] == "MSB":
        data[0]['centre'] = "Middle Sabi"
    elif data[0]['centre'] == "RUT":
        data[0]['centre'] = "Rutenga"
    elif data[0]['centre'] == "GUT":
        data[0]['centre'] = "Gutu"
    elif data[0]['centre'] == "CHR":
        data[0]['centre'] = "Chiredzi"
    elif data[0]['centre'] == "MAS":
        data[0]['centre'] = "Mashava"
    elif data[0]['centre'] == "MSV":
        data[0]['centre'] = "Masvingo Urban"
    elif data[0]['centre'] == "MTD":
        data[0]['centre'] = "Mutare District"
    elif data[0]['centre'] == "MND":
        data[0]['centre'] = "Manicaland District"
    elif data[0]['centre'] == "MSD":
        data[0]['centre'] = "Masvingo District"
    elif data[0]['centre'] == "MTG":
        data[0]['centre'] = "Mutare Garage"
    elif data[0]['centre'] == "MSG":
        data[0]['centre'] = "Masvingo Garage"
        
    context = {
        "workorder": data[0],
        "number_of_jobs": num_jobs,
        "fullname": fullname
    }
    return render(request, 'beweb/workorder/workorder_view.html', context)


def job(request):
    job_id = request.GET.get('q', '')
    username = request.user.username
    decision = request.GET.get('decision', '')
    comments = request.GET.get('comments', '')
    
    try:
        job_workflow = Jobworkflow.objects.filter(
            job=job_id)[-0].workflow_id if Jobworkflow.objects.filter(job=job_id) else None
    except:
        job_workflow=None
    job_workflow_id = Jobworkflow.objects.filter(job = job_id)[-0].job_workflow_id
    workflow_code = Workflow.objects.filter(workflow_id = job_workflow)[0].workflow_code
    nextaction = Workflow.objects.filter(workflow_code = workflow_code)[0].role_code

    usr , tkn = user_authenticate(username)
    headers =  {'Authorization': "Token "+tkn+"","Content-Type": "application/json"}

    status = Job.objects.filter(job_id=job_id).values("status")[0]['status']
    role_name = ''
    approve = ''
    reject = ''
    if status >= 4:
        url="http://172.20.0.70:8087/beapi/job/awaiting/action/"+usr
        rs=requests.get(url=url,headers=headers)
        jobsdata =rs.json()
        
        role_name = jobsdata[0]["role_name"]
        approve = jobsdata[0]["approve"]
        reject = jobsdata[0]["reject"]

    url="http://172.20.0.70:8087/beapi/job/"+ job_id+"/"
    r=requests.get(url=url,headers=headers)
    data=r.json()
    team_data=data[0]['job_progress'][0]['jobteam_members']

    end_date=data[0]['job_progress'][0]['end_dt']   
    team_leader=data[0]['job_progress'][0]['jobteam_members'][0]['teamleader']

    employee_data = execsys(team_leader)    
    fullname=employee_data['firstname'] +" " + employee_data['surname'] 
    section=employee_data['section']    
    try:
        start = datetime.strptime(
            data[0]['start_date'], "%Y-%m-%d") if data[0]['start_date'] else ''
        end = datetime.strptime(
            data[0]['expected_end_dt'], "%Y-%m-%d %H:%M:%S") if data[0]['expected_end_dt'] else ''
        delta = (datetime(end.year, end.month, end.day, end.hour, end.minute, end.second)-datetime(start.year,
                                                                                                   start.month, start.day, start.hour, start.minute, start.second)) if start and end else ''
    except:
        delta = ''

    context = {
        "job": data[0],
        "section": section,
        "team_data": data[0]['job_progress'][0]['jobteam_members'],
        "team_members": len(team_data),
        "open_mileage": data[0]['job_progress'][0]['open_mileage'],
        "close_mileage": data[0]['job_progress'][0]['close_mileage'],
        "status": data[0]['job_progress'][0]['status'],
        "start_date": data[0]['start_date'],
        "expected_end_dt": data[0]['expected_end_dt'],
        "fleet": data[0]['job_progress'][0]['fleet_no'],
        "job_progress": data[0]['job_progress'],
        "trigger": data[0]['trigger'],
        "team_leader": fullname,
        "nextaction": nextaction,
        "status": status,
        "role_name": role_name,
        "approve": approve,
        "reject": reject
    }
    return render(request, 'beweb/job/jobview.html', context)



def get_team_progress():
    team_table = JobTeamTable(my_team)
    team_table.paginate(page=request.GET.get('page', 1), per_page=2)
    jobp_table = JobProgressTable(my_progress)
    jobp_table.paginate(page=request.GET.get('page', 1), per_page=2)
    return team_table, jobp_table


class MyAsset(View):
    def get(self, request, *args, **kwargs):
        transformers = Transformer.objects.all()
        switch = Switchgear.objects.all()
        submeter = Substationmeter.objects.all()
        feeder = Feeder.objects.all()
        pole = Pole.objects.all()
        selected = ""
        centre = ""
        centre_code = ""
        data = execsys(request.user.username)
        centre_code = data['section']
        centre, centre_code = get_center(centre_code)
        username = data['username']

        transformer_table = TransformerTable(
            Transformer.objects.filter(centre=centre))
        transformer_table.paginate(page=request.GET.get('page', 1), per_page=5)
        RequestConfig(request).configure(transformer_table)
        return render(request, 'beweb/asset.html', {
            'transformers': transformers, 'switch': switch, 'submeter': submeter, 'selected': selected, 'transformer_table': transformer_table, 'feeder': feeder, 'pole': pole, 'centre': centre, 'centre_code': centre_code
        })

    def post(self, request, *args, **kwargs):
        return HttpResponse('Are you sure you want to save data')


def get_user(request):
    username = request.user.username
    data = execsys(username)
    myteam = ""
    team_leaders = []
    Teams = Team.objects.all()
    for teamleader in Teams:
        if teamleader.team_leader not in [member.team_leader for member in team_leaders]:
            team_leaders.append(teamleader)
            # my_teams[teamleader.team_leader]=[]
    myteam = artisan_team(username)
    myteam = ""
    teams = ""
    return render(request, 'beweb/wo.html', {
        'data': data, 'myteam': myteam, 'teams': teams, 'team_leaders': team_leaders
    })


def artisan_team1(ecnum):
    leader = ecnum
    teams = Team.objects.all()
    myteam = Team.objects.filter(team_leader=leader)
    return myteam, teams


def artisan_team(ecnum):
    leader = ecnum
    teams = Team.objects.all()
    myteam = Team.objects.filter(team_leader=leader)
    return myteam



@login_required(login_url='/login')
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request, 'beweb/landing.html', {
            'titeam_leaderse': 'Home Page',
            'year': datetime.now().year,
        }
    )


def dashboard(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    data = execsys(request.user.username)
    centre = data["section"]

    return render(
        request, 'beweb/index.html', {
            'titeam_leaderse': 'Dashboard',
            'year': datetime.now().year, 'centre': centre
        }
    )


@login_required(login_url='/login')
def landing(request):
    return render(
        request, 'beweb/landing.html', {
            'titeam_leaderse': 'Bussiness Apps',
            'year': datetime.now().year,
        }
    )


def viewJobs(request):
    return render(request, 'beweb/jobs.html')


class ListJobs(View):

    def get(self, request, *args, **kwargs):
        open_jobs = 'open'
        data = execsys(request.user.username)
        section = data["section"]
        return render(request, 'beweb/reports/mywork.html', {"section": section})


def workorder_jobs(request, workorder_id):
    username = request.user.username
    usr, tkn = user_authenticate(username)
    headers = {'Authorization': "Token "+tkn +
               "", "Content-Type": "application/json"}
    url = "http://172.20.0.70:8087/beapi/workorder/jobs/" + workorder_id
    r = requests.get(url=url, headers=headers)
    data = r.json()
    context = {
        "workorder_id": workorder_id,
        "jobs": data[0]['jobs'],
    }

    return render(request, 'beweb/job/workorder_jobs.html', context)


def jobprogress(request):
    job_progress_id = request.GET.get('q', '')
    username = request.user.username
    usr, tkn = user_authenticate(username)
    headers = {'Authorization': "Token "+tkn +
               "", "Content-Type": "application/json"}

    url = "http://172.20.0.70:8087/beapi/jobprogress/" + job_progress_id
    r = requests.get(url=url, headers=headers)
    data = r.json()
    teamleader = execsys(data[0]['jobteam_members'][0]['teamleader'])
    context = {
        "job_progress_id": data[0]['job_progress_id'],
        "jobteam": ',    '.join([MyTeam['description'] for MyTeam in data[0]['jobteam_members']]),
        "teamleader": teamleader['firstname']+" "+teamleader['surname'],
        "comments": data[0]['comments'],
        "status": data[0]['status'],
        "start_dt": (datetime.strptime(data[0]['start_dt'], "%Y-%m-%d %H:%M:%S") if data[0]['start_dt'] else ''),
        "end_dt": (datetime.strptime(data[0]['end_dt'], "%Y-%m-%d %H:%M:%S") if data[0]['end_dt'] else ''),
        "job": data[0]['job'],
        "fleet_no": data[0]['fleet_no'],
        "open_mileage": data[0]['open_mileage'],
        "dt":  datetime.now(),
        "close_mileage": data[0]['close_mileage']
    }
    return render(request, 'beweb/job/jobprogress.html', context)


def seejob(request):
    """Renders the jobs View page"""
    return render(
        request, 'beweb/view_job.html'
    )


def editjob(request):
    """Renders the job edit page"""
    job_id = request.GET.get('q', '')
    username = request.user.username
    usr, tkn = user_authenticate(username)
    headers = {'Authorization': "Token "+tkn +
               "", "Content-Type": "application/json"}

    url = "http://172.20.0.70:8087/beapi/job/" + job_id+"/"
    r = requests.get(url=url, headers=headers)
    data = r.json()
    team_data = data[0]['job_progress'][0]['jobteam_members']
    end_date = data[0]['job_progress'][0]['end_dt']
    team_leader = data[0]['job_progress'][0]['jobteam_members'][0]['teamleader']
    employee_data = execsys(team_leader)
    fullname = employee_data['firstname'] + " " + employee_data['surname']
    context = {
        "job": data[0],
        "team_data": data[0]['job_progress'][0]['jobteam_members'],
        "team_members": len(team_data),
        "open_mileage": data[0]['job_progress'][0]['open_mileage'],
        "close_mileage": data[0]['job_progress'][0]['close_mileage'],
        "status": data[0]['job_progress'][0]['status'],
        "start_date": data[0]['job_progress'][0]['start_dt'],
        "fleet": data[0]['job_progress'][0]['fleet_no'],
        "job_progress": data[0]['job_progress'],
        "team_leader": fullname
    }
    return render(request, 'beweb/job/jobedit.html', context)


class ChangeJob(APIView):
    def get(self, request, *args, **kwargs):
        job_id = request.GET['job_number']
        username = request.user.username
        usr, tkn = user_authenticate(username)
        headers = {'Authorization': "Token "+tkn +
                   "", 'Content-Type': 'application/json'}
        url = "http://172.20.0.70:8087/beapi/jobupdate/" + job_id
        description = request.GET['description']
        start_date = request.GET['start_date']
        type = request.GET['type']
        trigger = request.GET['trigger']
        fleet = request.GET['fleet']
        asset_type = request.GET['plant_equipment']
        expected_end_dt = request.GET['expected_end_dt']
        data = {
            "job_id": job_id,
            "description": description,
            # "job_progress":[
            #     {
            #     "fleet_no":fleet
            #     }
            # ],
            "type": type,
            "start_date": start_date,
            "expected_end_dt": expected_end_dt,
            "trigger": trigger,
            "asset_type": asset_type
        }
        data = json.dumps(data)
        r = requests.patch(url=url, data=data, headers=headers)

        URL = "http://172.20.0.70:8087/beapi/job/" + job_id+"/"
        r1 = requests.get(url=URL, headers=headers)
        data1 = r1.json()
        team_data = data1[0]['job_progress'][0]['jobteam_members']
        end_date = data1[0]['job_progress'][0]['end_dt']
        team_leader = data1[0]['job_progress'][0]['jobteam_members'][0]['teamleader']
        employee_data = execsys(team_leader)
        fullname = employee_data['firstname'] + " " + employee_data['surname']
        section = employee_data['section']
        try:
            start = datetime.strptime(
                data1[0]['job_progress'][0]['start_dt'],  "%Y-%m-%d %H:%M:%S")
            end = datetime.strptime(
                data1[0]['job_progress'][0]['end_dt'],  "%Y-%m-%d %H:%M:%S")
            delta = (datetime(end.year, end.month, end.day, end.hour, end.minute, end.second) -
                     datetime(start.year, start.month, start.day, start.hour, start.minute, start.second))
        except:
            delta = ''

        context = {
            "job": data1[0],
            "section": section,
            "team_data": data1[0]['job_progress'][0]['jobteam_members'],
            "team_members": len(team_data),
            "open_mileage": data1[0]['job_progress'][0]['open_mileage'],
            "close_mileage": data1[0]['job_progress'][0]['close_mileage'],
            "status": data1[0]['job_progress'][0]['status'],
            "start_date": data1[0]['job_progress'][0]['start_dt'],
            "start_dt": (datetime.strptime(data1[0]['job_progress'][0]['start_dt'], "%Y-%m-%d %H:%M:%S") if data1[0]['job_progress'][0]['start_dt'] else ''),
            "expected_end_dt": (datetime.strptime(data1[0]['expected_end_dt'], "%Y-%m-%d %H:%M:%S") if data1[0]['expected_end_dt'] else ''),
            "fleet": data1[0]['job_progress'][0]['fleet_no'],
            "job_progress": data1[0]['job_progress'],
            "team_leader": fullname,
            "hours": delta
        }
        jobprogress = data1[0]['job_progress']
        return render(request, 'beweb/job/jobview.html', context)




def wo(request):
    """Renders the E84 page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'beweb/wo.html',
        {
            'titeam_leaderse': 'E84 Page',
            'year': datetime.now().year,
        }
    )


def all_centres():
    url = "http://172.20.0.70:8082/centres/"
    r = requests.get(url=url)
    data = r.json()
    centres = {}

    for value in data:
        if value['scode'] == "URB":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "ENV":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "RSP":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "NYA":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "CHP":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "CHM":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "MSB":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "RUT":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "GUT":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "CHR":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "MAS":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "MSV":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "MTD":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "MND":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "MSD":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "MTG":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
        elif value['scode'] == "MSG":
            centrecode = value['scode']
            centres[centrecode] = value['centrename']
    return centres


def create(request):
    data = execsys(request.user.username)
    centre_code = data['section']
    work_order = "wo"+datetime.now().strftime("%Y%m%d%H%M") + \
        str(random.randrange(000000, 100000))
    username = data['username']
    centre, centre_code = get_center(centre_code)
    centres = all_centres()
    request.session['work_order'] = work_order
    request.session['centre'] = centre
    request.session['centre_code'] = centre_code
    request.session['centres'] = centres
    request.session['username'] = username 
    request.session['year']=(datetime.now()).isoformat()     
    return render(
        request,
        'beweb/workorder/create.html',
        {
            'work_order': work_order, 'centre': centre, 'centre_code': centre_code, 'centres': centres, 'username': username,
            'year': datetime.now(),
        })


class Mywo(View):
    def get(self, request, *args, **kwargs):
        username = request.user.username
        data = execsys(username)
        username = data['username']
        description = request.GET['description']
        supervisor = request.GET['supervisor']
        date = datetime.now().strftime("%Y%m%d%H%M")
        centre_code = request.GET['centre_code']
        centre = centre_code
        work_order_id = request.GET['work_order_id']
        job_id = "jo"+datetime.now().strftime("%Y%m%d%H%M") + \
            str(random.randrange(000000, 100000))
        team_leaders = []
        jobtp = JobType.objects.filter(type='Line Inspection').values("job_type_id", "type")
        Teams = Team.objects.values('team_leader_id').distinct()
        team_leaders = [team_leader['team_leader_id'] for team_leader in Teams]

        teams = {}
        for team_leader in team_leaders:
            team_members = [team_member['team_member'] for team_member in Teams.values(
            ) if team_member['team_leader_id'] == team_leader]
            data = execsys(team_leader)
            teamleader = {
                "ec_number": team_leader,
                "firstname": data['firstname'],
                "lastname": data['surname']
            }
            members = []
            for member in team_members:
                data1 = execsys(member)
                first_name = data1['firstname']
                last_name = data1['surname']
                our_team = {
                    "ec_number": member,
                    "firstname": first_name,
                    "lastname": last_name
                }
                members.append(our_team)
            team_sheet = []
            team_sheet.append(teamleader)
            team_sheet.append(members)
            teams[team_leader] = team_sheet
            team_leader = ''

        # variable declared to allow for creation of Job starting from a workorder (already created). Logic implemented in the SaveJob view`s if statement
        request.session['workorder_number']='' 
        request.session['description'] = description 
        request.session['teams'] = teams         
        request.session['job_type_id'] = jobtp[0]['job_type_id']
        request.session['type'] = jobtp[0]['type']
        return render(request, 'beweb/job/create.html', {
            'wo': work_order_id, 'job_id': job_id, 'centre': centre, 'centre_code': centre_code, 'username': username, 'description': description,
            'year': datetime.now(), 'teams': teams, 'jobtp': jobtp,
        })

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('Are you sure you want to save data')


class Create_E117_Job(View):
    def get(self,request,*args,**kwargs):
        workorder_Id = request.GET.get('q', '')
        # print("-------------",job_type)
        request.session['workorder_number']=workorder_Id
        username = request.user.username
        data = execsys(username)
        centre_code = data['section']
        username = data['username']
        centre, centre_code = get_center(centre_code)
        jobtype = JobType.objects.filter(Q(type='Line Inspection') | Q(type='Installation Inspection')).values("job_type_id", "type")
        date = datetime.now()
        job_id = "jo"+datetime.now().strftime("%Y%m%d%H%M") + \
            str(random.randrange(000000, 100000))
        username = data['username']
        section = data['section']
        teams = {}
        # for team_leader in team_leaders:
        #     team_members = [team_member['team_member'] for team_member in Teams.values(
        #     ) if team_member['team_leader_id'] == team_leader]
        #     data = execsys(team_leader)
        #     teamleader = {
        #         "ec_number": team_leader,
        #         "firstname": data['firstname'],
        #         "lastname": data['surname']
        #     }

        return render(request, 'beweb/job/create_E117.html',{'work_order': workorder_Id, 'job_id': job_id, 'centre': centre, 'centre_code': centre_code, 'username': username,
            'year': datetime.now(),'jobtype':jobtype})

    def post(self, request, *args, **kwargs):
        return HttpResponse('Are you sure you want to save data')




class SaveJobandAddAsset(View):
    def get(self, request, *args, **kwargs):
        team_members = []
        username = request.user.username
        data = execsys(username)
        centre_code = data['section']
        username = data['username']
        section = data['section']
        centre, centre_code = get_center(centre_code)
        wo = request.GET['wo']
        assignee = request.GET['assignee']
        job_number = request.GET['job_number']
        job_type = request.GET['jobtype']
        trigger = request.GET['trigger']
        fleet = request.GET['fleet']
        start_date = request.GET['start_date']
        asset_type = request.GET['asset_type']
        job_description = request.GET['description']
        team_mmbr = request.GET['tnames']
        team_members = team_mmbr.split(", ")
        expected_end_dt = request.GET['expected_end_dt']
        createdby = request.user.username
        username = createdby
        jobtp = JobType.objects.filter(type='Line Inspection').values("job_type_id")
        request.session['assignee'] = assignee 
        request.session['trigger'] = trigger 
        request.session['fleet'] = fleet
        request.session['start_date'] = start_date 
        request.session['asset_type'] = asset_type 
        request.session['job_description'] = job_description
        request.session['team_members'] = team_members 
        request.session['expected_end_dt'] = expected_end_dt 
        request.session['section']=section
        request.session['job_number']=job_number     
        request.session['job_type_id']=request.GET['job_type_id']

        if asset_type=='feeder':
            column_one='Feeder Id'
            column_two='Name'
            column_three='Voltage'
            column_four='Length'
            data_one='feedercode'
            data_two='name'
            data_three='voltagelevel'
            data_four='length'
        elif asset_type=='station':
            column_one='Station Id'
            column_two='Name'
            column_three='Classification'
            column_four='Enclosure'
            data_one='stationid'
            data_two='name'
            data_three='classification'
            data_four='enclosure'
        elif asset_type=='pole':
            column_one="Pole Id"
            column_two="Pole Material"
            column_three="Feeder"
            column_four="Position Type"
            data_one='poleid'
            data_two='material'
            data_three='feeder'
            data_four='positiontype'
        elif asset_type=='meter':
            column_one='Meter Id'
            column_two='Meter No.'
            column_three='Make'
            column_four='Metering Type'
            data_one='meterid'
            data_two='meterno'
            data_three='make'
            data_four='meteringtype'
        elif asset_type=='switchgear':
            column_one='Switchgear Id'
            column_two='Type'
            column_three='Voltage Rating'
            column_four='Feeder Code'
            data_one='switchgearid'
            data_two='type'
            data_three='voltagerating'
            data_four='feedercode'
        elif asset_type=='transformer':
            column_one='Transformer Id'
            column_two='Make'
            column_three='Voltage Ratio'
            column_four='Name'
            data_one='transformerid'
            data_two='make'
            data_three='voltageratio'
            data_four='name'      
        return render(request, 'beweb/assets/assets.html', {
            'joid': job_number, 'wo': wo, 'centre': centre, 'centre_code': centre_code, 'username': username,
            'year': datetime.now(),  'asset_type': asset_type, 'column_one': column_one,
            'column_two': column_two, 'column_three': column_three, 'column_four': column_four, 'data_one': data_one,
            'data_two': data_two, 'data_three': data_three, 'data_four': data_four,
        })


class SaveJob(View):
    def get(self, request, *args, **kwargs):
        if not request.session['workorder_number']:
            username=request.session['username'] 
            description=request.session['description']
            supervisor=request.session['username']
            centre=request.session['centre_code']
            centre_code=request.session['centre_code']
            work_order_id=request.session['work_order']  
            date=datetime.now().strftime("%Y%m%d%H%M") 
            createdby=request.session['username'] 
            wo=request.session['work_order']
            data = execsys(username)
            section = data['section']
            assignee = request.GET['assignee']
            job_number = request.GET['job_number']
            job_type = request.GET['jobtype']
            job_description = request.GET['description']
            team_mmbr = request.GET['tnames']
            team_members = team_mmbr.split(", ")
            start_date = request.GET['start_date']
            trigger = request.GET['trigger']
            fleet = request.GET['fleet']
            asset_type = request.GET['asset_type']
            expected_end_dt = request.GET['expected_end_dt']
            wo1 = save_wo(username, description, supervisor,
                        centre, date, centre_code, work_order_id)
            joid = Save_Job(createdby,assignee, job_type ,wo,job_description,expected_end_dt,centre,section,job_number,trigger,start_date,asset_type)
            jp = job_progress(job_number ,createdby,fleet)
            a=save_team(username ,assignee , jp,team_members)
            del request.session['description']
            del request.session['centre_code']
            del request.session['work_order']
            del request.session['workorder_number'] 
        else:
            wo=request.session['workorder_number']
            createdby=request.user.username
            username=request.user.username
            assignee=request.GET['assignee']
            job_type=request.GET['job_type_id']
            job_description=request.GET['description']
            expected_end_dt=request.GET['expected_end_dt']
            data = execsys(request.user.username)
            centre = data['section']
            section=data['section']  
            job_number=request.GET['job_number']  
            trigger=request.GET['trigger']  
            start_date=request.GET['start_date']  
            asset_type=request.GET['asset_type'] 
            fleet=request.GET['fleet']  
            team_mmbr = request.GET['tnames']
            team_members = team_mmbr.split(", ")                    
            joid = Save_Job(createdby,assignee, job_type ,wo,job_description,expected_end_dt,centre,section,job_number,trigger,start_date,asset_type)
            jp = job_progress(job_number ,createdby,fleet)
            a=save_team(username ,assignee , jp,team_members) 
            del request.session['workorder_number']            
        return render(request, 'beweb/job/notification.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Are you sure you want to save data')



class Myjob(View):
    def get(self, request, *args, **kwargs):
        team_members = []
        username = request.user.username
        data = execsys(username)
        centre_code = data['section']
        username = data['username']
        section = data['section']
        centre, centre_code = get_center(centre_code)
        wo = request.GET['wo']
        assignee = request.GET['assignee']
        job_type = request.GET['jobtype']
        description = request.GET['description']
        team_mmbr = request.GET['tnames']
        trigger = request.GET['trigger']
        fleet = request.GET['fleet']
        start_date = request.GET['start_date']
        asset_type = request.GET['asset_type']
        team_members = team_mmbr.split(", ")
        expected_end_dt = request.GET['expected_end_dt']
        createdby = request.user.username
        username = createdby
        jobtp = JobType.objects.filter(
            type='Line Inspection').values("job_type_id")
        joid = save_jobworkflow(createdby, assignee, job_type,
                                wo, description, expected_end_dt, centre, section)
        jp = job_progress(joid, createdby, fleet)
        a = save_team(username, assignee, jp, team_members)
        return render(request, 'beweb/assets/create.html', {
            'joid': joid, 'wo': wo, 'centre': centre, 'centre_code': centre_code, 'username': username,
            'year': datetime.now(), 'jobtp': jobtp, "a": a, 'jp': jp
        })


class MyjobAsset(View):
    def post(self, request, *args, **kwargs):
        username = request.user.username
        wo = request.form['wo']
        jobid = request.form['jobid']
        asset_id = request.form['equipment_id']
        asset_name = request.form['make']
        asset_type = request.form['asset_type']
        asset_number = request.form['asset_number']
        asset_serial = request.form['asset_serial']
        data = {
            "asset_id": asset_id,
            "asset_name": asset_name,
            "asset_type": asset_type,
            "asset_number": asset_number,
            "asset_serial": asset_serial,
        }
        url = 'http://172.20.0.70:8087/beapi/jobupdate/' + str(jobid)
        usr, tkn = user_authenticate(username)
        headers = {'Authorization': "Token "+tkn +
                   "", "Content-Type": "application/json"}

        r = requests.patch(url=url, data=data, headers=headers)
        job = Job.objects.filter(job_id=jobid)
        return render(request, 'beweb/reports/mywork.html', {
            'job': job
        })


def generate_job_progress_id():
    jp_id = datetime.now().strftime("%Y%m%d%H%M") + \
        str(random.randrange(000000, 100000))
    return jp_id


def job_progress(job_id, createdby, fleet):
    jp_id = generate_job_progress_id()
    usr, tkn = user_authenticate(createdby)
    headers = {'Authorization': "Token "+tkn +
               "", "Content-Type": "application/json"}

    url = "http://172.20.0.70:8087/beapi/jobprogresspost"
    data = {
        "job_progress_id": "jp" + str(jp_id),
        "created_by": createdby,
        "created_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "comments": "",
        # "action": "",
        "status": 1,
        "fleet_no": fleet,
        "job": str(job_id)
    }
    data = json.dumps(data)

    r = requests.post(url=url, data=data, headers=headers)
    response_data = r.json()
    jp_id="jp" + str(jp_id)
    return jp_id


def save_jobworkflow(created_by, job_id, workflow_id, created_on):
    usr, tkn = user_authenticate(created_by)
    headers = {'Authorization': "Token "+tkn +
               "", "Content-Type": "application/json"}
    url = "http://172.20.0.70:8087/beapi/jobworkflowpost"
    data = {
        "workflow": workflow_id,
        "job_workflow_id": "jwf" + datetime.now().strftime("%Y%m%d%H%M") + str(random.randrange(000000, 100000)),
        "job": job_id,
        "created_by": created_by,
        "created_on": created_on,
    }
    data = json.dumps(data)

    r = requests.post(url=url, data=data, headers=headers)
    response_data = r.json()


def generate_job_team_id():
    jt = datetime.now().strftime("%Y%m%d%H%M") + \
        str(random.randrange(000000, 100000))
    return jt


def save_team(username, assignee, jp_id, team_members):
    team_leaders = assignee
    for membr in team_members:
        member = membr.partition('%')[2]
        membername = membr.partition('%')[0]
        if member:
            id = generate_job_team_id()
            usr, tkn = user_authenticate(username)
            url = "http://172.20.0.70:8087/beapi/jobteampost"
            headers = {'Authorization': "Token "+tkn +
                       "", "Content-Type": "application/json"}

            data = {
                "job_team_id": "jt" + id,
                "ec_num": member,
                "start_dt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "end_dt": "",
                "description": membername,
                "teamleader": team_leaders,
                "job_progress": jp_id
            }
            data = json.dumps(data)
            r = requests.post(url=url, data=data, headers=headers)
            response_data = r.json()
            member_id=member
        pass


def post_data(url, payload, headers):
    r = requests.request("POST", url, data=payload, headers=headers)
    response = r.json()
    return response


def generate_work_order_id():
    wo = datetime.now().strftime("%Y%m%d%H%M") + \
        str(random.randrange(000000, 100000))
    return wo


def save_wo(username, description, supervisor, centre, date, centre_code, work_order_id):
    wo = work_order_id
    usr, tkn = user_authenticate(username)
    url = 'http://172.20.0.70:8087/beapi/workorderpost'
    headers = {'Authorization': "Token "+tkn +
               "", 'Content-Type': 'application/json'}
    data = {
        "work_order_id": wo,
        "created_by": supervisor,
        "created_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "modified_by": "",
        "modified_on": None,
        "description": description,
        "centre": centre,
        "comments": None,
        "status": 1
    }
    data = json.dumps(data)
    r = requests.post(url=url, data=data, headers=headers)
    response_data = r.json()
    wo = response_data["work_order_id"]
    return wo


def generate_job_id():
    job_id = datetime.now().strftime("%Y%m%d%H%M") + \
        str(random.randrange(000000, 100000))
    return job_id


def Save_Job(createdby, assignee, job_type, wo, job_description, expected_end_dt, centre, section, job_number, trigger, start_date, asset_type):
    usr, tkn = user_authenticate(createdby)
    action_dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    workflow_code, workflow_id = updateworkflow(section, job_type)
    url = 'http://172.20.0.70:8087/beapi/jobpost'
    headers = {'Authorization': "Token "+tkn +
               "", "Content-Type": "application/json"
    }

    data = {
        "job_id": job_number,
        "created_by": createdby,
        "created_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": job_type,
        "description": job_description,
        "assignee": assignee,
        "start_date": start_date,
        "trigger": trigger,
        "expected_end_dt": expected_end_dt,
        "workflow": workflow_code,
        "status": 1,
        "work_order": wo,        
        "asset_type": asset_type
    }

    data = json.dumps(data)
    r = requests.post(url=url, data=data, headers=headers) 
    response_data = r.json()    
    created_on=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    jo=job_number
    save_jobworkflow(createdby, jo, workflow_id, created_on)
    return job_number


def updateworkflow(section, job_type):
    workflow_code = Appflow.objects.filter(section=section, app=job_type).values(
        'workflow_code')[0]['workflow_code']
    workflow_id = Workflow.objects.filter(
        workflow_code=workflow_code, step=1).values('workflow_id')[0]['workflow_id']
    return workflow_code, workflow_id


class AddJob(View):
    def get(self, request, *args, **kwargs):
        workorder_Id = request.GET.get('q', '')
        request.session['workorder_number']=workorder_Id
        username = request.user.username
        data = execsys(username)
        centre_code = data['section']
        username = data['username']
        centre, centre_code = get_center(centre_code)
        date = datetime.now()
        job_id = "jo"+datetime.now().strftime("%Y%m%d%H%M") + \
            str(random.randrange(000000, 100000))
        team_leaders = []
        jobtp = JobType.objects.filter(type='Line Inspection').values("job_type_id", "type")
        Teams = Team.objects.values('team_leader_id').distinct()
        team_leaders = [team_leader['team_leader_id'] for team_leader in Teams]

        workorder = Workorder.objects.filter(
            work_order_id=workorder_Id).values()
        username = data['username']
        section = data['section']

        teams = {}
        for team_leader in team_leaders:
            team_members = [team_member['team_member'] for team_member in Teams.values(
            ) if team_member['team_leader_id'] == team_leader]
            data = execsys(team_leader)
            teamleader = {
                "ec_number": team_leader,
                "firstname": data['firstname'],
                "lastname": data['surname']
            }
            members = []
            for member in team_members:
                data1 = execsys(member)
                first_name = data1['firstname']
                last_name = data1['surname']
                our_team = {
                    "ec_number": member,
                    "firstname": first_name,
                    "lastname": last_name
                }
                members.append(our_team)
            team_sheet = []
            team_sheet.append(teamleader)
            team_sheet.append(members)
            teams[team_leader] = team_sheet
            team_leader = ''
        return render(request, 'beweb/job/create.html', {
            'wo': workorder_Id, 'job_id': job_id, 'centre': centre, 'centre_code': centre_code, 'username': username,
            'year': datetime.now(), 'teams': teams, 'jobtp': jobtp, "description": workorder[0]['description'],
        })


def get_available_artisans(artisans,leaders):
    available_artisans=artisans
    for leader in leaders: 
        for artisan in artisans:        
            if artisan['username'] == leader['team_leader']:
                available_artisans.remove(artisan)
    return available_artisans


def create_team(request):  
    users = requests.get(url="http://172.20.0.70:8082/users/").json()
    if("specialisation" in request.GET):
        specialisation = request.GET['specialisation']
        team_leaders = TeamLeader.objects.filter(specialisation=specialisation).values('team_leader')       
        artisans = [user for user in users if ((user['designation'] == 'Artisan - ' + request.GET['specialisation']) and user['status'] == 'active')]
        available_artisans=get_available_artisans(artisans,team_leaders)
        artisan_assistants = [user for user in users if ((user['designation'] == 'Artisan Assistant - '+request.GET['specialisation']) and user['status'] == 'active')]
        return render(request, 'beweb/team/create.html', {
            'Artisans': available_artisans, 'ArtisanAssistants': artisan_assistants, 'specialisation': specialisation
        })
    else:
        return render(request, 'beweb/team/create.html', {
        })


def view_Teams(request):
    username = request.user.username
    usr, tkn = user_authenticate(username)
    headers = {'Authorization': "Token "+tkn +
            "", "Content-Type": "application/json"}
    url = "http://172.20.0.70:8087/beapi/teams"
    teams = requests.get(url=url, headers=headers)
    team_d = teams.json()
    leaders= []

    for leader in team_d:
        team_data=execsys(leader['team_leader'])       
        team = {
            'ec_number':leader['team_leader'],
            'fullname':team_data['firstname']+" "+team_data['surname'],
            'specialisation':leader['specialisation'],
            'members':len(leader['members'])
        }
        leaders.append(team)
    return render(request, 'beweb/team/teamsview.html',{'leaders':leaders})


def editTeam(self,request):   
    return render(request,'beweb/team/teamedit.html')


def view_Team(request,ec_number):
    username = request.user.username
    usr, tkn = user_authenticate(username)   
    headers = {'Authorization': "Token "+tkn +
            "", "Content-Type": "application/json"}
    url = "http://172.20.0.70:8087/beapi/teams/"+ ec_number
    teams = requests.get(url=url, headers=headers)
    team_data = teams.json()
    
    team_list=[]
    for team in team_data:
        leader_data=execsys(team['team_leader'])
        team_leader=leader_data['firstname']+" "+leader_data['surname']
        specialisation=team['specialisation']
        
        for member in team['members']:
            member_data=execsys(member['team_member'])                        
            team = {               
                "team_members":member_data['firstname']+" "+member_data['surname']
            }
            team_list.append(team)
    return render(request, 'beweb/team/viewteam.html',{'team_list':team_list,'team_leader':team_leader,'specialisation':specialisation})


def addteam(request):
    url1 = "http://172.20.0.70:8087/beapi/teampost"
    createdby = request.user.username
    usr, tkn = user_authenticate(createdby)
    headers = {'Authorization': "Token "+tkn +
               "", "Content-Type": "application/json"}
    data = requests.get(url="http://172.20.0.70:8082/users/").json()
    tmbrs = (request.GET['teammember']).split(", ")
    tmbrs = tmbrs[:-1]
    tldr = (request.GET['teamleader']).split("  ")
    lecnums = [x['username'] for x in data if (
        (x['firstname'] == tldr[0])and (x['surname'] == tldr[1]))]
    if lecnums:
        tms = []
        for lecnum in lecnums:
            for member in tmbrs:
                tmbr = (member).split("  ")
                ecnums = [x['username'] for x in data if (
                    (x['firstname'] == tmbr[0])and (x['surname'] == tmbr[1]))]
                if ecnums:
                    for ecnum in ecnums:
                        tms.append({
                            "team_id": "tm" + datetime.now().strftime("%Y%m%d%H%M") + str(random.randrange(000000, 100000)),
                            "created_by": createdby,
                            "created_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "team_leader": lecnum,
                            "team_member": ecnum,
                            "specialisation": request.GET['teamspecialisation']
                        })
            data1 = {"team_leader": lecnum, "team": tms,
                     "specialisation": request.GET['teamspecialisation']
                     }
            data1 = json.dumps(data1)
            r = requests.post(
                url="http://172.20.0.70:8087/beapi/teampost", data=data1, headers=headers)
            response_data = r.json()

    return render(request, 'beweb/team/notification.html', {
    })


def listForms(request):
    job_id = request.GET.get('job_id', '')
    context = {
        "job_id": job_id
    }
    return render(request, 'beweb/job/forms.html', context)


def displayE84Form(request):
    return render(request, 'beweb/job/e84.html')


def e84Form(request):
    e84_general_id = request.GET.get('q', '')
    username = request.user.username
    usr, tkn = user_authenticate(username)
    headers = {'Authorization': "Token "+tkn +
               "", "Content-Type": "application/json"}

    url = "http://172.20.0.70:8087/beapi/e84general/" + e84_general_id
    r = requests.get(url=url, headers=headers)
    data = r.json()
    employee_data = execsys(data[0]['created_by'])
    fullname = employee_data['firstname'] + " " + employee_data['surname']
    created_on = (datetime.strptime(
        data[0]['created_on'], "%Y-%m-%d %H:%M:%S") if data[0]['created_on'] else '')
    context = {
        "e84_data": data[0],
        "inspections": data[0]['inspections'],
        "fullname": fullname,
        "created_on": created_on
    }
    return render(request, 'beweb/job/e84.html', context)


class FormsView(APIView):
    def get(self, request, job_id):
        forms = JobFormsModel.objects.filter(job_id=job_id)
        serializer = JobFormSerializer(forms, many=True).data
        return Response(serializer)


class JobsViewProcedure(APIView):
    '''
    Arguments:
        [username,section,status]
    Returns:
        Job id and Workorder id for the specified user
    '''

    def get(self, request, username, section, status):
        jobs = Job.objects.jobs_view_procedure(
            username=username, section=section, status=1)
        return Response(jobs)


class JobsViewSet(APIView):
    '''
    Returns a list of  jobs awaiting action in the system
    '''

    def get(self, request, ec_num):
        jobs = Jobworkflow.objects.job_awaiting_action_procedure(ec_num=ec_num)
        return Response(jobs)

class TeamsView(APIView):

    def get(self,request):
        username = request.user.username
        usr, tkn = user_authenticate(username)
        headers = {'Authorization': "Token "+tkn +
                "", "Content-Type": "application/json"}
        url = "http://172.20.0.70:8087/beapi/teams"
        teams = requests.get(url=url, headers=headers)
        team_data = teams.json()
        employee_data = execsys(team_data[0]['team_leader'])
        fullname = employee_data['firstname'] + " " + employee_data['surname']

        return Response(team_data)


class ProgressJobs(APIView):
    '''
    Arguments:
        [username,section]
    Returns:
        Job id and Workorder id for the specified user
    '''

    def get(self, request, username, section, status):
        jobs = Job.objects.jobs_view_procedure(
            username=username, section=section, status=2)
        return Response(jobs)


class SuspendedJobs(APIView):
    '''
    Arguments:
        [username,section]
    Returns:
        Job id and Workorder id for the specified user
    '''

    def get(self, request, username, section, status):
        jobs = Job.objects.jobs_view_procedure(
            username=username, section=section, status=3)
        return Response(jobs)



class WorkorderViewSet(APIView):
    def get(self, request, centre):
        if centre == 'MSD':
            workorder = Workorder.objects.filter(Q(centre='MSV') | Q(centre='GUT') | Q(
                centre='RUT') | Q(centre='MAS') | Q(centre='CHR') | Q(centre='MSG') | Q(centre='MSD'))
            serializer = WorkorderSerializers(workorder, many=True).data
        elif centre == 'MND':
            workorder = Workorder.objects.filter(Q(centre='CHM') | Q(centre='MSB') | Q(
                centre='CHP') | Q(centre='NYA') | Q(centre='RSP') | Q(centre='MND'))
            serializer = WorkorderSerializers(workorder, many=True).data
        elif centre == 'MTD':
            workorder = Workorder.objects.filter(Q(centre='ENV') | Q(
                centre='URB') | Q(centre='MTG') | Q(centre='MTD'))
            serializer = WorkorderSerializers(workorder, many=True).data
        else:
            workorder = Workorder.objects.filter(Q(centre=centre))
            serializer = WorkorderSerializers(workorder, many=True).data
        return Response(serializer)


class OnlySaveWorkorder(View):
    def get(self, request, *args, **kwargs):
        username = request.user.username
        data = execsys(username)
        username = data['username']
        description = request.GET['description']
        supervisor = request.GET['supervisor']
        date = datetime.now().strftime("%Y%m%d%H%M")
        centre_code = request.GET['centre_code']
        centre = centre_code
        work_order_id = request.GET['work_order_id']
        wo = save_wo(username, description, supervisor,
                     centre, date, centre_code, work_order_id)
        my_work = Workorder.objects.filter(work_order_id=wo)

        workorder_table = WorkorderTable1(my_work)
        workorder_table.paginate(page=request.GET.get('page', 1), per_page=2)
        RequestConfig(request).configure(workorder_table)

        return render(request, 'beweb/workorder/notification.html', {'workorder_table': workorder_table})

    def post(self, request, *args, **kwargs):
        return HttpResponse('Are you sure you want to save data')


def editwork(request):
    work_order_id = request.GET.get('q', '')
    username = request.user.username
    usr, tkn = user_authenticate(username)
    headers = {'Authorization': "Token "+tkn +
               "", "Content-Type": "application/json"}

    url = "http://172.20.0.70:8087/beapi/single/workorder/" + work_order_id+"/"
    r = requests.get(url=url, headers=headers)
    data = r.json()
    num_jobs = len(data[0]['jobs'])
    context = {
        "workorder": data[0],
        "number_of_jobs": num_jobs
    }
    return render(request, 'beweb/workorder/workorder_edit.html', context)


class SaveEditedWorkorder(View):
    def get(self, request, *args, **kwargs):
        wo = request.GET['work_order_id']
        description = request.GET['description']
        username = request.user.username
        usr, tkn = user_authenticate(username)
        url = 'http://172.20.0.70:8087/beapi/workorderpatch/'+wo
        headers = {'Authorization': "Token "+tkn +
                   "", 'Content-Type': 'application/json'}
        data = {
            "description": description
        }
        data = json.dumps(data)
        r = requests.patch(url=url, data=data, headers=headers)
        response_data = r.json()
        url = "http://172.20.0.70:8087/beapi/single/workorder/" + wo
        rs = requests.get(url=url, headers=headers)
        data1 = rs.json()
        num_jobs = len(data1[0]['jobs'])
        context = {
            "workorder": data1[0],
            "number_of_jobs": num_jobs
        }
        return render(request, 'beweb/workorder/workorder_view.html', context)


def Job_workflow(request):
    job_id = request.GET.get('job_id', '')
    username = request.user.username
    status = request.GET.get('status', 0)
    opt = request.GET.get('opt', '0')
    wkf_id = 0
    decision = request.GET.get('decision', '0')
    apv = 1
    if decision == "8":
        apv = -1

    comments = request.GET.get('comments', '')
    actioner, tkn = user_authenticate(username)
    job_workflow = Jobworkflow.objects.filter(
        job=job_id).values("workflow_id")[0]['workflow_id']
    job_workflow_id = Jobworkflow.objects.filter(
        job=job_id, action=None).values("job_workflow_id")[0]['job_workflow_id']
    jobworkflow = Jobworkflow.objects.filter(job_workflow_id=job_workflow_id).select_related(
        'workflow').values('workflow__workflow_code', 'workflow__step').first()
    step = jobworkflow['workflow__step']
    next_step = step + apv
    workflow_cd = jobworkflow['workflow__workflow_code']
    workflowid = Workflow.objects.filter(
        workflow_code=workflow_cd, step=next_step).values('workflow_id').first()
    if workflowid:
        wkf_id = workflowid['workflow_id']

    jobworkflowpatch_url = 'http://172.20.0.70:8087/beapi/jobworkflowpatch/'+job_workflow_id
    headers = {'Authorization': "Token "+tkn +
               "", 'Content-Type': 'application/json'}
    data = {
        "ec_num": actioner,
        "action": decision,
        "action_dt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "comments": comments
    }
    data = json.dumps(data)

    r = requests.patch(url=jobworkflowpatch_url, data=data, headers=headers)
    response_data = r.json()

    url = "http://172.20.0.70:8087/beapi/jobworkflowpost"
    data = {
        "workflow": wkf_id,
        "job_workflow_id": "jwf" + datetime.now().strftime("%Y%m%d%H%M") + str(random.randrange(000000, 100000)),
        "job": job_id,
        "created_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data = json.dumps(data)

    if wkf_id > 0:
        r = requests.post(url=url, data=data, headers=headers)
        response_data = r.json()

    data = execsys(request.user.username)
    section = data['section']
    jobupdate_url = 'http://172.20.0.70:8087/beapi/jobupdate/'+job_id
    jobupdate_data = {"status": decision}
    jobupdate_data = json.dumps(jobupdate_data)
    jobupdate_r = requests.patch(
        url=jobupdate_url, data=jobupdate_data, headers=headers)
    jobupdate_response_data = jobupdate_r.json()
    return render(request, 'beweb/reports/mywork.html', {"section": section})


def myjobs(request):
    usr, tkn = user_authenticate(request.user.username)
    headers = {'Authorization': "Token "+tkn +
               "", 'Content-Type': 'application/json'}
    url = "http://172.20.0.70:8087/beapi/job/awaiting/action/"+usr
    rs = requests.get(url=url, headers=headers)
    jobsdata = rs.json()
    data = execsys(request.user.username)
    section = data['section']
    jobs_records = []
    for job in jobsdata:
        job_id = job["job_id"]
        approve = job["approve"]
        role_name = job["role_name"]
        url1 = "http://172.20.0.70:8087/beapi/job/" + job_id+"/"
        r = requests.get(url=url1, headers=headers)
        jobdata = r.json()
        assignee = jobdata[0]['assignee']
        description = jobdata[0]['description']
        data = execsys(assignee)
        artisan = data['surname']+" "+data['firstname']
        jobs_records.append({"job_id": job_id, "approve": approve, "artisan": artisan,
                             "description": description, "nextaction": role_name})
    return render(request, 'beweb/reports/mywork.html', {'data': jobs_records, "section": section})

def reports(request):
    data = execsys(request.user.username)
    centre_code = data['section']
    username = data['username']
    centre, centre_code = get_center(centre_code)
    centres = all_centres()
    job_type= JobType.objects.filter(type='Line Inspection').values("job_type_id","type")
    return render(request,'beweb/reports/reports.html',{'centre': centre, 'centre_code': centre_code, 'centres': centres,'job_type':job_type})



