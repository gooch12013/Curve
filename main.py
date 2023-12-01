import random
import matplotlib.pyplot as plt

num_sets = 255
num_numbers = 10
random_sets = [[random.randint(1, 100) for _ in range(num_numbers)] for _ in range(num_sets)]

averages = []

for i, set in enumerate(random_sets, start=1):
    avg = sum(set) / len(set)  
    averages.append(avg) 
    print(f"Set {i}: {set}, Average: {avg}")

print("\nList of 255 averages:", averages)

plt.plot(averages, marker='o')  # 'o' creates circular markers for each point
plt.title('Averages of 255 Sets of Random Numbers')
plt.xlabel('Set Number')
plt.ylabel('Average Value')
plt.grid(True)
plt.show()