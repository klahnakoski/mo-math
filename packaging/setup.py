# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from setuptools import setup
setup(
    author='Kyle Lahnakoski',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 4 - Beta","Programming Language :: Python :: 3.8","Programming Language :: Python :: 3.9","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)","Programming Language :: Python :: 3.10","Programming Language :: Python :: 3.11","Programming Language :: Python :: 3.12"],
    description='More Math! Many of the aggregates you are familiar with, but null-safe',
    extras_require={"tests":["mo-json>=6.527.24034","mo-testing>=3.124.20293"]},
    include_package_data=True,
    install_requires=["mo-dots==9.531.24035","mo-future==7.531.24035"],
    license='MPL 2.0',
    long_description="\n# More Math!  \n\nBasic math functions that have been stabilized to act well over `Null`/`None`/`NaN`\n\n\n|Branch      |Status   |\n|------------|---------|\n|master      | [![Build Status](https://app.travis-ci.com/klahnakoski/mo-math.svg?branch=master)](https://travis-ci.com/github/klahnakoski/mo-math) |\n|dev         | [![Build Status](https://app.travis-ci.com/klahnakoski/mo-math.svg?branch=dev)](https://travis-ci.com/github/klahnakoski/mo-math)    |\n\n\n\n## Overview\n\nMany of the basic math functions you know and love, with the additional benefit \nthat they do not throw exceptions and do not return `NaN`. \n\nThese functions are all module methods. Be sure you call the functions \nwith `mo_math.` prefix, like \n\n    import mo_math\n\tmo_math.abs(-42)\n\nor rename the functions\n\n    from mo_math import abs as mo_abs\n    mo_abs(-42)\n\nThis prevents confusion with the `__builtin__` functions by the same name   \n\n\n## Functions\n\nFunctions are generally [conservative](https://github.com/mozilla/ActiveData/blob/dev/docs/jx_decisive_operators.md#definitions) in the face of nulls: Specifically, they return `Null` if any of their operands are not a number.\n\nMost functions need no introduction, but some are interesting:\n\n- `round(value, decimal=7, digits=None)` - Rounds to 7 decimal points, unless specified differently.  Rounding to `decimal=0` will return an `int`. The useful parameter here is `digits`, which rounds to a specified number of significant digits.\n- `floor(value, mod=1)` - The `mod`ulo parameter is used to specify the granularity of the floor function.\n- `ceiling(value, mod=1)` - Return the smallest value, that's equal or larger than `value`, with suitable granularity.\n- `mod(value, mod=1)` - Works on floats\n- `approx_str(value)` - Round values, and return `text` (`unicode` in py2, `str` in py3) \n- `sign(v)` - Missing from the Python library \n\n\nThe all-caps aggregate functions accept only one parameter; an iterable. They are [decisive](https://github.com/mozilla/ActiveData/blob/dev/docs/jx_decisive_operators.md#definitions) operators: Non-numbers are ignored, if no values are numbers then the aggregate will return `Null`.\n\n- `COUNT(values)`\n- `SUM(values)` \n- `PRODUCT(values)` \n- `MIN(values)` \n- `MAX(values)` \n\n## Crypto\n\nThe AES and RSA crypto functions provide structured input/output on top of `cryptography` library. The intent is to reveal the signed/encrypted structures so third parties can decode the data.\n",
    long_description_content_type='text/markdown',
    name='mo-math',
    packages=["mo_math.vendor.aespython","mo_math.vendor.strangman","mo_math.vendor","mo_math"],
    url='https://github.com/klahnakoski/mo-math',
    version='7.531.24035'
)