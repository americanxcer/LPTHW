def scan(userinput):
  words = userinput.split() # split words of sentence
  result = []
  for word in words:
      result.append(classify(word))
  return result

def classify(word):
    #test if word is direction,
    #if so return ('direction', word)
    if word in ['north', 'south', 'east', 'west', 'slowly']:
        return ('direction', word)
    #test if word is a verb
    #if so return ('verb', word)
    elif word in ['throw', 'shoot', 'dodge', 'tell', 'place', 'kill', 'go', 'jump']:
        return ('verb', word)
    #test if word is a stop
    #if so return ('stop' word)
    elif word in ['the', 'in', 'of', 'a']:
        return ('stop', word)
    #test if word is a noun
    # if so return ('noun', word)
    elif word in ['bomb', 'joke']:
        return ('noun', word)

    else:
        try:
            thenumber = int(word)
            return ('number', thenumber)
        except ValueError:
            # word is not a number:
            return ('error', word)
