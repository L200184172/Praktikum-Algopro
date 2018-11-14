Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Name = 'Hafshah Fitri Afifah'
>>> NIM = 'L200184172'
>>> x = '1'+NIM[7:]
>>> a = int(x)
>>> b = len(Name)
>>> type(a)
<class 'int'>
>>> ## because variable 'x' that originally a string has been converted into an integer using the variable 'int ()'. it can also called type cast.
>>> type(b)
<class 'int'>
>>> ## because variable 'b' represents the number of members of the variable 'name'. and the number is included in the integer type because it is an integer (in indonesia we call it 'bilangan bulat').
>>> a/b
58.6
>>> ## because variable 'a' is 1172 and variable 'b' is 20, so 1172 is divided by 20 equals 58.6
>>> a//b
58
>>> ## because // is an arithmetic operator which when executed will produce an integer (without decimal). so 58.6 is rounded to 58.
>>> 10*(a-999)
1730
>>> ## because variable 'a' is 1172, so when it is reduced by 999 it produces a value of 173. then when multiplied by 10 produces a value of 1730. The arithmetic operation above is done by prioritizing the operations in parentheses.
>>> b**2
400
>>> ## because ** is an arithmetic operator that states the rank of a number, so that b ** 2 can also be read 'b' power 2. while variable 'b' states the number of members of the variable 'name', where the number of members of the variable 'name' is 20. so, b ** 2 is 400.
>>> a%b
12
>>> ## because % is an arithmetic operator that states modulus (the remainder of the operating division number). In the operation of the number above , variable 'a' (which is worth 1172) divided by variable 'b' (which is worth 20) produces a value of 58 with the remainder of 12. Then a% b is equal to 12.
>>> c = 12.5
>>> ## variable 'c' is rated 12.5.
>>> type(c)
<class 'float'>
>>> ## because the variable 'c' is 12.5, where 12.5 is a decimal number. and decimal numbers are class 'float'.
>>> a/c
93.76
>>> ## because / is an arithmetic operator that states division. variable 'a' is 1172 and variable 'c' is 12.5, so 1172 divided by 12.5 is equal to 93.76
>>> a//c
93.0
>>> ## because // is an arithmetic operator that states division with integer results (integers, by removing numbers behind commas).
>>> a%c
9.5
>>> ## because % is an arithmetic operator that states modulus (the remainder of the division of a number operation). in the number operation above, variable 'a' (which is 1172) divided by variable 'c' (which is 12.5) produces a value of 93 with the remainder of 9.5. then a%c equals to 9.5
>>> c>b
False
>>> ## because variable 'c' is 12.5 and variable 'b' is 20, so statement 'c' is greater than 'b' is false .
>>> type(c>b)
<class 'bool'>
>>> ## because c > b is a comparison operation where the result is true or false .
>>> a>b and b>c
True
>>> ## because variable 'a' is 1172, variable 'b' is 20, and variable 'c' is 12.5, then the statement 'a' is greater than 'b' and 'b' is greater than 'c' is true.
>>> a>1100 or b<10
True
>>> ## because the variable 'a' which is 1172 is greater than 1100, so the statement 'a' greater than 1100 is true, while the variable 'b' which is 20 is greater than 10, so the statement 'b' smaller than 10 is false. in the rule 'or', if one or both operands are true, then the condition will be true.
