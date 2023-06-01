from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Області"
        ordering = ['id']
        db_table = "Regions"


class Settlement(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Населений пункт"
        verbose_name_plural = "Населені пункти"
        ordering = ['id']
        db_table = "Settlements"

class ClubMember(models.Model):
    id = models.AutoField(primary_key=True)
    patronymic = models.CharField(max_length=255)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=[('woman', 'Жіноча'), ('man', 'Чоловіча')])
    nationality = models.CharField(max_length=10, choices=[('ukrainian', 'Українська'), ('polish', 'Польська'),
                                                           ('italian', 'Італійська')])
    settlement = models.ForeignKey(Settlement, on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'^(\+\d{1,2})?[- ]?\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{2})[- ]?(\d{2})$',
        message="Номер телефону повинен бути у форматі: '+380123456789' або '096-456-78-90' або '0983456789'."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=20,
        blank=True,
    )
    education = models.CharField(max_length=10, choices=[('higher', 'Вища'), ('average', 'Середня'), ('none', 'Немає')])
    activity_field = models.CharField(max_length=255, blank=True)
    hobby = models.TextField(max_length=500, blank=True)
    pets = models.CharField(max_length=255, blank=True)
    favorite_holiday = models.CharField(max_length=120, blank=True)
    favorite_color = models.CharField(max_length=120, blank=True)
    favorite_dish = models.CharField(max_length=120, blank=True)
    favorite_drink = models.CharField(max_length=120, blank=True)
    favorite_musician = models.CharField(max_length=120, blank=True)
    favorite_actor = models.CharField(max_length=120, blank=True)
    favorite_book = models.CharField(max_length=120, blank=True)
    favorite_movie = models.CharField(max_length=120, blank=True)
    appreciate_in_people = models.TextField(max_length=500, blank=True)
    repulsive_in_people = models.TextField(max_length=500, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Учасник клубу"
        verbose_name_plural = "Учасники клубу"
        ordering = ['id']
        db_table = "Club_members"


class MarriedCouple(models.Model):
    id = models.AutoField(primary_key=True)
    husband = models.ForeignKey(ClubMember, on_delete=models.CASCADE, related_name='couple_as_husband')
    wife = models.ForeignKey(ClubMember, on_delete=models.CASCADE, related_name='couple_as_wife')
    date_marriage = models.DateField()

    def __str__(self):
        return f"{self.husband.user.first_name} {self.husband.user.last_name} - {self.wife.user.first_name} {self.wife.user.last_name}"

    class Meta:
        ordering = ['id']
        verbose_name = "Складена пара"
        verbose_name_plural = "Складені пари"
        db_table = "Married_couples"
