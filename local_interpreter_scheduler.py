import sys

from src.conf.config import Setting
from src.scheduler.module import Scheduler

scheduler = Scheduler(setting=Setting)

print('- Running scheduler with stdin')
scheduler.run_forever(sys.stdin)
