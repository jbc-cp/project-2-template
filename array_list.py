
# dd: ArrayList Data Definition
# arr is built in object array
# Rest is recursive object, of type AnyList

class ArrayList:
    def __init__(self, array, size, capacity):
        self.array = array
        self.size = size
        self. capacity = capacity
    def __eq__(self, other):
        return (type(other) == type(self)
                and other.array == self.array
                and other.size == self.size
                and other.capacity == self.capacity
                )
    def __repr__(self):
        return ("ArrayList(%r, %r, %r)" % (self.array, self.size, self.capacity))

# purpose: returns an empty list of type AnyList
# signature None -> AnyList
# function header
def empty_list():
    return ArrayList([None] * 10, 0, 10)

# purpose: inserts value val at index idx in a given array list
# signature ArrayList, int, int -> ArrayList
# function header

def add(arraylist, index, num):
    if index > arraylist.size - 1 or index < 0:
        raise IndexError()
    else:
        arraylist.size += 1
        if arraylist.size > arraylist.capacity:
            newCapacity = arraylist.capacity * 2
            newArray = [None] * newCapacity
            x = 0
            for i in range(arraylist.size):
                if i == index:
                    x = arraylist.array[i]
                    newArray[i] = num
                    newArray[i+1] = x
                else:
                    newArray[i] = arraylist.array[i]
            return ArrayList(newArray, arraylist.size, newCapacity)
        else:
            n = empty_list()
            for i in range(arraylist.size):
                if i == index:
                    x = arraylist.array[i]
                    n.array[i] = num
                    n.array[i+1] = x
                else:
                    n.array[i] = arraylist.array[i]
            return ArrayList(n, arraylist.size, arraylist.capacity)

# purpose: returns size of list
# signature array_lst -> int
# function header
def length(arraylist):
    return arraylist.size

# purpose: returns element of list
# signature array_lst, int -> int
# function header
def get(arraylist, index):
    if index > arraylist.size - 1 or index < 0:
        raise IndexError()
    else:
        return arraylist.array[index]
    
# purpose: returns element of list
# signature array_lst, int -> int
# function header
def set(arraylist, index, num):
    if index > arraylist.size -1 or index < 0:
        raise IndexError()
    else:
        arraylist.array[index] = num
        return arraylist

# purpose: returns list with removed element
# signature array_lst, int -> tuple
# function header
def remove(arraylist, index):
    if index > arraylist.size - 1 or index < 0:
        raise IndexError()
    else:
        newArray = [None]*arraylist.capacity
        arraylist.size -= 1
        for i in range(arraylist.size):
            if index == i:
                for j in range(index, arraylist.size):
                    newArray[j] = arraylist.array[j + 1]
                return arraylist.array[index], ArrayList(newArray, arraylist.size, arraylist.capacity)
            else:
                newArray[i] = arraylist.array[i]
        return arraylist.array[index], ArrayList(newArray, arraylist.size, arraylist.capacity)
