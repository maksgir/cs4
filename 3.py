from datetime import datetime
from main import WithoutLibs
from second import with_libs

start_time = datetime.now()
for i in range(10):
    a = WithoutLibs(f' {i}')
    a.go()
t1 = datetime.now() - start_time
print(t1)

start_time = datetime.now()
for i in range(10):
    with_libs(f' {i}')
t2 = datetime.now() - start_time
print(t2)
