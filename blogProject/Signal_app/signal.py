from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_save

from django.contrib.auth.models import User
from Auth_app.models import Contact
from django.dispatch import receiver



#reciever function
def login_success(sender,request,user,**kwargs):
    print("User Logged In singal")
    print("Sender",sender)
    print("Request",request)
    print("User",user)
    print("kwargs",kwargs)
    # write logic to send email
    
#connecting the signal to the receiver function
user_logged_in.connect(login_success,sender=User) #method 1



@receiver(user_logged_out,sender=User) #method 2
def log_out_receiver(sender,request,user,**kwargs):
    print("--------------User Logged Out singal--------------------")
    print("Sender",sender)
    print("Request",request)
    print("User",user)
    print("kwargs",kwargs)


@receiver(pre_save,sender=Contact) 
def pre_save_signal(sender,instance,**kwargs):
    print("--------------User Pre Save singal--------------------")
    print("Sender",sender)
    print("kwargs",kwargs)
