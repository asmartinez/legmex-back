from django.urls import path
from .views import PersonaList
from .views import Login,Logout

urlpatterns = [
    path('persona/',PersonaList.as_view(), name = 'persona_list'),
    path('login/',Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view()),
]
