# Laboratory Exercise 1 and 2

![FINKI](https://upload.wikimedia.org/wikipedia/mk/6/60/%D0%9B%D0%BE%D0%B3%D0%BE-%D0%A4%D0%98%D0%9D%D0%9A%D0%98.jpg)

**Student:** Vangel Hristov

**Index**: 181233

**Course:** Multimedia Systems

# Description

Implementation of LZW and Arithmetic Coding compression algorithms using only python built-ins without any external libraries. The implementation for the both algorithms is done in two functions:
 - `encode` - which encodes the original string
 - `decode` - which decodes the encoded string back to the original string

these functions are in the `src.lzw` and `src.arithmetic` modules respectively.

Alongside the implementations, unit testing is also done for both algorithms.

To run the unit tests, run the following command:

```
make test
```
