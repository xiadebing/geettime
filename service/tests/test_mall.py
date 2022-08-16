import requests

from service.api.Mall import Mall


class TestMall:
    def setup_class(self):
        print("setup_class")

    def setup(self):
        print("setup")

    def test_login(self):
        """
        :rtype: String
        """
        r = Mall.login(self, "judy", "123456")
        assert r.status_code == 200
        print(r.text)
        assert r.json()['errmsg'] == "成功"
        print()
        if r.json()["data"]["token"]:
            return r.json()["data"]["token"]
        else:
            return ""

    def test_list(self):
        if not self.test_login():
            return "无法登陆"
        r = Mall.getList(self, "3D", "1", "10", self.test_login())
        print(r.text)
        assert r.status_code == 200
        assert r.json()['errmsg'] == "成功"

    def test_add_goods(self):
        if not self.test_login():
            return "无法登陆"
        r = Mall.addGoods(self, 1064006, 1, 76, self.test_login())
        print(r.text)
        assert r.status_code == 200
        assert r.json()['errmsg'] == "成功"

    def test_get_cart_index(self):
        if not self.test_login():
            return "无法登陆"
        r = Mall.getCartIndex(self,  self.test_login())
        print(r.text)
        assert r.status_code == 200
        assert r.json()['errmsg'] == "成功"

    def teardown(self):
        print("teardown")

    def teardown_class(self):
        print("teardown_class")