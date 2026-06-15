l = [11, 22, 4, 33, 44, 55]
n = len(l)
print(f"length={n}")

# max
maxnum = max(l)
print(f"max num= {maxnum}")

# min

minnum = min(l)
print(f"min num= {minnum}")
# sum
suml = sum(l)
print(f"sum= {suml}")

# sort
l2 = sorted(l)
print(f"old list = {l}")
print(f"new list = {l2}")

l2 = sorted(l, reverse=True)
print(f"old list = {l}")
print(f"new list = {l2}")
