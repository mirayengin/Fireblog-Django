from django.urls import path
from .views import ProductMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", ProductMVS)
# router.register("/profile/", )

urlpatterns = [
    
]
urlpatterns += router.urls