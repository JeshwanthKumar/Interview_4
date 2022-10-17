# TC : O(len(wordsDict))
# SC : O(max(occurrence(word1),occurrence(word2)))
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        minimum=len(wordsDict)  #Initialize minimum to length of wordsDict
        if(word1==word2):   #If both word1 and word2 are the same 
            word1List=[]    #Initialize wordList as an empty array
            for i in range(len(wordsDict)): #Iterate throught the wordsDict
                if(wordsDict[i]==word1):    #If wordsDict[i] is equal to word1
                    word1List.append(i) #Append the index into word1List
            for j in range(1,len(word1List)):   #Iterate throught the word1List from 1, lenght of the list
                diff = abs(word1List[j-1]-word1List[j]) #diff is difference between absolute value of word1List[j-1] and word1List[j]
                minimum = min(minimum,diff) #Set minimum between minimum and diff
        else:   #Else they are different words
            word1List=[]    #Initialize word1List as an empty arrray
            word2List=[]    #Initialize qord2List as an empty array
            
            for i in range(len(wordsDict)): #Iterate through wordsDict
                if(wordsDict[i]==word1):    #If wordsDict[i] is equal to word1 append it to the word1List
                    word1List.append(i)
                elif(wordsDict[i]==word2):  #Else if wordsDict[i] is equal to word2 then append it to word2List
                    word2List.append(i)
            ptr1=0  #Initialize ptr1 pointer to 0
            ptr2=0  #Intiialize ptr2 pointer to 0
            while(ptr1<len(word1List) and ptr2<len(word2List)): #Iterate for ptr1<lenght of word1List and ptr2 < lenght of word2List
                diff = abs(word2List[ptr2]-word1List[ptr1]) #Difference between the absolute values of word2List[ptr2] and word1List[ptr1]
                minimum=min(diff,minimum)   #minimum between the diff and minimum
                if(word2List[ptr2]<word1List[ptr1]):    #If the word2List[ptr2] is less than word1List[ptr1]
                    ptr2+=1 #Increment ptr2 by 1
                else:   #Else increment ptr1 by 1
                    ptr1+=1
                    
        return minimum  #Return the minimum which will give the shortes between the words