import requests


class Mall:
    def login(self, username, password):
        r = requests.post(
            "https://litemall.hogwarts.ceshiren.com/wx/auth/login",
            json={"username": username,
                  "password": password,
                  },
            headers={'X-Litemall-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0aGlzIGlzIGxpdGVtYWxsIHRva2VuIiwiYXVkIjoiTUlOSUFQUCIsImlzcyI6IkxJVEVNQUxMIiwiZXhwIjoxNjYwNTg1NTMyLCJ1c2VySWQiOjQxLCJpYXQiOjE2NjA1NzgzMzJ9.lSXOWMf6Uy6Cqz0gk1ZNIqXHJEqJcwVxSfiTZ_lAei8'}
        )
        return r

    def getList(self, keyword, page, limit, token):
        r = requests.get(url='http://litemall.hogwarts.ceshiren.com/wx/goods/list',
                         params={'keyword': keyword,
                                 'page': page,
                                 'limit': limit
                                 },
                         headers={'X-Litemall-Token': token}
                         )
        return r

    def addGoods(self, goodsId, number, productId, token):
        url = "http://litemall.hogwarts.ceshiren.com/wx/cart/add"
        r = requests.post(url=url,
                          json={
                              'goodsId': goodsId,
                              'number': number,
                              'productId': productId,
                          },
                          headers={'X-Litemall-Token': token}
                          )
        return r

    def getCartIndex(self, token):
        """ 购物车列表接口 """
        url = "http://litemall.hogwarts.ceshiren.com/wx/cart/index"
        r = requests.get(url=url,
                         headers={'X-Litemall-Token': token}
                         )
        return r