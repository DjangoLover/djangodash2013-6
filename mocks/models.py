from django.db import models


class Blueprint(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def actions_count(self):
        return self.actions.count()

    def __unicode__(self):
        return self.name


class Action(models.Model):
    REQUEST_METHOD_CHOICES = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
    )
    blueprint = models.ForeignKey(Blueprint, related_name='actions')
    description = models.CharField(max_length=255)
    request_method = models.CharField(choices=REQUEST_METHOD_CHOICES, max_length=6)
    request_path = models.CharField(max_length=255)
    request_accept = models.CharField(default='application/json', max_length=255)
    response_status_code = models.PositiveSmallIntegerField()
    response_content = models.TextField(blank=True, null=True)
    response_content_type = models.CharField(default='application/json', max_length=32)

    class Meta:
        ordering = ('request_path', 'request_method')
        unique_together = ('request_method', 'request_path', 'request_accept')

    def __unicode__(self):
        return '%s %s (%s)' % (self.request_method, self.request_path, self.response_status_code)


class Request(models.Model):
    request_method = models.CharField(max_length=6)
    request_path = models.CharField(max_length=255)
    request_accept = models.CharField(max_length=255)
    request_body = models.TextField(blank=True, null=True)
    response_status_code = models.PositiveSmallIntegerField()
    response_content = models.TextField(blank=True, null=True)
    response_content_type = models.CharField(max_length=32)
    requested = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['requested']

    def __unicode__(self):
        return '%s %s (%s) @ %s' % (self.request_method, self.request_path, self.response_status_code, self.requested)
