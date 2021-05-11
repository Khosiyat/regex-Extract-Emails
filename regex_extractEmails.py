#READY TO POST

                                                                   #Copywrite Warning: Owner of the code is Gulcheera Academy(Khosiyat Sabirova)
                                                        #This code can be used by anyone for free, but the name "Gulcheera Academy" must be acknowledged 
import pandas as pd
import numpy as np
import matplotlib as plt
import re
import warnings
#%matplotlib inline

example_textData4=["30-538-917-33-62", "80 948 649 96 23","90.316. 221.23.19","hosiyatSabirova@gmail.com","hosiyat.sabirova@academy.uz","hosiyat-88-sabirova@my-home.com","https://www.apple.com","http://www.banana.net", "@this is great post", "#IT @my godfather http://bit.ly/3h63x  he did not deserve this","#culture_art Here is a post of modern art"]
#extract emails
def extract_emails(inputText):
  email_list=[]

  for word in inputText:
    #You may change the regular expression patterns
    email=re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", word)
    email_list.append(email)
  #return email_list
  print(email_list)

extract_emails(example_textData4)
