def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])
    
sentence= "hello world python"
result=reverse_words(sentence)
print(result)



def remove_duplicates(list):
    unique_list=[]
    
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
    
numbers=[4, 2, 4, 5, 2, 3, 5, 1]
result=remove_duplicates(numbers)
print(result)


def find_common_elements(list1, list2): 
    common = [] 
    for item in list1: 
        if item in list2 and item not in common: 
            common.append(item) 
    return common 
 
list1 = [1, 2, 3, 4] 
list2 = [3, 4, 5, 6] 
 
result = find_common_elements(list1, list2) 
print(result) 



def word_frequency(sentence): 
    # Convert to lowercase 
    sentence = sentence.lower() 
     
    # Split into words 
    words = sentence.split() 
     
    # Dictionary to store word counts 
    freq = {} 
     
    for word in words: 
        if word not in freq: 
            freq[word] = 1 
        else: 
            freq[word] += 1 
             
    return freq 
 
 
# Example 
sentence = "the cat and the hat" 
result = word_frequency(sentence) 
print(result)



def find_pairs(lst, target): 
    pairs = [] 
    seen = set() 
     
    for num in lst: 
        complement = target - num 
        if complement in lst and (min(num, complement), max(num, complement)) not in seen: 
            # Avoid duplicates and count each pair only once 
            pairs.append((num, complement)) 
            seen.add((min(num, complement), max(num, complement))) 
    return pairs 
 
# Example input 
numbers = [2, 4, 3, 5, 7, 8, -1] 
target = 6 
 
result = find_pairs(numbers, target) 
print(result)  # Output: [(2, 4), (3, 3), (7, -1)]