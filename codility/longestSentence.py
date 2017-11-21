
S = "We test coders. Give us a try?"
def solution(S):
    return max(len(sentence.split()) for sentence in S.split('.'))
        
print(solution(S))
    
