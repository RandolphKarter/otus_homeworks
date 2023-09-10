import json
import re
import subprocess
import argparse
from pprint import pprint


arg_parser = argparse.ArgumentParser(description='Log parser')
arg_parser.add_argument('-dir', '--dir_name', default='/var/log', help='Logs directory name')
arg_parser.add_argument('-file', '--file_name', default='*.log', help='Log file name')
args = arg_parser.parse_args()


def get_logs_files() -> str:
    dir_name = args.dir_name
    file_name = args.file_name
    return subprocess.run(
        f'find {dir_name} -name {file_name}',
        shell=True, capture_output=True, check=True).stdout.decode().strip()


def parse_log_files(files: str) -> list:
    print(f'Start working with files: {files}')
    result = []
    for item in files.split():
        with open(item, 'r') as f:
            regex = (r'^(?P<remote_host>[\d\.]*).*'
                     r'\[(?P<request_time>.*)\]\s'
                     r'\"(?P<request_method>\S*)\s'
                     r'(?P<request_url>\S*)\s'
                     r'(?P<request_version>.*)\"\s'
                     r'(?P<http_code>\d{,3})\s'
                     r'(?P<bytes>\S*)\s'
                     r'\"(?P<referer>.*)\"\s'
                     r'\"(?P<user_agent>.*)\"\s'
                     r'(?P<request_duration>\d*)$')
            for row in f:
                try:
                    pars_line = re.search(regex, row)
                    result.append({
                        'remote_host': pars_line.group('remote_host'),
                        'request_time': pars_line.group('request_time'),
                        'request_method': pars_line.group('request_method'),
                        'request_url': pars_line.group('request_url'),
                        'request_version': pars_line.group('request_version'),
                        'http_code': pars_line.group('http_code'),
                        'bytes': pars_line.group('bytes'),
                        'referer': pars_line.group('referer'),
                        'user_agent': pars_line.group('user_agent'),
                        'request_duration': pars_line.group('request_duration')
                    })
                except AttributeError:
                    print(f'Oops. Сould not parse this log:\n {row}')
    print(f'Finished parsing log files')
    return result


def get_count(log: list, value: str) -> dict:
    value_list = [item[value] for item in log]
    result = {}
    for item in value_list:
        if item not in result:
            result.update(({item: value_list.count(item)}))
    print(f'Completed count with value: {value}')
    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))


def get_longest_requests(log: list) -> list:
    sorted_log = sorted(log, key=lambda x: int(x['request_duration']), reverse=True)
    print(f'Finished sorting by duration')
    return sorted_log[:3]


def create_report_file(data: list):
    with open('report.json', 'w') as f2:
        pprint(data)
        s = json.dumps(data, indent=4)
        f2.write(s)


log_dict = parse_log_files(get_logs_files())
log_data = [{
    'Count of requests': len(log_dict),
    'Count by methods': get_count(log_dict, 'request_method'),
    'Top of IP': dict(list(get_count(log_dict, 'remote_host').items())[:3]),
    'Top by duration': [
        {
            'duration': item["request_duration"],
            'method': item["request_method"],
            'url': item["request_url"],
            'ip': item["remote_host"],
            'date and time': item["request_time"]
        } for item in get_longest_requests(log_dict)
    ]
}]
create_report_file(log_data)
