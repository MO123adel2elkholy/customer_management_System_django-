from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.models import Group
    # profile created using user
# @receiver(post_save , sender=User )
def profile_create(sender , instance , created , **kwargs):
    if created :
        group = Group.objects.get(name='customers')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
        )
        print('profile created successfuly ')

post_save.connect(profile_create , sender=User)

# profile updated  using user

# @receiver(post_save , sender=User )
# def profile_update(sender , instance , created , **kwargs):
#     if created ==False:
#         instance.profile.save()
#         print("profile updated successfuly ")

# post_save.connect(profile_create , sender=User)