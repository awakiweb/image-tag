from django.db import models


class Resource(models.Model):
    county_file = models.FileField(upload_to='files', null=False, blank=False)
    city_file = models.FileField(upload_to='files', null=False, blank=False)
    active = models.BooleanField(default=True)

    def county_file_url(self):
        return self.county_file.url

    def city_file_url(self):
        return self.city_file.url
