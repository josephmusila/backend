from django.urls import path
from . import apis


urlpatterns = [
    path("register/",apis.RegisterApi.as_view(),name="register"),
    path("login/",apis.login,name="login"),
    path("user/<search>",apis.UserApi.as_view(),name="user"),
    path("logout/",apis.LogoutApi.as_view(),name="logout"),
    path('search/<search>',apis.SearchResultWorker.as_view(),),
    # path("test/<search>",apis.Muser,name="test"),
    path("image/",apis.AddImage.as_view(),name="image"),
    path("listImage/",apis.imagesList,name="listImages"),
    path("notifications/<id>",apis.NotificationsView.as_view(),name="notifications"),

    # job request urls

    path("workerRequest/",apis.Req.as_view(),name="request-worker"),
    path("request_status/<requested_by>",apis.GetRequestForService.as_view(),name="request_status"),


    #payment gateways

    # path("payments/mpesa",apis.getAccessToken,name="mpesa"),
    # path('payments/pay', apis.lipa_na_mpesa_online, name='lipa_na_mpesa'),


    # # customer to business urls
    # path('c2b/register', apis.register_urls, name="register_mpesa_validation"),
    # path('c2b/confirmation', apis.confirmation, name="confirmation"),
    # path('c2b/validation', apis.validation, name="validation"),
    # path('c2b/callback', apis.call_back, name="call_back"),
    

    # path("users/account=<str:email>/",apis.GetUser.as_view(),name="custuser"),
    path('logged/', apis.LoggedInUserView.as_view())
]
                                                                                                                                                                                                                 