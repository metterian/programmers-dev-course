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
    for i in range((end - start) // 2 + 1):
        if s[start + i] != s[end - i]:
            return False

    return True


def solution(s):
    for answer in range(len(s), 0, -1): # 문자열 최대 길이에서 하나씩 줄여나갑니다.
        start = 0 # 0에서
        end = answer - 1 # answer 길이까지

        while end < len(s):
            if is_palindrome(s, start, end): # 팰린드롬인지 확인합니다
                return answer; # 팰린드롬이면 그대로 리턴
            start += 1
            end += 1 # 한 칸씩 순회합니다.

    return 1 # 한 글자일 경우 1을 리턴합니다.
