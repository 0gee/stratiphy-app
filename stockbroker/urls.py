"""
URL configuration for stockbroker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# stockbroker/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('stocks.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

#curl -X GET "http://127.0.0.1:8000/api/holdings/" \
#-H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMDQ2MTQ1MCwiaWF0IjoxNzIwMzc1MDUwLCJqdGkiOiJkMDFjNDMyMzlmOTc0ODI2ODQxNTk2YWNhZDliN2JhMCIsInVzZXJfaWQiOjJ9.325omfahtcqK_SBPCLlKwmo0M-XI0lL9LKRrTYQ--Wc","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwMzc1MzUwLCJpYXQiOjE3MjAzNzUwNTAsImp0aSI6ImJiYjUxNDJhYmRmODRiOTRhNzNjN2E1Y2Y3YzY1YTY1IiwidXNlcl9pZCI6Mn0.34wUBlrPFW2M7RJrjus8RxmBgvyDAGtug7S3CL51WjA"
