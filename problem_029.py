def problem_29(target= 100):
    results = []
    for a in range(2, target+1):
	for b in range(2, target+1):
		if a**b not in results:
			results.append(a**b)
    return len(results)

problem_29()
