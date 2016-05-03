import string
import numpy as np

class MyOpenLinearDict(object):
    def __init__(self):
#initializing a numpy array fo
        self.mydict = np.ndarray(shape=(1000,), dtype = tuple)
#setting a counter that increments everytime the function rehashes
        self.counter = 0
#returns
        return

#insert function
    def insert(self, key, value):
#creates a tuple for the MyOpenLinearDict
        dict_tup = (key,value)
#finds location of key within the MyOpenLinearDict
        location = self.locate(key)
#if the location within the linear address
        if location != None and location >= 0:
#increments the value by 1, with the location at 0
            incvalue = self.mydict[location][0] + 1
#finds the value thats associated with the key
            skey = self.mydict[location][1]
            self.mydict[location] = (skey, incvalue)
                 
        else:
            hkey = self.mhash(self.mydict, key)
            self.mydict[hkey] = dict_tup
            self.counter = self.counter + 1
        
        lfact = self.counter / self.mydict.size
        if lfact >= .50:
            #implement rehash
            self.rehash(self)

        
       # lfact = (self.counter)/(self.mydict.size)
    def locate(self, key):
        for i in range(self.mydict.size):
            akey = hash(key)
            hkey = ( akey + i ) % self.mydict.size
            if self.mydict[hkey] != None:
                akey = hash(key)
                hkey = ( akey + i ) % self.mydict.size
                if self.mydict[hkey][0] == key:
                   return key
        return -1
    
    def delete(self, key):
        hkey = MyOpenLinearDict.locate(self, key)
        if key in self.mydict:
            self.mydict[hkey] = ("-1", -1)
            self.counter -= 1
        return
    
    def getkeyval(self):
        tuplel = []
        for i in range(self.mydict.size):
            if self.dict[i] != None or self.mydict[i][0] != "-1":
                tuplel.append(self.mydict[i])
        return tuplel
 
    def value(self, key):
        hkey = MyOpenLinearDict.locate(self, key)
        return self.mydict[hkey][1]
    
    def contains(self, key):
        return key in self.mydict
    
    def dump(self):
        for k in self.mydict:
            print(k, self.mydict[k])
    
    def mhash(self, key,mydict):
        for i in range(mydict.size):
            akey = hash(key)
            hkey = (akey + i) % self.size
            if mydict[hkey] == None or mydict[hkey][0] == "-1":
                return hkey
    
    def rehash(self):
        mydict = np.ndarray(shape=(self.mydict.size*2),dtype=tuple)
        
        for i in range(self.mydict.size):
            tup = (self.mydict[i][0], self.mydict[i][1])
            hkey = MyOpenLinearDict.mhash(tup[0], mydict)
            mydict[hkey] = tup
        
        self.mydict = mydict
        return

class MyOpenLinearSet(object):
    def __init__(self):
        self.myset = set([]) #change to mysetdict
        return

    def insert(self, key):
        self.myset.add(key)
        return
    
    def contains(self, key):
        return key in self.myset

    def dump(self):
        for k in self.myset:
            print(k)

class MyOpenQuadraticDict(object):
    def __init__(self):
#initializing a numpy array fo
        self.mydict = np.ndarray(shape=(1000,), dtype = tuple)
#setting a counter that increments everytime the function rehashes
        self.counter = 0
#returns
        return

#insert function
    def insert(self, key, value):
#creates a tuple for the MyOpenQuadraticDict
        dict_tup = (key,value)
#finds location of key within the MyOpenQuadraticDict
        location = self.locate(key)
#if the location within the linear address
        if location != None and location >= 0:
#increments the value by 1, with the location at 0
            incvalue = self.mydict[location][0] + 1
#finds the value thats associated with the key
            skey = self.mydict[location][1]
            self.mydict[location] = (skey, incvalue)
                 
        else:
            hkey = self.mhash(self.mydict, key)
            self.mydict[hkey] = dict_tup
            self.counter = self.counter + 1
        
        lfact = self.counter / self.mydict.size
        if lfact >= .50:
            #implement rehash
            self.rehash(self)

        
       # lfact = (self.counter)/(self.mydict.size)
    def locate(self, key):
        for i in range(self.mydict.size):
            akey = hash(key)
            hkey = ( akey + i ) % self.mydict.size
            if self.mydict[hkey] != None:
                akey = hash(key)
                hkey = ( akey + i ) % self.mydict.size
                if self.mydict[hkey][0] == key:
                   return key
        return -1
    
    def delete(self, key):
        hkey = MyOpenLinearDict.locate(self, key)
        if key in self.mydict:
            self.mydict[hkey] = ("-1", -1)
            self.counter -= 1
        return
    
    def getkeyval(self):
        tuplel = []
        for i in range(self.mydict.size):
            if self.dict[i] != None or self.mydict[i][0] != "-1":
                tuplel.append(self.mydict[i])
        return tuplel
 
    def value(self, key):
        hkey = MyOpenLinearDict.locate(self, key)
        return self.mydict[hkey][1]
    
    def contains(self, key):
        return key in self.mydict
    
    def dump(self):
        for k in self.mydict:
            print(k, self.mydict[k])
    
    def mhash(self, key,mydict):
        for i in range(mydict.size):
            akey = hash(key)
            hkey = (akey + i + i^2) % self.size
            if mydict[hkey] == None or mydict[hkey][0] == "-1":
                return hkey
    
    def rehash(self):
        mydict = np.ndarray(shape=(self.mydict.size*2),dtype=tuple)
        
        for i in range(self.mydict.size):
            tup = (self.mydict[i][0], self.mydict[i][1])
            hkey = MyOpenLinearDict.mhash(tup[0], mydict)
            mydict[hkey] = tup
        
        self.mydict = mydict
        return


