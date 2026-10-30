# 报错时先看哪一层

- **找不到docker / compose**：先完成适用环境的官方安装并启动引擎；`docker info`必须正常。脚本不自动安装、不代签协议。Windows确认使用Linux容器模式。
- **permission denied连接docker.sock**：当前账户或运行沙箱没有引擎权限。按你所在环境的正常授权流程处理，不用chmod777，不把socket对外发布。本次宿主沙箱曾阻止Python启动器子进程连接socket，获对应执行权限后原入口通过；这不是应用启动成功。
- **镜像或依赖下载超时**：需要访问Docker Hub/PyPI。核实组织允许的代理/镜像配置，保留哈希校验；不要关TLS验证、去掉固定摘要或把Token写进配置。本次Mac首次下载与哈希安装实际通过，不代表中国各网络均可直连。
- **容器显示healthy，浏览器却打不开**：先看`docker compose -p repogo-compose-lab ps`是否出现`127.0.0.1:18640->8000/tcp`。本次发现仅接internal网络时端口未发布，已通过给web单独front网络修复；store仍只接内部网络。不把健康检查当浏览器可访问证据。
- **18640端口占用**：先停止自己的同项目旧服务；若要换端口，只改compose.yaml左侧的18640，随后重建，并相应改浏览器地址。不要结束不明进程。
- **503/存储断开**：这是错误页，不是成功页。执行`docker compose -p repogo-compose-lab up -d --wait --wait-timeout 120`，读`logs --tail 30 store web`。不要因暂时读不到就删卷重来。
- **重建后似乎空了**：核对仍使用`-p repogo-compose-lab`、原compose文件和同一Docker context。不同项目名或不同引擎会读取不同卷；不要反复新增便签掩盖问题。确认有没有执行删卷或重置引擎。
- **为什么不支持任意多用户？** 这是本机教学页，没有账号隔离、生产CSRF方案、业务权限或高可用设计，不适合公网开放。便签仅用假数据，最多120字。

支持范围见SERVICE.md。调试时只分享已脱敏的必要错误、系统和版本，不提供密码、Token或整份私人日志。
