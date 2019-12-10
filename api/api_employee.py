import requests

import api


class ApiEmployee:
    # 初始化
    def __init__(self):
        # 定义添加员工连接对象
        self.url_add= api.BASE_URL + '/api/sys/user'
        # 员工
        self.url_elployee = api.BASE_URL + '/api/sys/user/{}'
    # 添加员工
    def api_post_employee(self,username,mobile,workNumber):
        # 定义json数据
        data = {'username':username,'mobile':mobile,'workNumber':workNumber

        }
        # 调用post方法 必须return
        return requests.post(url=self.url_add,json=data,headers=api.headers)
    # 修改员工
    def api_put_employee(self):
        pass
    # 查询员工
    def api_get_employee(self):
        pass
    # 删除员工
    def api_delete_employee(self,user_id):
        return requests.delete(url=self.url_elployee.format(user_id),headers=api.headers)
