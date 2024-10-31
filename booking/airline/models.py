from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_full_profile_info(self):
        """Возвращает полную информацию о профиле."""
        return {
            'username': self.user.username,
            'bio': self.bio,
            'location': self.location,
            'image_url': self.image.url if self.image else None,
        }

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
