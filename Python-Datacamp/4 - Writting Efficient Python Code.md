# WRITTING EFFICIENT PYTHON CODE
# Foundations for efficiencies

* Write clean as faster codes
* Profile code bottlenecks
* Eliminate bad design patterns with standard libs
* Efficient:
  * Minimal completion time
  * Minimal resource consumption (memory footprint)

## Pythonic Approach
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

## Building with built-ins
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

## **Range()**
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

## **Enumerate()**
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
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)

```
output = [(0,'a'),(1,'b'),(2,'c')]

## **map()**
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

## The power of Numpy arrays
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
## Numpy array Broadcasting
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
## Numpy indexing
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

## Numpy array Boolean indexing
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

## Exercise
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

# Timing and profiling code
## Examining runtime
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
## Coding Profilling for Runtime
* Describe how often and how often something is executed
* Line-by-line analyses
* package used: *pip install line_profiler*
* timeit would only give the total function time, or you would need to declate time it in every single line of the function
* After install the package:
```py
# load the profiler in the session
%load_ext line_profiler
# use the lprun, -f flag to tell your are timming a function
# tell the function name, and then use the function as usuall
%lprun -f convert_units convert_units(heroes, hts, wts)
```
* It ouputs a nice table with many good performance info:  
<img src="https://github.com/cassiobolba/Python/blob/master/Python-Datacamp/src-img/line_profiler_output.jpg"/>     
fig 2 - line profiler output

## Coding Profilling for Memory Usage
Can use sys lib to inspect the size of an object, this is the quick and dirty way:
```py
import sys
num_list [*range(1000)]
sys.getsizeof(num_list)
# output: 9112
```
To check the memory footprint, can use a memory_profiler lib:
* Detailed stats on memory consumption
* line-by-line analyses
```py
# install the lib
pip install memory_profiler
# load to session
%load_ext memory_profiler
# use it on the function, similar to lprun
%mprun -f convert_units convert_units (heroes, hts, wts)
```
Drawbacks:
* Functions must be imported when using memory_profiler
* must create a function in a .py file and import it another session that is loading the memory profiler
```py
# This func was created and placed in the same folder
# my_funcs is my files that is containing the convert_units function
from my_funcs import convert_units
# load to session
%load_ext memory_profiler
# use it on the function, similar to lprun
%mprun -f convert_units convert_units (heroes, hts, wts)
```
* The output is pretty much the same as lprun, but with memory data (in mb)
* It queries memory usage by the system, so it may vary a little at every run
* But you can still get good insights from it

# Gaining efficiencies
## Combinining, counting and iterating
Let's say we have a list os pokemons and we want to combine:
```py
names = ['Bulbasaur','Charmander','Squirtle']
hps = [45,39,44]

combined = []

for i,pokemon in enumerate(names):
  combined.append((pokemon,hps[i]))

print(combined)
```
But this is not elegant and efficient.  
Then, use Zip:
```py
names = ['Bulbasaur','Charmander','Squirtle']
hps = [45,39,44]

combined_zip = zip(names, hps)
# combined zip is packed, then use * to unpack
combined_zip_list [*combined_zip]
print(combined_zip_list)
```
## Collection Module
* Standard library
* Specialized datatypes as alternative to: dict, list, set and tuple
* The notable ones:
  * namedtuple: 
  * deque: fast list for append and pop
  * Counter: dict for counting hashable objects
  * OrderedDict: dict that retain order of entries
  * defaultdict: dict that calls a factory function to supply missing values

## collections.Counter()
We want to count the number each value appears in a list. The non-pythonic approach, and not efficient:
```py
names = ['Bulbasaur','Charmander','Squirtle','Bulbasaur','Charmander','Squirtle','Bulbasaur']
type_counts = {}
for poke_type in names:
  if poke_type not in type_counts:
    type_counts[poke_type] = 1
  else:
    type_counts[poke_type] += 1
print(type_counts)
```
To do in a pythonic way, use the collection.Counter() function, it is faster, easier to read, and it is also ordered by the highest count:
```py
names = ['Bulbasaur','Charmander','Squirtle','Bulbasaur','Charmander','Squirtle','Bulbasaur']
from collections import Counter
type_counts = Counter(names)
print(type_counts)
```
## itertools Module
* Part of standard libraries
* Functional tools for creating iterators
* te notable ones:
  * infinite iterators: count, cycle, repeat
  * Finite iterators: accumnulate, chain, zip_longest
  * Combination generators: product, permutation, combinations

## itertools.Combinations()
If we want to create all possible combinations, we could do it with for loops, but it is not very efficient:
```py
names = ['Bulbasaur','Charmander','Squirtle','Pikachu']
combos = []

for x in names:
  for y in names:
    # condition to eliminate equal combinations
    if x == y:
      continue
    # condition to check if either combinations are already in the list
    if ((x,y) not in combos) & ((y,x) not in combos):
      combos.append((x,y))
print(combos)
```
Using the itertools:
```py
names = ['Bulbasaur','Charmander','Squirtle','Pikachu']
from itertools import combinations
combos = combinations(names,2)
combos_exp = [*combos]
print(combos_exp)
```

## Set Theoty
We oftenlly want to compare collection of objects, it works better with set types.
* Python has built-in set datatype with some mehtods:
  * intersection(): check if all elements are in both sets
  * difference(): check elements in one set but not in other
  * symetric_difference(): all elements in exaclty one set
  * union(): all elements that are in either sets
Sets are used for efficient membership testing:
* Check if a value exisst in a sequence or not
* use in operator in sets are more perfomrnat than using in regular lists

## Comparing Objects
We could use a logical for loop to find elements present in both lists:
```py
names_a = ['Bulbasaur','Charmander','Squirtle','Pikachu']
names_b = ['Bulbasaur','Pidgey','Caterpie','Pikachu']
common = []
for poke_a in names_a:
  for poke_b in names_b:
    if poke_a == poke_b:
      common.append(poke_a)
print(common)
```
This is extremelly not efficient! Instead, use set data type:
```py
set_a = set(names_a)
set_b = set(names_b)
set_a.intersection(set_b)
```
To check the pokemons in one list but not in the other:
```py
# what is in a but not in b
set_a.difference(set_b)
# or the opposite, what is b but not in a
set_b.difference(set_a)
```
To check what is in only one set, not in both
```py
set_a.symmetric_difference(set_b)
```
To combine the sets, creating unique values (even if in both sets, it won't be repeated)
```py
set_a.union(set_b)
```
Use set also to create unique list, instead of creating for loops to check if an intem in a list is new or not.

## Eliminating Loops
Looping is a common practice in python. There are few patterns:
* for loops: iterate over a sequence puece-by-piece
* while loop: iterate until a condition is met
* nested loops: one loop inside another
Using multiple loops are costly, inefficient and time consuming. If we follow the zen of python "flat is better", we are actually reducing loops and and flattening the code for more efficiency.  
Let's say we want to sum every list inside the list, there are many ways to do it:
```py
stats = [ 
  [90,92,75,60],
  [20,25,15,90],
  [65,130,60,75]
]
# non pythonic way
totals = []
for row in stats:
  totals.append(sum(row))
print(totals)

# using list comprehension
totals_comp = print([sum(row) for row in stats])

# using map function
totals_map = print(*map(sum,stats))
```
You can also use numpy to eliminate arrays, qhen want to perform calculations:
```py
stats = np.array([ 
  [90,92,75,60],
  [20,25,15,90],
  [65,130,60,75]
])
import numpy as np
sum_np = stats.sum(axis=1)
print(sum_np)
```

## Writting Better Loops
There are times where loops as unavoidable! So, follow some good practices for writting loops:
* Understand what is being done with each loop iteration
* Move one-time calculations outside (above) the loop
* Use holistic conversions outrside (below) the loop
* Anything that is done once should be outside the loop
Example, we want to find the pokemons with attack power greater than average (considering that this is the only option):
```py
pkm = np.array(['Bulbasaur','Charmander','Squirtle','Pikachu'])
atck = np.array([130,110,65,95])

for i,j in zip (pkm,atck):
  total_attack_avg = atck.mean()
  if j > total_attack_avg:
    print(
      "{}'s attack is greater than average : {}!".format(i,total_attack_avg)
    )
```
The variable *total_attack_avg* should be calculated only once, because if it is inside the loop, it is being calculated every time, but the values is the same. This one-time calculation should be moved to above the for loop. Test with %timeit and find the performance difference.   
Another example is when you want to create a list of list combining lists. If you use zip, it returns a tuple that you need to convert to a list. If you do inside the loop, it is less efficient that doing outside the loop:
```py
#  %%timeit
pkm = ['Bulbasaur','Charmander','Squirtle','Pikachu']
atck = [130,110,65,95]
lgnd = [True, False,True, False]
poke_data = []
for poke_tuple in zip(pkm,atck,lgnd):
  poke_list = list(poke_tuple)  
  poke_data.append(poke_list)
print(poke_data)
```
The approach above is less efficient, below we see a solution moving the holistic conversion outside the loop, and doing at once:
```py
# %%timeit
pkm = ['Bulbasaur','Charmander','Squirtle','Pikachu']
atck = [130,110,65,95]
lgnd = [True, False,True, False]
poke_data_tuples = []
for poke_tuple in zip(pkm,atck,lgnd):
  poke_data_tuples.append(poke_tuple)

poke_data = print([*map(list, poke_data_tuples)])
```
Use the timeit function to compare both performances!

# Basic Pandas Otimization
## Intro to pandas DataFrame iteration
So far we used only standard libraries data, now we gonna use pandas lib and define the best practices for iterating over pandas. To recap:
* Pandas in a data analysis Lib
* Main data structure is the DF
  * tabular data with labeled rows and columns
  * Built on top of numpy array structure
Creating the pandas df for studies: Baseball data!
```py
import pandas as pd
data = [
  ['ARI','NL',2012,734,688,81,162,0],
  ['ATL','NL',2012,700,600,94,162,1],
  ['BAL','AL',2012,712,705,93,162,1],
  ['BOS','AL',2012,734,806,69,162,0],
  ['CHC','NL',2012,613,759,61,162,0]
]
baseball_df = pd.DataFrame(data,columns = ['Team','League','Year','RS',"RA","W",'G','Playoffs'])
df
```
## Calculating win percentage
Let's say we want to cerate a column called win_percentage in our DF. First, create the formula to do the calculation.The formula to calculate win percentage is:
```py
import numpy as np
def calc_win_perc(wins, games_played):
  win_perc = wins / games_played
  return np.round(win_perc,2)
```
Then, create the loop to iterate over the df and calculate for each row:
```py
win_perc_list = []
# iterate the number of times equal to the number os rows in the df
for i in range(len(baseball_df)):
  # use the iloc to save the current row iteration in row variable as index
  row = baseball_df.iloc[i]
  # save the column regarding wins and games played in variables
  wins = row['W']
  games_played = row['G']
  # use the function created before
  win_perc = calc_win_perc(wins, games_played)
  # append the result to list outside the loop
  win_perc_list.append(win_perc)
# finnaly, to create a new columns is very easy
baseball_df['WP'] = win_perc_list
```
GREAT, DONE! But in a very inneficient way.   
When it comes to iterating over row, pandas offer the command .iterrows():
```py
win_perc_list = []

for i,row in baseball_df.iterrows():
  wins = row['W']
  games_played = row['G']
  win_perc = calc_win_perc(wins, games_played)
  win_perc_list.append(win_perc)
baseball_df['WP'] = win_perc_list
```
The iterrows module saved 1 line in the code, but turned it in much more efficient, because I don't need to create my indexes, they are given by the function.

Nice work! Since .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs, you can either split this tuple and use the index and row-values separately (as you did with for i,row in pit_df.iterrows()), or you can keep the result of .iterrows() in the tuple form (as you did with for row_tuple in pit_df.iterrows()).

If using i,row, you can access things from the row using square brackets (i.e., row['Team']). If using row_tuple, you would have to specify which element of the tuple you'd like to access before grabbing the team name (i.e., row_tuple[1]['Team']).

With either approach, using .iterrows() will still be substantially faster than using .iloc.

## Another iterator method: **.itertuples()**
* It is similar to iterrows, but usually more efficient
* Iterrows deliver a tuple taht you can access by row[index]
* itertuples deliver a special data type called named tuple, and you can access via . notation  
Coparing the efficiency:
```py
%%timeit
for row_tuple in baseball_df.iterrows():
  print(row_tuple)
```
versus
```py
%%timeit
for row_namedtuple in baseball_df.itertuples():
  print(row_namedtuple)
```
SIGNIFICANT GAIN!  
Reason: iterrows stored the data in pandas series which are more complez then named tuples.

### Accesing data: iterrows x itertuples
To access data in iterrows, use the bracket notation:
```py
for row_tuple in baseball_df.iterrows():
  # Access the column team
  print(row_tuple[1]['TEAM'])
```
Same in itertuples use the . (dot) notation:
```py
for row_tuple in baseball_df.itertuples():
  # Access the column team
  print(row_tuple.Team)
```