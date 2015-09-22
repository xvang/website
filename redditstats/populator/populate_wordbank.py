from redditstats.wordbank.models import Word







words_to_add = ['amazing',
                'awesome',
                'blithesome',
                'excellent',
                'fabulous',
                'fantastic',
                'favorable',
                'merciful',
                'fortuitous',
                'great',
                'incredible',
                'ineffable',
                'mirthful',
                'outstanding',
                'perfect',
                'propitious',
                'remarkable',
                'smart',
                'spectacular',
                'splendid',
                'stellar',
                'stupendous',
                'super',
                'ultimate',
                'unbelievable',
                'wondrous',
                'normal',
                'empathetic',
                ]


counter = 0
for word in words_to_add:
    
    try:
        d = Word.objects.get(adjective__exact=str(word).lower())
    except:
        counter = counter + 1
        new_word = Word.objects.create(adjective=word)
        new_word.save()
   

print("All Done! ", counter, " new word(s) added.")

        