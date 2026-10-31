# 来源与许可

RepoGo 原创：中文便签页面、Flask应用、运行器、Compose/Dockerfile配置、中文手册、原创流程图及自己实跑的页面截图。本仓库是运行知识与原创示例，不是Docker官方发行版或Redis镜像的二次售卖。原创文件按本仓库MIT许可证提供。

上游：Docker Compose <https://github.com/docker/compose>，本期验证v5.5.1，tag指向 `bdafee22a6d8c58f2bc2158ce8beb9509d5687e6`，Apache-2.0。附UPSTREAM-LICENSE.txt，未打包其二进制或源码。

Redis：本例特意固定7.2分支7.2.17官方镜像，BSD-3-Clause（COPYING：<https://github.com/redis/redis/blob/7.2/COPYING>）。不把其他版本许可泛化为BSD。本仓库只引用官方镜像地址，不含镜像。

Python基础镜像、Python/Flask/Jinja/Werkzeug/Click/Redis客户端/Gunicorn等按各项目许可证分发，安装由固定哈希依赖与官方镜像渠道完成；不将教程MIT覆盖到第三方组件。基础镜像引用的官方来源 <https://hub.docker.com/_/python>，Redis <https://hub.docker.com/_/redis>。

说明依据：<https://docs.docker.com/compose/gettingstarted/>、<https://docs.docker.com/get-started/docker-concepts/running-containers/persisting-container-data/>。第三方博客仅作写作结构观察，不复制其正文、图或个人经历。AI辅助编写与图解排版；效果图片来自自己实际运行，示意图另标。

Gitee维护仓库已于2026-10-31星球首发后公开，并完成匿名访问核验：<https://gitee.com/lushengjie/repogo-compose>。当前说明同步于2026-10-31；原始交付包与发布审核记录保留首发时的实际状态。