class MyOpenQuadraticSet(object):
    def __init__(self):
        self.myset = set([]) 
        return

    def insert(self, key):
        self.myset.add(key)
        return
    
    def contains(self, key):
        return key in self.myset

    def dump(self):
        for k in self.myset:
            print(k)
            
class MyOpenChainDict(object):
    def __init__(self):
#initializing a numpy array fo
        self.mydict = np.ndarray(shape=(1000,), dtype = tuple)
#setting a counter that increments everytime the function rehashes
        self.counter = 0
#returns
        return

#insert function
    def insert(self, key, value):
#creates a tuple for the LinearDict
        dict_tup = (key,value)
#finds location of key within the MyOpenLinearDict
        location = self.locate(key)
#if the location within the linear address
        if location != None and location >= 0:
#increments the value by 1, with the location at 0
            incvalue = self.mydict[location][0] + 1
#finds the value thats associated with the key
            skey = self.mydict[location][1]
            self.mydict[location] = (skey, incvalue)
                 
        else:
            hkey = self.mhash(self.mydict, key)
            self.mydict[hkey] = dict_tup
            self.counter = self.counter + 1
        
        lfact = self.counter / self.mydict.size
        if lfact >= .50:
            #implement rehash
            self.rehash(self)
            
    def locate(self, key):
        for i in range(self.mydict.size):
            akey = hash(key)
            hkey = ( akey + i ) % self.mydict.size
            if self.mydict[hkey] != None:
                akey = hash(key)
                hkey = ( akey + i ) % self.mydict.size
                if self.mydict[hkey][0] == key:
                   return key
         return -1
    
    def delete(self, key):
        hkey = MyOpenLinearDict.locate(self, key)
        if key in self.mydict:
            self.mydict[hkey] = ("-1", -1)
            self.counter -= 1
        return
    
    def getkeyval(self):
        tuplel = []
        for i in range(self.mydict.size):
            if self.dict[i] != None or self.mydict[i][0] != "-1":
                tuplel.append(self.mydict[i])
        return tuplel
 
    def value(self, key):
        hkey = MyOpenLinearDict.locate(self, key)
        return self.mydict[hkey][1]
    
    def contains(self, key):
        return key in self.mydict
    
    def dump(self):
        for k in self.mydict:
            print(k, self.mydict[k])
    
    def mhash(self, key,mydict):
        for i in range(mydict.size):
            akey = hash(key)
            hkey = (akey + i) % self.size
            if mydict[hkey] == None or mydict[hkey][0] == "-1":
                return hkey
    
    def rehash(self):
        mydict = np.ndarray(shape=(self.mydict.size*2),dtype=tuple)
        
        for i in range(self.mydict.size):
            tup = (self.mydict[i][0], self.mydict[i][1])
            hkey = MyOpenLinearDict.mhash(tup[0], mydict)
            mydict[hkey] = tup
        
        self.mydict = mydict
        return
        
class MyOpenChainSet(object):
    def __init__(self):
        self.myset = set([]) #change to mysetdict
        return

    def insert(self, key):
        self.myset.add(key)
        return
    
    def contains(self, key):
        return key in self.myset

    def dump(self):
        for k in self.myset:
            print(k)

######## End code which needs to be modified ##########

# Store the set of stop words in a set object
stop_words_file = "stopwords.txt"
stop_words = MyOpenLinearSet()
#stop_words = MyOpenQuadraticSet()
#stop_words = MyOpenChainSet

with open(stop_words_file) as f:
    for l in f:
        stop_words.insert(l.strip())


# Download file from https://snap.stanford.edu/data/finefoods.txt.gz        
# Remember to gunzip before using
review_file = "foods_test.txt"

review_words = []
for i in range(5):
    review_words.append(MyOpenLinearDict())
#    review_words.append(MyOpenQuadraticDict())
#    review_words.append(MyOpenChainDict())
    

    
with open(review_file, encoding='LATIN-1') as f:
    lines = f.readlines()
    idx = 0
    num_lines = len(lines) - 2
    while idx < num_lines:
        while not lines[idx].startswith("review/score"):
            idx = idx + 1

        # Jump through hoops to satisfy the Unicode encodings 
        l = lines[idx].encode('ascii', 'ignore').decode('ascii')
        l = l.strip().split(":")[1].strip()

        # Extract rating
        rating = int(float(l))
        while not lines[idx].startswith("review/text"):
            idx = idx + 1
            
        l = lines[idx].encode('ascii', 'ignore').decode('ascii').strip().lower()
        text = l.split(":")[1].strip()
        text = text.translate(str.maketrans("","", string.punctuation))

        # Extract words in the text 
        words = text.split(" ")
        # words = [x.strip(string.punctuation) for x in text.split(" ")]
        for w in words:
            if len(w) and not stop_words.contains(w):
                if review_words[rating - 1].contains(w):
                    count = review_words[rating - 1].value(w) + 1
                else:
                    count = 1
                review_words[rating - 1].insert(w, count)

# Print out the top words for each of the five ratings 
for i in range(5):
    freq_words = sorted(review_words[i].get_key_values(), key=lambda tup: tup[1], reverse=True)
    print(i+1, freq_words[0:20])
    
