"""
URL configuration for navegabit_back project.

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
from django.contrib import admin
from django.urls import path, include
from card.urls import cards_patterns
from home.urls import menu_patterns
from translate.urls import translate_patterns
from django.conf import settings
from django.conf.urls.static import static
from userprofile.urls import userprofile_patterns
urlpatterns = [
    path('cards/', include(cards_patterns.urls)),
    path('home/', include(menu_patterns.urls)),
    path('translate/', include(translate_patterns.urls)),
    path('translate_patterns/', include(translate_patterns.urls)),
    path('admin/', admin.site.urls),
    path('', include("admin_volt.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)