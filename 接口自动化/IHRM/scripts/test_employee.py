# 导包
import unittest
from 接口自动化.IHRM.api.Employee_management import EmployeeApi
from 接口自动化.IHRM.utils import common_assert
# 创建测试类
class TestEmployee(unittest.TestCase):
    employee_id = None
    # employee_id = 1288061322868658176
    # 前置处理
    def setUp(self):
        self.employee_api = EmployeeApi()
        # 调用登录接口进行登录

    # 添加员工测试用例设计
    def test01_add_employee(self):
        add_employee_data = {
            "username": "jack0709t0728888", # 用户名唯一
            "mobile": "13212072998", # 手机号唯一
            "timeOfEntry": "2020-07-09",
            "formOfEmployment": 1,
            "workNumber": "072899", # 员工ID唯一性
            "departmentName": "销售",
            "departmentId": "1266699057968001024",
            "correctionTime": "2020-07-30T16:00:00.000Z"
        }
        # 获取响应结果
        response =self.employee_api.add_employee(add_employee_data=add_employee_data)
        print(response.json())
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        common_assert(self, response)  # 剩余的值 直接使用公共断言方法的默认值即可
        # 提取员工ID
        TestEmployee.employee_id = response.json().get("data").get("id")

    # 修改员工
    def test02_update_employee(self):
        update_employee_data = {"username": "rose0728"}
        response = self.employee_api.update_employee(employee_id=TestEmployee.employee_id,update_data=update_employee_data)
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        common_assert(self,response)  # 剩余的值 直接使用公共断言方法的默认值即可


    # 查询员工
    def test03_get_employee(self):
        # 获取响应结果
        response = self.employee_api.get_employee(TestEmployee.employee_id)
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        common_assert(self, response)  # 剩余的值 直接使用公共断言方法的默认值即可


    # 删除员工
    def test04_delete_employee(self):
        # 获取响应结果
        response = self.employee_api.delete_employee(TestEmployee.employee_id)
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        common_assert(self, response)  # 剩余的值 直接使用公共断言方法的默认值即可