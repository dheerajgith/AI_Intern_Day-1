import numpy as np
a=np.random.randint(1,100,10)
print(f"Mean score: {np.mean(a):.2f}\nStd Dev: {np.std(a):.2f}\nMax marks: {np.max(a):.2f}\nLowest {np.min(a):.2f}")
print("No.of students passed:", np.sum(a>=40))
print("no.o students with more than 90 marks:",np.sum(a>90))
print("Sorted marks:", np.sort(a))
print("Marks above 90:",a>90)# creates a boolean array true where the element satisfies the condition.