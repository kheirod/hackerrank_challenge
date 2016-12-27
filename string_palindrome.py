def is_anagram(s, low, high, key):
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        elif key is not None:
            return -1
        elif is_anagram(s, low, high-1, high) is not -1:
            return high
        elif is_anagram(s, low+1, high, low) is not -1:
            return low

    if key is not None:
        return key
    return -1

n=int(input())
for _ in range(n):
    s = str(raw_input())
    print(is_anagram(s, 0, len(s)-1, None))
