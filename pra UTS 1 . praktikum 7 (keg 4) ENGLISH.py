Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Name = 'Hafshah Fitri Afifah'
>>> NIM = 172
>>> High = 1.55
>>> Weight = 40
>>> YearOfBirth = 1999
>>> I = (YearOfBirth, Weight, High , NIM, Name)
>>> Data = [YearOfBirth, Weight, High , NIM, Name]
>>> type(I)
<class 'tuple'>
>>> ## because variable 'I' is a string of data that stores various types of data that cannot be changed (imuttable) which are marked with usage ().
>>> I[0]
1999
>>> ## because I[0] declares the 1st index of variable 'I'
>>> a = NIM%4; I[a]
1999
>>> ## because variable 'a' is the remainder of the division of the variable 'NIM' (which is 172) with 4, which produces a value of 0. so that I[a] is I[0] which is 1999 (year of birth).
>>> type (I[a])
<class 'int'>
>>> ## because I [a] is 1999, where 1999 is included in the 'integer class' which is an integer.
>>> I[a:4]
(1999, 40, 1.55, 172)
>>> ## because I [a: 4] declares the 1st index up to the 4th index of variable 'I' which has the year of birth, weight, height, and NIM.
>>> type(I[4])
<class 'str'>
>>> ## because I [4] declares the 4th index of variable 'I', which is the variable 'Name' that is valued as 'Hafshah Fitri Afifah' where the variable belongs to the 'string class'.
>>> I[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    I[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> ## I [0] = 'ok' cannot be executed because variable 'I' is a tuple class, so it cannot be changed (imuttable).
>>> type(Data)
<class 'list'>
>>> ## because the variable 'Data' is in the form of threads that store various types of data, and its contents can be changed, which is marked by the use of [].
>>> type(Data[4])
<class 'str'>
>>> ## because Data [4] states the 4th index of the variable 'Data', that is the variable 'Name' which is valued as 'Hafshah Fitri Afifah' where the variable belongs to the 'string class'.
>>> Data [4][5]
'a'
>>> ## because Data [4][5] states the 4th index of the variable 'Data', that is variable 'Name' which is valued as 'Hafshah Fitri Afifah' where the 5th index of the variable is the letter 'a'.
>>> Data [4][a:6]
'Hafsha'
>>> ## because Data [4][a: 6] states the 4th index of the variable 'Data', that is the variable 'Name', which is valued 'Hafshah Fitri Afifah' where the 1st to 6th index of the variable 'Name' is the word 'Hafsha'.
>>> Data [0] = 'ok'; Data
['ok', 40, 1.55, 172, 'Hafshah Fitri Afifah']
>>> ## Data [0] = 'ok' is intended to change the 1st index of the list of variable 'Data' that was originally YearOfBirth (1999) to be 'ok'.
>>> Data [-a]
'ok'
>>> ## because Data[-a] states the 1st index of the new 'Data' list, which is 'ok'.
>>> range(a)
range(0, 0)
>>> ## because variable 'a' is 0, so range (a) is the range (0, 0).
