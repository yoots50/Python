def decorator(func):
    def wrapper():
        print("실행")
        func()
        print("종료")
        @decorator
        def func1():
            print("실행중")
        return func1()
    return wrapper

@decorator
def func1():
    print("실행중")

func1()
