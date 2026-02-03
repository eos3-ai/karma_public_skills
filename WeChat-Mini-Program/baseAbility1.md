# 网络

在小程序/小游戏中使用网络相关的 API 时，需要注意下列问题，请开发者提前了解。

## 1. 服务器域名配置

每个微信小程序需要事先设置通讯域名，小程序**只可以跟指定的域名进行网络通信**。包括普通 HTTPS 请求（[wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html)）、上传文件（[wx.uploadFile](https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/wx.uploadFile.html)）、下载文件（[wx.downloadFile](https://developers.weixin.qq.com/miniprogram/dev/api/network/download/wx.downloadFile.html)) 和 WebSocket 通信（[wx.connectSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.connectSocket.html)）。

从基础库 2.4.0 开始，网络接口允许与局域网 IP 通信，但要注意 **不允许与本机 IP 通信**。

从 2.7.0 开始，提供了 UDP 通信（[wx.createUDPSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/wx.createUDPSocket.html))。

从 2.18.0 开始，提供了 TCP 连接（[wx.createTCPSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/tcp/wx.createTCPSocket.html))，只允许与同个局域网内的非本机 IP 以及配置过的服务器域名通信。

如使用[微信云托管](https://cloud.weixin.qq.com/cloudrun?utm_source=wxdoc&utm_content=network)作为后端服务，则可无需配置通讯域名（在小程序内通过[callContainer](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/development/call/mini.html)和[connectContainer](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/development/websocket/miniprogram.html)通过微信私有协议向云托管服务发起 HTTPS 调用和 WebSocket 通信）。

#### 配置流程

服务器域名请在 「小程序后台-开发-开发设置-服务器域名」 中进行配置，配置时需要注意：

- 域名只支持 `https` ([wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html)、[wx.uploadFile](https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/wx.uploadFile.html)、[wx.downloadFile](https://developers.weixin.qq.com/miniprogram/dev/api/network/download/wx.downloadFile.html)) 和 `wss` ([wx.connectSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.connectSocket.html)) 协议；
- 域名不能使用 IP 地址（小程序的[局域网](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/mDNS.html) IP 除外）或 localhost；
- 对于 `https` 域名，可以配置端口，如 https://myserver.com:8080，但是配置后只能向 https://myserver.com:8080 发起请求。如果向 https://myserver.com、https://myserver.com:9091 等 URL 请求则会失败。如果不配置端口。如 https://myserver.com，那么请求的 URL 中也不能包含端口，甚至是默认的 443 端口也不可以。如果向 https://myserver.com:443 请求则会失败。
- 对于 `wss` 域名，无需配置端口，默认允许请求该域名下所有端口。
- 域名必须经过 ICP 备案；
- **出于安全考虑，`api.weixin.qq.com` 不能被配置为服务器域名，相关API也不能在小程序内调用。** 开发者应将 AppSecret 保存到后台服务器中，通过服务器使用 `getAccessToken` 接口获取 `access_token`，并调用相关 API；
- 不支持配置父域名，使用子域名。

## 2. DNS预解析域名

> 微信客户端 iOS 8.0.24，Android 8.0.23）开始支持。

小程序一般会依赖一些网络请求（如逻辑层的wx.request、渲染层的图片等网络资源），优化请求速度将会提升用户体验，而网络请求耗时中就包括DNS解析。DNS预解析域名，是框架提供的一种在小程序**启动时**，提前解析业务域名的技术。

### 配置流程

DNS域名配置请求「小程序后台-开发-开发设置-服务器域名」 中进行配置，配置时需要注意：

- 预解析域名无需填写协议头
- 预解析域名最多可添加 5 个
- 其他安全策略同服务器域名配置策略

## 3. 网络请求

#### 超时时间

- 默认超时时间是 **60s**；
- 超时时间可以在 `app.json` 或 `game.json` 中通过 [`networktimeout`](https://developers.weixin.qq.com/miniprogram/dev/framework/config.html) 配置
- 也可以在接口调用时指定超时时间，如 `wx.request({ timeout: 5000 })`，单位为ms。接口调用的`timeout`配置优先级高于`app.json`中的配置

### 使用限制

- 网络请求的 `referer` header 不可设置。其格式固定为 `https://servicewechat.com/{appid}/{version}/page-frame.html`，其中 `{appid}` 为小程序的 appid，`{version}` 为小程序的版本号，版本号为 `0` 表示为开发版、体验版以及审核版本，版本号为 `devtools` 表示为开发者工具，其余为正式版本；
- [wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html)、[wx.uploadFile](https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/wx.uploadFile.html)、[wx.downloadFile](https://developers.weixin.qq.com/miniprogram/dev/api/network/download/wx.downloadFile.html) 的最大并发限制是 **10** 个；
- [wx.connectSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.connectSocket.html) 的最大并发限制是 **5** 个。
- 小程序进入后台运行后，如果 **5s** 内网络请求没有结束，会回调错误信息 `fail interrupted`；在回到前台之前，网络请求接口调用都会无法调用。

### 返回值编码

- 建议服务器返回值使用 **UTF-8** 编码。对于非 UTF-8 编码，小程序会尝试进行转换，但是会有转换失败的可能。
- 小程序会自动对 BOM 头进行过滤（只过滤一个BOM头）。

### 回调函数

- **只要成功接收到服务器返回，无论 `statusCode` 是多少，都会进入 `success` 回调。请开发者根据业务逻辑对返回值进行判断。**

## 4. 常见问题

### HTTPS 证书

**小程序必须使用 HTTPS/WSS 发起网络请求**。请求时系统会对服务器域名使用的 HTTPS 证书进行校验，如果校验失败，则请求不能成功发起。由于系统限制，不同平台对于证书要求的严格程度不同。为了保证小程序的兼容性，建议开发者按照最高标准进行证书配置，并使用相关工具检查现有证书是否符合要求。

对证书要求如下：

- HTTPS 证书必须有效；
  - 证书必须被系统信任，即根证书已被系统内置
  - 部署 SSL 证书的网站域名必须与证书颁发的域名一致
  - 证书必须在有效期内
  - 证书的信任链必需完整（需要服务器配置）
- `iOS` 不支持自签名证书;
- `iOS` 下证书必须满足苹果 [App Transport Security (ATS)](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33) 的要求;
- TLS 必须支持 1.2 及以上版本。部分旧 `Android` 机型还未支持 TLS 1.2，请确保 HTTPS 服务器的 TLS 版本支持 1.2 及以下版本;
- 部分 CA 可能不被操作系统信任，请开发者在选择证书时注意小程序和各系统的相关通告。
  - [Chrome 56/57 内核对 WoSign、StartCom 证书限制周知](https://developers.weixin.qq.com/community/develop/doc/800026caeb042e45681583652b70910a)

> 证书有效性可以使用 `openssl s_client -connect example.com:443` 命令验证，也可以使用其他[在线工具](https://myssl.com/ssl.html)。

**除了网络请求 API 外，小程序中其他 `HTTPS` 请求如果出现异常，也请按上述流程进行检查。如 https 的图片无法加载、音视频无法播放等。**

### 跳过域名校验

在微信开发者工具中，可以临时开启 `开发环境不校验请求域名、TLS版本及HTTPS证书` 选项，跳过服务器域名的校验。此时，在微信开发者工具中及手机开启调试模式时，不会进行服务器域名的校验。

**在服务器域名配置成功后，建议开发者关闭此选项进行开发，并在各平台下进行测试，以确认服务器域名配置正确。**

> 如果手机上出现 “打开调试模式可以发出请求，关闭调试模式无法发出请求” 的现象，请确认是否跳过了域名校验，并确认服务器域名和证书配置是否正确。

### 海外用户请求加速

对于海外用户，可通过在海外也部署接入点来提速，可参考接入 [腾讯云全球应用加速服务](https://cloud.tencent.com/document/product/608) 或其他同类产品。

# 业务域名

> 基础库 1.6.4 开始支持，低版本需做 [兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 。

> 承载网页的容器。会自动铺满整个小程序页面，小游戏和个人类型的小程序暂不支持使用。 客户端 6.7.2 版本开始， [navigationStyle: custom](https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/app.html) 对 [web-view](https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html) 组件无效 小程序插件中不能使用。

为便于开发者灵活配置小程序，现开放小程序内嵌网页能力。

## 使用流程

### 1. 在管理后台配置业务域名

开发者登录小程序后台mp.weixin.qq.com，选择开发管理->开发设置->业务域名，点击新增，按照要求配置业务域名。目前小程序内嵌网页能力暂不开放给个人类型账号和小游戏账号。

![img](https://res.wx.qq.com/wxdoc/dist/assets/img/domain.dbb33f74.png)

### 2. 调用web-view组件实现小程序内嵌网页

在小程序管理后台成功配置业务域名后，才可使用web-view组件。小程序内调用web-view组件实现内嵌的网页，目前仅支持部分jsapi能力，关于web-view接口具体使用说明和限制，请 [点击查看](https://developers.weixin.qq.com/miniprogram/dev/component/web-view.html)

## 限制说明

1）每个小程序账号支持配置最多300个域名；

2）每个域名支持绑定最多100个主体的小程序；

3）域名只支持https协议，不支持IP地址；

4）业务域名需经过ICP备案，新备案域名需24小时后才可配置；

5）域名格式只支持英文大小写字母、数字及“- ”；

6）配置业务域名后，可打开任意合法的子域名；

# 局域网通信

基础库 2.4.0 提供了 [wx.startLocalServiceDiscovery](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.startLocalServiceDiscovery.html) 等一系列 mDNS API，可以用来获取局域网内提供 mDNS 服务的设备的 IP。 [wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html)/[wx.connectSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.connectSocket.html)/[wx.uploadFile](https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/wx.uploadFile.html)/[wx.downloadFile](https://developers.weixin.qq.com/miniprogram/dev/api/network/download/wx.downloadFile.html) 的 url 参数允许为 `${IP}:${PORT}/${PATH}` 的格式，当且仅当 IP 与手机 IP 处在同一网段且不与本机 IP 相同（一般来说，就是同一局域网，如连接在同一个 wifi 下）时，请求/连接才会成功。

在这种情况下，不会进行安全域的校验，不要求必须使用 https/wss，也可以使用 http/ws。

```js
wx.request({
  url: 'http://10.9.176.40:828'
  // 省略其他参数
})

wx.connectSocket({
  url: 'ws://10.9.176.42:828'
  // 省略其他参数
})
```

基础库 2.7.0 开始，提供了 [wx.createUDPSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/udp/wx.createUDPSocket.html) 接口用于进行 UDP 通信。通信规则同上，仅允许同一局域网下的非本机 IP。

## mDNS

目前小程序只支持通过 mDNS 协议获取局域网内其他设备的 IP。iOS 上 mDNS API 的实现基于 [Bonjour](https://developer.apple.com/bonjour/)，Android 上则是基于 [Android 系统接口](https://developer.android.com/training/connect-devices-wirelessly/nsd)。

> 由于操作系统相关能力变更，iOS 微信客户端 7.0.18 及以上版本无法使用 mDNS 相关接口，安卓版本不受影响

**serviceType**

发起 mDNS 服务搜索 [wx.startLocalServiceDiscovery](https://developers.weixin.qq.com/miniprogram/dev/api/network/mdns/wx.startLocalServiceDiscovery.html) 的接口有 serviceType 参数，指定要搜索的服务类型。

serviceType 的格式和规范，iOS [Bonjour Overview](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Articles/domainnames.html) 在 **Bonjour Names for Existing Service Types** 有提及。

![Bonjour serviceType.png](https://res.wx.qq.com/wxdoc/dist/assets/img/bonjour_service_type.a49156e7.png)

[Android 文档](https://developer.android.com/training/connect-devices-wirelessly/nsd) 对此也有提及。

![Android serviceType.png](https://res.wx.qq.com/wxdoc/dist/assets/img/android_service_type.4d2ed6c9.png)

# 移动解析HttpDNS

从基础库 [2.19.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始支持

开发者调用[wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html)时，可以开启移动解析HttpDNS服务。 该服务基于Http协议向服务商的DNS服务器发送域名解析请求，替代了基于DNS协议向运营商Local DNS发起解析请求的传统方式，可以避免Local DNS造成的域名劫持和跨网访问问题，解决移动互联网服务中域名解析异常带来的困扰。

## 小程序开发者使用移动解析说明

1. 前往[微信服务市场](https://fuwu.weixin.qq.com/service/detail/00022476b70ac08df25cfcefc57015)选购 HttpDNS 资源，并在服务详情页-接入文档获取Service ID。
2. 小程序调用[wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html)，将enableHttpDNS参数设置为true，并在httpDNSServiceId参数中填入选用的服务商Service ID。

### 代码示例

```js
wx.request({
  url: 'example.php', //仅为示例，并非真实的接口地址
  enableHttpDNS: true,
  httpDNSServiceId: 'wxa410372c837a5f26',
  success(res) {
    console.log('request success', res)
  },
  fail(res) {
    console.error('request fail', res)
  }
})
```

### 计费说明

1. 使用服务所产生的费用会按照实际调用服务商接口情况进行计费，定价策略由服务提供方制定，开发者需自行前往微信服务市场进行购买、续费等操作。
2. 微信侧每次代开发者调用服务商接口时，微信侧会进行缓存，缓存策略由服务商返回的ttl决定，因此不一定每次调用request接口都会产生费用。
3. 从基础库 v2.32.1 开始，若开发者的服务可用额度为0，仍在wx.request接口中声明使用服务商提供的移动解析能力时，会使用 localDNS 解析来兜底，并在 success 回调参数 exception.reasons ( reasons 是数组) 中返回 httpdns 欠费的错误信息和错误码，类似 `[{ "errMsg": "getDNSInfo:fail no enough httpdns quota", "errno": 602103 }]`。

### 注意事项

1. HttpDNS 不兼容网络代理

在基础库 v2.22.1 版本之前，当用户设备使用了网络代理，同时又开启了 enableHttpDNS 时，request 接口会调用失败，fail 回调 errMsg 中会包含 `ERR_PROXY_CONNECTION_FAILED` 字样，如 `{"errno":600001,"errMsg":"request:fail -130:net::ERR_PROXY_CONNECTION_FAILED"}` 或 `{"errno":600001,"errMsg":"request:fail errcode:-130 cronet_error_code:-130 error_msg:net::ERR_PROXY_CONNECTION_FAILED"}`。

为解决此问题，从基础库 v2.22.1 开始，若用户使用了网络代理，基础库会主动强制关闭 enableHttpDNS。开发者也可以通过 wx.getNetworkType 接口检查用户是否开启了网络代理。用法：

```js
wx.getNetworkType({
  success(res) {
    console.log(res.hasSystemProxy) // 开启网络代理时为 true，否则为 false
  }
})
```

### HttpDNS 相关错误码

| 错误码 | 说明                              |
| :----- | :-------------------------------- |
| 600000 | 网络错误                          |
| 602000 | 网络请求错误                      |
| 602001 | 系统错误                          |
| 602002 | http请求httpdns服务商错误         |
| 602101 | 小程序未在服务市场购买httpdns服务 |
| 602102 | 小程序在httpdns服务市场资源包过期 |
| 602103 | 小程序在httpdns服务市场额度不足   |
| 602104 | httpdns服务商返回结果为空         |
| 602105 | 调用httpdns服务商结果超时         |
| 602106 | httpdns服务商返回数据不合法       |
| 602107 | httpdns域名解析结果为空           |
| 602108 | 不支持的httpdns服务商id           |

## 移动解析服务提供商接入说明

为了保护微信客户端的安全，小程序使用的移动解析服务需要通过微信侧安全认证，认证后可在微信服务市场上架。

微信侧欢迎更多服务商为小程序提供移动解析服务。申请接入按照以下模板发送邮件，我们会有专人与您联系。

```md
收件人：servicemarket@tencent.com
主题：【上架服务市场】XXX（服务商）申请上架HttpDNS服务
正文：需要写明服务商的基本资料，包括不仅限于服务商名称、业务范围、技术证书、合作意向、联系方式等
```