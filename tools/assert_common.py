# 目的:封装断言
# 创建测试方法
def AssertCommon(self,r,status_code=200,message='操作成功！'):
    # 断言状态码
    self.assertEqual(status_code,status_code)
    # 断言success
    self.assertTrue(r.json().get('success'))
    # 断言code
    self.assertEqual(10000,r.json().get('code'))
    # 断言 message
    self.assertEqual(message,r.json().get('message'))

