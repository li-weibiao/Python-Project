# _*_ coding:utf-8   _*_
# 开发团队: M78宇宙警备队
# 作者： li
# 开发时间: 公元前一世纪
# 文件名称: studentsystem.py
# 开发工具: sublime
import re   # 导入正则表达式模块
import os   # 导入操作系统模块


filename = "students.txt"  # 定义保存学生信息的文件名

# 字典里的键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

def menu():
	# 输出菜单
	print('''
		---------------学生信息管理系统--------------
		                                          
		  ========================================  
 		                                         
		  1. 录入学生信息                            
		  2. 查找学生信息                           
		  3. 删除学生信息                           
		  4. 修改学生信息                           
		  5. 排序                                                       
		  6. 统计学生总人数                         
		  7，显示所有学生信息                        
		  0. 退出系统                               
		  ========================================  
		  说明：通过数字或↑↓方向键选择菜单            
		--------------------------------------------
		''')


def main():
	ctrl = True     # 标记是否退出系统
	while (ctrl):
		menu()      # 显示菜单
		option = input("请选择:")   # 选择菜单项
		option_str = re.sub("\D", "", option)   # re表示正则，sub表示替换, 这里是提取数字,\D匹配一个非数字字符
		if option_str in ["0", "1", "2", "3", "4", "5", "6", "7"]:
			option_str = int(option_str)
			# 退出系统
			if option_str == 0:
				print("您已退出学生信息管理系统！")
				ctrl = False

			# 录入学生信息
			elif option_str == 1:
				insert()

			# 查找学生信息
			elif option_str == 2:
				search()

			# 删除学生信息
			elif option_str == 3:
				delete()

			# 修改学生信息
			elif option_str == 4:
				modify() 

			# 排序
			elif option_str == 5:
				sort()

			# 统计学生总人数
			elif option_str == 6:
				total()

			# 显示所有学生信息
			elif option_str == 7:
				show()


'''1. 录入学生信息'''


def insert():
	studentList = []      # 保存学生信息的列表
	mark = True           # 是否继续添加
	while mark:
		# 请输入ID
		id = input("请输入ID(如1001):")
		if not id:
			break         # id为空，跳出循环

		# 请输入名字
		name = input("请输入名字:")
		if not name:
			break         # 名字为空，跳出循环

		try:
			# 请输入英语成绩
			english = int(input("请输入英语成绩:"))

			# 请输入python成绩
			python = int(input("请输入python成绩:"))

			# 请输入c语言成绩
			c = int(input("请输入c语言成绩:"))
		except:
			print("输入无效，不是整型数值...重新录入信息")
			continue

		# 将输入的学生信息保存到字典
		student_dic = {"id":id, "name":name, "english":english, "python":python, "c":c}  

		# 将学生字典添加到学生列表中
		studentList.append(student_dic)

		# 是否继续添加 n\y
		inputMark = input("是否继续添加？ (y/n):")
		if inputMark == "y":       # 继续添加
			mark = True
		else:                      # 不继续添加
			mark = False
	save(studentList)              # 将学生信息保存到文件
	print("学生信息录入完毕！")


# 将学生信息保存到文件
def save(student):
	try:
		students_txt = open(filename, "a")   # 以追加模式打开
	except Exception as e:
		students_txt = open(filename, "w")   # 文件不存在，创建文件并打开
	for info in student:
		students_txt.write(str(info) + "\n")  # 按行存储，添加换行符
	students_txt.close()      # 关闭文件

# r                    以只读方式打开文件。文件的指针将会放在文件的开头,这是默认模式。如果文件不存在抛出异常
# w                    以只写方式打开文件。如果文件存在会被覆盖。如果文件不存在,创建新文件
# a                    以追加方式打开文件。如果该文件已存在,文件指针将会放在文件的结尾。如果文件不存在,创建新文件进行写入
# r+                   以读写方式打开文件。文件的指针将会放在文件的开头。如果文件不存在,抛出异常
# w+                   以读写方式打开文件。如果文件存在会被覆盖。如果文件不存在,创建新文件
# a+                   以读写方式打开文件。如果该文件已存在,文件指针将会放在文件的结尾。如果文件不存在,创建新文件进行写入


'''2 查找学生信息'''


