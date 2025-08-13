with open("story.txt","r") as f:
    story=f.read()
    
    
words=set()
start_of_Word = -1
target_start="<"
target_end=">"
    
for i ,char in enumerate(story):
    if char == target_start:
        start_of_Word = i
    
    if char == target_end and start_of_Word !=-1:
        word=story[start_of_Word:i + 1]
        words.add(word)
        start_of_Word = -1
        
        
dictionary={}

for word in words:
    answer=input("please Enter a key word fro :"+word+":")
    dictionary[word]=answer
    
for word in words:
    story=story.replace(word,dictionary[word])
      
print(story)