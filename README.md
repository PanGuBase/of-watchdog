## 基于 of-watchdog 的自研 FaaS 定时调度平台

- 执行内部清理任务
- 执行爬虫同步任务
- 承接语言（node、python）
- 提供在线编辑代码的功能，编辑完直接部署
- 与 cron-connector 构建定时任务平台
- 集成wasm作为高并发调用

```
export fprocess="python /Users/gaozhe/GolandProjects/vpnbook/dev/of-watchdog/test/index.py"
export mode=serializing
go build .
brew install faas-cli
```

## 原生of-watchdog

```
1. http: 不使用该mode, http或者grpc服务将直接使用k8s调度    （使用 http request）
2. serializing：原生 watchdog模式    （底层 cmd 直接执行命令）  脚本场景
3. streaming: 流模式  （底层 cmd 直接执行命令）  反向代理   机器学习场景
4. static: 静态文件模式 (直接是文件服务)

```

## 原理(https://atbug.com/openfaas-case-study-zh/)

```
1. open-faas 通过http直接调用被 watchdog 包装的镜像

2. oci: https://www.zeng.dev/post/20200510-container-oci/
   基于oci可以快速的更新代码，docker只会更新代码层的layer，其他的层的不变

3. 事件链接器
   定时任务触发：https://github.com/openfaas/cron-connector
   trriggers触发器：https://github.com/openfaas/mqtt-connector
   消息队列：https://github.com/openfaas/nats-connector

4. 集成
   apisix集成：
   raspberry-pi集成：可以直接 shell或者 python2.7
   收集群控：sekiro+rust+k3s

5. 定时任务
   https://docs.openfaas.com/reference/cron/
```

![](doc/img.png)
![](doc/img_1.png)

## openfaas k8s原理

```
nats： 异步任务
openfaas-gateway: 通过函数名称唤醒服务
faas-nets: 判断是 函数调用还是http调用 由 of-watchdog 进一步调用
prometheus: 监控用
```

![](doc/img_2.png)
![](doc/img_3.png)
![](doc/img_4.png)

## 开源文章

```
https://juejin.cn/post/7114964607587844103
https://atbug.com/openfaas-case-study-zh/
```