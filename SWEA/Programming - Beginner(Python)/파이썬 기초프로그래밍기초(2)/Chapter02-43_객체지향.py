# -*- coding: utf-8 -*-
"""
코드 재사용으로 불필요한 작업 축소, 효율성 향상
-> 개발의 생산성을 높임


1. 객체지향의 이해
객체지향 프로그래밍(Object-Oriented Programming)
객체 형성(상태와 행위로 이루어짐) - 객체를 조립 - 프로그램 형성
객체는 값을 갖는 변수와 실행코드인 메소드를 묶어 놓은 것
ex) 자동차로 비유
변수: 연료량, 속도계
메서드: 주행기능(변수와 연관된 기능)
서로 연관된 변수와 메서드를 잘 파악하고 묶어 객체를 형성하는 것이 중요!

객체는 부품화되어 재사용성을 높인다.
이러한 부품객체를 만들기 위한 청사진, 설계도, 템플릿을 설계도라고 한다.
ex) 자동차 클래스
변수: 연료량, 속도계
메서드: 주행기능

객체지향의 구성요소: 클래스(Class), 객체(Object), 메서드(Method)
클래스(Class)
* 같은 문제 도메인에 속하는 속성(attribute)과 행위(behavior)를 정의
* 객체지향 프로그램의 기본적인 사용자 정의 데이터 타입

객체(Object)
* 메모리에 로딩된 클래스를 통해 클래스를 템플릿으로 하여 메모리 상에 생성된 정보로 인스턴스라고도 한다.
* 자신 고유의 속성을 가지며 클래스에서 정의한 행위를 수행한다.
* 객체의 행위는 클래스에서 정의된 행위에 대한 정의를 공유함으로써 메모리를 효율적으로 사용가능

메서드(Method)
* 메시지(Message)라고도 부름
* 클래스로부터 생성된 객체 사용시 객체에 명령을 내리는 행위
-> '객체가 가지고 있는 메소드를 호출한다' -> '객체에 메시지를 전달한다.'
* 한 객체의 속성을 조작할 목적으로 사용
* 객체 간의 통신은 메시지 전달을 통해 이루어짐

객체지향 프로그램의 특징
1) 추상화
객체에서 공통된 속성과 행위를 추출하는 것
공통의 속성과 행위를 찾아서 타입을 정의하는 과정

추상 데이터 타입
* 데이터 타입의 표현과 연산을 캡슐화
* 접근 제어를 통해 데이터의 정보를 은닉할 수 있음
추상 데이터 타입: 클래스
추상 데이터 타입의 인스턴스: 객체
추상 데이터 타입에서 정의된 연산: 메서드

2) 상속
클래스의 속성과 행위를 하위 클래스에 물려주는 것
새로운 클래스가 기존의 클래스의 데이터와 연산을 이용할 수 있게 하는 기능

기존 클래스:   부모, 기반, 상위, 슈퍼
새로운 클래스: 자식, 파생, 하위, 서브
* 하위 클래스를 이용해 프로그램의 요구에 맞추어 클래스 수정 가능
* 클래스 간의 종속 관계를 형성하여 객체 조직화

특징
2-1) 재사용으로 인해 코드가 줄어듦(재정의 X)
2-2) 범용적인 사용 가능
     ex) object 타입의 매개변수에는 string이나 int의 객체가 쓰여도 문제되지 않음
     => string과 int 모두 object를 상속받기 때문
2-3) 자료와 메서드의 자유로운 사용 및 추가 가능

3) 다형성
다양한 형태로 나타날 수 있는 특징
어떤 한 요소에 여러 개념을 넣어 놓은 것
오버라이딩(Overriding)
* 같은 이름의 메서드가 여러 클래스에서 다른 기능을 하는 것
오버로딩(Overloading)
* 같은 이름의 메서드가 인자의 개수나 자료형에 따라 다른 기능을 하는 것

메서드 오버라이딩
* 상속을 물려 받은 자료나 메서드를 그대로 사용하지 않고 하위 클래스에서 새로 정의해 사용하는 기법
* 상위 클래스의 메서드와 동일한 서명(매개변수의 타입, 개수, 리턴타입)을 가져야 함
-> 코드의 재사용성 향상

메서드 오버로딩
클래스 내부에 동일한 이름의 행위를 여러 개 정의하는 것
* 메서드의 이름은 같고, 매개변수의 타입과 수는 서로 달라야 함
* 리턴 타입은 관계하지 않음
* 메서드 이름을 하나로 통일 가능하며, 같은 이름의 메서드에 대해 여러 종류의 매개 변수를 받을 수 있음

예시)
멤머의 조직 관리를 위한 프로그램
멤버에 대한 딕셔너리 객체 필요
더 많은 멤버를 관리하기 위해 딕셔너리 객체를 리스트 객체의 하위 항목으로 필요
def create(name, age):
    return {"name": name, "age": age}

def to_str(person):
    return "{0}\t{1}".format(person["name"], person["age"])

members = [
    create("홍길동", 20),
    create("이순신", 45),
    create("강감찬", 35)
]

for member in members:
    print(to_str(member))



2. 클래스의 정의
객체를 생성하기 위한 청사진 또는 템플릿
멤버와 관련된 추상 데이터타입이 필요하다면
-> 멤버 클래스 설계 -> 멤버 클래스 제작 -> 객체 생성(프로그램 중심 역할)

# 클래스 정의
class 클래스명:
    ...

# 객체 생성
변수 = 클래스명() -> 생성자 메서드: 클래스 이름과 동일한 메서드
* 클래스의 코드 블록 안에 필드와 메서드를 정의해 사용할 수 있음
class Person:
    pass

# 생성자 메서드, member 객체 생성
member = Person()

# 첫번째 인자의 객체가 두번째 인자의 클래스 인스턴스인지 검사
if isinstance(member, Person):
    print("member는 Person의 클래스의 인스턴스입니다.")


객체의 생성과 소멸, 그리고 self
객체를 생성하기 위해 호출하는 생성자 메서드
-> __init__ 메서드 호출

객체가 소멸되지 전에 호출되는 소멸자 메서드
-> __del__ 메서드 호출


class 클래스명:
    # 클래스 생성자 메서드 정의
    def __init__(self, 매개변수목록):

    # 클래스 소멸자 메서드 정의
    def __del__(self):
    # 객체공간의 필드와 메서드에 접근할 경우 self.식별자 형식 이용
    # self를 제외한 매개변수는 사용하지 않음
ex)   
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{0} 객체가 생성되었습니다.".format(self.name))
        
    def __del__(self):
        print("{0} 객체가 제거되었습니다.".format(self.name))


# 생성자 메서드, member 객체 생성
member = Person("홍길동", 20)

print("{0}\t{1}".format(member.name, member.age))

print(dir(member))



3. 클래스와 인스턴스의 특징
[인스턴스 메서드]
self가 가리키는 객체의 필드 정보에 접근해 특정 목적의 기능을 수행하도록 정의된 메서드
ex)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{0} 객체가 생성되었습니다.".format(self.name))
        
    def __del__(self):
        print("{0} 객체가 제거되었습니다.".format(self.name))

    # 인스턴스 메서드
    def to_str(self): # name필드와 age필드를 문자열로 반환
        return "{0}\t{1}".format(self.name, self.age)

# Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성
members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

for member in members:
    # member 객체의 to_str 메서드를 호출해 반환된 문자열 값 출력
    print(member.to_str())
    
    
[인스턴스 변수]    
클래스 내에서 self.변수 형태를 가지는 변수
객체마다 가지고 있는 객체 고유의 정보

* 멤버 필드의 접근 제한이 이루어지지 않을 경우    
-> 캡슐화된 필드로 만드는 것이 필요할 수 있음
-> 입력시 유효성 검사를 할 수 없으므로 잘못된 값이 저장될 수 있음
-> 입력 데이터의 검증을 위해 적절한 멤버 필드의 접근 제한 필요
-> 변수 앞에 언더바 2개를 써서 private field 생성
ex) self.__name = name
-> getter/setter 메서드의 제공 여부에 대한 고민 필요!
getter: 멤버를 읽어오는 메서드, setter: 멤버를 변경하는 메서드

ex)
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("{0} 객체가 생성되었습니다.".format(self.__name))
        
    def __del__(self):
        print("{0} 객체가 제거되었습니다.".format(self.__name))

    # 인스턴스 메서드
    def to_str(self): # name필드와 age필드를 문자열로 반환
        return "{0}\t{1}".format(self.__name, self.__age)

    # __name 필드의 값을 반환하는 getter메서드
    def get_name(self):
        return self.__name

    # __age 필드의 값을 반환하는 메서드
    def get_age(self):
        return self.__age
    
    # age 값을 변경하는 메서드
    def set_age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age


# Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성
members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

for member in members:
    # member 객체의 to_str 메서드를 호출해 반환된 문자열 값 출력
    print(member.to_str())

members[0].set_age(-20)


Python은 getter/setter 기능을 대신할 수 있는 데코레이터(decorator)기능도 제공
ex)
class Person:
    ...
        @property의이름.setter
        def name(self):

* 변수 이름과 같은 메서드를 만들어 사용 가능
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        print("{0} 객체가 생성되었습니다.".format(self.__name))
        
    def __del__(self):
        print("{0} 객체가 제거되었습니다.".format(self.__name))

    # 인스턴스 메서드
    def to_str(self): # name필드와 age필드를 문자열로 반환
        return "{0}\t{1}".format(self.__name, self.__age)

    # 변수처럼 사용 가능
    # __name 필드 값을 반환하는 getter메서드의 역할
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age

    # 변수처럼 사용 가능
    # __name 필드 값을 반환하는 setter 메서드의 역할
    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age


[클래스 변수]
클래스 내에서 클래스명.변수 형식으로 선언된 변수

* 클래스 변수의 정의 및 접근
# 클래스 변수 정의
class 클래스명:
    클래스변수 = 값
    ...
# 클래스 변수 접근
클래스명.클래스변수
ex)
class Person:
    count = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{0} 객체가 생성되었습니다.".format(self.__name))

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

print("현재 Person 클래스의 인스턴스는 총 {0} 개입니다.".format(Person.count))


클래스 메서드의 정의
class 클래스명:
    ...
    @classmethod
    def 클래스메서드(cls-> 클래스 자신에 대한 참조 전달, 매개변수목록):
        ...

클래스 메서드의 사용
클래스명.클래스메서드(매개변수목록)
ex)
class Person:
    count = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{0} 객체가 생성되었습니다.".format(self.__name))
    ...
    
    
    @classmethod
    def get_info(cls):
        return "현재 Person 클래스의 인스턴스는 총 {0} 개입니다.".format(cls.count)

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

# Person클래스를 통해 호출
print(Person.get_info())

for member in members:
    # member 객체의 to_str 메서드를 호출해 반환된 문자열 값 출력
    print(member.to_str())
    
    
연산자 오버로딩
연산자를 중복해서 정의
ex)
class Person:
    count = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{0} 객체가 생성되었습니다.".format(self.__name))
    ...
    
    def __gt__(self, other):
        return self.__age > other.__age
    
    def __ge__(self, other):
        return self.__age >= other.__age
    
    def __lt__(self, other):
        return self.__age < other.__age
        
    def __le__(self, other):
        return self.__age <= other.__age
    
    def __eq__(self, other):
        return self.__age == other.__age
    
    def __ne__(self, other):
        return self.__age != other

# Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성
members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

cnt = len(members)
i = 0
while True:
    print("members[{0}] > members[{1}] => {2}".format(i, i + 1, members[i] > members[i + 1]))
    i += 1
    if i == cnt - 1:
        print("members[{0}] > members[{1}] => {2}".format(i, 0, members[i] > members[0]))
        break
    
    
__str()__ 메서드
__str()__ 메서드 구현 -> str()함수에 객체를 전달해 문자열로 변환
ex)
class Person:
    count = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{0} 객체가 생성되었습니다.".format(self.__name))
    ...
    
    def __str__(self):
        # 문자열 반환
        return "{0}\t{1}".format(self.__name, self.__age)
    
    
# Person 클래스의 객체 세 개를 항목으로 가진 members 리스트 객체 생성
members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

for member in members:
    # Person 클래스의 객체 전달하면 __str__ 메서드 호출
    print(str(member))    
    
    
    
4. 클래스 상속
[클래스 상속]
부모 클래스 -> 자식 클래스
파이썬에서는 단일 상속만 지원!

class 클래스명(부모클래명):
ex)
class Parent:
    def __init__(self, family_name):
        self.__family_name = family_name
        print("Parent 클래스의 __init__() ...")
        
    @property
    def family_name(self):
        return self.__family_name
    

class Child(Parent): # Parent클래스 상속
    def __init__(self, first_name, last_name):
        Parent.__init__(self, last_name)
        # 부모 클래스의 __family_name 필드를 매개변수 last_name으로 초기화
        # super().__init__(last_name) -> super() 호출과 생성자 호출을 결합해 동일한 효과 얻음
        self.__first_name = first_name
        print("Child 클래스의 __init__() ...")
        
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
        
    @property
    def name(self):
        return "{0} {1}".format(self.family_name, self.first_name)
        # Parent 클래스의 family_name속성의 반호나 값과
        # Child 클래스의 first_name속성의 반환 값을 문자열로 만들어 반환
        
child = Child("길동", "홍")

print(child.family_name)
print(child.first_name)
print(child.name)
print("==========>")
child.first_name = "길순"
print(child.name)


[메서드 오버라이딩]
부모 클래스에 있는 메서드와 동일한 서명을 가진 메서드를
자식 클래스에서 다시 정의해 사용하는 것
ex)
class Parent:
    def __init__(self, family_name):
        self.__family_name = family_name
        print("Parent 클래스의 __init__() ...")
        
    @property
    def family_name(self):
        return self.__family_name
    
    def print_info(self):
        print("Parent: {0}".format(self.family_name))

class Child(Parent): # Parent클래스 상속
    def __init__(self, first_name, last_name):
        Parent.__init__(self, last_name)
        # super().__init__(last_name)
        self.__first_name = first_name
        print("Child 클래스의 __init__() ...")
        
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
        
    @property
    def name(self):
        return "{0} {1}".format(self.family_name, self.first_name)
        
    def print_info(self):
        Parent.print_info(self)
        # super().print_info()
        print("Child: {0}".format(self.name))
        
        
child = Child("길동", "홍")

print(child.print_info())


[오름차순/내림차순으로 정렬하기]
Student 클래스
* 프라이빗 필드를 가지고 있음
* 읽기 전용 name, gender의 프로퍼티
* 읽기, 쓰기 모두 가능한 height 프로퍼티
* 특수함수__repr__에 대한 정의를 가짐
ex)
class Student:
    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height
        
    @property
    def name(self):
        return self.__name
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height
        
    # 객체를 출력할 때 많이 사용
    def __repr__(self):
        return "{0}(name: {1}, gender:{2}, height:{3})"\
            .format(self.__class__.__name__, self.name, self.gender, self.height)
            

students = [
    Student("홍길동", "남", 176.5),
    Student("이순신", "남", 188.5),
    Student("유관순", "여", 158.4),
    Student("강감찬", "남", 182.2),
    ]
    
    
for student in students:
    print(student)
    
# sorting된 결과를 출력하고 싶을 때
print("name으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name):
    print(student)
print("name으로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name, reverse=True):
    print(student)
print("height으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height):
    print(student)
print("height으로 내름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height, reverse=True):
    print(student)

"""



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    