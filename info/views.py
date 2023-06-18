from django.db.models import Q
from django.shortcuts import render
from .models import ClubMember, Region, Settlement
from django.contrib.auth.models import User
import random, string
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def main_page(request, name="Аліно", color=""):
    return render(request, 'info/main_page.html', {'name': name, 'color': color})

def couples(request):
    return render(request, 'info/couples.html')

@login_required(login_url='/accounts/login/')
def forum(request):
    return render(request, 'info/forum.html')

def applications_display(request):
    club_members = ClubMember.objects.all()
    users = User.objects.all()
    return render(request, 'info/applications_display.html', {'club_members': club_members, 'users': users})

def accepted(request):
    return render(request, 'info/accepted.html')
def apply(request):
    regions = Region.objects.order_by('title').all()
    settlements = []
    return render(request, 'info/apply.html', {'regions': regions, 'settlements': settlements})


def search(request):
    query = request.GET.get('query')

    search_results = ClubMember.objects.filter(
        Q(user__last_name__icontains=query) | Q(user__first_name__icontains=query))

    results = []
    for cm in search_results:
        results.append({
            'is_accepted': cm.is_accepted,
            'last_name': cm.user.last_name,
            'first_name': cm.user.first_name,
            'patronymic': cm.patronymic,
            'birthday': cm.birthday,
            'gender': cm.gender,
            'region': cm.settlement.region,
            'settlement': cm.settlement,
            'email': cm.user.email,
            'education': cm.education,
        })

    return JsonResponse(results, safe=False)
def get_settlements(request):
    region_id = request.GET.get('region_id')
    settlements = Settlement.objects.filter(region__id=region_id).order_by('title').values('id', 'title')
    return JsonResponse(list(settlements), safe=False)


def create_club_member(request):
    if request.method == 'GET':
        return render(request, 'info/applications_display.html')
    if request.method == 'POST':
        email = request.POST["email"]
        '''if User.objects.filter(email=email).exists():
            messages.error(request, 'Користувач з таким email вже існує.')
            return redirect('info/apply.html')'''  # Перенаправление обратно на страницу с формой
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        patronymic = request.POST["patronymic"]
        birthday = request.POST["birthday"]
        gender = request.POST["gender"]
        nationality = request.POST["nationality"]
        region_id = request.POST['region']
        region = Region.objects.get(id=region_id)
        settlement_id = request.POST['settlement']
        settlement = Settlement.objects.get(id=settlement_id)
        phone_number = request.POST["phone_number"]
        '''if not re.match(r'^(\+\d{1,2})?[- ]?\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{2})[- ]?(\d{2})$', phone_number):
            phone_number = None'''
        education = request.POST["education"]
        activity_field = request.POST["activity_field"]
        hobby = request.POST["hobby"]
        pets = request.POST["pets"]
        favorite_holiday = request.POST["favorite_holiday"]
        favorite_color = request.POST["favorite_color"]
        favorite_dish = request.POST["favorite_dish"]
        favorite_drink = request.POST["favorite_drink"]
        favorite_musician = request.POST["favorite_musician"]
        favorite_actor = request.POST["favorite_actor"]
        favorite_book = request.POST["favorite_book"]
        favorite_movie = request.POST["favorite_movie"]
        appreciate_in_people = request.POST["appreciate_in_people"]
        repulsive_in_people = request.POST["repulsive_in_people"]

        user = User(username=email, password=make_password(generate_password(8)), first_name=first_name, last_name=last_name, email=email)
        user.save()

        club_member = ClubMember(user=user, patronymic=patronymic, birthday=birthday, gender=gender,
                                 nationality=nationality, settlement=settlement,
                                 phone_number=phone_number,
                                 education=education, activity_field=activity_field, hobby=hobby, pets=pets,
                                 favorite_holiday=favorite_holiday, favorite_color=favorite_color,
                                 favorite_dish=favorite_dish,
                                 favorite_drink=favorite_drink, favorite_musician=favorite_musician,
                                 favorite_actor=favorite_actor,
                                 favorite_book=favorite_book, favorite_movie=favorite_movie,
                                 appreciate_in_people=appreciate_in_people, repulsive_in_people=repulsive_in_people)
        club_member.save()
        club_members = ClubMember.objects.order_by('id')

        return render(request, 'info/accepted.html',  {'club_members':club_members, 'password': generate_password(8)})

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password





