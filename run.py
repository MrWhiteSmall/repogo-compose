"""RepoGo fixed-project Compose launcher. Does not install Docker or delete volumes."""
import argparse
import subprocess
import sys
from pathlib import Path

def main():
    ap = argparse.ArgumentParser(description='中文便签练习：启动、停止、重建；保留数据卷')
    ap.add_argument('action', nargs='?', choices=['start', 'stop', 'recreate', 'status', 'check'], default='start')
    args = ap.parse_args()
    actions = {'start': ['up', '-d', '--build', '--wait', '--wait-timeout', '120'],
               'stop': ['down'], 'recreate': ['up', '-d', '--force-recreate', '--wait', '--wait-timeout', '120'],
               'status': ['ps'], 'check': ['config', '--quiet']}
    cmd = ['docker', 'compose', '-p', 'repogo-compose-lab'] + actions[args.action]
    try:
        result = subprocess.run(cmd, cwd=Path(__file__).resolve().parent)
    except FileNotFoundError:
        print('没有找到 docker。请先按 DEPLOY.md 安装并启动适用的容器引擎。', file=sys.stderr)
        return 2
    if result.returncode == 0:
        print('操作完成。入口：http://127.0.0.1:18640/；stop 只停止容器，保留数据卷。')
    return result.returncode

if __name__ == '__main__':
    raise SystemExit(main())
