from django.db import models

from cities.models import City


class Project(models.Model):
    name = models.CharField(max_length=150)
    city = models.ForeignKey(City, related_name='projects', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return "{}".format(self.name)


class ProjectFile(models.Model):
    project = models.ForeignKey(Project, related_name='project_files', on_delete=models.CASCADE)
    geo_json_file = models.FileField(upload_to='geojson', null=False, blank=False)
    excel_file = models.FileField(upload_to='excel', null=False, blank=False)

    active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return "{}".format(self.excel_file.name)

    def geo_json_file_url(self):
        return self.geo_json_file.url

    def excel_file_url(self):
        return self.excel_file.url
