
from datetime import datetime

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from PIL import Image as PILImage, Image
from io import StringIO,BytesIO
import sys

# Create your models here.
from django.forms import CharField


# _sessions = (
#     ('2005-06', '2005-06'),
#     ('2006-07', '2006-07'),
#     ('2007-08', '2007-08'),
#     ('2008-09', '2008-09'),
#     ('2009-10', '2009-10'),
#     ('2010-11', '2010-11'),
#     ('2011-12', '2011-12'),
#     ('2012-13', '2012-13'),
#     ('2013-14', '2013-14'),
#     ('2014-15', '2014-15'),
#     ('2015-16', '2015-16'),
#     ('2016-17', '2016-17'),
#     ('2017-18', '2017-18'),
#     ('2018-19', '2018-19'),
#     ('2019-20', '2019-20'),
# )


class Alumni(models.Model):
    name = models.CharField(max_length=200, default='', blank=True)
    session = models.CharField(max_length=7, default='', blank=True)
    current_position = models.CharField(max_length=1000, default='', blank=True)
    address = models.CharField(max_length=700, default='', blank=True)
    contact_no = models.CharField(max_length=14, default='', blank=True)
    email = models.CharField(max_length=100, default='', blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    profile_picture = models.ImageField(default='', blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.session

    def save(self):
        # Opening the uploaded image
        if self.profile_picture:
            im = Image.open(self.profile_picture)

            output = BytesIO()

            # Resize/modify the image
            im = im.resize((640, 640))

            # after modifications, save it to the output
            im.save(output, format='JPEG', quality=60)
            output.seek(0)

            # change the imagefield value to be the newley modifed image value
            self.profile_picture = InMemoryUploadedFile(
                output, 'ImageField', "%s.jpg" % self.profile_picture.name.split('.')[0],
                'image/jpeg', sys.getsizeof(output), None)

        super(Alumni, self).save()
