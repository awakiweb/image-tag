from django.db import models


class Image(models.Model):
    url = models.TextField()

    def get_tags(self):
        # get tags
        image_tags = ImageTag.objects.filter(image=self)
        tags = [image_tag.tag for image_tag in image_tags]

        return tags


class Tag(models.Model):
    name = models.CharField(max_length=100)


class ImageTag(models.Model):
    image = models.ForeignKey(Image, related_name='image_tags', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='image_tags', on_delete=models.CASCADE)
