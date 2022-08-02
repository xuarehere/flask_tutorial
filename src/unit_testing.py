import unittest

from hello import sayhello


class SayHelloTestCase(unittest.TestCase):  # 测试用例

    def setUp(self):  # 测试固件
        pass

    def tearDown(self):  # 测试固件
        pass

    def test_sayhello(self):  # 第 1 个测试
        rv = sayhello()
        self.assertEqual(rv, 'Hello!')

    def test_sayhello_to_somebody(self):         # 第 2 个测试
        rv = sayhello(to='Grey')                 # sayhello() 函数调用的返回值保存为 rv 变量（return value）
        self.assertEqual(rv, 'Hello, Grey!')     # 来判断返回值内容是否符合预期。如果断言方法出错，就表示该测试方法未通过。

    def test_sayhello_Error(self):  # 第 2 个测试
        rv = sayhello(to='Right')
        self.assertEqual(rv, 'Hello, Error!')

if __name__ == '__main__':
    unittest.main()