"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from article.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from contact.views import *


urlpatterns = [
    path("", home__view, name="home"),
    path("admin/", admin.site.urls),
    path("about/", about__view, name="about"),
    path("articles/", articles__view, name="articles"),
    path("dashboard/", dashboard__view, name="dashboard"),
    path("add-article/", addarticle__view, name="add-article"),
    path("update/<int:id>", article__update__view, name="update-article"),
    path("delete/<int:id>", article__delete__view, name="delete-article"),
    path("article-detail/<int:id>", article__detail__view, name="article-detail"),
    path("account/", include("account.urls")),
    # ckeditor config
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("comment/<int:id>", add__comment__view, name="comment"),
    path("comment-del/<int:id>", comment__delete__view, name="comment-delete"),
    path("contact/", contact__page, name="contact"),
    # path("contact/", include("contact.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set-language/<str:language>", set_language, name="set-language"),
]

handler404 = "article.views.custom_404"  # new


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns = [
#     *i18n_patterns(*urlpatterns, prefix_default_language=False),
#     path("set-language/<str:language>", views.set_language, name="set-language"),
# ]
