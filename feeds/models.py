from django.db import models


class KeywordModel(models.Model):
    keyword = models.CharField(max_length=100)
    keyword_list = models.CharField(max_length=400)
    tag_list = models.CharField(max_length=3000,default = '')

    def __str__(self):
        return "%s" % (self.keyword)