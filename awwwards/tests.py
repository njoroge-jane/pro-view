from django.test import TestCase

# Create your tests here.
from .models import Image,Profile


class TestImage(TestCase):
  def setUp(self):
    self.profile=Profile(user=self.user,bio='home is best',avatar='image.jpg')
    self.image=Image(title='home',image='image.jpg',profile=self.profile,caption='Eat or Sleep')


  def test_instance(self):
    self.assertTrue(isinstance(self.image,Image))


  def test_save_image(self):
    self.profile.save_profile()
    self.image.save_image()

    self.assertTrue(len(Image.objects.all())==1)


  def test_delete_image(self):
    self.profile.save_profile()
    self.image.save_image()

    self.image_to_delete=Image.objects.filter(caption='Eat or Sleep').first()
    self.image_to_delete.delete_image()
    self.assertTrue(len(Image.objects.all())==0)