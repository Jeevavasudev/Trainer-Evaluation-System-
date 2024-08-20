from django.urls import path
from.import views 
from.views import detailfeedback

# from .views import GetFeedbackView, SuccessView
urlpatterns = [
    path('',views.index),
    path('accounts/login/',views.loginview,name='login'),
    path('trainerlogin',views.trainerlogin,name='trainerlogin'),
    path('home',views.home,name='home'),
    path('logout',views.logout_view),
    # path('reset',views.Resethome, name="Reset"),
    # path('passwordreset',views.resetPassword),
    path('accounts/signup/',views.sign_up,name="signup"),
    path('trainersignuphome',views.trainerhome,name='trainersignuphome'),
    path('trainersignup',views.trainersign_up),
    path('feedback',views.feedback,name='feedback'),
    path('feedbackdetail',views.detailfeedback,name='submit-form'),
    path('deletefeedback/<int:fid>',views.deletefeedback,name='delete'),
    # path('updatefeedback',views.updatefeedback,name='update'),
    path('feedbacklistview',views.feedbacklistview,name='feedbacklistview'),
    # path('submit-form',views.submit_form ,name='submit-form'),
    # path('display',views.display),
    
   
    # path('feedback', GetFeedbackView.as_view(), name='GetFeedbackView'),
    # path('success/',SuccessView.as_view(), name='SuccessView')
    
]