def search():
	mark = True
	student_query = []  # 保存查询结果的学生列表
	while mark:
		id = ""
		name = ""
		if os.path.exists(filename):
			mode = input("按ID查输入1；按姓名查输入2：")
			if mode == "1":  # 按学生编号查询
				id = input("请输入学生ID：")
			elif mode == "2":  # 按学生姓名查询
				name = input("请输入学生姓名：")
			else:
				print("您的输入有误，请重新输入！")
				search()  # 重新查询
			with open(filename, 'r') as file:  # 打开文件
				student = file.readlines()  # 读取全部内容
				for list in student:
					d = dict(eval(list))  # 字符串转字典
					if id is not "":  # 判断是否按ID查询
						if d['id'] == id:
							student_query.append(d)  # 将找到的学生信息保存到列表中
						elif name is not "":  # 判断是否按姓名查询
							if d['name'] == name:
								student_query.append(d)  # 将找到的学生信息保存到列表中
				show_student(student_query)  # 显示查询结果,调用show_student()函数，在后面 7 显示所有学生信息那里定义
				student_query.clear()  # 清空列表
				inputMark = input("是否继续查询？（y/n）:")
				if inputMark == "y":
					mark = True
				else:
					mark = False
		else:
			print("暂未保存数据信息...")
			return


'''3 删除学生成绩信息'''


def delete():
	mark = True  # 标记是否循环
	while mark:
		studentId = input("请输入要删除的学生ID：")
		if studentId is not "":  # 判断是否输入要删除的学生
			if os.path.exists(filename):  # 判断文件是否存在，os.path模块主要用于获取文件的属性，
			# 在这里的exists是判断路径path是否存在，存在返回True,不存在，返回False。参考地址:https://www.runoob.com/python/python-os-path.html
				with open(filename, 'r') as rfile:  # 打开文件
					student_old = rfile.readlines()  # 读取全部内容
			else:
				student_old = []
			ifdel = False  # 标记是否删除
			if student_old:  # 如果存在学生信息
				with open(filename, 'w') as wfile:  # 以写方式打开文件,以空白文件覆盖新文件的方式
					d = {}  # 定义空字典
					for list in student_old:
						d = dict(eval(list))  # 字符串转字典，eval函数就是实现list、dict、tuple与str之间的转化
						if d['id'] != studentId:
							wfile.write(str(d) + '\n')  # 将一条学生信息写入文件，因为会重新写入新文件，以空白文件会覆盖新文件，那么不等于要删除的学生ID就将它重新写入文件
						else:
							ifdel = True  # 标记已经删除， 等于要删除的学生ID就不管它。
					if ifdel:
						print("ID为 %s 的学生信息已经被删除..." % studentId)
					else:
						print("没有找到ID为 %s 的学生信息..." % studentId)
			else:  # 不存在学生信息
				print("无学生信息...")
				break  # 退出循环
			show()  # 显示全部学生信息
			inputMark = input("是否继续删除？ (y/n)")
			if inputMark == "y":
				mark = True  # 继续删除
			else:
				mark = False  # 退出删除学生信息功能


'''4 修改学生成绩信息'''


def modify():
	show()  # 显示全部学生信息
	if os.path.exists(filename):  # 判断文件是否存在
		with open(filename, 'r') as rfile:  # 打开文件
			student_old = rfile.readlines()  # 读取全部内容
	else:
		return
	student_id = input("请输入要修改的学生ID：")
	with open(filename, 'w') as wfile:  # 以只写模式打开文件
		for student in student_old:
			d = dict(eval(student))  # 字符串转字典
			if d["id"] == student_id:  # 是否为要修改的学生
				print("找到了这名学生，可以修改他的信息！")
				while True:  # 输入要修改的信息
					try:
						d["name"] = input("请输入姓名：")
						d["english"] = int(input("请输入英语成绩："))
						d["python"] = int(input("请输入python成绩："))
						d["c"] = int(input("请输入c语言成绩："))
					except:
						print("您的输入有误，请重新输入！")
					else:  # 跳出循环
						break
				student = str(d)  # 将字典转换为字符串
				wfile.write(student + "\n")  # 将修改的信息写入到文件
				print("修改成功！")
			else:
				wfile.write(student)  # 将未修改的信息写入到文件(老文件的信息写入到文件)
	mark = input("是否继续修改其他学生信息？ (y/n)：")
	if mark == "y":
		modify()  # 重新执行修改操作
