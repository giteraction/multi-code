class Car():
    instance_count=0

    def __init__(self,color,speed,size):
        self.color=color
        self.speed=speed
        self.size=size
        Car.instance_count+=1
        print(f'객체수:{Car.instance_count}')
    def move(self):
        self.speed+=10

car1=Car('black',0,'big')
car2=Car('red',20,'small')
car3=Car('red',20,'small')

i=0
while True:
    i+=1
    
    if i>5:
        break
    car1.move()

print(car1.speed)

print(f'class의 총 인스턴스 개수:{car1.instance_count}')