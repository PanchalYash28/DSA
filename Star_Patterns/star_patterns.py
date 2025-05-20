# 1. Print a vertical line of 10 stars
size = 10
for i in range(size):
    print('*')

# Output:
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *

# 2. Print a 10x10 grid of stars
size = 10
for i in range(size):
    print(' * ' * size)

# Output:
#  *  *  *  *  *  *  *  *  *  * 
#  *  *  *  *  *  *  *  *  *  * 
#  *  *  *  *  *  *  *  *  *  * 
#  *  *  *  *  *  *  *  *  *  * 
#  *  *  *  *  *  *  *  *  *  * 
#  *  *  *  *  *  *  *  *  *  * 
#  *  *  *  *  *  *  *  *  *  * 
#  *  *  *  *  *  *  *  *  *  * 
#  *  *  *  *  *  *  *  *  *  * 
#  *  *  *  *  *  *  *  *  *  * 

# 3. Left-aligned increasing triangle
size = 10
for i in range(size):
    print('* ' * (i + 1))

# Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * * * 
# * * * * * * * 
# * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * * * 

# 4. Left-aligned decreasing triangle
size = 10
for i in range(size):
    count = size - i
    print('* ' * count)

# Output:
# * * * * * * * * * * 
# * * * * * * * * * 
# * * * * * * * * 
# * * * * * * * 
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# 5. Right-aligned decreasing triangle
size = 10
for i in range(size):
    count = size - i
    print(' ' * i + '* ' * count)

# Output:
# * * * * * * * * * * 
#  * * * * * * * * * 
#   * * * * * * * * 
#    * * * * * * * 
#     * * * * * * 
#      * * * * * 
#       * * * * 
#        * * * 
#         * * 
#          * 

# 6. Right-aligned increasing triangle
size = 10
for i in range(size):
    count = size - i
    print(' ' * count + '* ' * (i + 1))

# Output:
#           * 
#          * * 
#         * * * 
#        * * * * 
#       * * * * * 
#      * * * * * * 
#     * * * * * * * 
#    * * * * * * * * 
#   * * * * * * * * * 
#  * * * * * * * * * * 
