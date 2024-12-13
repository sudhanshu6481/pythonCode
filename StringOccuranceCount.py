def _string_occurance_count(string, word):
     if word in string:
         x=string.count(word)
         print('The '+word+' appears '+str(x)+' times')

string="learn pytho python"
word="python"

_string_occurance_count(string, word)