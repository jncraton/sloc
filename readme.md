SLOC
====

In software engineering, [source lines of code (SLOC)](https://en.wikipedia.org/wiki/Source_lines_of_code) has been used as a measure of productivity and developer effort. This lab provides the opportunity to create a simple Python SLOC counter while continuing to explore string and file operations.

For the purpose of this lab, we simply define a source line of code as any line that is not blank and is not a comment.

Learning Objectives
-------------------

After completing this lab, students will be able to:

- Create Python programs that iterate over files line by line
- Write data to files for long-term storage

Task
----

Create a Python program that can count the source lines of code in a Python file. A sample program run against the included [example.py](example.py) file from this repository is shown below:

    Enter Python file for SLOC count: example.py
    Lines: 12
    SLOC: 3

The program should also write a report to `report.txt` that lists total lines, blank lines, comment lines, and source lines of code. An example `report.txt` file is included in the repository and shown below:

    Lines 12
    Blank Lines 4
    Comments 5
    SLOC 3

Handout code is provided in [sloc.py](sloc.py) that includes a definitions and tests for `is_blank` and `is_comment` helper functions. Complete these functions first.

With those helper functions available, you can then create a program that does the following:

1. Asks the user for a source file to read
2. Opens the file, properly accounting for possible errors
3. Iterates the file and computes appropriate counts
4. Displays these counts directly for the user
5. Writes counts to `report.txt` for review later

Resources
---------

The following resources may be helpful in completing this assignment:

- [PY4E Files Chapter](https://www.py4e.com/html3/07-files)
- [PY4E Strings Chapter](https://www.py4e.com/html3/06-strings)
