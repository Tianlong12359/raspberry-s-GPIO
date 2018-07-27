from gpiozero import PWMLED
from time import sleep

z = PWMLED(26)
x = PWMLED(19)
c = PWMLED(13)
v = PWMLED(6)
b = PWMLED(5)
n = PWMLED(21)
m = PWMLED(20)
d = PWMLED(16)
a = PWMLED(12)
s = PWMLED(1)

while True:
    z.value = 1
    sleep(0.5)
    z.value = 0
    sleep(0.5)
    x.value = 1
    sleep(0.5)
    x.value = 0
    sleep(0.5)
    c.value = 1
    sleep(0.5)
    c.value = 0
    sleep(0.5)
    v.value = 1
    sleep(0.5)
    v.value = 0
    sleep(0.5)
    b.value = 1
    sleep(0.5)
    b.value = 0
    sleep(0.5)
    n.value = 1
    sleep(0.5)
    n.value = 0
    sleep(0.5)
    m.value = 1
    sleep(0.5)
    m.value = 0
    sleep(0.5)
    d.value = 1
    sleep(0.5)
    d.value = 0
    sleep(0.5)
    a.value = 1
    sleep(0.5)
    a.value = 0
    sleep(0.5)
    s.value = 1
    sleep(0.5)
    s.value = 0
    sleep(0.5)