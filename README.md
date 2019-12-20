# pol
[![Build Status](https://travis-ci.com/Allain18/pol.svg?branch=master)](https://travis-ci.com/Allain18/pol)

Command line calculator using reverse polish notation

## Usage
As a command line tool: __pol__

pol can also be use as a module
```python 
import rpn_calculator
cal = rpn_calculator.Calculator()
cal.evaluate("1 2 +")
# print 3
```

## Install
pol can be install from pip
```
pip install rpn-calculator
```
If you want to install from a source distribution, extract the tarball and run the following command
```
python setup.py install
```

## Documentation
This README is the Documentation

## [Repo](https://github.com/Allain18/pol)
The code is on github

## List of commands
__"+"__: Take 2 numbers from the stack, add them and put the result in the stack

__"-"__: Take 2 numbers from the stack, substracte them and put the result in the stack

__"*"__: Take 2 numbers from the stack, mul them and put the result in the stack

__"/"__: Take 2 numbers from the stack, divise them and put the result in the stack

__"**"__: Take 2 numbers from the stack, apply power and put the result in the stack

__"and"__: Take 2 numbers from the stack, apply a bitwise "and" and put the result in the stack

__"or"__: Take 2 numbers from the stack, apply a bitwise "or" and put the result in the stack

__"xor"__: Take 2 numbers from the stack, apply a bitwise "xor" and put the result in the stack

__"<<"__: Take 2 numbers from the stack, apply a left shift and put the result in the stack

__">>"__: Take 2 numbers from the stack, apply a right shift and put the result in the stack

__"abs"__: Make absolute the last value of the stack

__"inv"__: Inverse the last number of the stack

__"switch"__: Switch the last 2 numbers of the stack

__"copy"__: Copy the last number of the stack and add it to the stack

__"pi"__: Add pi to the stack

__"tau"__: Add tau to the stack

__"."__: Take one number from the stack and print it

__".."__: Take one number from the stack and print it in hex format

__"bin"__: Take one number from the stack and print it in binary format

__"s"__: Print the stack

__"clear"__: Empty the stack

__"q"__: Quit the program

## License

MIT
