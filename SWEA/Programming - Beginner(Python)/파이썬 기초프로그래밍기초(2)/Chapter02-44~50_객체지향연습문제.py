# -*- coding: utf-8 -*-
"""
Chapter02-44
다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.
[입력] 89, 90, 100
[출력] 국어, 영어, 수학의 총점: 279

[풀이]
class Student:
    def __init__(self, kor, mat, eng):
        self.__kor = kor
        self.__mat = mat
        self.__eng = eng
        self.__total = self.__kor + self.__mat + self.__eng
        
    def total_score(self):
        return "국어, 영어, 수학의 총점: {0}".format(self.__total)

kor, mat, eng = map(int, input().split(", "))
students = Student(kor, mat, eng)
print(students.total_score())



Chapter02-45
국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고
메서드를 호출하는 코드를 작성해봅시다.
[입력] 입력값 없음
[출력] 
대한민국
대한민국

[풀이]
class Korean:
    Nationality = "대한민국"
    
    @classmethod # 정적 메소드
    def printNationality(cls):
        return cls.Nationality
        
print(Korean.printNationality())
print(Korean.printNationality())



Chapter02-46
name 프로퍼티를 가진 Student를 부모 클래스로, major 프로퍼티를 가진
GraduateStudent 자식 클래스를 정의하고 이 클래스의 객체를
다음과 같이 문자열로 출력하는 코드를 작성하십시오.
[입력] 입력값 없음
[출력] 
이름: 홍길동
이름: 이순신, 전공: 컴퓨터

[풀이]
class Student:
    def __init__(self, name):
        self.__name = name
        
    @property
    def name(self):
        return self.__name
    
    def __repr__(self):
        print("이름: {0}".format(self.name))
        
    
class GraduateStudent(Student):
    def __init__(self, name, major):
        Student.__init__(self, name)
        # super.__init__(self, name)
        self.__major = major

    @property
    def major(self):
        return self.__major
    
    def __repr__(self):
        print("이름: {0}, 전공: {1}".format(super().name, self.major))
        
s1 = Student("홍길동")
s2 = GraduateStudent("이순신", "컴퓨터")

s1.__repr__()
s2.__repr__()



Chapter02-47
반지름 정보를 갖고, 원의 면적을 계산하는 메서드를 갖는 Circle 클래스를 정의하고,
생성한 객체의 원의 면적을 출력하는 프로그램을 작성하십시오.
[입력] 입력값 없음
[출력] 원의 면적: 12.56

[풀이]
import math

PI = math.pi

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__area = PI * (self.__radius ** 2)
        
    @property
    def area(self):
        return self.__area
    
    
circle = Circle(2)
print("원의 면적: {0:0.2f}".format(circle.area))


Chapter02-48
가로, 세로 정보을 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고,
생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.
[입력] 입력값 없음
[출력] 사각형의 면적: 20

[풀이]
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        

    def area(self):
        return self.width * self.height
        
rectangle = Rectangle(4, 5)
print("사각형의 면적: {0}".format(rectangle.area()))



Chapter02-49
Shape를 부모 클래스로 Square 자식 클래스를 정의하는 코드를 작성하십시오.
Square 클래스는 length 필드를 가지며, 0을 반환하는 Shape 클래스의 area 메서드를
length * length 값을 반환하는 메서드로 오버라이딩합니다.
[입력] 입력값 없음
[출력] 정사각형의 면적: 9

[풀이]
class Shape:
    def __init__(self, length):
        self.__length = length
    
    @property
    def length(self):
        return self.__length
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self, length)
    
    def area(self):
        return self.length ** 2

square = Square(3)
print("정사각형의 면적: {0}".format(square.area()))



Chapter02-50
Person를 부모 클래스로 Male, Female 자식 클래스를 정의하는 코드를 작성하십시오.
"Unknown"을 반환하는 Person 클래스의 getGender 메서드를 Male 클래스와 Female 클래스는
"Male", "Female" 값을 반환하는 메서드로 오버라이딩합니다.
[입력] 입력값 없음
[출력] 
Male
Female

[풀이]
class Person:
    def __init__(self, gender):
        self.gender = gender
    
    def get_Gender(self):
        return print("Unknown")


class Male(Person):
    def __init__(self, gender):
        super().__init__(gender)
    
    def get_Gender(self):
        return "Male"

class Female(Person):
    def __init__(self, gender):
        super().__init__(gender)
    
    def get_Gender(self):
        return "Female"

person1 = Male("male")
person2 = Female("female")

print(person1.get_Gender())
print(person2.get_Gender())
"""


        
        

        
        
        
        
        



