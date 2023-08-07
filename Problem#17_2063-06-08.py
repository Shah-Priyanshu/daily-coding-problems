""" 
Problem :
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory 
subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 
represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. 
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within 
our file system. For example, in the second example above, the longest absolute path is 
"dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, 
return the length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""
import random
class Solution:
    def length_longest_absolute_path(file_system):
        max_length = 0
        stack = [(0, 0)]  # (level, current_length)

        for line in file_system.split('\n'):
            level = line.count('\t')  # Calculate the level of indentation
            name = line.lstrip('\t')  # Remove the tabs to get the name of the directory/file

            # Remove any existing directories/files from the stack that are deeper than the current level
            while len(stack) > level + 1:
                stack.pop()

            if '.' in name:  # Check if it's a file
                file_length = len(name) + stack[-1][1]  # Length of the file plus the length of the current directory path
                max_length = max(max_length, file_length)
            else:
                # If it's a directory, update the stack with its length
                stack.append((level + 1, len(name) + stack[-1][1] + 1))  # +1 to account for the slash separator

        return max_length


#__main__
file_system1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
file_system2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

print(Solution.length_longest_absolute_path(file_system1))  # Output: 20
print(Solution.length_longest_absolute_path(file_system2))  # Output: 32