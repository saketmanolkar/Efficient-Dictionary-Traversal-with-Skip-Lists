#!/usr/bin/env python
# coding: utf-8

# In[55]:


from time import process_time
import matplotlib.pyplot as plt
import random
add_time=[]
delete_time=[]
search_time=[]
count=0
count_list=[]

#We are taking add_time, delete_time and search_time to measure
#Time Complexity of Addition, Deletion and Search Functions respectively

class Node(object): #We have taken this class to implement Node.
    
    
    def __init__(self, key, level):
        self.key = key
        self.forward = [None]*(level+1) # list to hold references to node of different level 
  
class SkipList(object):
    
    def __init__(self, max_lvl, P):
        
        self.MAXLVL = max_lvl
        
        self.P = P
  
        self.header = self.createNode(self.MAXLVL, -1)
    
        self.level = 0  # current level of skip list
      
   
    def createNode(self, lvl, key): # create  new node
        n = Node(key, lvl)
        return n
      
    
    def randomLevel(self):# create random level for node
        lvl = 0
        while random.random()<self.P and lvl<self.MAXLVL:lvl += 1
        return lvl
  
    
    def insertElement(self, key):# insert given key in skip list
        t5 = process_time()
        update = [None]*(self.MAXLVL+1)# create update array and initialize it
        current = self.header
        
        #We initially take a pointer starting from the highest level of Skip List and
        #move the current pointer forward while key is greater than key next to current pointer
        #Else we update the current pointer and move one level down to continue our search
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and                   current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        #After reaching level 0 we move our pointer right which is our desired node
  
        current = current.forward[0]
  
        if current == None or current.key != key:
            # Generate a random level for node
            rlevel = self.randomLevel()

            if rlevel > self.level:
                for i in range(self.level+1, rlevel+1):
                    update[i] = self.header
                self.level = rlevel
  
            # create new node with random level generated
            n = self.createNode(rlevel, key)
  
            # insert node by rearranging references 
            for i in range(rlevel+1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n
                
            # If at level i the next node is not our target node then we break the loop and
            #there is no requirement to move to further level
  
            print("Successfully inserted key {}".format(key))
            global count
            count=count+1
            count_list.append(count)
        t6 = process_time()
        add_time.append(t6-t5)
        

  
    def removeElement(self, search_key):
        t3 = process_time()
        # create update array and initialize it
        update = [None]*(self.MAXLVL+1)
        current = self.header
  
        for i in range(self.level, -1, -1):
            while(current.forward[i] and current.forward[i].key < search_key):
                current = current.forward[i]
            update[i] = current
   
        current = current.forward[0]
  
        # If current node is target node
        if current != None and current.key == search_key:
            
            #We start our pointer from lowest level and rearrange our pointer to remove target node 
            #similar to the execution of singly linked list 
  
            for i in range(self.level+1):
        
             #If at level i the next node is not our target node then we break the loop and
            #there is no requirement to move to further level
  
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
  
            # Remove levels having no elements
            while(self.level>0 and self.header.forward[self.level] == None):
                self.level -= 1
            print("Successfully deleted {}".format(search_key))
            global count
            count=count-1
            count_list.append(count)
        else:
            print("This key does not exsist")
            count_list.append(count)
        t4 = process_time()
        delete_time.append(t4-t3)
        
  
    def findElement(self, key): 
        t1 = process_time()
        current = self.header
        
        #We start our pointer from highest level of skip list and move the current pointer forwards
        #while key is greater than key next to current pointer
        #Else we update the current pointer and move one level to continue our search
        
        for i in range(self.level, -1, -1):
            while(current.forward[i] and current.forward[i].key < key):
                current = current.forward[i]
  
        current = current.forward[0]
  

        if current and current.key == key:
            print("Found key ", key)
        else:
            print("This key is not present",key)
        t2 = process_time()
        search_time.append(t2-t1)


        
    
    
    def displayList(self): # Display skip list level wise
        print("\n*****Skip List******")
        global count
        print("count:",count)
        head = self.header
        for lvl in range(self.level+1):
            print("Level {}: ".format(lvl), end=" ")
            node = head.forward[lvl]
            while(node != None):
                print(node.key, end=" ")
                node = node.forward[lvl]
            print("")


# DECALRING A SKIP LIST

# In[56]:


xyz = SkipList(16, 0.5) #Here we first Declare a skiplist of maximum 16 levels


# In[57]:


abc = random.sample(range(0, 100), 50) #list of 50 randomly generated elements is created and assigned to a variable 


# PLOTTING THE GRAPH FOR INSERTION OPERATION

# In[58]:


for i in range(len(abc)): #Inserting all the randomly generated elements indivisually in the skip list 
    xyz.insertElement(abc[i]) #using for loop


# In[59]:


xyz.displayList()


# In[60]:


print("List of elements in skip list after each insert operation: ",count_list) 
print("number of time instances recorded after each insertion:",len(add_time))
print("Number of Elements in Skiplist:",count)
print("List of time taken for each insertion is:",add_time)


# In[61]:


plt.plot(count_list,add_time)
 
# naming the x axis
plt.xlabel('Size')
# naming the y axis
plt.ylabel('Insertion Time')
 
# giving a title to my graph
plt.title('SIZE BY INSERTION TIME')
 
# function to show the plot
plt.show()


# In[62]:


xyz.displayList()


# PLOTTING THE GRAPH FOR DELETION OPERATION

# In[63]:


count=count_list[-1] #Here we are setting the count of skiplist to the last element of count list
count_list=[]       

xyz.removeElement(1)
xyz.removeElement(99)
xyz.removeElement(25)
xyz.removeElement(28)
xyz.removeElement(80)
xyz.removeElement(30)
xyz.removeElement(2)
xyz.removeElement(98)


# In[64]:


print("List of elements in skip list after each deletion operation: ",count_list)
print("number of time instances recorded After deletion operation:",len(delete_time))
print("Number of Elements in Skiplist:",count)
print("Search time is:",delete_time)


# In[65]:


plt.plot(count_list,delete_time)
 
# naming the x axis
plt.xlabel('SIZE')
# naming the y axis
plt.ylabel('DELETE TIME')
 
# giving a title to my graph
plt.title('SIZE BY DELETE TIME')
 
# function to show the plot
plt.show()


# In[66]:


xyz.displayList()


# PLOTTING THE GRAPH FOR SEARCH OPERATION

# In[67]:


count=count_list[-1] #Here we are setting the count of skiplist to the last element of count list
count_list=[]

xyz.removeElement(7)
xyz.findElement(17)
xyz.removeElement(9)
xyz.findElement(19)
xyz.removeElement(96)
xyz.findElement(24)
xyz.removeElement(69)
xyz.findElement(71)
xyz.removeElement(53)
xyz.findElement(2)
xyz.removeElement(41)
xyz.findElement(75)
xyz.removeElement(50)
xyz.findElement(27)


# In[68]:


print("Number of Elements in Skiplist:",count)
print("List of elements in skip list after search Operation: ",count_list)
print("number of time instances recorded After search operation:",len(search_time))
print("Search time is:",search_time)


# In[69]:


plt.plot(count_list,search_time)
 
# naming the x axis
plt.xlabel('SIZE')
# naming the y axis
plt.ylabel('SEARCH TIME')
 
# giving a title to my graph
plt.title('SIZE BY SEARCH TIME')
 
# function to show the plot
plt.show()


# In[54]:


def Average(lst):
    return sum(lst) / len(lst)
Insertion_time_Average=Average(add_time)
Deletion_time_Average=Average(delete_time)
Search_time_Average=Average(search_time)

print("Insertion time Average:",Insertion_time_Average)
print("Deletion time Average:",Deletion_time_Average)
print("Search time Average:",Search_time_Average)


# In[ ]:




