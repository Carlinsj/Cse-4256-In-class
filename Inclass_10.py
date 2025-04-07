# Question 1
def median(numbers):
    sorted_numbers = sorted(numbers)
    count = 0
    for _ in sorted_numbers:
        count += 1
    if count == 0:
        raise ValueError("The list is empty, median is undefined.")
    mid_index = count // 2 
    if count % 2 == 1:
        return sorted_numbers[mid_index]
    else:
        return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2

# Question 2
def mode(numbers):
    freq = {}
    max_count = 0
    modes = set()
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        if freq[num] > max_count:
            max_count = freq[num]
            modes = {num}
        elif freq[num] == max_count:
            modes.add(num)
    return modes

# Question 3
def arithmetic_mean(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    if count == 0:
        raise ValueError("The list is empty, arithmetic mean is undefined.")
    return total / count

#Question 4
def olympic_mean(numbers):
    total = 0
    count = 0
    first = True
    for num in numbers:
        total += num
        count += 1
        if first:
            min_val = num
            max_val = num
            first = False
        else:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
    if count < 3:
        raise ValueError("Need at least three elements to compute the Olympic mean.")
    adjusted_sum = total - (min_val + max_val)
    adjusted_count = count - 2

    return adjusted_sum / adjusted_count

# Question 5
def geometric_mean(numbers):
    product = 1
    count = 0
    for num in numbers:
        product *= num
        count += 1
    if count == 0:
        raise ValueError("The list is empty, geometric mean is undefined.")
    return product ** (1.0 / count)

# Question 6
def harmonic_mean(numbers):
    total_reciprocal = 0
    count = 0
    for num in numbers:
        if num == 0:
            raise ValueError("Harmonic mean is undefined for lists containing zero.")
        total_reciprocal += 1.0 / num
        count += 1

    if count == 0:
        raise ValueError("The list is empty, harmonic mean is undefined.")
    
    return count / total_reciprocal

# Question 7
def sample_variance(numbers):
    count = 0
    mean = 0.0
    M2 = 0.0  
    for x in numbers:
        count += 1
        delta = x - mean
        mean += delta / count
        delta2 = x - mean
        M2 += delta * delta2
    if count < 2:
        raise ValueError("At least two elements are required to compute sample variance.")
    return M2 / (count - 1)