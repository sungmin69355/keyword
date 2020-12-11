from django.db import models


class KeywordModel(models.Model):
    keyword = models.CharField(max_length=100)
    keyword_list = models.CharField(max_length=400)

    def __str__(self):
        return "%s - %s" % (self.keyword, self.keyword_list)