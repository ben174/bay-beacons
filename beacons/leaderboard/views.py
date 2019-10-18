from django.shortcuts import render, get_object_or_404

from beacons.models import Beacon, Touch


def touch(request, key):
    beacon = get_object_or_404(Beacon, key=key)
    Touch.objects.create(beacon=beacon)
