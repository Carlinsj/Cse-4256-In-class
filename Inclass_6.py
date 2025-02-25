# Question 1a
def union(s1, s2):
    result = []
    for item in s1:
        if item not in result:
            result.append(item)
    for item in s2:
        if item not in result:
            result.append(item)
    return set(result)

# Question 1b  
def difference(s1, s2):
    result = []
    for item in s1:
        if item not in s2:
            result.append(item)
    return set(result)

# Question 1c
def is_subset(s1, s2):
    for item in s1:
        if item not in s2:
            return False
    return True

# Question 1d
def are_disjoint(s1, s2):
    for item in s1:
        if item in s2:
            return False
    return True

# Question 1e
def symmetric_difference(s1, s2):
    result = []
    for item in s1:
        if item not in s2:
            result.append(item)
    for item in s2:
        if item not in s1:
            result.append(item)
    return set(result)

# Question 1f
def cartesian_product(s1, s2):
    result = []
    for item1 in s1:
        for item2 in s2:
            result.append((item1, item2))
    return set(result)

# Question 2a
def union_2(*sets):
    result = []
    for s in sets:
        for item in s:
            if item not in result:
                result.append(item)
    return set(result)

# Question 2b
def isdisjoint_2(*sets):
    seen = set()
    for s in sets:
        for item in s:
            if item in seen:
                return False
            seen.add(item)
    return True

# Question 3
def is_well_formed(string):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in string:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return len(stack) == 0

# Question 4
def rpn(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
    return stack[0] if stack else None

