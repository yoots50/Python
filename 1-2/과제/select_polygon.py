import turtle

turtle.shape("turtle")

select = int(input("그리고 싶은 도형을 선택하세요 (1: 삼각형, 2: 사각형, 3:원) >>> "))

if select == 1:
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
elif select == 2:
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
elif select == 3:
    turtle.circle(50)

turtle.done()
