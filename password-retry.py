#密碼輸入程式
password = 'a123456'
x = 3
while True:
	a = input('請輸入密碼: ')
	if a == password:
		print('登入成功!')
		break
	elif a != password:
		if x > 1:
			print('密碼錯誤，你還有' ,x - 1 ,'次機會')
			x = x - 1
		elif x <= 1:
			print('你輸入錯誤三次，系統將停止3分鐘。')
			break