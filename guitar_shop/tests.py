from django.test import TestCase
from .models import Guitar

class GuitarModelTest(TestCase):
    def setUp(self):
        # create a Guitar object with valid data
        self.valid_guitar = Guitar.objects.create(
            gid=1, name="Fender Stratocaster", color="Sunburst",
            isElectric=True, price=1000.0
        )  

    def test_creation(self):
        # check that the valid Guitar object was saved successfully
        guitar = Guitar.objects.get(gid=1)
        self.assertEqual(guitar.name, "Fender Stratocaster")    #Check if the name is the good one
        self.assertEqual(guitar.color, "Sunburst")              #Same with the color
        self.assertTrue(guitar.isElectric) 
        self.assertEqual(guitar.price, 1000.0)

    def test_gid_error(self):
        # create a Guitar object with the same gid as the valid guitar
        with self.assertRaises(Exception) as context:
            Guitar.objects.create(
                gid=1, name="Gibson Les Paul", color="Cherry",
                isElectric=True, price=2000.0
            )
        self.assertIn('Duplicate entry', str(context.exception))    #Check if the system throws the good exception

    def test_invalid_creation(self):
        # create a Guitar object with invalid data
        with self.assertRaises(Exception) as context:
            Guitar.objects.create(
                gid=2, name="", color="Red",
                isElectric="Yes", price="Invalid Price"
            )
        self.assertIn('value must be either True or False', str(context.exception)) #Check if the system throws the good exception

    def test__update(self):
        # update the valid Guitar object with new data
        self.valid_guitar.color = "Black"
        self.valid_guitar.price = 1500.0
        self.valid_guitar.save()

        # check that the update was successful
        guitar = Guitar.objects.get(gid=1)
        self.assertEqual(guitar.color, "Black")
        self.assertEqual(guitar.price, 1500.0)

    def test_guitar_deletion(self):
        # delete the valid Guitar object
        self.valid_guitar.delete()

        # check that the deletion was successful
        with self.assertRaises(Guitar.DoesNotExist):
            Guitar.objects.get(gid=1)
