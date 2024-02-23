class MySet:
    def __init__(self, enumberable = []):
        self.dictionary = {}
        for value in enumberable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        # Add a value as a key on the Dictionary
        self.dictionary[value] = True 
        # Return the updated set
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
    
    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'
    

# set = MySet([1,2,3,4,5])

# # set.add(7)

# # print(set.__str__())
