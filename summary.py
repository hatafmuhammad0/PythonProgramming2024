# Python Data Types Summary Tree

#! 1. Primitive Data Types
'''
- int: 
    - Integer numbers (e.g., 5, -10, 42)
    - Immutable
    - Supports arithmetic operations

- float: 
    - Floating-point numbers (e.g., 3.14, -0.001)
    - Immutable
    - Precision up to ~15 decimal places

- complex: 
    - Complex numbers (e.g., 2 + 3j)
    - Immutable
    - Represents numbers with real and imaginary parts

- bool: 
    - Boolean values (True, False)
    - Subtype of int
    - Immutable

- NoneType: 
    - Represents a null value (None)
    - Singleton (only one instance exists)
    - Immutable
"""

#! 2. Sequence Data Types
"""
- str:
    - Text data (e.g., "hello", "world")
    - Immutable
    - Supports indexing, slicing, concatenation

- list: 
    - Ordered, mutable collection (e.g., [1, 2, 3])
    - Mutable
    - Supports indexing, slicing, adding/removing elements

- tuple: 
    - Ordered, immutable collection (e.g., (1, 2, 3))
    - Immutable
    - Supports indexing, slicing

- range: 
    - Immutable sequence of numbers (e.g., range(0, 10))
    - Immutable
    - Often used in loops
"""

#! 3. Set Data Types
"""
- set: 
    - Unordered collection of unique elements (e.g., {1, 2, 3})
    - Mutable
    - Does not support indexing or slicing
    - Supports mathematical operations (union, intersection, etc.)

- frozenset: 
    - Immutable version of set (e.g., frozenset({1, 2, 3}))
    - Immutable
    - Supports the same operations as set, but elements can't be added or removed
"""

#! 4. Mapping Data Types
"""
- dict: 
    - Key-value pairs (e.g., {"name": "John", "age": 30})
    - Mutable
    - Keys must be immutable (str, int, tuple, etc.)
    - Values can be any type
"""

#! 5. Binary Data Types
"""
- bytes: 
    - Immutable sequence of bytes (e.g., b"hello")
    - Immutable
    - Used to represent binary data

- bytearray: 
    - Mutable sequence of bytes (e.g., bytearray(b"hello"))
    - Mutable

- memoryview: 
    - Memory-efficient view of binary data (e.g., memoryview(bytes_object))
    - Mutable or immutable depending on the underlying object
"""

#! 6. Special Data Types
"""
- type: 
    - Type objects for creating and interacting with types and classes
    - Example: type(5) gives <class 'int'>

- NoneType: 
    - Only one instance: None
    - Represents the absence of value
"""

#! 7. Collection Data Types
"""
- list:
    - Ordered, mutable collection of elements (e.g., [1, "apple", 3.5])
    - Mutable
    - Supports multiple data types

- tuple:
    - Ordered, immutable collection of elements (e.g., (1, "apple", 3.5))
    - Immutable
"""

# Characteristics Summary:
"""
- Mutable types: Can be modified after creation (list, set, dict, bytearray)
- Immutable types: Cannot be changed after creation (int, float, bool, str, tuple, frozens
'''
'''
#! Type	        Mutable?	Example
List	        Yes	        my_list = [1, 2, 3]; my_list[0] = 10
Dictionary	    Yes	        my_dict = {"a": 1}; my_dict["a"] = 10
Set	            Yes	        my_set = {1, 2}; my_set.add(3)
Bytearray	    Yes	        bytearray(b"hello")[0] = 120
Int	            No	        x = 5; x = 10 (New object created)
Float	        No	        y = 3.14; y = 2.71
String	        No	        s = "hello"; s = "world"
Tuple	        No	        my_tuple = (1, 2, 3)
Frozenset	    No	        frozenset({1, 2, 3})
Bytes	        No	        b"hello"
'''