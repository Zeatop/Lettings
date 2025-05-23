from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def profiles_index(request):

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis  dolor id facilisis ,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique


def profile(request, username):

    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
