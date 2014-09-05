# coding=utf-8
import sys
# define tone dictionary
tone_dic = {u'ā':'a1', u'á':'a2', u'ǎ':'a3', u'à':'a4', u'ō':'o1', u'ó':'o2', u'ǒ':'o3', u'ò':'o4', u'ē':'e1', u'é':'e2', u'ě':'e3', u'è':'e4', u'ī':'i1', u'í':'i2', u'ǐ':'i3', u'ì':'i4', u'ū':'u1', u'ú':'u2', u'ǔ':'u3', u'ù':'u4', u'ǘ':'v2', u'ǚ':'v3', u'ǜ':'v4'}
tone_set = []
# read file
f = open(sys.argv[1],'r')
file_name = sys.argv[1].split('.')
file_name = file_name[0] + '.pyv'
print(file_name)
pen = open(file_name,'w')
# load lines
wordList = list(f)
# read lines and execute treatment one by one
for word in wordList:
    # extract syllables of one word
    syllables = word.split()
    # iterate each syllable of one word
    for syllable in syllables:
        phones = list(unicode(syllable,'utf-8'))
        numPhones = len(phones)
        for i in range(numPhones):
           if phones[i] > u'z':
               #tone_set.append(phone)
               #print('_' + tone_dic[phone] + '_'),
               tone = tone_dic[phones[i]]
               phones[i] = tone[0]
               phones.append(tone[1])
          # else:
          #     print(phone),
        print(phones)
        print('\n')
        for phone in phones:
            pen.write(phone.encode('utf-8'))
        pen.write(' ')
  #  print("\n")
#for tone in tone_set:
#    pen.write(tone.encode('utf-8'))
    pen.write('\n')
f.close()
pen.close()

