import sys

from src.conf.config import Setting
from src.scheduler.scheduler import Scheduler

scheduler = Scheduler(setting=Setting)

print('- Running scheduler with stdin')
scheduler.run_forever(sys.stdin)
