def potegowanie(pod, wyk):
    if wyk==0:
        return 1
    else:
        return pod*potegowanie(pod, wyk-1)

print(potegowanie(2,5))