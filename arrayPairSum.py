def pair_sum(arr,k):
    if len(arr)<2:
        return
    seen = set()
    output = set()

    for num in arr:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
    return '\n'.join(map(str,list(output)))
print(pair_sum([1,2,3,2],4))
