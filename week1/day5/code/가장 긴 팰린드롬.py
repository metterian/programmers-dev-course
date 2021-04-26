#%%
s = "abcdcba"

# %%
def solution(s):
    def expand(left: int , right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1
        return s[left+1:right-1]

    if len(s) <  2 or s == s[::-1]:
        return len(s)

    result = ''
    for i in range(len(s) -1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return len(result)

# %%

def is_palindrome(s, start, end):
    for i in range((end-start)//2+1):
        if s[start+i] != s[end-i]:
            return False
    return True



def solution(s):
    for answer in range(len(s), 0, -1):
        start, end = 0, answer - 1
        while end < len(s):
            if is_palindrome(s, start, end):
                return answer
            start += 1
            end += 1
    return 1

solution(s)



# %%
