from django.db import models
from random import randint
# Create your models here.



class Word(models.Model):
    
    adjective = models.CharField(max_length=20)

    
    def __string__(self):
        return self.adjective
        
    def get_random_adjective(self):
        all_adjectives = Word.objects.all()
        
        '''
        size = len(all_adjectives)
        random_element = randint(0, size)
        word_object = all_adjectives[random_element]
        adjective = word_object.adjective
        '''

        return all_adjectives[randint(0, (len(all_adjectives)-1))].adjective