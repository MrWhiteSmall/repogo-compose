# 部署、环境与数据

## 前提与费用

安装官方 Docker Engine + Compose 插件，或适用于你的系统和组织的 Docker Desktop：<https://docs.docker.com/compose/install/>。安装、条款和系统权限由本人确认。Desktop 的适用收费条款不由本教程代为判断。没有模型账号、GPU、云数据库或订阅 API 依赖；下载流量、磁盘和计算资源仍有成本。

先确认 `docker info` 和 `docker compose version` 正常。固定验证版本 Compose 5.5.1；构建基础镜像及 Redis 镜像在 compose/Dockerfile 中按 SHA256 摘要固定，Python 全依赖在 `requirements-lock.txt` 中固定版本和文件哈希。首次构建需要连 Docker Hub 和 PyPI。后续依赖安全更新需要重新验证并改锁，不会悄悄跟随 latest。

启动器 Python 3.9+ 仅调用 Docker，不在主机安装 Flask。没有 Python 时，可直接在项目目录运行：

```sh
docker compose -p repogo-compose-lab up -d --build --wait --wait-timeout 120
```

## 三系统边界

| 主机 | 入口 | 本次状态 |
| --- | --- | --- |
| macOS ARM64 | `bash start.sh` / `python3 run.py start` | Apple Silicon + Docker Desktop，核心保存/重建/存储断开恢复已测；访达双击未测 |
| macOS Intel | 同上，镜像平台需要适配 | 未实测 |
| Windows x64/ARM64 | `start.cmd` / `py -3 run.py start`；Docker 使用 Linux 容器模式 | 未实测；本机 Windows VM 输入仍受阻；不是 Windows 容器镜像 |
| Linux x86_64/ARM64 | `bash start.sh`；Engine + Compose 插件 | 主机核心未通过：shenji Slurm CPU 作业222963在compute73找不到docker；未安装系统服务或提权；ARM64未测 |

Mac 内部运行 Linux 容器不代表独立 Linux 主机、Windows 或 x64 模拟均已测。不要为运行教程随意放开 Docker socket 或改全局权限。

## 端口与隔离

网页只发布 `127.0.0.1:18640`，Redis 的6379不发布到主机。两服务经内部 `lab` 网络通信；web 另接 `front` 网络以便本机访问端口。web以非root运行，只读根文件系统，临时目录用tmpfs，去掉capabilities；每服务限定128MB、0.5CPU、80进程。设置仅适用于这个低流量练习，不是通用生产配额。

已安装/引擎可用后的一键启动不等于第一次电脑环境配置“一键完成”。页面没有账号与跨设备同步；不要把端口改成公网地址直接上线。

## 数据在哪

Compose 项目名固定为 `repogo-compose-lab`，具名卷为 `repogo-compose-lab_notes`。Redis把便签写到卷中的 `/data`。Mac/Windows Desktop 的卷位于引擎的Linux虚拟机中，不等于 Finder/资源管理器可直接打开的本机同名目录。不要直接改卷内部AOF文件。

查看挂载（只读）：

```sh
docker volume inspect repogo-compose-lab_notes
docker compose -p repogo-compose-lab ps
```

`run.py stop`保留卷；删卷、重置Desktop、磁盘故障依然可使内容消失。需保留真实数据时先另行制定离线备份与恢复测试，本期没有声称已完成可靠备份。

## 更新与清理

更新前停止写入、备份数据并保留当前版本；新版在另一个明确项目/卷中验证后再迁移。重建不会自动清理旧镜像。停止本练习只用 `python3 run.py stop`，不运行全局 prune、不清理其他服务或数据卷。本期不提供自动迁移、跨主机同步、生产认证或商业托管。
