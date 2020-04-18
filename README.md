# pol
[![Build Status](https://travis-ci.com/Allain18/pol.svg?branch=master)](https://travis-ci.com/Allain18/pol)

Command line calculator using [reverse polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

Decimal, hexadecimal, binary and octal number are supported

## Usage
As a command line tool: __pol__

```
~$ pol
Reverse polish notation calculator
>5 10 * .
50
>0xA 0x6 + ..
0x10
>q //quit the program
~$
```

Instructions are [below](#list-of-commands)

pol can also be use as a module
```python 
import rpn_calculator
cal = rpn_calculator.Calculator()
cal.evaluate("1 2 + dec")
# print 3
```

## Install
pol can be install from pip
```
pip install rpn-calc
```
If you want to install from a source distribution, extract the tarball and run the following command
```
python setup.py install
```

## Documentation
This README is the Documentation

## [Repo](https://github.com/Allain18/pol)
The code is on github

## Own commands
You can write your own command

By default commands from file ~/.pol (if exists) are add to the calculator

You can add other files with the flag -f/--file

Command must be on the format {name_of_command:command}

Example of valid command:
```
double : 2 *
```

## Options
```
usage: pol [-h] [-v] [-l] [--ignore-local-config] [-f FILE [FILE ...]]

A RPN calculator written in python
Support decimal, hexadecimal, binary and octal

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show the version number and exit
  -l, --list            list all commands available and exit
  --ignore-local-config
                        don't add commands from ~/.pol
  -f FILE [FILE ...], --file FILE [FILE ...]
                        file with customs commands
```
## List of commands
`+` : Take 2 numbers from the stack, add them and put the result in the stack

`-` : Take 2 numbers from the stack, substracte them and put the result in the stack

`*` : Take 2 numbers from the stack, mul them and put the result in the stack

`/` : Take 2 numbers from the stack, divise them and put the result in the stack

`//` : Take 2 numbers from the stack, divise them and put the integer result in the stack

`%` : Take 2 numbers from the stack, divise them and put the remainder in the stack

`**` : Take 2 numbers from the stack, apply power and put the result in the stack

`exp` : Apply e**x to the last number of the stack

`log10` : Apply log10 to the last number of the stack

`log2` : Apply log2 to the last number of the stack

`ln` : Apply natural logarithm to the last number of the stack

`and` : Take 2 numbers from the stack, apply a bitwise "and" and put the result in the stack

`or` : Take 2 numbers from the stack, apply a bitwise "or" and put the result in the stack

`xor` : Take 2 numbers from the stack, apply a bitwise "xor" and put the result in the stack

`<<` : Take 2 numbers from the stack, apply a left shift and put the result in the stack

`>>` : Take 2 numbers from the stack, apply a right shift and put the result in the stack

`abs` : Make absolute the last value of the stack

`inv` : Inverse the last number of the stack

`neg` : Change the sign of the last number in the stack

`sin` : Replace the last number in the stack with the sine of itself (measured in radians)

`cos` : Replace the last number in the stack with the cosine of itself (measured in radians)

`tan` : Replace the last number in the stack with the tangent of itself (measured in radians)

`asin` : Replace the last number in the stack with the arc sine of itself (measured in radians)

`acos` : Replace the last number in the stack with the arc cosine of itself
        (measured in radians)

`atan` : Replace the last number in the stack with the arc tangent of itself
        (measured in radians)

`switch` : Switch the last 2 numbers of the stack

`del` : Delete the last number in the stack

`copy` : Copy the last number of the stack and add it to the stack

`pi` : Add pi to the stack

`tau` : Add tau to the stack

`e` : Add e to the stack

`dec` : Print the last number of the stack and remove it

`hex` : Print in hexadecimal format the last number of the stack and remove it

`bin` : Print in binary format the last number of the stack and remove it

`oct` : Print in octal format the last number of the stack and remove it

`s` : Print the stack

`clear` : Empty the stack

`help` : Print help; Same as pol --list

`q` : Quit the program

## License

MIT
