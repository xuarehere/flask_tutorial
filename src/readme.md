

# unit_testing.py

```shell

(venv) D:\C_cache\py\flask_tutorial\src>python unit_testing.py
.F.
======================================================================
FAIL: test_sayhello_Error (__main__.SayHelloTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "unit_testing.py", line 24, in test_sayhello_Error
    self.assertEqual(rv, 'Hello, Error!')
AssertionError: 'Hello, Right!' != 'Hello, Error!'
- Hello, Right!
+ Hello, Error!


----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)

(venv) D:\C_cache\py\flask_tutorial\src>

```