print("\n-----------------PROGRAM START----------------------------")
#Sentence to convert
name = input("\nEnter the name/sentence to make acronym-")
name = name.split()

#Words To ignore
stopwords = ["I","i","The","the","To",'to',"A",'a',"For",'for',"By",'by',"An",'an',"Am",'am',"So",'so',"It",'it',"And",'and',"Of","of"]

acro = []
for i in range(len(name)):
    string = name[i]
    first_letter = string[0].upper()
    if string not in stopwords:
        acro.append(first_letter)

#Joining the list of Capital Letters
s=""
acro = s.join(acro)
print("\nAcronym made - ",acro)
print("\n------------------CODE END------------------------------\n")