"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from backend import views
from instructor.views import InstructorViewSet
from student.views import StudentViewSet
from session.views import Sessions

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'instructors/', InstructorViewSet.as_view()),
    path(r'instructors/<int:pk>/', InstructorViewSet.as_view()),
    path(r'students/', StudentViewSet.as_view()),
    path(r'students/<int:pk>/', StudentViewSet.as_view()),
    # path(r'sessions/', Sessions.as_view()),
    # path('sessions/<pk>/', SessionDetail.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)