from django.db import models
from django.utils.translation import pgettext_lazy, ugettext_lazy as _
from django.conf import settings


class PilotProfile(models.Model):
    '''
    By default:
    1. Username
    2. Password
    3. Email
    4. First_name
    5. Last_name
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    url = models.SlugField(_('URL'), max_length=256)
    date_created = models.DateTimeField(_("Date Added"), auto_now_add=True)

    birthday = models.DateField(_('Birthday'), blank=True, null=True)
    SEX = (
        (None, '-----'),
        ('1', _('Male')),
        ('2', _('Female')),
    )
    sex = models.CharField(_('Sex'), choices=SEX, max_length=2, blank=True)
    user_photo = models.ImageField(_('Pilot profile image'), upload_to='pilots/', blank=True)
    address = models.CharField(_("Address"), max_length=255, blank=True)
    contact_info = models.TextField(_('Contact information'))
    description = models.TextField(_('Main description'), blank=True)

    area = models.CharField(_('Area of responsibility'), blank=True)
    SCOUTING_TYPES = (
        (None, '-----'),
        ('Video', _('Video')),
        ('Photo', _('Photo')),
        ('LIDAR', _('LIDAR')),
    )
    scout_type = models.CharField(_('Scouting type'), choices=SCOUTING_TYPES, max_length=10, blank=True)
    drone_model = models.CharField(_('Drone model'), max_length=100, blank=True)
    DRONE_TYPES = (
        (None, '-----'),
        ('Plane', _('Plane')),
        ('Copter', _('Copter')),
    )
    drone_type = models.CharField(_('Drone type'), choices=DRONE_TYPES, max_length=10, blank=True)
    sensor_type = models.CharField(_('Sensor type'), blank=True, help_text='RGB, NGB, NRB, lidar, etc')
    category = models.ManyToManyField(Category, verbose_name=_('Category'),
                                      related_name='pilots', blank=True)
    price = models.CharField(_('Pricing'), help_text='price per Ha/Hour, Min Order', blank=True)

    rating = models.FloatField(_('Rating'), null=True, editable=False)

    status = models.CharField(_("Status"), max_length=100, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        ordering = ('name',)
        verbose_name = _('Pilot')
        verbose_name_plural = _('Pilots')


class ClientProfile(models.Model):
    '''
    By default:
    1. Username
    2. Password
    3. Email
    4. First_name
    5. Last_name
    '''
    address = models.CharField(_("Address"), max_length=255, blank=True)
    contact_info = models.TextField(_('Contact information'))
    user_photo = models.ImageField(_('Pilot profile image'), upload_to='pilots/', blank=True)

    # status = models.CharField()

    class Meta:
        ordering = ('name',)
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')


class Order(models.Model):
    name = models.CharField()
    description = models.CharField()
    budget = models.CharField()
    status = models.CharField()
    sensor_type = models.CharField()
    address = models.CharField()
    shape_on_map = models.CharField()

    date_on_add = models.DateField()
    date_start = models.DateField()
    date_finish = models.DateField()

    category = models.ManyToManyField(Category)

    pilot = models.ForeignKey(PilotProfile)
    client = models.ForeignKey(ClientProfile)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')


class Delivery(models.Model):
    description = models.CharField()

    pilot = models.ForeignKey(Pilot)
    client = models.ForeignKey(Client)
    order = models.ForeignKey(Order)

    data = models.CharField()
    date_on_add = models.DateField()
    status = models.CharField()
    # status = models.CharField()


class Category(models.Model):
    name = models.CharField()
    description = models.CharField()
