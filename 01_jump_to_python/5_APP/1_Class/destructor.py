class TestDestructor:
    def __init__(self, magic_number):
        self.magic_number = magic_number
        print("%d번 객체 생성자가 호출되었습니다." % self.magic_number)

    def __del__(self):
        print("%d번 객체 소멸자가 호출되었습니다." % self.magic_number)


def test_td_func():
    l_td = TestDestructor(2)
    input("함수 종료대기")


test_td_func()
destructorTester = TestDestructor(7)
# del destructorTester # 프로그램을 종료하기전 명시적으로 메모리 상에서 삭제하였기 때문에
# 이 객체는 소멸이 되고 소멸될 때 호출되는 소멸자가 실행된다.
input("프로그램 종료 대기")
