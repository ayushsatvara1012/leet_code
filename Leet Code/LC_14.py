def longest_common_prefix(str):
    if not str:
        return ''
    sorted_str = sorted(str, key=len)

    for i in range(len(sorted_str[0])):  # i=0
        for s in sorted_str[1:]:  # char = flower
            if sorted_str[0][i] != s[i]:
                return sorted_str[0][:i]
    return sorted_str[0]


print(longest_common_prefix(["ower", "flow", "flight"]))
