# 导包
import time
import unittest
from test10_unittest_tpshop import TPShopLogin
from test12_unittest_params import TPShopLogin2
from tools.HTMLTestRunner import HTMLTestRunner


# 封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TPShopLogin))
suite.addTest(unittest.makeSuite(TPShopLogin2))

# 指定报告路径
report = "./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(report, "wb") as f:
    # 创建HTMLTestRunner运行器
    runner = HTMLTestRunner(f, title="tpshop接口测试报告")

    # 执行测试套件
    runner.run(suite)