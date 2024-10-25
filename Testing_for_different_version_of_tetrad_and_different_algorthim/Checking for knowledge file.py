#!/usr/bin/env python
# coding: utf-8

# In[88]:


# Open the file for reading into different category
with open('/Users/jonah/Downloads/Y0_Y1_Model_knolwedge(1).txt', 'r') as file:
    # Initialize a dictionary to store the categories
    categories = []
    
    # Initialize an empty string for the categore

    # Read the file line by line
    for line_number, line in enumerate(file, start=1):
        # Check if the line number is between 1 and 5
        if line_number > 3 and line_number <= 8:
            # Split the line based on the delimiter
            data = line.strip().split(' ')
#             print(data)
            categories.append(data[2:])

# Print the categories and their corresponding data
#print(categories)
    
def starts_with_number(line):
    """Returns True if the given line starts with a number, False otherwise."""
    if line.strip() == "":
        return False  # skip empty lines
    first_char = line.strip()[0]  # get the first non-space character
    return first_char.isdigit()  # check if it's a digit

import filecmp

with open('/Users/jonah/Desktop/reuslt/graspfci_1686168513146_out.txt', 'r') as file:
    # Read the file line by line
    for line2 in file:
        if starts_with_number(line2):
            data2 = line2.strip().split(' ')
            #print(data2)
            
            for sublist in categories:
#                 print(sublist)
#                 print(data2[1])
#                 print(data2[3])
                if data2[1] in sublist:
                    index1 = categories.index(sublist)
                if data2[3] in sublist:
                    index2 = categories.index(sublist)
            if index1 < index2:
                print(line2)
            #print(index1,index2)


# In[ ]:




