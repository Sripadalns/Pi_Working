
from subprocess import Popen

commands = [
    'python /home/pi/TV_001.py',
    'python /home/pi/TV_003.py',
    'python /home/pi/TV_005.py',    
    'python /home/pi/TV_006.py',
    'python /home/pi/TV_007.py',
    'date; sleep 5; date',
    'date; df -h; sleep 3; date',
    'date; hostname; sleep 2; date',
    'date; uname -a; date',
]
# run in parallel
processes = [Popen(cmd, shell=True) for cmd in commands]
# do other things here..
# wait for completion
for p in processes: p.wait()

