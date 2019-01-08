
# More Math!  

Basic math functions that have been stabilized to act well over `Null`/`None`/`NaN`

## Overview

Many of the basic math functions you know and love, with the additional benefit 
that they do not throw exceptions and do not return `NaN`. 

These functions are all module methods. Be sure you call the functions 
with `mo_math.` prefix, like 

	mo_math.abs(-42)

This prevents confusion with the `__builtin__` functions by the same name   


## Functions

Functions are generally "conservative" in the face of nulls: Specifically, they return `Null` if any of their operands are not a number.

Most functions need no introduction, but some are interesting:

- `round(value, decimal=7, digits=None)` - Rounds to 7 decimal points, unless specified differently.  Rounding to `decimal=0` will return an `int`. The useful parameter here is `digits`, which rounds to a specified number of significant digits.
- `floor(value, mod=1)` - The `mod`ulo parameter is used to specify the granularity of the floor function.
- `ceiling(value, mod=1)` - Return the smallest value, that's larger than `value`, with suitable granularity.
- `mod(value, mod=1)` - Works on floats
- `approx_str(value)` - Round values, and return unicode 
- `sign(v)` - Missing from the Python library 


The all-caps aggregate functions accept only one parameter; an iterable. They are "decisive" operators: Non-numbers are ignored, if no values are numbers then the aggregate will return `Null`.

- `COUNT(values)`
- `SUM(values)` 
- `PRODUCT(values)` 
- `MIN(values)` 
- `MAX(values)` 

