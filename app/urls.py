
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from .views import change_password

urlpatterns = [
    path("",views.index,name='index'),
    path("index/",views.index,name='index'),
    path("base/",views.base),
    path("about/",views.about),
    path("contactus/", views.contact_view),
    path("category/<slug:val>",views.categoryview.as_view(),name="categoryy"),
    path("category/<val>",views.Categorytitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>",views.productdetail.as_view(),name="product-detail"),
    path('signup/', views.signup, name='signup'),
    path("login/", views.CustomLoginView, name='login'),
    path("change_password/",views.change_password,name="change_password"),
    path('password_change_done/', views.password_change_done, name='password_change_done'),
    path("logout",views.Logout_View,name='Logout_View'),

    # Other URL patterns

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)