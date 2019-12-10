# 导包
import unittest
# 创建测试套件
from tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover('./scripts')
with open('./report/report.html','wb')as f:
    HTMLTestRunner(stream=f,title='登录,添加,修改,查询,删除').run(suite)