# 上面代码中，调用 eval()函数，用于执行一个字符串表达式并且返回表达式的值。


'''5 排序'''


def sort():
	show()  # 显示全部学生信息
	if os.path.exists(filename):  # 判断文件是否存在
		with open(filename, 'r') as file:  # 以只读模式打开文件
			student_old = file.readlines()  # 读取全部内容
			student_new = [] 
		for list in student_old:
			d = dict(eval(list))  # 字符串转字典
			student_new.append(d)  # 将转换后的字典添加到列表中
	else:
		return
	ascORdesc = input("请选择（0升序；1降序）：")
	if ascORdesc == "0":  # 按升序排序
		ascORdescBool = False  # 标记变量，为False表示升序排序
	if ascORdesc == "1":  # 按降序排序
		ascORdescBool = True  # 标记变量，为True表示降序排序
	else:
		print("您的输入有误，请重新输入！")
		sort()
	mode = input("请选择排序方式（1按英语成绩排序；2按python成绩排序；3按C语言成绩排序；0按总成绩排序）：")
	if mode == "1":  # 按英语成绩排序
		student_new.sort(key=lambda x: x["english"], reverse=ascORdescBool)  # 在排序时，通过lambda表达式指定的排序规则，key=lambda x: x["english"] 表示按字典的english键进行排序；reverse = ascORdescBool 表示是否为降序排序，ascORdescBool的值为True，表示降序排序
	elif mode == "2":  # 按Python成绩排序
		student_new.sort(key=lambda x: x["python"], reverse=ascORdescBool)
	elif mode == "3":  # 按C语言成绩排序
		student_new.sort(key=lambda x: x["c"], reverse=ascORdescBool)
	elif mode == "0":  # 按总成绩排序
		student_new.sort(key=lambda x: x["english"] + x["python"] + x["c"], reverse=ascORdescBool)
	else:
		print("您的输入有误，请重新输入！")
		sort()
	show_student(student_new)  # 显示排序结果
# 上面的代码中，调用列表的sort()方法实现排序


'''6 统计学生总数'''


def total():
	if os.path.exists(filename):  # 判断文件是否存在
		with open(filename, 'r') as rfile:  # 打开文件
			student_old = rfile.readlines()  # 读取全部内容
			if student_old:
				print("一共有 %d 名学生" % len(student_old))  # 统计学生人数
			else:
				print("还没有录入学生信息！")
	else:
		print("暂未保存数据信息...")


'''7 显示所有学生信息'''


def show():
	student_new = []
	if os.path.exists(filename):  # 判断文件是否存在
		with open(filename, 'r') as rfile:  # 打开文件
			student_old = rfile.readlines()  # 读取全部内容
		for list in student_old:
			student_new.append(eval(list))  # 将找到的学生信息保存到列表中
		if student_new:
			show_student(student_new)
	else:
		print("暂未保存数据信息...")
# 上面的代码，调用show_student()函数，将学生信息显示到控制台上。


# 将保存在列表中的学生信息显示出来
def show_student(studentList):
	if not studentList:  # 如果没有要显示的数据
		print("(o@.@o) 无数据信息 (o@.@o) \n")
		return
	# 定义标题显示格式
	format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
	print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))  # 按指定格式显示标题
	# 定义具体内容显示格式
	format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
	for info in studentList:  # 通过for循环将列表中的数据全部显示出来
		print(format_data.format(info.get("id"),
								info.get("name"), str(info.get("english")),str(info.get("python")),
								str(info.get("c")),
								str(info.get("english") + info.get("python") + info.get("c")).center(12)))
    # 上面的代码中，使用了字符串的format()方法对其进行格式化。其中在指定字符串的显示格式时，数字表示所占宽度，符号“^”表示居中显示，“\t”表示添加一个制表符


if __name__ == "__main__":
	main()



# 小结：本项目主要使用 Python语言开发了一个学生信息管理系统,项目的核心是对文件、列表和字典进
# 行操作。其中,对文件进行操作是用来永久保存学生信息;而将学生信息以字典的形式存储到列表
# 中,是为了方便对学生信息的查找、修改和删除。通过本项目应该熟练并掌握对文
# 件进行创建、打开和修改等操作的方法,其次还应该掌握对字典和列表进行操作的方法,尤其是对
# 列表进行自定义排序规则,这是本项目的难点,需读者仔细体会并做到融会贯通
