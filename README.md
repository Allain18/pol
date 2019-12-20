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
`+` : Take 2 numbers from the stack, add them and put the result in the stack

`-` : Take 2 numbers from the stack, substracte them and put the result in the stack

`*` : Take 2 numbers from the stack, mul them and put the result in the stack

`/` : Take 2 numbers from the stack, divise them and put the result in the stack

`//` : Take 2 numbers from the stack, divise them and put the integer result in the stack

`%` : Take 2 numbers from the stack, divise them and put the remainder in the stack

`**` : Take 2 numbers from the stack, apply power and put the result in the stack

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

`.` : Take one number from the stack and print it

`..` : Take one number from the stack and print it in hex format

`bin` : Take one number from the stack and print it in binary format

`s` : Print the stack

`clear` : Empty the stack

`q` : Quit the program

## License

MIT
