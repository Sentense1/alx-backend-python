Python - Variable Annotations

Variable annotations in Python are a way to provide additional information about variables, particularly their data types, using the : symbol. Variable annotations were introduced in Python 3.6 as part of PEP 526 (Python Enhancement Proposal).

Variable annotations serve two main purposes:

Type Hinting: They can be used to indicate the expected data type of a variable, helping developers and tools like type checkers understand the intended usage of the variable.

Documentation: They can provide documentation about the variable's purpose, usage, or any other relevant information.

Here's how variable annotations work:

variable_name: data_type = value


variable_name: This is the name of the variable.
data_type: This is an optional annotation indicating the expected data type of the variable.
value: This is an optional initial value assigned to the variable.
Here's an example:

name: str = "John"
age: int

In this example:

name is a variable of type str with an initial value of "John".
age is a variable of type int, but it does not have an initial value specified.
Variable annotations can be used with various data types, including built-in types, user-defined classes, and even generic types when used with type hints from the typing module.

Here's an example of using a variable annotation with a generic type:

from typing import List

numbers: List[int] = [1, 2, 3, 4, 5]

Variable annotations are often used in combination with type hints to improve code readability and maintainability. Additionally, they can be useful when using type checkers like MyPy to catch type-related errors in your code during development.
