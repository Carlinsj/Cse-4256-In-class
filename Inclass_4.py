import random

# Question 1
def ice_cream(trials):
    meeting_count = 0

    for _ in range(trials):
        bill_arrival = random.uniform(0, 30)  # Bill arrives between 0 and 30 minutes
        lilly_arrival = random.uniform(0, 30)  # Lilly arrives between 0 and 30 minutes

        if bill_arrival < lilly_arrival and lilly_arrival - bill_arrival <= 5:
            meeting_count += 1  # Bill waits for Lilly within 5 minutes
        elif lilly_arrival < bill_arrival and bill_arrival - lilly_arrival <= 7:
            meeting_count += 1  # Lilly waits for Bill within 7 minutes

    probability = round(meeting_count / trials, 2)
    return probability

# Question 2
def matches_helper():
    book1, book2 = 20, 20  # Each book starts with 20 matches
    matches_used = 0

    while book1 > 0 and book2 > 0:
        if random.choice([True, False]):  # Randomly choose a book
            book1 -= 1
        else:
            book2 -= 1
        matches_used += 1

    return matches_used

def matches(trials):
    total_matches = sum(matches_helper() for _ in range(trials))
    return round(total_matches / trials, 2)

# Question 3a
def die_rolls(trials):
    roll_counts = {i: 0 for i in range(2, 13)}  # Initialize dictionary for sums 2 to 12

    for _ in range(trials):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)  # Roll two dice and sum
        roll_counts[roll_sum] += 1

    # Convert counts to percentages and round to the nearest tenth
    roll_percentages = {key: round((value / trials) * 100, 1) for key, value in roll_counts.items()}

    return roll_percentages

# Question 3b
def die_rolls(trials, n):
    roll_counts = {i: 0 for i in range(n, 6 * n + 1)}  # Initialize dictionary for sums n to 6*n

    for _ in range(trials):
        roll_sum = sum(random.randint(1, 6) for _ in range(n))  # Roll n dice and sum
        roll_counts[roll_sum] += 1

    # Convert counts to percentages and round to the nearest tenth
    roll_percentages = {key: round((value / trials) * 100, 1) for key, value in roll_counts.items()}

    return roll_percentages

# Question 4
import random

def birthday():
    trials = 100000  # Number of trials for accuracy
    success_count = 0

    for _ in range(trials):
        people = 0
        birthdays = set()

        while True:
            new_birthday = random.randint(1, 365)  # Assign a random birthday (ignoring leap years)
            people += 1

            if new_birthday in birthdays:  # Check for a duplicate birthday
                break
            birthdays.add(new_birthday)

        if people >= 23:  # The known theoretical answer is 23
            success_count += 1

    return round(success_count / trials * 100, 2)

# Question 5
"""Alice is more likely to finish rolling sooner than Bob. 
This is because the probability of rolling a 5 followed by a 6 is slightly higher than rolling two consecutive 5s."""
