from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='/home/taycode/Desktop/myetl/env/bin/python3 /home/taycode/Desktop/myetl/kafka_get.py')
job.minute.every(1)

cron.write()
print(job.is_valid())
