from django.test import TestCase

from items.models import Armor, BonusModifier
from . import xml_parser


# Create your tests here.
class TestXMLParser(TestCase):

    def setUp(self):
        xml_parser.parse_entities('persistence/testdata/armory_test.xml')

    def test_armory(self):
        armory = Armor.objects.all()
        self.assertIsNotNone(armory.get(name="Adamantine Breastplate"))
        self.assertEqual(2, armory.filter(type="Heavy Armor").count())
        self.assertEqual(1, armory.filter(type="Light Armor").count())
        self.assertEqual(1, armory.filter(type="Medium Armor").count())
        self.assertEqual(2, armory.filter(type="Shield").count())
        self.assertEqual(1, armory.filter(cursed=True).count())
        self.assertEqual(2, armory.filter(requires_attunement=True).count())
        self.assertEqual(2, armory.filter(stealth_disadvantage=True).count())
        self.assertEqual(2, armory.filter(strength_requirement=15).count())
        self.assertEqual(2, armory.filter(weight=65).count())

    def test_bonus_modifier(self):
        ac_mods = BonusModifier.objects.filter(applied_to="ac")
        self.assertEqual(1, ac_mods.count())
        self.assertEqual(2, ac_mods.first().modifier)
