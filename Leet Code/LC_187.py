from PyObjCTools.AppHelper import endSheetMethod


def dnaSubarray(s):
    start = 0
    check_dna = ['A', 'G', 'C', 'T']
    seen = set()
    repeated = set()

    for end in range(len(s)):
        window = s[start:end + 1]

        if s[end] in check_dna:
            if len(window) == 10:
                if window in seen:
                    repeated.add(window)
                else:
                    seen.add(window)
                start+=1
        else:
            start=end+1
    return list(repeated)

dnaSubarray('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
