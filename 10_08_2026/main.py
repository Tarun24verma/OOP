import geometry
import main2

print(geometry.area_square(5))
print(geometry.area_circle(5))


student1 = main2.Student(name='Ali', roll=12, marks=88)
student1.display()
print('Grade:', student1.grade())

account = main2.BankAccount(balance=1000)
print('Balance before interest:', account.balance)
print('Balance after interest:', account.apply())