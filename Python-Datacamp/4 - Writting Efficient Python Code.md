# WRITTING EFFICIENT PYTHON CODE
## Foundations for efficiencies

* Write clean as faster codes
* Profile code bottlenecks
* Eliminate bad design patterns with standard libs
* Efficient:
  * Minimal completion time
  * Minimal resource consumption (memory footprint)

### Pythonic Approach
* Focus on readability
* Use pythons constructs as intended
```py
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Nonthing-Pythonic
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# Better, close to Pythonic
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# Pythonic
best_list = [name for name in names if len(name) >= 6]
print(best_list)
```

### Building with built-ins
* Part of standard python installation
* Perform faster
* Built in types:
  * list
  * tuple
  * set
  * dict
* Built in functions:
  * print
  * len
  * range
  * round
  * enumerate
  * map
  * zip
* Built in modules
  * os
  * sys
  * itertools
  * collections
  * math

#### **Range()**
* Creates a range of values
```py
# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
# * is for unpacking and kind of replace the for loop
nums_list2 = [*range(1,12,2)]
print(nums_list2)
```

#### **Enumerate()**
* Creates index for each element in a list
* Suppose you had a list of people that arrived at a party you are hosting. The list is ordered by arrival (Jerry was the first to arrive, followed by Kramer, etc.):
```py
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,names) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)

```
output = [(0,'a'),(1,'b'),(2,'c')]

#### **map()**
* Apply a funtion to each element in an object
* first args is the function to apply, second is the element
* Suppose you wanted to create a new list (called names_uppercase) that converted all the letters in each name to uppercase. you could accomplish this with the below for loop:
```py
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)
```
```py
nums = [1.5,2.6,3.4]
round_nums = map(round,nums)
print(round_nums)
```
output = [1,3,3]
* map can be used with lambda to apply a function on the fly withou defining it
```py
nums = [1,2,3]
sqrd = map(lambda x: x ** 2, nums)
print(sqrd)
```

### The power of Numpy arrays
* Fundamental package for data a numerical operations
* It is usually faster than built in python funcs
* Are homogeneous, all elements in an array must be same type
* It convert numbers to same type
* By removing the need to identify the type, it becomes fastes
```py
nums = list(range(5))
# [0,1,2,3,5]
import numpy as np
num_np = np.array(range(5))
# ([0,1,2,3,4])
```
#### Numpy array Broadcasting
* NP allow broadcasting
* Lists in python don't do
* Ex: want to multiply all elements in a lsit by a number:
  * can't do directly
  * have to create a for loop
  * or create a list comprehension
* None of these approaches are faster then numpy
```py
nums = np.array([1,2,3])
nums ** 2
# array([1,4,9])
# this is not allowed in lists
```
#### Numpy indexing
* For 1D lists, not much difference
* For 2D lists the sintaxe of numpy is simpler and faster:

<img src="https://github.com/cassiobolba/Python/blob/master/Python-Datacamp/src-img/4-numpy_indexing.jpg"/>   
fig 1 - numpy_indexing

```py
nums = np.array([[ 1  2  4  4  5]
                [ 6  7  9  9 10]])
# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)
```

#### Numpy array Boolean indexing
* Easy way to filter or get values based on a true of false condition:
* To do the same in lists, need to create a list comprehension or for loop
```py
nums = [-1,-2,3,4]
nums_np = np.array(nums)

nums_np > 0
# >>> array ([false,false,true,true])

nums_np[nums_np >0]
# >>> array ([3,4])
```

#### Exercise
```py
# List from 10 to 50, incremented by 10
# Create a list of arrival times
arrival_times = [*range(10, 60, 10)]
print(arrival_times)
# You realize your clock is three minutes fast. Convert the arrival_times list into a numpy array 
# (called arrival_times_np) and use NumPy broadcasting to subtract three minutes from each arrival time.
# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3
# Use list comprehension with enumerate() to pair each guest in the names list to their updated arrival 
# time in the new_times array. You'll need to use the index variable created from using enumerate() 
# on new_times to index the names list.
# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

```

## Timing and profiling code
### Examining runtime
* Comparing run time allow us to pick the fastest code
* Calculate runtime with Ipython magic command %timeit
```py
# pass the magic command before the code to measure
%timeit rand_nums = np.random.rand(1000)
```
* It outputs the mean time + std dev, number or runs and loops in each run
* It does multiple runs in order to get more acurate results than measring only one run
* Can set the number or runs and loops using -r and -n
```py
%timeit -r2 -n10 rand_nums = np.random.rand(1000)
```
* if using one % it runs in only one line
* If passing two %% it runs on multiple lines code
```py
# pass the magic command before the code to measure
%%timeit
nums = []
for x in range(10):
  nums.append(x)
```
* Can save the time output to a variable, passing the value -o
```py
times = %timeit -o rand_nums = np.random.rand(1000)
```
* Then can use few methods to analyze the ouputs
  * times.timings (list of times saved)
  * times.best (best timing saved)
  * times.worst
* It allow to compare runtime
```py
# measuring the time to create a formal dict
f_time = %timeit -o formal_dict = dict()
# measuring the time to crete an informal dict
l_time = %timeit -o literal_dict = {}
# comaparing the runtime
diff = (f_time.average - l_time.average) * (10**9)
print(f"the difference it {diff}")
```
