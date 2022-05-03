import math
import random
import statistics
import keyword


print(random.randint(0,100))

# The mean is the average. gotten by taking the sum of all the numbers and dividing it by the number of numbers.
# The median is the middle number in an ordered list from smallest to largest
# The mode is the most frequently occuring value in  a list of numbers.

# mean
nums = [1,5,33,12,46,33,2]
print("The mean: \n", statistics.mean(nums))
# median
print("The median: \n",statistics.median(nums))
# mode
print("The mode: \n",statistics.mode(nums))
# Another function from the statistics module
print("Another built in function from the statistics module called variance: \n",statistics.variance(nums))

print(keyword.iskeyword('for'))
print(keyword.iskeyword('football'))