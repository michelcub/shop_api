from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls), path("api/", include("user.api.urls")),
    path("api/", include('product.urls'))

]
