# Read n (number of participants) and k (the benchmark position)
n, k = map(int, input().split())
 
# Read the non-increasing list of scores
scores = list(map(int, input().split()))
 
# Get the threshold score at the k-th position (using 0-based indexing)
threshold_score = scores[k - 1]
 
# Count how many scores are positive and >= the threshold score
advancing_participants = sum(1 for score in scores if score >= threshold_score and score > 0)
 
# Print the final count
print(advancing_participants)