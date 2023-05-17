# rewrite this script to fit these details (

# src = "/data/prod/"
# dest = "/data/prod_backup/"
# subprocess.call(["rsync", "-arq", src, dest])):

# #!/usr/bin/env python3
# from multiprocessing import Pool
# def run(task):

#   # Do something with task here
#     print("Handling {}".format(task))
# if __name__ == "__main__":
#   tasks = ['task1', 'task2', 'task3']
#   # Create a pool of specific number of CPUs
#   p = Pool(len(tasks))
#   # Start each task within the pool     
#   p.map(run, tasks)


#!/usr/bin/env python
import subprocess
from multiprocessing import Pool

src = "/home/student-00-62a7a14a2e69/data/prod/"
dest = "/home/student-00-62a7a14a2e69/data/prod_backup/"

def run(task):
    subprocess.call(["rsync", "-arq", src, dest])
    print("Handling {}".format(task))

if __name__ == "__main__":
    tasks = ['file1', 'file2', 'file3']
    # Create a pool of specific number of CPUs
    p = Pool(len(tasks))
    # Start each task within the pool
    p.map(run, tasks)

