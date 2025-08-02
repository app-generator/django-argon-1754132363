# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Server(models.Model):

    #__Server_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    interface = models.ForeignKey(WireguardInterface, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, null=True, blank=True)
    peers = models.ForeignKey(WireguardPeer, on_delete=models.CASCADE)
    public_key = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Server_FIELDS__END

    class Meta:
        verbose_name        = _("Server")
        verbose_name_plural = _("Server")


class Client(models.Model):

    #__Client_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    interface = models.ForeignKey(WireguardInterface, on_delete=models.CASCADE)
    peer = models.ForeignKey(WireguardPeer, on_delete=models.CASCADE)
    public_key = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_modified = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Client_FIELDS__END

    class Meta:
        verbose_name        = _("Client")
        verbose_name_plural = _("Client")


class Wireguardinterface(models.Model):

    #__Wireguardinterface_FIELDS__
    private_key = models.TextField(max_length=255, null=True, blank=True)
    primary_dns = models.TextField(max_length=255, null=True, blank=True)
    secondary_dns = models.TextField(max_length=255, null=True, blank=True)
    mtu = models.IntegerField(null=True, blank=True)
    table = models.IntegerField(null=True, blank=True)
    listen_port = models.IntegerField(null=True, blank=True)
    ipv4_address = models.CharField(max_length=255, null=True, blank=True)
    ipv6_address = models.CharField(max_length=255, null=True, blank=True)

    #__Wireguardinterface_FIELDS__END

    class Meta:
        verbose_name        = _("Wireguardinterface")
        verbose_name_plural = _("Wireguardinterface")


class Wireguardpeer(models.Model):

    #__Wireguardpeer_FIELDS__
    public_key = models.TextField(max_length=255, null=True, blank=True)
    endpoint = models.CharField(max_length=255, null=True, blank=True)
    allowed_ips = models.TextField(max_length=255, null=True, blank=True)
    persistent_keepalive = models.IntegerField(null=True, blank=True)

    #__Wireguardpeer_FIELDS__END

    class Meta:
        verbose_name        = _("Wireguardpeer")
        verbose_name_plural = _("Wireguardpeer")



#__MODELS__END
