#!/bin/python

from random import choice 

# create list of animes
animes = [['naruto', 'pepehype', 'long', 'series'],
        ['haikyuu', 'sports', 'short', 'series'],
        ['clannad', 'sad', 'short', 'series'],
        ['toradora', 'romance', 'short', 'series']]

# input method
print('What mood are you in?')
mood = input()

# loop through and find a matching mood
for item in animes:
    if item[1] == mood:
        print(mood + ' anime: ' + item[0])
