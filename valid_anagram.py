# checks if s and t are anagrams
def isAnagram(s, t):
    if sorted(s) == sorted(t):
        return True
    return False
