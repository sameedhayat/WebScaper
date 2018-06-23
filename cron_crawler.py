from crontab import CronTab

cron = CronTab(user='sameedhayat')
job = cron.new(command='python example1.py')
job.minute.every(1)

cron.write()