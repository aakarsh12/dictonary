import json
from difflib import get_close_matches

data = json.load(open("dictf.json"))


def output(word):
  if word.upper() in data:  
    return data[word.upper()]
  elif word.lower() in  data:
     return data[word]  
  elif word.title() in data:
      return data[word.title()]
  elif len( get_close_matches(word, data.keys())) >0:
      print("did you mean %s" %get_close_matches(word, data.keys())[0])
      w= input("press y for yes and n for no ")
      if w =="y":
          return data[get_close_matches(word, data.keys())[0]]
      else:
          print("word not in dictionary") 

  else:
    print("Word not in dictionary")


word = input("Enter the word \n")
meaning = output(word)
if type(meaning)!= list:
  print(meaning)
else:
    c=1
    for i in meaning:
        print(f'{c} --> {i}') 
        c+=1 
