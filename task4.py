from typing import Optional

def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # The value on the test of each call is true if the index is valid, and false, if not.
    if test:                            # This check prevents an index error.
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # The value of first is None
second = checked_access([1, 0, 1], 2)    # The value of second is 1
print()
######################################################################################################################################################
def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # This statement is evaluated in the first call, and the values being added are 4 + 2 + 3
    elif len(L) > 1:
        result = len(L[0]) + len(L[1])                # This statement is evaluated in the third call, and the values being added are 7 + 4
    elif len(L) > 0:
        result = len(L[0])                            # This statement is evaluated in the second call, and the value is 12 (no values being added)
    else:
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()
######################################################################################################################################################
def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # The value of words is 6
         # the value of first is 5, and the value of second is 6
         # The word "Avoid" and "such" were added to the end of the words list and converted to uppercase versions.
print()
