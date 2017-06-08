pyg ="ay"; letter=input("enter the letter you want to translate"); if len(letter)>0 and letter.isalpha(): word = letter.lower(); first=word[0] if(first=="a" or first=="e" or first=="i" or first=="o" or first=="u"):

        print (word+pyg);

   else :

        print (word[1:]+first+pyg);
else : print ("not acceptable");
