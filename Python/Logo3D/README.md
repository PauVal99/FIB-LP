# Logo3D

Logo3D is a declarative and interpreted programming language with 3D drawing build in functions.

## Installation

```bash
pip3 install -r requirements.txt
antlr4 -Dlanguage=Python3 -no-listener -visitor Logo3D.g
```

## Usage

Execute a program:
```bash
python3 Logo3D.py program.l3d
```

Execute a program starting in an arbitrary proc, `main()` by default:
```bash
python3 Logo3D.py program.l3d proc param1 param2
```

Usage of [Turtle3D.py](Turtle3D.py), for further documentation read source file:
```python
from Turtle3D import Turtle3D

turtle = Turtle3D

turtle.forward(3)
turtle.right(45)
turtle.forward(2)
```

## Description

All Logo3D instructions are implemented moreover module. Proc definitions and calls must have *(* after its name. Whitespace are not permitted.

 + `foo()` -> is ok.
 + `foo ()` -> syntax error.

Conditional expressions can be non-boolean, everything except 0 is *True*.`1+1` is resolved as *True*. By default, all variables initialize with 0.

Some execution exceptions are implemented and break current execution.

<br/>

All Turtle3D methods are implemented and documented.

## Tests

There are some sample tests:
 + [test-fizzbuzz.l3d](test-fizzbuzz.l3d)
 + [test-euclides.l3d](test-euclides.l3d)
 + [test-quadrat_blau.l3d](test-quadrat_blau.l3d)
 + [test-espiral.l3d](test-espiral.l3d)

## Author

Pau Val
 + **DNI:** 46470753N
 + **email:** [pau.val@estudiantat.upc.edu](mailto:pau.val@estudiantat.upc.edu)