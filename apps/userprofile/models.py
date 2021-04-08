from django.db import models
from django.contrib.auth.models import User
from apps.job.models import Application
from PIL import Image

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username} Userprofile'

    def save(self, *args, **kwargs):
        super(Userprofile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])
    


class ConversationMessage(models.Model):
    application = models.ForeignKey(Application, related_name='conversationmessages', on_delete=models.CASCADE) 
    content = models.TextField()

    created_by = models.ForeignKey(User, related_name='conversationmessages', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']


