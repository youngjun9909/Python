class User:
  userName = "aaa"
  password = "123"
  name = '박영쥰'
  email = 'ㅇㅇㄴ'
  address

  def getUserInfo(self):
    return f'''
userName: {self.userName}
password: {self.password}
name: {self.name}
email: {self.email}
address: {address}
'''


user1 = User()
print(user1.getUserInfo("부산"))