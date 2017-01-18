from django.db import models
from django.utils.translation import pgettext_lazy, ugettext_lazy as _
from django.conf import settings
from decimal import Decimal


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


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
    # date_created = models.DateField(_("Date Added"), auto_now_add=True, blank=True, null=True)

    birthday = models.DateField(_('Birthday'), blank=True, null=True)
    SEX = (
        (None, '-----'),
        ('1', _('Male')),
        ('2', _('Female')),
    )
    sex = models.CharField(_('Sex'), choices=SEX, max_length=2, blank=True)
    user_photo = models.ImageField(_('Pilot profile image'), upload_to='pilots/', blank=True)
    address = models.CharField(_("Pilot address"), max_length=255, blank=True)
    contact_info = models.TextField(_('Pilot contact information'))
    description = models.TextField(_('Main description'), blank=True)

    area = models.CharField(_('Area of responsibility'), max_length=256, blank=True)
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
    sensor_type = models.CharField(_('Sensor type'), blank=True, max_length=256, help_text='RGB, NGB, NRB, lidar, etc')
    category = models.ManyToManyField(Category, verbose_name=_('Category'),
                                      related_name='pilots', blank=True)
    price = models.CharField(_('Pricing'), max_length=256, help_text='price per Ha/Hour, Min Order', blank=True)

    rating = models.FloatField(_('Rating'), null=True, editable=False)

    status = models.CharField(_("Status"), max_length=100, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    birthday = models.DateField(_('Birthday'), blank=True, null=True)
    SEX = (
        (None, '-----'),
        ('1', _('Male')),
        ('2', _('Female')),
    )
    sex = models.CharField(_('Sex'), choices=SEX, max_length=2, blank=True)
    # date_created = models.DateField(_("Date Added"), auto_now_add=True, blank=True, null=True)

    address = models.CharField(_("Client address"), max_length=255, blank=True)
    contact_info = models.TextField(_('Client contact information'))
    user_photo = models.ImageField(_('Client profile image'), upload_to='pilots/', blank=True)

    # status = models.CharField()

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')


class Order(models.Model):
    title = models.CharField(_('Order title'), max_length=256)

    url = models.SlugField(_('URL'), max_length=256)
    description = models.TextField(_('Main description'), blank=True)

    budget = models.DecimalField(_('Budget'), decimal_places=2, max_digits=12, default=Decimal('0.00'))

    status = models.CharField(_('Status'), max_length=100)  # !!!

    sensor_type = models.CharField(_('Sensor type'), max_length=100, blank=True, help_text='RGB, NGB, NRB, lidar, etc')

    address = models.CharField(_("Client address"), max_length=255, blank=True)

    shape_on_map = models.CharField(_('Shape on map'), max_length=100)  # !!!

    date_created = models.DateField(_('Creating date'), auto_now_add=True, blank=True, null=True)

    date_start = models.DateField(_('Start date'), blank=True, null=True)
    date_finish = models.DateField(_('Finish date'), blank=True, null=True)

    category = models.ManyToManyField(Category, verbose_name=_('Category'),
                                      related_name='category_orders', blank=True)

    pilot = models.ForeignKey(PilotProfile, verbose_name=_('Pilot'), related_name='pilot_orders')
    client = models.ForeignKey(ClientProfile, verbose_name=_('Client'), related_name='client_orders')

    class Meta:
        ordering = ('title',)
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')


class Delivery(models.Model):
    description = models.TextField(_('Description'), blank=True)

    pilot = models.ForeignKey(PilotProfile, verbose_name=_('Pilot'))
    client = models.ForeignKey(ClientProfile, verbose_name=_('Client'))
    order = models.ForeignKey(Order, verbose_name=_('Order'))

    data = models.TextField(_('Data'))

    date_created = models.DateField(_('Creating date'), auto_now_add=True, blank=True, null=True)

    delivered = models.BooleanField(_('Is delivered?'), default=False)

    class Meta:
        verbose_name = _('Delivery')
        verbose_name_plural = _('Deliveries')
