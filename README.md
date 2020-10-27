# pol
[![Build Status](https://travis-ci.com/Allain18/pol.svg?branch=master)](https://travis-ci.com/Allain18/pol)

Command line calculator using [reverse polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

Decimal, hexadecimal, binary and octal number are supported

## Usage
As a command line tool: __pol__

```
~$ pol
Reverse polish notation calculator
>5 10 * dec
50
>0xA 0x6 + hex
0x10
>q //quit the program
~$
```

Instructions are [below](#list-of-commands)

pol can also be use as a module
```python 
import rpn_calc
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

## Config file
You can write your own command

By default commands from file ~/pol.yml (if exists) are add to the calculator

You can add other files with the flag -f/--file

Config files are written in YAML

### Currently supported parameters
- shortcut: shortcut to commands (see example below)
- rounding: parameter used to round number (default: 0)

### Example of a valid config file
```YAML
shortcut:
 - double = 2 * # double the last value of the stack
 - 10* = 10 switch ** # same as 10 {x} **
rounding: 3
```
Command must be on the format {name_of_command = command}

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

`sqrt` : Replace the last number in the stack with the square root of itself

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

`acos` : Replace the last number in the stack with the arc cosine of itself (measured in radians)

`atan` : Replace the last number in the stack with the arc tangent of itself (measured in radians)

`torad` : Convert the last number from degree to radian

`todeg` : Convert the last number from radian to degree

`switch` : Switch the last 2 numbers of the stack

`del` : Delete the last number in the stack

`copy` : Copy the last number of the stack and add it to the stack

`pi` : Add pi to the stack

`tau` : Add tau to the stack

`e` : Add e to the stack

`sum` : Take all the number of the stack and add the sum

`fact` : Replace the last number in the stack with its factorial

`round` : Round the last number in the stack

`ave` : Take all the number of the stack and add the average

`dec` : Print the last number of the stack and remove it

`hex` : Print in hexadecimal format the last number of the stack and remove it

`bin` : Print in binary format the last number of the stack and remove it

`oct` : Print in octal format the last number of the stack and remove it

`ratio` : Print in integer ratio format the last number of the stack and remove it

`s` : Print the stack

`clear` : Empty the stack

`help` : Print help; Same as pol --list

`q` : Quit the program

## License

MIT
