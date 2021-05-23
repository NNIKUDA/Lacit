"""

Скрипт запуска демонстрации работы системы из двух сервисов и клиента

"""

import subprocess  # для запуска сервисов и клиента

with open(r'log\learn.log', 'wt') as lf:
  with open(r'log\apply.log', 'wt') as af:
    learn_proc = subprocess.Popen(
      ['python', r'dop\learn.py'],
      stdout=lf
    )
    apply_proc = subprocess.Popen(
      ['python', r'dop\apply.py'],
      stdout=af
    )
    subprocess.run(['dop\sleep.exe', '2'])
    subprocess.run(['python', r'dop\client.py'])
    for proc in [learn_proc, apply_proc]:
      proc.terminate()
      proc.wait()
