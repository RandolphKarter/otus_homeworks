import subprocess
from datetime import datetime
from typing import Iterator


def ps_aux_run() -> list:
    stdout = subprocess.run('ps aux', shell=True, capture_output=True, check=True).stdout.decode().splitlines()
    stdout_headers = stdout[0].split()
    stdout_data = [stdout_row.split(None, len(stdout_headers) - 1) for stdout_row in stdout[1:]]
    return [dict(zip(stdout_headers, stdout_row)) for stdout_row in stdout_data]


def get_user_processes(ps_result: list) -> dict:
    users = {user['USER'] for user in ps_result}
    users_processes_count = {}
    for user in users:
        count = 0
        for ps_result_row in ps_result:
            if ps_result_row['USER'] == user:
                count += 1
                users_processes_count.update({user: count})
    sorted_users_processes_count = dict(sorted(users_processes_count.items(), key=lambda i: i[1], reverse=True))
    return sorted_users_processes_count


def get_sum(ps_result: list, value: str) -> int | float:
    process_sum = 0
    match value:
        case '%CPU':
            for ps_result_row in ps_result:
                cpu = float(ps_result_row[value])
                process_sum += cpu
            return round(process_sum, 1)
        case 'RSS':
            for ps_result_row in ps_result:
                rss = int(ps_result_row[value])
                process_sum += rss
            return round(process_sum / 1024, 1)


def get_max_proc(ps_result: list, value: str) -> str:
    count = 0
    name = ''
    for ps_result_row in ps_result:
        match value:
            case '%CPU':
                cpu = float(ps_result_row['%CPU'])
                if cpu > count:
                    count = cpu
                    name = ps_result_row['COMMAND']
            case 'RSS':
                rss = int(ps_result_row['RSS'])
                if rss > count:
                    count = rss
                    name = ps_result_row['COMMAND']
    return name


def user_processes_generator(users_processes_dict: dict) -> Iterator[str]:
    for key, value in users_processes_dict.items():
        yield f'{key}: {value}'


stdout_list = ps_aux_run()
users_processes = get_user_processes(stdout_list)
user_process = user_processes_generator(users_processes)
mem_sum = get_sum(stdout_list, 'RSS')
cpu_sum = get_sum(stdout_list, '%CPU')
max_proc_mem = get_max_proc(stdout_list, 'RSS')
max_proc_cpu = get_max_proc(stdout_list, '%CPU')

data = [
    'Отчёт о состоянии системы:',
    f'Пользователи системы: {", ".join(list(users_processes.keys()))}',
    f'Процессов запущено: {len(stdout_list)}',
    'Пользовательских процессов:',
    f'{chr(10).join([next(user_process) for item in range(len(users_processes))])}',
    f'Всего памяти используется: {mem_sum} mb',
    f'Всего CPU используется: {cpu_sum}%',
    f'Больше всего памяти использует: {max_proc_mem[:20]}',
    f'Больше всего CPU использует: {max_proc_cpu[:20]}'
]

with open(f'{datetime.today().isoformat("-", "minutes")}-processes_report.txt', 'w') as f:
    for row in data:
        print(row)
        f.write(str(row) + '\n')
