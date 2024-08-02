def divide_apples(weights, contributions):
    total_amount = sum(contributions.values())
    total_weight = sum(weights)
    
    weight_distribution = {person: (amount / total_amount) * total_weight for person, amount in contributions.items()}
    
    weights.sort(reverse=True)
    
    result = {person: [] for person in contributions}
    remaining_weights = weights.copy()
    
    for person in contributions:
        person_total_weight = 0
        person_target_weight = weight_distribution[person]
        
        i = 0
        while i < len(remaining_weights):
            if person_total_weight + remaining_weights[i] <= person_target_weight:
                result[person].append(remaining_weights[i])
                person_total_weight += remaining_weights[i]
                remaining_weights.pop(i)
            else:
                i += 1
    
    return result

contributions = {'Ram': 50, 'Shyam': 30, 'Achyut': 20}
weights = []
print("Enter weights and -1 for stopping: ")
while True:
    weight = int(input())
    if weight == -1:
        break
    weights.append(weight)
result = divide_apples(weights, contributions)
print("Result:")
for person, apples in result.items():
  print(f"{person}: {', '.join(map(str, apples))}")

