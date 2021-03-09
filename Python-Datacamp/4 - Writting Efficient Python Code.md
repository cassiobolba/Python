<img src="https://github.com/cassiobolba/Data-Engineering/blob/master/src/img/2%20-%20Streamlined%20data%20with%20pandas/fig%201%20-%20Dataframe.JPG?raw=true"/>   
fig 1 - Dataframes 

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

#### Range()
* Creates a range of values
```py
# start para, end param, increment between params
even = range(1,11,2)
```

#### Enumerate()
* Creates index for each element in a list
```py
letters = ['a','b','c']
indexed_letters = enumerate(letters)
print(indexed_letters)
```
output = [(0,'a'),(1,'b'),(2,'c')]

#### map()
* Apply a funtion to each element in an object
* first args is the function to apply, second is the element
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
