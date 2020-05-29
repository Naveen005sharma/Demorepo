#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Node:
    
    element = None 
    left_child_address = None 
    right_child_address = None 
    parent_address = None 


# In[10]:


import numpy as np


# In[11]:


random_numbers = np.random.randint(low=78,high=150,size=10)


# In[12]:


random_numbers


# In[13]:


root_node = None


# In[14]:


def create_binary_search_tree(function_root_node,element_of_node):
    
    if function_root_node == None:
        
        function_root_node = Node()
        
        function_root_node.element = element_of_node
        
        return function_root_node
    
    elif element_of_node <= function_root_node.element:
        
        function_root_node.left_child_address = create_binary_search_tree(function_root_node.left_child_address,element_of_node)
        
    elif element_of_node > function_root_node.element:
        
        function_root_node.right_child_address = create_binary_search_tree(function_root_node.right_child_address,element_of_node)
        
    return function_root_node


# In[15]:


for single_element in random_numbers:
    
    root_node = create_binary_search_tree(root_node,single_element)


# In[19]:


def post_order_traversal(root_node):
    
    if root_node == None:
        
        return 
    
    print(root_node.element)
    
    post_order_traversal(root_node.right_child_address)
    post_order_traversal(root_node.left_child_address)
    
   


# In[20]:


post_order_traversal(root_node)


# In[18]:


def BFS_traversal(root_node):
    
    bfs = []
    
    bfs.append(root_node)
    
    while lne(bfs) != 0:
        
        


# In[ ]:




