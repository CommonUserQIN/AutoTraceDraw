import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600)
t.pensize(5)
t.pencolor('red')

f=open('C:\\Users\\Administrator\\Desktop\\data.txt')
datas=[]
for line in f:
    line=line.replace('\n','')
    datas.append(list(map(eval,line.split(','))))
f.close()

for i in range(len(datas)):
    t.pencolor(datas[i][3],datas[i][4],datas[i][5])
    t.fd(datas[i][0])
    if datas[i][1]:
        t.right(datas[i][2])
    else:
        t.left(datas[i][2])
t.hideturtle()
t.done()