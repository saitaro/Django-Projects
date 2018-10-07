from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Company(models.Model):
    name = models.CharField(max_length=127)
    
    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    def service(self):
        # return Skill.objects.filter(masters__employer__name=self.name).distinct()
        return self.masters.all().values_list('skills__name', flat=True).distinct()


class Skill(models.Model):
    name = models.CharField(max_length=127, blank=False)

    def __str__(self):
        return self.name


class Master(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, related_name='masters')
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL,
                                related_name='masters')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'masters'

# @receiver(post_save, sender=Master)
# def add_to_group(sender, instance, created, **kwargs):
#     if created:
#         instance.groups.add(Group.objects.get(name='Masters'))


class Order(models.Model):
    client = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    service = models.ForeignKey(Skill, related_name='orders', on_delete=models.CASCADE)
    executor = models.ForeignKey(Master, related_name='jobs', null=True, on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(auto_now_add=True)
    execution_date = models.DateTimeField(null=True)
    
    def set_execution_date(self, date):
        self.execution_date = date

    def __str__(self):
        return '{} – {} by {} for {}'.format(
            str(self.pk), self.service, self.executor, self.client
        )

