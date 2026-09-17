lists_questions = [
    {
        "topic": "Lists",
        "ques": "What is the output of x = [10, 20, 30]; print(x[-1])?",
        "options": ["10", "20", "30", "Error"],
        "answer": "30"
    },
    {
        "topic": "Lists",
        "ques": "What is the output of x = [1, 2, 3, 4]; print(x[1:3])?",
        "options": ["[1, 2]", "[2, 3]", "[2, 3, 4]", "[1, 2, 3]"],
        "answer": "[2, 3]"
    },
    {
        "topic": "Lists",
        "ques": "Which method adds one item to the end of a list?",
        "options": ["insert()", "append()", "extend()", "add()"],
        "answer": "append()"
    },
    {
        "topic": "Lists",
        "ques": "What is the result of [1, 2] + [3, 4]?",
        "options": ["[4, 6]", "[1, 2, 3, 4]", "[[1, 2], [3, 4]]", "Error"],
        "answer": "[1, 2, 3, 4]"
    },
    {
        "topic": "Lists",
        "ques": "What does list.pop() do by default?",
        "options": [
            "Removes the first item",
            "Removes the last item and returns it",
            "Removes all items",
            "Returns the list length"
        ],
        "answer": "Removes the last item and returns it"
    },
    {
        "topic": "Lists",
        "ques": "What is the output? x = [3, 1, 2]; x.sort(); print(x)",
        "options": ["[3, 1, 2]", "[1, 2, 3]", "None", "Error"],
        "answer": "[1, 2, 3]"
    },
    {
        "topic": "Lists",
        "ques": "What is the output? x = [3, 1, 2]; y = x.sort(); print(y)",
        "options": ["[1, 2, 3]", "None", "True", "Error"],
        "answer": "None"
    },
    {
        "topic": "Lists",
        "ques": "Which expression creates a new sorted list without modifying the original?",
        "options": ["list.sort()", "sorted(list)", "list.order()", "sort(list)"],
        "answer": "sorted(list)"
    },
    {
        "topic": "Lists",
        "ques": "What is the output of x = [1, 2, 3]; x.insert(1, 10); print(x)?",
        "options": ["[10, 1, 2, 3]", "[1, 10, 2, 3]", "[1, 2, 10, 3]", "[1, 2, 3, 10]"],
        "answer": "[1, 10, 2, 3]"
    },
    {
        "topic": "Lists",
        "ques": "What is the output of x = [1, 2]; x.extend([3, 4]); print(x)?",
        "options": ["[1, 2, [3, 4]]", "[1, 2, 3, 4]", "[3, 4, 1, 2]", "Error"],
        "answer": "[1, 2, 3, 4]"
    },
    {
        "topic": "Lists",
        "ques": "What is the output of x = [1, 2, 3, 4]; print(x[::-1])?",
        "options": ["[1, 2, 3, 4]", "[4, 3, 2, 1]", "[4, 3, 2]", "Error"],
        "answer": "[4, 3, 2, 1]"
    },
    {
        "topic": "Lists",
        "ques": "What does x[::2] return for x = [0, 1, 2, 3, 4, 5]?",
        "options": ["[0, 1, 2]", "[1, 3, 5]", "[0, 2, 4]", "[2, 4]"],
        "answer": "[0, 2, 4]"
    },
    {
        "topic": "Lists",
        "ques": "What is the output? x = [1, 2, 3]; print(2 in x)",
        "options": ["True", "False", "2", "Error"],
        "answer": "True"
    },
    {
        "topic": "Lists",
        "ques": "What happens when remove() is called with a value that does not exist?",
        "options": ["Returns None", "Does nothing", "Raises ValueError", "Raises KeyError"],
        "answer": "Raises ValueError"
    },
    {
        "topic": "Lists",
        "ques": "What is the output? x = [1, 2, 2, 3]; print(x.count(2))",
        "options": ["1", "2", "3", "True"],
        "answer": "2"
    },
    {
        "topic": "Lists",
        "ques": "What does x.index(5) return if 5 exists at index 2?",
        "options": ["5", "1", "2", "True"],
        "answer": "2"
    },
    {
        "topic": "Lists",
        "ques": "What is the output? x = [1, 2, 3]; y = x; y.append(4); print(x)",
        "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "[4]", "Error"],
        "answer": "[1, 2, 3, 4]"
    },
    {
        "topic": "Lists",
        "ques": "What is the output? x = [1, 2, 3]; y = x.copy(); y.append(4); print(x)",
        "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "[4]", "Error"],
        "answer": "[1, 2, 3]"
    },
    {
        "topic": "Lists",
        "ques": "Which expression creates a list containing squares from 0 to 4?",
        "options": [
            "[x for x in range(5)]",
            "[x**2 for x in range(5)]",
            "[x*2 for x in range(5)]",
            "square(x for x in range(5))"
        ],
        "answer": "[x**2 for x in range(5)]"
    },
    {
        "topic": "Lists",
        "ques": "What is the output? x = [1, 2, 3, 4]; print(x[1:-1])",
        "options": ["[1, 2, 3]", "[2, 3]", "[2, 3, 4]", "[1, 4]"],
        "answer": "[2, 3]"
    }
]
dictionary_questions = [
    {
        "topic": "Dictionaries",
        "ques": "What does a dictionary use to access a value?",
        "options": ["Index", "Key", "Position", "Slice"],
        "answer": "Key"
    },
    {
        "topic": "Dictionaries",
        "ques": "What is the output? d = {'a': 10}; print(d['a'])",
        "options": ["a", "10", "'a'", "Error"],
        "answer": "10"
    },
    {
        "topic": "Dictionaries",
        "ques": "What does d.get('x') return when 'x' does not exist?",
        "options": ["0", "False", "None", "KeyError"],
        "answer": "None"
    },
    {
        "topic": "Dictionaries",
        "ques": "What does d.get('x', 100) return if 'x' does not exist?",
        "options": ["None", "0", "100", "KeyError"],
        "answer": "100"
    },
    {
        "topic": "Dictionaries",
        "ques": "What happens if you assign a new value to an existing key?",
        "options": ["A duplicate key is created", "The old value is replaced", "An error occurs", "The dictionary becomes a set"],
        "answer": "The old value is replaced"
    },
    {
        "topic": "Dictionaries",
        "ques": "What does d.keys() return?",
        "options": ["Only values", "Keys", "Key-value tuples", "Indexes"],
        "answer": "Keys"
    },
    {
        "topic": "Dictionaries",
        "ques": "What does d.values() return?",
        "options": ["Keys", "Values", "Indexes", "Key-value pairs"],
        "answer": "Values"
    },
    {
        "topic": "Dictionaries",
        "ques": "What does d.items() provide?",
        "options": ["Only keys", "Only values", "Key-value pairs", "Indexes"],
        "answer": "Key-value pairs"
    },
    {
        "topic": "Dictionaries",
        "ques": "What is the output? d = {'a': 1, 'b': 2}; print(len(d))",
        "options": ["1", "2", "3", "4"],
        "answer": "2"
    },
    {
        "topic": "Dictionaries",
        "ques": "What is the output? d = {'a': 1}; d['b'] = 2; print(d)",
        "options": [
            "{'a': 1}",
            "{'b': 2}",
            "{'a': 1, 'b': 2}",
            "Error"
        ],
        "answer": "{'a': 1, 'b': 2}"
    },
    {
        "topic": "Dictionaries",
        "ques": "Which method removes a key and returns its value?",
        "options": ["remove()", "pop()", "delete()", "discard()"],
        "answer": "pop()"
    },
    {
        "topic": "Dictionaries",
        "ques": "What does popitem() remove?",
        "options": ["The first key", "A random key", "The last key-value pair", "All keys"],
        "answer": "The last key-value pair"
    },
    {
        "topic": "Dictionaries",
        "ques": "What is the output? d = {'a': 1}; print('a' in d)",
        "options": ["True", "False", "1", "Error"],
        "answer": "True"
    },
    {
        "topic": "Dictionaries",
        "ques": "When using 'in' directly on a dictionary, what is checked?",
        "options": ["Values", "Keys", "Both", "Indexes"],
        "answer": "Keys"
    },
    {
        "topic": "Dictionaries",
        "ques": "What is the output? d = {'a': 1, 'b': 2}; print(d.get('c', 0))",
        "options": ["None", "0", "False", "Error"],
        "answer": "0"
    },
    {
        "topic": "Dictionaries",
        "ques": "What is the output? d = {'a': 1}; d.update({'b': 2}); print(d)",
        "options": [
            "{'a': 1}",
            "{'b': 2}",
            "{'a': 1, 'b': 2}",
            "Error"
        ],
        "answer": "{'a': 1, 'b': 2}"
    },
    {
        "topic": "Dictionaries",
        "ques": "Which is a valid dictionary comprehension?",
        "options": [
            "{x for x in range(5)}",
            "{x: x**2 for x in range(5)}",
            "[x: x**2 for x in range(5)]",
            "(x: x**2 for x in range(5))"
        ],
        "answer": "{x: x**2 for x in range(5)}"
    },
    {
        "topic": "Dictionaries",
        "ques": "What is the output? d = {'a': 1, 'b': 2}; print(list(d.keys()))",
        "options": ["['a', 'b']", "[1, 2]", "[('a', 1), ('b', 2)]", "Error"],
        "answer": "['a', 'b']"
    },
    {
        "topic": "Dictionaries",
        "ques": "What happens when d['missing'] is accessed and the key does not exist?",
        "options": ["Returns None", "Returns False", "Raises KeyError", "Creates the key"],
        "answer": "Raises KeyError"
    },
    {
        "topic": "Dictionaries",
        "ques": "Which loop correctly unpacks keys and values?",
        "options": [
            "for k, v in d.items():",
            "for k, v in d.keys():",
            "for k, v in d.values():",
            "for k + v in d:"
        ],
        "answer": "for k, v in d.items():"
    }
]
string_questions = [
    {
        "topic": "Strings",
        "ques": "What is the output of 'Python'[0]?",
        "options": ["P", "y", "Python", "Error"],
        "answer": "P"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'Python'[-1]?",
        "options": ["P", "n", "o", "Error"],
        "answer": "n"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'Python'[1:4]?",
        "options": ["Pyt", "yth", "ytho", "tho"],
        "answer": "yth"
    },
    {
        "topic": "Strings",
        "ques": "What does split() normally return?",
        "options": ["String", "List", "Tuple", "Set"],
        "answer": "List"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'a,b,c'.split(',')?",
        "options": ["['a', 'b', 'c']", "('a', 'b', 'c')", "'abc'", "Error"],
        "answer": "['a', 'b', 'c']"
    },
    {
        "topic": "Strings",
        "ques": "What does replace() return?",
        "options": ["The modified original string", "A new string", "None", "A list"],
        "answer": "A new string"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'hello'.replace('l', 'x')?",
        "options": ["hexxo", "hexlo", "hello", "xxhello"],
        "answer": "hexxo"
    },
    {
        "topic": "Strings",
        "ques": "What does find() return when the substring is not found?",
        "options": ["None", "-1", "False", "Error"],
        "answer": "-1"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'Python'.find('th')?",
        "options": ["1", "2", "3", "-1"],
        "answer": "2"
    },
    {
        "topic": "Strings",
        "ques": "Which method removes whitespace from both ends of a string?",
        "options": ["strip()", "trim()", "clean()", "remove()"],
        "answer": "strip()"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'python'.upper()?",
        "options": ["Python", "PYTHON", "python", "Error"],
        "answer": "PYTHON"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'PYTHON'.lower()?",
        "options": ["Python", "PYTHON", "python", "Error"],
        "answer": "python"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'hello'.count('l')?",
        "options": ["1", "2", "3", "0"],
        "answer": "2"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'hello world'.startswith('hello')?",
        "options": ["True", "False", "hello", "Error"],
        "answer": "True"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'hello.py'.endswith('.py')?",
        "options": ["True", "False", ".py", "Error"],
        "answer": "True"
    },
    {
        "topic": "Strings",
        "ques": "Which statement about strings is correct?",
        "options": [
            "Strings are mutable",
            "Strings are immutable",
            "Strings can only contain letters",
            "Strings cannot be sliced"
        ],
        "answer": "Strings are immutable"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of '-'.join(['a', 'b', 'c'])?",
        "options": ["abc", "a-b-c", "['a-b-c']", "Error"],
        "answer": "a-b-c"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of '  Python  '.strip()?",
        "options": ["'  Python  '", "'Python'", "'Python  '", "Error"],
        "answer": "'Python'"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'banana'.replace('a', 'o', 1)?",
        "options": ["bonana", "banono", "banana", "bonono"],
        "answer": "bonana"
    },
    {
        "topic": "Strings",
        "ques": "What is the output of 'Python'[::2]?",
        "options": ["Pto", "yhn", "Ptohn", "Python"],
        "answer": "Pto"
    }
]
function_questions = [
    {
        "topic": "Functions",
        "ques": "What keyword is used to define a function?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "topic": "Functions",
        "ques": "What does a function return if there is no return statement?",
        "options": ["0", "False", "None", "Error"],
        "answer": "None"
    },
    {
        "topic": "Functions",
        "ques": "What is the difference between a parameter and an argument?",
        "options": [
            "They are always identical",
            "Parameter is in definition, argument is passed during call",
            "Argument is in definition, parameter is passed during call",
            "There is no difference"
        ],
        "answer": "Parameter is in definition, argument is passed during call"
    },
    {
        "topic": "Functions",
        "ques": "What is the output? def add(a, b): return a + b; print(add(2, 3))",
        "options": ["2", "3", "5", "None"],
        "answer": "5"
    },
    {
        "topic": "Functions",
        "ques": "What happens after a return statement executes?",
        "options": [
            "The function continues normally",
            "The function stops and returns the value",
            "Only the current line stops",
            "Python restarts the function"
        ],
        "answer": "The function stops and returns the value"
    },
    {
        "topic": "Functions",
        "ques": "What does a default parameter provide?",
        "options": [
            "A value used when no argument is supplied",
            "A required argument",
            "A global variable",
            "A return value"
        ],
        "answer": "A value used when no argument is supplied"
    },
    {
        "topic": "Functions",
        "ques": "What is the output? def f(x=10): return x; print(f())",
        "options": ["None", "10", "Error", "0"],
        "answer": "10"
    },
    {
        "topic": "Functions",
        "ques": "What does *args collect?",
        "options": ["Keyword arguments", "Positional arguments", "Only strings", "Dictionary keys"],
        "answer": "Positional arguments"
    },
    {
        "topic": "Functions",
        "ques": "What does **kwargs collect?",
        "options": ["Positional arguments", "Keyword arguments", "Only integers", "Lists"],
        "answer": "Keyword arguments"
    },
    {
        "topic": "Functions",
        "ques": "What type is kwargs inside the function?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    },
    {
        "topic": "Functions",
        "ques": "What type is args inside the function?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Tuple"
    },
    {
        "topic": "Functions",
        "ques": "What is the output? def f(a, b=2): return a*b; print(f(3))",
        "options": ["3", "5", "6", "Error"],
        "answer": "6"
    },
    {
        "topic": "Functions",
        "ques": "What is the main benefit of using functions?",
        "options": [
            "They eliminate variables",
            "They improve reuse and organization",
            "They make Python faster in every case",
            "They remove the need for loops"
        ],
        "answer": "They improve reuse and organization"
    },
    {
        "topic": "Functions",
        "ques": "What is a local variable?",
        "options": [
            "A variable accessible everywhere",
            "A variable defined inside a function",
            "A dictionary key",
            "A constant"
        ],
        "answer": "A variable defined inside a function"
    },
    {
        "topic": "Functions",
        "ques": "What is the output? def f(): x = 10; print(x); f()",
        "options": ["10", "None", "Error", "x"],
        "answer": "10"
    }
]
for_questions = [
    {
        "topic": "For loops",
        "ques": "What does for x in range(5) iterate over?",
        "options": ["1 to 5", "0 to 4", "0 to 5", "1 to 4"],
        "answer": "0 to 4"
    },
    {
        "topic": "For loops",
        "ques": "What is the output of list(range(2, 7))?",
        "options": ["[2, 3, 4, 5, 6]", "[2, 3, 4, 5, 6, 7]", "[1, 2, 3, 4, 5, 6]", "[2, 7]"],
        "answer": "[2, 3, 4, 5, 6]"
    },
    {
        "topic": "For loops",
        "ques": "What does range(0, 10, 2) produce?",
        "options": ["0, 1, 2, 3", "0, 2, 4, 6, 8", "2, 4, 6, 8, 10", "1, 3, 5, 7, 9"],
        "answer": "0, 2, 4, 6, 8"
    },
    {
        "topic": "For loops",
        "ques": "What is the output? for x in [1,2,3]: print(x, end=' ')",
        "options": ["1 2 3", "0 1 2", "[1,2,3]", "Error"],
        "answer": "1 2 3"
    },
    {
        "topic": "For loops",
        "ques": "Which keyword skips the current iteration?",
        "options": ["break", "continue", "pass", "skip"],
        "answer": "continue"
    },
    {
        "topic": "For loops",
        "ques": "Which keyword stops the loop completely?",
        "options": ["stop", "continue", "break", "exit"],
        "answer": "break"
    },
    {
        "topic": "For loops",
        "ques": "What is the output? for i in range(5): if i == 3: break; print(i)",
        "options": ["0 1 2", "0 1 2 3", "3 4", "0 1 2 3 4"],
        "answer": "0 1 2"
    },
    {
        "topic": "For loops",
        "ques": "What is the output? for i in range(5): if i == 2: continue; print(i)",
        "options": ["0 1 2 3 4", "0 1 3 4", "2", "0 1"],
        "answer": "0 1 3 4"
    },
    {
        "topic": "For loops",
        "ques": "What does enumerate() commonly provide in a loop?",
        "options": ["Only values", "Index and value", "Only indexes", "Keys and values"],
        "answer": "Index and value"
    },
    {
        "topic": "For loops",
        "ques": "What is the output? for i, x in enumerate(['a','b'], start=1): print(i,x)",
        "options": ["0 a / 1 b", "1 a / 2 b", "a 1 / b 2", "Error"],
        "answer": "1 a / 2 b"
    },
    {
        "topic": "For loops",
        "ques": "What does a nested loop mean?",
        "options": [
            "A loop with no condition",
            "A loop inside another loop",
            "A loop with a function",
            "A loop that runs once"
        ],
        "answer": "A loop inside another loop"
    },
    {
        "topic": "For loops",
        "ques": "What is the output? total=0; for x in [2,4,6]: total += x; print(total)",
        "options": ["6", "10", "12", "14"],
        "answer": "12"
    },
    {
        "topic": "For loops",
        "ques": "Which is a valid list comprehension?",
        "options": [
            "[x for x in range(5)]",
            "[for x in range(5)]",
            "list x in range(5)",
            "x for [x] in range(5)"
        ],
        "answer": "[x for x in range(5)]"
    },
    {
        "topic": "For loops",
        "ques": "What is the output of [x*2 for x in range(4)]?",
        "options": ["[0, 1, 2, 3]", "[0, 2, 4, 6]", "[2, 4, 6, 8]", "[1, 2, 3, 4]"],
        "answer": "[0, 2, 4, 6]"
    },
    {
        "topic": "For loops",
        "ques": "What does zip() commonly allow you to do?",
        "options": [
            "Sort a list",
            "Combine corresponding elements from iterables",
            "Remove duplicates",
            "Reverse a list"
        ],
        "answer": "Combine corresponding elements from iterables"
    }
]
while_questions = [
    {
        "topic": "While loops",
        "ques": "When does a while loop continue running?",
        "options": [
            "While the condition is True",
            "While the condition is False",
            "Only once",
            "Forever automatically"
        ],
        "answer": "While the condition is True"
    },
    {
        "topic": "While loops",
        "ques": "What is the output? x=0; while x<3: print(x); x+=1",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "Infinite loop"],
        "answer": "0 1 2"
    },
    {
        "topic": "While loops",
        "ques": "What can cause an infinite while loop?",
        "options": [
            "The condition never becomes False",
            "Using int()",
            "Using print()",
            "Using a variable"
        ],
        "answer": "The condition never becomes False"
    },
    {
        "topic": "While loops",
        "ques": "Which keyword exits a while loop immediately?",
        "options": ["continue", "break", "pass", "return"],
        "answer": "break"
    },
    {
        "topic": "While loops",
        "ques": "Which keyword skips to the next iteration?",
        "options": ["break", "continue", "skip", "next"],
        "answer": "continue"
    },
    {
        "topic": "While loops",
        "ques": "What is the output? x=5; while x>2: x-=1; print(x)",
        "options": ["5", "4 3 2", "3 2", "2"],
        "answer": "2"
    },
    {
        "topic": "While loops",
        "ques": "What is a common use of while loops?",
        "options": [
            "Repeating until a condition changes",
            "Always iterating through a dictionary",
            "Sorting data",
            "Creating a function"
        ],
        "answer": "Repeating until a condition changes"
    },
    {
        "topic": "While loops",
        "ques": "What happens if x=1 and the condition is while x>5?",
        "options": [
            "The loop runs once",
            "The loop does not run",
            "Infinite loop",
            "Error"
        ],
        "answer": "The loop does not run"
    },
    {
        "topic": "While loops",
        "ques": "Which structure is useful for repeatedly asking for valid user input?",
        "options": ["while loop", "tuple", "set", "lambda"],
        "answer": "while loop"
    },
    {
        "topic": "While loops",
        "ques": "What must usually change inside a counting while loop to avoid an infinite loop?",
        "options": [
            "The loop condition variable",
            "The function name",
            "The print statement",
            "The data type of Python"
        ],
        "answer": "The loop condition variable"
    }
]
tuple_questions = [
    {
        "topic": "Tuples",
        "ques": "Which brackets are commonly used to create a tuple?",
        "options": ["[]", "{}", "()", "<>"],
        "answer": "()"
    },
    {
        "topic": "Tuples",
        "ques": "What is the main difference between a list and tuple?",
        "options": [
            "Tuple is immutable",
            "List is immutable",
            "Tuple cannot contain strings",
            "List cannot contain numbers"
        ],
        "answer": "Tuple is immutable"
    },
    {
        "topic": "Tuples",
        "ques": "What is the output of t=(10,20,30); print(t[1])?",
        "options": ["10", "20", "30", "Error"],
        "answer": "20"
    },
    {
        "topic": "Tuples",
        "ques": "How do you create a single-element tuple?",
        "options": ["(5)", "(5,)", "[5]", "{5}"],
        "answer": "(5,)"
    },
    {
        "topic": "Tuples",
        "ques": "What happens if you try t[0] = 10 on a tuple?",
        "options": ["It works", "TypeError", "None", "Creates a new tuple"],
        "answer": "TypeError"
    },
    {
        "topic": "Tuples",
        "ques": "What does tuple.count(x) return?",
        "options": ["Index of x", "Number of occurrences of x", "True/False", "Tuple length"],
        "answer": "Number of occurrences of x"
    },
    {
        "topic": "Tuples",
        "ques": "What does tuple.index(x) return?",
        "options": ["Number of occurrences", "Index of x", "Value of x", "None"],
        "answer": "Index of x"
    },
    {
        "topic": "Tuples",
        "ques": "What is tuple unpacking?",
        "options": [
            "Converting tuple to set",
            "Assigning tuple elements to variables",
            "Deleting tuple elements",
            "Sorting a tuple"
        ],
        "answer": "Assigning tuple elements to variables"
    },
    {
        "topic": "Tuples",
        "ques": "What is the result of a,b = (10,20)?",
        "options": ["a=20,b=10", "a=10,b=20", "Error", "a=(10,20),b=None"],
        "answer": "a=10,b=20"
    },
    {
        "topic": "Tuples",
        "ques": "What is the output of (1,2) + (3,4)?",
        "options": ["(4,6)", "(1,2,3,4)", "[1,2,3,4]", "Error"],
        "answer": "(1,2,3,4)"
    },
    {
        "topic": "Tuples",
        "ques": "Can a tuple contain a list?",
        "options": ["Yes", "No", "Only empty lists", "Only integers"],
        "answer": "Yes"
    },
    {
        "topic": "Tuples",
        "ques": "Why might a tuple be preferred for fixed data?",
        "options": [
            "It is immutable",
            "It automatically sorts",
            "It removes duplicates",
            "It only stores numbers"
        ],
        "answer": "It is immutable"
    }
]
set_questions = [
    {
        "topic": "Sets",
        "ques": "What is a major property of sets?",
        "options": [
            "They allow duplicate values",
            "They store unique values",
            "They are indexed",
            "They are immutable"
        ],
        "answer": "They store unique values"
    },
    {
        "topic": "Sets",
        "ques": "What is the result of set([1,2,2,3])?",
        "options": ["{1,2,2,3}", "{1,2,3}", "[1,2,3]", "(1,2,3)"],
        "answer": "{1,2,3}"
    },
    {
        "topic": "Sets",
        "ques": "Which method adds one element to a set?",
        "options": ["append()", "add()", "insert()", "push()"],
        "answer": "add()"
    },
    {
        "topic": "Sets",
        "ques": "Which method adds multiple elements from an iterable?",
        "options": ["extend()", "update()", "append()", "merge()"],
        "answer": "update()"
    },
    {
        "topic": "Sets",
        "ques": "What does discard() do if the element does not exist?",
        "options": ["Raises KeyError", "Does nothing", "Returns False", "Creates it"],
        "answer": "Does nothing"
    },
    {
        "topic": "Sets",
        "ques": "What does remove() do if the element does not exist?",
        "options": ["Does nothing", "Raises KeyError", "Returns None", "Creates it"],
        "answer": "Raises KeyError"
    },
    {
        "topic": "Sets",
        "ques": "What does intersection represent?",
        "options": ["Elements in either set", "Common elements", "Unique elements", "All elements"],
        "answer": "Common elements"
    },
    {
        "topic": "Sets",
        "ques": "What does union represent?",
        "options": ["Common elements only", "All unique elements", "Only first set", "Only second set"],
        "answer": "All unique elements"
    },
    {
        "topic": "Sets",
        "ques": "What is the result of {1,2,3} - {2}?",
        "options": ["{2}", "{1,3}", "{1,2,3}", "set()"],
        "answer": "{1,3}"
    },
    {
        "topic": "Sets",
        "ques": "What does 'in' check on a set?",
        "options": ["Index", "Membership", "Order", "Length"],
        "answer": "Membership"
    },
    {
        "topic": "Sets",
        "ques": "Can you access a set using set[0]?",
        "options": ["Yes", "No", "Only if sorted", "Only with integers"],
        "answer": "No"
    },
    {
        "topic": "Sets",
        "ques": "What is a common use of sets?",
        "options": [
            "Removing duplicate values",
            "Maintaining exact order",
            "Index-based access",
            "Storing key-value pairs"
        ],
        "answer": "Removing duplicate values"
    }
]
functional_questions = [
    {
        "topic": "Lambda / Map / Filter",
        "ques": "What is a lambda function?",
        "options": [
            "A function without a name, usually for a small expression",
            "A loop",
            "A dictionary",
            "A class"
        ],
        "answer": "A function without a name, usually for a small expression"
    },
    {
        "topic": "Lambda / Map / Filter",
        "ques": "What is the output of (lambda x: x * 2)(5)?",
        "options": ["5", "7", "10", "Error"],
        "answer": "10"
    },
    {
        "topic": "Lambda / Map / Filter",
        "ques": "What does map() do?",
        "options": [
            "Applies a function to each item",
            "Removes duplicates",
            "Filters only False values",
            "Sorts a list"
        ],
        "answer": "Applies a function to each item"
    },
    {
        "topic": "Lambda / Map / Filter",
        "ques": "What does filter() do?",
        "options": [
            "Transforms every element",
            "Keeps elements that satisfy a condition",
            "Sorts elements",
            "Combines dictionaries"
        ],
        "answer": "Keeps elements that satisfy a condition"
    },
    {
        "topic": "Lambda / Map / Filter",
        "ques": "What is list(map(lambda x: x*2, [1,2,3]))?",
        "options": ["[1,2,3]", "[2,4,6]", "[1,4,9]", "Error"],
        "answer": "[2,4,6]"
    },
    {
        "topic": "Lambda / Map / Filter",
        "ques": "What is list(filter(lambda x: x>2, [1,2,3,4]))?",
        "options": ["[1,2]", "[2,3,4]", "[3,4]", "[1,2,3,4]"],
        "answer": "[3,4]"
    },
    {
        "topic": "Lambda / Map / Filter",
        "ques": "What does map() return in Python 3?",
        "options": ["A list", "A map iterator", "A tuple", "A set"],
        "answer": "A map iterator"
    },
    {
        "topic": "Lambda / Map / Filter",
        "ques": "What does filter() return in Python 3?",
        "options": ["A list", "A filter iterator", "A tuple", "A dictionary"],
        "answer": "A filter iterator"
    },
    {
        "topic": "Lambda / Map / Filter",
        "ques": "Which converts a map object to a list?",
        "options": ["list()", "tuple()", "set()", "convert()"],
        "answer": "list()"
    },
    {
        "topic": "Lambda / Map / Filter",
        "ques": "What is list(map(lambda x: x+1, range(3)))?",
        "options": ["[0,1,2]", "[1,2,3]", "[2,3,4]", "[1,3,5]"],
        "answer": "[1,2,3]"
    },
    {
        "topic": "Lambda / Map / Filter",
        "ques": "What is list(filter(lambda x: x%2==0, range(6)))?",
        "options": ["[1,3,5]", "[0,2,4]", "[2,4,6]", "[0,1,2]"],
        "answer": "[0,2,4]"
    },
    {
        "topic": "Lambda / Map / Filter",
        "ques": "Which is generally more readable for complex multi-step logic?",
        "options": [
            "A very complicated lambda",
            "A normal named function",
            "A set",
            "A tuple"
        ],
        "answer": "A normal named function"
    }
]
mixed_questions = [
    {
        "topic": "Mixed",
        "ques": "What is the output? x=[1,2,3]; print(x[-2])",
        "options": ["1", "2", "3", "Error"],
        "answer": "2"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? d={'a':1}; print(d.get('b'))",
        "options": ["0", "False", "None", "Error"],
        "answer": "None"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? print(all([True,1,'hello']))",
        "options": ["True", "False", "1", "Error"],
        "answer": "True"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? print(any([False,0,'', 'Python']))",
        "options": ["True", "False", "Python", "Error"],
        "answer": "True"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? a,b = [10,20]; print(b,a)",
        "options": ["10 20", "20 10", "[10,20]", "Error"],
        "answer": "20 10"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? print(list(zip([1,2], ['a','b'])))",
        "options": [
            "[(1,'a'),(2,'b')]",
            "[(1,2),('a','b')]",
            "[1,2,'a','b']",
            "Error"
        ],
        "answer": "[(1,'a'),(2,'b')]"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? x=[3,1,2]; print(sorted(x)); print(x)",
        "options": [
            "[1,2,3] then [1,2,3]",
            "[1,2,3] then [3,1,2]",
            "None then [3,1,2]",
            "Error"
        ],
        "answer": "[1,2,3] then [3,1,2]"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? x=[1,2]; y=x; y.append(3); print(x)",
        "options": ["[1,2]", "[1,2,3]", "[3]", "Error"],
        "answer": "[1,2,3]"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? x=[1,2]; y=x.copy(); y.append(3); print(x)",
        "options": ["[1,2]", "[1,2,3]", "[3]", "Error"],
        "answer": "[1,2]"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? print([x**2 for x in range(4) if x%2==0])",
        "options": ["[0,2]", "[0,4]", "[1,4]", "[0,1,4,9]"],
        "answer": "[0,4]"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? d={'a':1,'b':2}; print([v for v in d.values() if v>1])",
        "options": ["[1]", "[2]", "[1,2]", "None"],
        "answer": "[2]"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? s={1,2,2,3}; print(len(s))",
        "options": ["2", "3", "4", "Error"],
        "answer": "3"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? t=(1,2,3); print(t[1:])",
        "options": ["(1,2)", "(2,3)", "[2,3]", "Error"],
        "answer": "(2,3)"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? print('Python'.lower().replace('p','j'))",
        "options": ["python", "jython", "Python", "Jython"],
        "answer": "jython"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? def f(x): return x*2; print(f(4))",
        "options": ["4", "6", "8", "None"],
        "answer": "8"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? nums=[1,2,3]; print(list(map(lambda x:x+10, nums)))",
        "options": ["[1,2,3]", "[11,12,13]", "[10,20,30]", "Error"],
        "answer": "[11,12,13]"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? nums=[1,2,3,4]; print(list(filter(lambda x:x%2, nums)))",
        "options": ["[1,3]", "[2,4]", "[0,2,4]", "[1,2,3,4]"],
        "answer": "[1,3]"
    },
    {
        "topic": "Mixed",
        "ques": "Which data structure is best suited for key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    },
    {
        "topic": "Mixed",
        "ques": "Which statement correctly compares sort() and sorted()?",
        "options": [
            "Both always modify the original",
            "sort() modifies the list; sorted() returns a new sorted result",
            "sorted() modifies the list; sort() returns a new list",
            "Neither can sort"
        ],
        "answer": "sort() modifies the list; sorted() returns a new sorted result"
    },
    {
        "topic": "Mixed",
        "ques": "What is the output? x=0; while x<3: x+=1; print(x)",
        "options": ["0", "1", "3", "Infinite loop"],
        "answer": "3"
    }
]
questions = (
    lists_questions
    + dictionary_questions
    + string_questions
    + function_questions
    + for_questions
    + while_questions
    + tuple_questions
    + set_questions
    + functional_questions
    + mixed_questions
)
print("Total questions:", len(questions))