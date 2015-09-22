from redditor.models import SampleChart



print(SampleChart.objects.all())


'''
month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)
'''


q = SampleChart(month = 9, boston_temp=51.2, houston_temp = 33.56)

q.save()

print(SampleChart.objects.all())