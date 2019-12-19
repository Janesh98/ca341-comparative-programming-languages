def longestCommonPrefix(l):
    if not l:
        return ""
    return lcp(l, 0, len(l)-1)

def lcp(l, left, right):
    if left == right:
        return l[left]
    else:
        mid = (left + right) // 2
        return prefix(lcp(l, left, mid), lcp(l, mid + 1, right))

def prefix(s1, s2, i=0):
    # get min(s1, s2) because ["inter", "inte"], s1 is longer so the last index is out of range for s2.
    if i == len(min(s1, s2)):       # lcp of strings can only be a max length of the smallest string.
        return s1[:i]
    elif s1[i] != s2[i]:            # as soon as we have uncommon letters between the two strings, we know
        return s1[:i]               # the lcp is everything up to but not including the index letter.
    return prefix(s1, s2, i + 1)    # recursively iterate through strings

def main():
    long_l = ["interview", "interrupt", "integrate", "intermediate","interdependent", "intermediary", "interstellar", "intergalactic", "interim", "interchangeable", "interconversion", "intercorrelated"]
    l = ["interview", "interrupt", "integrate", "intermediate"]
    print(longestCommonPrefix(l))

if __name__ == '__main__':
    main()


"""  how it recursively divides and conquers in lcp() function
     by splitting the input into left and right each with two strings
     and then finding the longest common prefix using prefix()

     interview, interrupt     integrate, intermediate
                  |                       |
                inter                   inte
                    \\                 /
                     \\               /
                            inte
"""