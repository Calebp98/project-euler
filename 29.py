vals = []
for a in range(2,101):
    for b in range(2,101):
        if a**b not in vals:
            vals.append(a**b)
print(len(vals))
