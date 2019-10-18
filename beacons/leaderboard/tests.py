from django.test import TestCase

from leaderboard.models import Beacon
from django.contrib.auth.models import User


class BeaconTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email='test@test.com')
        user.is_superuser = True
        user.save()
        self.beacon = Beacon.objects.create()

    def test_beacon_generates_a_key(self):
        """Verifies each new beacon object generates a unique key"""

        self.assertEqual(len(self.beacon.key), 10)

    def test_beacon_has_a_default_owner(self):
        self.assertTrue(self.beacon.owner.is_superuser)
