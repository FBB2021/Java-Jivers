from email.mime.multipart import MIMEMultipart
from sqlite3 import DatabaseError
from uuid import UUID
from django.shortcuts import render
from Login.models import User
from Login.serializers import UserSerializer
# csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# viewsets
from rest_framework import viewsets, status
from rest_framework.response import Response

# hashing raw user instance password
from django.contrib.auth.hashers import make_password

# allow upload file
from django.core.files.storage import default_storage
# The IsAdminUser permission class will deny permission to any user,
# unless user.is_staff is True in which case permission will be allowed.
from rest_framework.permissions import IsAuthenticated
# send email
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import ssl

from django.db.models import Q

import sys
sys.path.append("..")
from inventorySystem import settings


@csrf_exempt
def userApi(request, id=0):
    # get all the user
    if request.method=='GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data,safe=False)
    
    # add user
    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        print(user_serializer.errors)
        return JsonResponse("Failed to add", safe = False)

    # edit user's data
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(UserId = user_data['UserId'])
        user_serializer = UserSerializer(user, data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        return JsonResponse("Failed to update", safe = False)

    # delete user through UserId, not the objectId
    elif request.method=='DELETE':
        user = User.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Delete Successfully", safe = False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name, safe=False)

@csrf_exempt
def userSearch(request, username):
    if request.method=='GET':
        user = User.objects.filter(Q(username__contains=username) | Q(username__icontains=username))
        user_serializer = UserSerializer(user, many=True)
    return JsonResponse(user_serializer.data,safe=False) 


class UserViewSet(viewsets.ModelViewSet):
    # ModelViewSet provided support for 'get', 'put', 'post' and 'delete'
    # However User cannot be added through this way for security regulations
    # of rest_framework.
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        name = self.request.query_params.get('name', None)
        print(name)
        if name is not None:
            queryset = queryset.filter(Q(username__contains=name) | Q(username__icontains=name))
        return queryset

    # for cases an user to create another user
    def create(self, request, *args, **kwargs):
        username = request.data['username']
        pwd_raw = request.data['password']
        email = request.data['email']

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response("A user with that username already exists.", \
                status=status.HTTP_406_NOT_ACCEPTABLE)


        # create user_info as a User typed instence of serializer
        user_info = User(serializer)
        user_info.username = username
        user_info.set_password(pwd_raw)
        user_info.is_active = "True"
        user_info.email = email
        # Uncomment the below if wanna login with this instance in Django Admin
        #user_info.is_superuser = "True" 
        user_info.is_staff = "True"

        self.perform_create(user_info)
        user_info.save()
        
        headers = self.get_success_headers(user_info)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def update(self, request, *args, **kwargs):
        username = request.data['username']
        pwd_raw = request.data['password']
        pwd_hashed = make_password(pwd_raw)
        request.data['password'] = pwd_hashed

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class UserCreateViewSet(viewsets.ModelViewSet):
    # this class is for user sign up without any login.
    permission_classes = []
    http_method_names = ['post','get']
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        feedback = "Have you forgot login to the system?"
        return Response(feedback, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        instance = User.objects.get(UUID=kwargs['pk'])
        instance.is_active = True
        instance.save()
        data = {
            'status': 'Fantastic, your account is now activated :)',
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        username = request.data['username']
        pwd_raw = request.data['password']
        email = request.data['email']

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response("A user with that username already exists.", \
                status=status.HTTP_406_NOT_ACCEPTABLE)


        # create user_info as a User typed instence of serializer
        user_info = User(serializer)
        user_info.username = username
        user_info.set_password(pwd_raw)
        user_info.is_superuser= "False"
        user_info.is_active = "False" # waiting for email authentication
        # can only create general user by this method by safety concerns
        # modify role of this instance by another admin user
        user_info.role = "General" 
        # Uncomment the below if wanna login with this instance in Django Admin
        #user_info.is_superuser = "True" 
        user_info.email = email

        self.perform_create(user_info)
        user_info.save()
        
        uuid = user_info.UUID

        #print(f"here the url: {uuid} \n")

        url = request.build_absolute_uri(uuid)
        '''
        result = send_mail(
            subject = "Activation_JavaJivers Warehouse System", # subject
            message = f"Hi, please click on the following link to activate your account: {url}",
            from_email = settings.EMAIL_HOST_USER,
            #recipient_list = [user_info.email],
            recipient_list=[user_info.email],
            fail_silently = False,
        )

        print(f"sending result {result}")
        '''
        
        html_text = '''<!doctype html><html ⚡4email data-css-strict><head><meta charset="utf-8"><style amp4email-boilerplate>body{visibility:hidden}</style><script async src="https://cdn.ampproject.org/v0.js"></script><style amp-custom>.es-desk-hidden { display:none; float:left; overflow:hidden; width:0; max-height:0; line-height:0;}body { width:100%; font-family:arial, "helvetica neue", helvetica, sans-serif;}table { border-collapse:collapse; border-spacing:0px;}table td, body, .es-wrapper { padding:0; Margin:0;}.es-content, .es-header, .es-footer { table-layout:fixed; width:100%;}p, hr { Margin:0;}h1, h2, h3, h4, h5 { Margin:0; line-height:120%; font-family:arial, "helvetica neue", helvetica, sans-serif;}.es-left { float:left;}.es-right { float:right;}.es-p5 { padding:5px;}.es-p5t { padding-top:5px;}.es-p5b { padding-bottom:5px;}.es-p5l { padding-left:5px;}.es-p5r { padding-right:5px;}.es-p10 { padding:10px;}.es-p10t { padding-top:10px;}.es-p10b { padding-bottom:10px;}.es-p10l { padding-left:10px;}.es-p10r { padding-right:10px;}.es-p15 { padding:15px;}.es-p15t { padding-top:15px;}.es-p15b { padding-bottom:15px;}.es-p15l { padding-left:15px;}.es-p15r { padding-right:15px;}.es-p20 { padding:20px;}.es-p20t { padding-top:20px;}.es-p20b { padding-bottom:20px;}.es-p20l { padding-left:20px;}.es-p20r { padding-right:20px;}.es-p25 { padding:25px;}.es-p25t { padding-top:25px;}.es-p25b { padding-bottom:25px;}.es-p25l { padding-left:25px;}.es-p25r { padding-right:25px;}.es-p30 { padding:30px;}.es-p30t { padding-top:30px;}.es-p30b { padding-bottom:30px;}.es-p30l { padding-left:30px;}.es-p30r { padding-right:30px;}.es-p35 { padding:35px;}.es-p35t { padding-top:35px;}.es-p35b { padding-bottom:35px;}.es-p35l { padding-left:35px;}.es-p35r { padding-right:35px;}.es-p40 { padding:40px;}.es-p40t { padding-top:40px;}.es-p40b { padding-bottom:40px;}.es-p40l { padding-left:40px;}.es-p40r { padding-right:40px;}.es-menu td { border:0;}s { text-decoration:line-through;}p, ul li, ol li { font-family:arial, "helvetica neue", helvetica, sans-serif; line-height:150%;}ul li, ol li { Margin-bottom:15px; margin-left:0;}a { text-decoration:underline;}.es-menu td a { text-decoration:none; display:block; font-family:arial, "helvetica neue", helvetica, sans-serif;}.es-menu amp-img, .es-button amp-img { vertical-align:middle;}.es-wrapper { width:100%; height:100%;}.es-wrapper-color, .es-wrapper { background-color:#FAFAFA;}.es-header { background-color:transparent;}.es-header-body { background-color:transparent;}.es-header-body p, .es-header-body ul li, .es-header-body ol li { color:#333333; font-size:14px;}.es-header-body a { color:#666666; font-size:14px;}.es-content-body { background-color:#FFFFFF;}.es-content-body p, .es-content-body ul li, .es-content-body ol li { color:#333333; font-size:14px;}.es-content-body a { color:#5C68E2; font-size:14px;}.es-footer { background-color:transparent;}.es-footer-body { background-color:#FFFFFF;}.es-footer-body p, .es-footer-body ul li, .es-footer-body ol li { color:#333333; font-size:12px;}.es-footer-body a { color:#333333; font-size:12px;}.es-infoblock, .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li { line-height:120%; font-size:12px; color:#CCCCCC;}.es-infoblock a { font-size:12px; color:#CCCCCC;}h1 { font-size:46px; font-style:normal; font-weight:bold; color:#333333;}h2 { font-size:26px; font-style:normal; font-weight:bold; color:#333333;}h3 { font-size:20px; font-style:normal; font-weight:bold; color:#333333;}.es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:46px;}.es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:26px;}.es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px;}a.es-button, button.es-button { border-style:solid; border-color:#5C68E2; border-width:10px 30px 10px 30px; display:inline-block; background:#5C68E2; border-radius:0px; font-size:20px; font-family:arial, "helvetica neue", helvetica, sans-serif; font-weight:normal; font-style:normal; line-height:120%; color:#FFFFFF; text-decoration:none; width:auto; text-align:center;}.es-button-border { border-style:solid solid solid solid; border-color:#2CB543 #2CB543 #2CB543 #2CB543; background:#5C68E2; border-width:0px 0px 0px 0px; display:inline-block; border-radius:0px; width:auto;}body { font-family:arial, "helvetica neue", helvetica, sans-serif;}@media only screen and (max-width:600px) {p, ul li, ol li, a { line-height:150% } h1, h2, h3, h1 a, h2 a, h3 a { line-height:120% } h1 { font-size:36px; text-align:left } h2 { font-size:26px; text-align:left } h3 { font-size:20px; text-align:left } .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:36px; text-align:left } .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:26px; text-align:left } .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px; text-align:left } .es-menu td a { font-size:12px } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:14px } .es-content-body p, .es-content-body ul li, .es-content-body ol li, .es-content-body a { font-size:16px } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:14px } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px } *[class="gmail-fix"] { display:none } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left } .es-m-txt-r amp-img { float:right } .es-m-txt-c amp-img { margin:0 auto } .es-m-txt-l amp-img { float:left } .es-button-border { display:inline-block } a.es-button, button.es-button { font-size:20px; display:inline-block } .es-adaptive table, .es-left, .es-right { width:100% } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%; max-width:600px } .es-adapt-td { display:block; width:100% } .adapt-img { width:100%; height:auto } td.es-m-p0 { padding:0 } td.es-m-p0r { padding-right:0 } td.es-m-p0l { padding-left:0 } td.es-m-p0t { padding-top:0 } td.es-m-p0b { padding-bottom:0 } td.es-m-p20b { padding-bottom:20px } .es-mobile-hidden, .es-hidden { display:none } tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden { width:auto; overflow:visible; float:none; max-height:inherit; line-height:inherit } tr.es-desk-hidden { display:table-row } table.es-desk-hidden { display:table } td.es-desk-menu-hidden { display:table-cell } .es-menu td { width:1% } table.es-table-not-adapt, .esd-block-html table { width:auto } table.es-social { display:inline-block } table.es-social td { display:inline-block } td.es-m-p5 { padding:5px } td.es-m-p5t { padding-top:5px } td.es-m-p5b { padding-bottom:5px } td.es-m-p5r { padding-right:5px } td.es-m-p5l { padding-left:5px } td.es-m-p10 { padding:10px } td.es-m-p10t { padding-top:10px } td.es-m-p10b { padding-bottom:10px } td.es-m-p10r { padding-right:10px } td.es-m-p10l { padding-left:10px } td.es-m-p15 { padding:15px } td.es-m-p15t { padding-top:15px } td.es-m-p15b { padding-bottom:15px } td.es-m-p15r { padding-right:15px } td.es-m-p15l { padding-left:15px } td.es-m-p20 { padding:20px } td.es-m-p20t { padding-top:20px } td.es-m-p20r { padding-right:20px } td.es-m-p20l { padding-left:20px } td.es-m-p25 { padding:25px } td.es-m-p25t { padding-top:25px } td.es-m-p25b { padding-bottom:25px } td.es-m-p25r { padding-right:25px } td.es-m-p25l { padding-left:25px } td.es-m-p30 { padding:30px } td.es-m-p30t { padding-top:30px } td.es-m-p30b { padding-bottom:30px } td.es-m-p30r { padding-right:30px } td.es-m-p30l { padding-left:30px } td.es-m-p35 { padding:35px } td.es-m-p35t { padding-top:35px } td.es-m-p35b { padding-bottom:35px } td.es-m-p35r { padding-right:35px } td.es-m-p35l { padding-left:35px } td.es-m-p40 { padding:40px } td.es-m-p40t { padding-top:40px } td.es-m-p40b { padding-bottom:40px } td.es-m-p40r { padding-right:40px } td.es-m-p40l { padding-left:40px } .es-desk-hidden { display:table-row; width:auto; overflow:visible; max-height:inherit } }</style></head>
<body><div class="es-wrapper-color"> <!--[if gte mso 9]><v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"> <v:fill type="tile" color="#fafafa"></v:fill> </v:background><![endif]--><table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0"><tr><td valign="top"><table cellpadding="0" cellspacing="0" class="es-content" align="center"><tr><td class="es-info-area" align="center"><table class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: transparent" bgcolor="rgba(0, 0, 0, 0)"><tr><td class="es-p20" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tr><td width="560" align="center" valign="top"><table cellpadding="0" cellspacing="0" width="100%" role="presentation"><tr><td align="center" class="es-infoblock"><p><a target="_blank">View online version</a></p></td></tr></table></td></tr></table></td></tr></table></td>
</tr></table><table cellpadding="0" cellspacing="0" class="es-header" align="center"><tr><td align="center"><table bgcolor="#ffffff" class="es-header-body" align="center" cellpadding="0" cellspacing="0" width="600"><tr><td class="es-p10t es-p10b es-p20r es-p20l" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tr><td width="560" class="es-m-p0r" valign="top" align="center"><table cellpadding="0" cellspacing="0" width="100%"><tr><td align="center" style="display: none"></td></tr></table></td></tr></table></td></tr></table></td>
</tr></table><table cellpadding="0" cellspacing="0" class="es-content" align="center"><tr><td align="center"><table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600"><tr><td class="es-p30t es-p30b es-p20r es-p20l" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tr><td width="560" align="center" valign="top"><table cellpadding="0" cellspacing="0" width="100%" role="presentation"><tr><td align="center" class="es-p10t es-p10b" style="font-size: 0px"><amp-img src="https://zhoecz.stripocdn.email/content/guids/CABINET_67e080d830d87c17802bd9b4fe1c0912/images/55191618237638326.png" alt style="display: block" width="100" height="72"></amp-img></td></tr><tr><td align="center" class="es-p10b es-m-txt-c"><h1 style="font-size: 46px;line-height: 46px">Confirm Your Email</h1></td>
</tr><tr><td align="center" class="es-p5t es-p5b es-p40r es-p40l es-m-p0r es-m-p0l"><p>Hi there, welcome to the Smart House, an inventory management system by JavaJivers&nbsp;:)<br><br>You’ve received this message because your email address has been registered with our site. Please click the button below to verify your email address and confirm that you are the owner of this account.</p></td></tr><tr><td align="center" class="es-p10t es-p5b"><p>If you did not register with us, please disregard this email.</p></td>
</tr><tr><td align="center" class="es-p10t es-p10b"> <!--[if mso]><a href="'''+url+'''" target="_blank" hidden> <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" esdevVmlButton href="'''+url+'''" style="height:44px; v-text-anchor:middle; width:282px" arcsize="14%" stroke="f" fillcolor="#5c68e2"> <w:anchorlock></w:anchorlock> <center style='color:#ffffff; font-family:arial, "helvetica neue", helvetica, sans-serif; font-size:18px; font-weight:400; line-height:18px; mso-text-raise:1px'>CONFIRM YOUR EMAIL</center> </v:roundrect></a><![endif]--> <!--[if !mso]><!-- --><span class="msohide es-button-border" style="border-radius: 6px"><a href="'''+url+'''" class="es-button" target="_blank" style="border-left-width: 30px;border-right-width: 30px;border-radius: 6px">CONFIRM YOUR EMAIL</a></span> <!--<![endif]--></td>
</tr><tr><td align="center" class="es-p5t es-p5b es-p40r es-p40l es-m-p0r es-m-p0l"><p>Once confirmed, this email will be uniquely associated with your account.</p></td></tr></table></td></tr></table></td></tr></table></td></tr></table><table cellpadding="0" cellspacing="0" class="es-footer" align="center"><tr><td align="center"><table class="es-footer-body" align="center" cellpadding="0" cellspacing="0" width="640" style="background-color: transparent"><tr><td class="es-p20t es-p20b es-p20r es-p20l" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tr><td width="600" align="left"><table cellpadding="0" cellspacing="0" width="100%" role="presentation"><tr><td align="center" class="es-p35b"><p>Java Jivers team from IT Project (COMP30022, 2022s2)@Unimelb<br>Address:The University of Melbourne Grattan Street, Parkville,Victoria, 3010, Australia</p></td></tr></table></td></tr></table></td></tr></table></td>
</tr></table><table cellpadding="0" cellspacing="0" class="es-content" align="center"><tr><td class="es-info-area" align="center"><table class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: transparent" bgcolor="rgba(0, 0, 0, 0)"><tr><td class="es-p20" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tr><td width="560" align="center" valign="top"><table cellpadding="0" cellspacing="0" width="100%" role="presentation"><tr><td align="center" class="es-infoblock"><p><a target="_blank"></a>No longer want to receive these emails?&nbsp;<a href target="_blank">Unsubscribe</a>.<a target="_blank"></a></p></td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr></table></div></body></html>'''

        message = MIMEMultipart()
        
        message['From'] = settings.EMAIL_HOST_USER
        message['To'] = user_info.email
        message['Subject'] = 'Activation_JavaJivers Warehouse System'

        message.attach(MIMEText(html_text,"html"))
        email_string = message.as_string()

        context= ssl.create_default_context()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST,465,context=context) as server:
            server.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
            server.sendmail(settings.EMAIL_HOST_USER,user_info.email,email_string)


        headers = self.get_success_headers(user_info)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)