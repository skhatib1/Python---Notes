## Dictionaries
```python
myDictionary = {} # - Create empty dictionary
myDictionary["text"]  = 2 # If key exists, change value. If not, create new key/value pair
myDictionary = {('Step''Father'):'James'} # - Tuples can be keys
myDictionary['Mother'] # - Print value for key 'mother' (answer is 'Jessica')
myDictionary['Mother'] = 'Natasha' # - Change value for 'Mother'
```

## Functions
```python
len(myDictionary) # - Number of (key,value) paris in dictionary
sorted(myDictionary) # - Prints myDictionary values sorted by key
```

## Dictionary Methods

```python
myDictionary.get("key") # - Returns value of specified key 
myDictionary.keys() # - Returns list with each key as an item
myDictionary.values() # - Returns list of values, with each value as an item
myDictionary.items() # - Returns key-value pair
myDictionary.pop(k) # - Removes (key, value) pair from dictionary, and returns value
myDictionary.update(randomDictionary) # - Adds (key, value) pair to dictionary
```


## Search in Dictionary
```python
'Mother' in myDictionary # - True if 'mother' is a key in dictionary, else False
'Mother' not in myDictionary # - False if 'mother' is a key in dictionary, else True
```


## Get Dictionary Key as String

```python
myDictionary = {"key1": "value1", "key2": "value2"}
first_key = list(myDictionary)[0]
```
