
unique = lambda e: sorted([el for el in set(e)])

transposeDict = lambda d: {d[key] : key for key in d.keys()}

mex = lambda e: next(x for x in range(1,len(e)+2) if x not in set(e))

frequencyDict = lambda s: {ch : s.count(ch) for ch in set(s)}
