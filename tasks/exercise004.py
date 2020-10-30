# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    punct_lst=["!",",",".",";","?",":"]

    lst_text=text.split()#convert string to a list
    new_lst_text=[]
    punct=None

#Assumption: Punctuation exist only at the end of the sentence and at the end of word.
    for letter in lst_text[-1]: # check if there is a punctuation at the last element of the array
      if letter in punct_lst:
        punct_index=lst_text[-1].index(letter)#Find the place of the punctuation
        punct=lst_text[-1][punct_index:] #Get the punctuation itself
        lst_text[-1]=lst_text[-1][:punct_index]#change the last element without punctuation (by slicing punctuation)
        break

    for item in lst_text:
        item=item[1:]+item[0]+"ay"
        new_lst_text.append(item)
    
    if punct is not None:
      new_lst_text[-1]=new_lst_text[-1]+punct

    new_text=" ".join(new_lst_text) 
    return new_text