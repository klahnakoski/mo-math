
More Math!  
==========

Basic math functions that have been stabilized to act well over `Null`

Overview
--------

Many of the basic math functions you know and love, with the additional benefit 
that they do not throw exceptions and do not return `NaN`. Rather, all function 
return `Null` in the exceptional case.

These functions are all static methods. This ensures you call the functions 
with `Math.` prefix, like 

	Math.abs(-42)

This prevents confusion with the built-in functions by the same name   


Functions
---------

Most functions need no introduction, so are not listed here. Some of the interesting ones are:

- `Math.round(value, decimal=7, digits=None)` - Rounds to 7decimal points, unless specified differently.  Rounding to `decimal=0` will return an `int`. The useful parameter here is `digits`, which rounds to a specified number of significant digits.
- `Math.floor(value, mod=1)` - The `mod`ulo parameter is used to specify the granularity of the floor function.
- `Math.ceiling(value, mod=1)` - Return the smallest value, that's larger than `value`, with suitable granularity.
- `Math.mod(value, mod=1)` - Works on floats
- `Math.approx_str(value)` - Round values, and return unicode 
- `Math.sign(v)` - Missing from the Python library 



The all-caps aggregate functions accept only one parameter; an iterable. Null 
values are ignored. If all values are Null, the function returns Null.

- `COUNT(values)` 
- `SUM(values)` - 
- `PRODUCT(values)` - 
- `MIN(values)` - 
- `MAX(values)` - 

