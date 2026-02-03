# 页面路由

在小程序中，所有页面的创建、销毁及状态转换都由页面路由来表达和进行控制。以下内容会简单介绍小程序的页面路由相关逻辑。

## 路由的时机

路由会以事件形式表示，由微信客户端下发给小程序基础库，下发后客户端和基础库将分别同时处理这一次路由事件。路由事件的发起可以大致分为以下两类：

1. 通过用户的操作（如按下返回按钮）发起。通过这种方式发起时，路由事件将直接由客户端下发到基础库执行；
2. 由开发者通过 API（如 `wx.navigateTo`）或者组件（如 `<navigator>`）发起。通过这种方式发起时，基础库将首先向客户端发起路由请求，客户端确认路由可以被执行后，再将路由事件下发到基础库。其中，如果路由被确定执行，API 的 `success` 回调函数或组件的 `success` 事件将被触发，否则将触发 `fail`。

当一次路由被确定执行（API 或组件通知 `success`）时，没有操作可以取消这一次路由。

当多次路由被连续发起时，如果当前的路由事件还未处理完毕，后续的路由事件将等待当前路由处理，并排队依次执行，直到所有待处理的路由都被执行完毕。

> 一个简单的例子：用户点击返回按钮触发了 `navigateBack`，小程序在页面栈当前栈顶页的 `onUnload` 中调用 `wx.redirectTo`，**并不能** 将当前正在被销毁的页面重定向为一个新页面，而是会先完成页面返回，再将页面返回后的新栈顶页重定向到新的页面。

## 页面栈

目前，小程序的页面会被组织为一个页面栈加若干不在栈中的悬垂页面的组合形式。其中，页面栈按顺序存放了通过跳转依次打开的页面，而当前已经创建但非活跃的 tabBar 页面及处于画中画模式（如 [`video`](https://developers.weixin.qq.com/miniprogram/dev/component/video.html#小窗特性说明)、[`live-player`](https://developers.weixin.qq.com/miniprogram/dev/component/live-player.html#小窗特性说明) 等）中的页面将以悬垂页面的形式存在。

全局接口 [`getCurrentPages`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/getCurrentPages.html) 可以用来获取当前页面栈。

小程序冷启动完成后，在整个小程序存活过程中（除去某次路由执行到一半的中间状态外），页面栈中都将存在至少一个页面。

页面栈的具体行为可以参见下面具体路由行为中的详细描述。

## 路由的监听及响应

### 页面生命周期函数

每个小程序页面都有若干生命周期函数，如 `onLoad`, `onShow`, `onRouteDone`, `onHide`, `onUnload` 等。它们可以在页面注册时定义，并会在相应的时机触发。所有生命周期函数及它们各自的含义和触发时机可以参见 [Page 接口](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#生命周期回调函数)，下面的内容也将详细说明每个路由将如何触发页面的生命周期函数。

### 页面路由监听

从基础库版本 [3.5.5](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，基础库提供了一组针对路由事件的监听函数。相比页面生命周期函数，它们能更好地针对某次路由进行响应。详见 [页面路由监听](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-event-listener)。

## 路由类型

小程序目前的路由类型可以大致分为以下七种：

### 1. 小程序启动

- openType: `appLaunch`

小程序启动路由 `appLaunch` 表示一个新的小程序启动，并加载第一个页面。`appLaunch` 在每个小程序实例中会且仅会出现一次，且每个小程序实例启动时的第一个路由事件必定为 `appLaunch`。

**触发方式**

`appLaunch` 仅能由小程序冷启动被动触发，不能由开发者主动触发，启动后也不能通过其他用户操作触发。

**页面栈及生命周期处理**

由于 `appLaunch` 必定是启动时的第一个路由，而路由前没有任何页面存在，此时页面栈必定为空。`appLaunch` 会创建路由事件指定的页面，并将其推入页面栈作为栈中唯一的页面。在这个过程中，这个页面的 `onLoad`, `onShow` 两个生命周期将依次被触发。

### 2. 打开新页面

- openType: `navigateTo`

打开新页面路由 `navigateTo` 表示打开一个新的页面，并将其推入页面栈。

**触发方式**

1. 调用 API [`wx.navigateTo`](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateTo.html), [`Router.navigateTo`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Router.html)
2. 使用组件 [``](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html)
3. 用户点击一个视频小窗（如 [`video`](https://developers.weixin.qq.com/miniprogram/dev/component/video.html#小窗特性说明)）

`navigateTo` 的目标必须为非 tabBar 页面。

**页面栈及生命周期处理**

`navigateTo` 事件发生时，页面栈当前的栈顶页面将首先被隐藏，触发 `onHide` 生命周期；之后框架将创建路由事件指定的页面，并将其推入页面栈作为新的栈顶。在这个过程中，这个新页面的 `onLoad`, `onShow` 两个生命周期将依次被触发。

作为一种特殊情况，如果 `navigateTo` 事件发生时，页面栈当前的栈顶页面满足小窗模式逻辑，或事件由用户点击视频小窗发起，那么页面栈及生命周期的的处理会有所不同。

### 3. 页面重定向

- openType: `redirectTo`

页面重定向路由 `redirectTo` 表示将页面栈当前的栈顶页面替换为一个新的页面。

**触发方式**

1. 调用 API [`wx.redirectTo`](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.redirectTo.html), [`Router.redirectTo`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Router.html)
2. 使用组件 [``](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html)

`redirectTo` 的目标必须为非 tabBar 页面。

**页面栈及生命周期处理**

`redirectTo` 事件发生时，页面栈当前的栈顶页面将首先被弹出并销毁，在此过程中，这个栈顶页面的 `onUnload` 生命周期将被触发；之后框架将创建路由事件指定的页面，并将其推入页面栈作为新的栈顶。在这个过程中，这个新页面的 `onLoad`, `onShow` 两个生命周期将依次被触发。

### 4. 页面返回

- openType: `navigateBack`

页面返回路由 `navigateBack` 表示将页面栈当前的栈顶的若干个页面依次弹出并销毁。

**触发方式**

1. 调用 API [`wx.navigateBack`](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateBack.html), [`Router.navigateBack`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Router.html)
2. 使用组件 [``](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html)
3. 用户按左上角返回按钮，或触发操作系统返回的动作（如按下系统返回键、屏幕边缘向内滑动等）
4. 用户点击一个视频小窗（如 [`video`](https://developers.weixin.qq.com/miniprogram/dev/component/video.html#小窗特性说明)）

如果页面栈中当前只有一个页面，`navigateBack` 调用请求将失败（无论指定的 `delta` 是多少）；

如果页面栈中当前的页面数量少于调用时指定的 `delta` + 1（即调用后页面数量将少于一个），`navigateBack` 将弹出到只剩页面栈当前的页面栈底的页面为止（即至少保留一个页面）。

**页面栈及生命周期处理**

`navigateBack` 事件发生时，页面栈当前的栈顶页面将被弹出并销毁，并触发这个页面的 `onUnload` 生命周期；以上操作将被重复执行多次，直到弹出的页面数量等于指定的页面数量，或当前页面栈中只剩下一个页面。之后，页面栈新的栈顶页面的 `onShow` 生命周期将被触发。

一种特殊情况是，如果 `navigateBack` 发生时，页面栈当前的栈顶页面满足小窗模式逻辑，或事件由用户点击视频小窗发起，那么页面栈及生命周期的的处理会有所不同。

### 5. Tab 切换

- openType: `switchTab`

Tab 切换路由 `switchTab` 表示切换到指定的 tab 页面。

**触发方式**

1. 调用 API [`wx.switchTab`](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.switchTab.html), [`Router.switchTab`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Router.html)
2. 使用组件 [``](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html)
3. 用户点击 Tab Bar 中的 Tab 按钮

`switchTab` 的目标必须为 tabBar 页面。

**页面栈及生命周期处理**

由于 `navigateTo` 和 `redirectTo` 不能指定 tabBar 页面作为目标，因此当一个 tabBar 页面出现在页面栈中时，它必定为页面栈的第一个页面（即栈底页面）；同时，框架会保证任一 tabBar 页面在小程序中最多同时存在一个页面实例。`switchTab` 的行为主要基于这两点进行。

`switchTab` 事件发生时，如果当前页面栈中存在多于一个页面，页面栈当前的栈顶页面将被弹出并销毁，并触发这个页面的 `onUnload` 生命周期；以上操作将被重复执行多次，直到页面栈中只剩下一个页面。之后，根据页面栈中仅剩的页面进行不同的处理：

- 如果这个页面即为目标 tabBar 页面：
  - 如果路由事件开始时页面栈中存在多于一个页面（即目标 tabBar 页面不是栈顶页面），触发目标 tabBar 页面的 `onShow` 生命周期；
  - 否则（路由事件开始时目标 tabBar 页面是栈顶页面），不触发任何生命周期，直接结束；
- 否则（该页面不为目标 tabBar 页面时）：
  1. 将这个页面从页面栈中弹出；
  2. - 如果这个页面为其他 tabBar 页面，该页面成为悬垂页面，并：
       - 如果路由事件开始时页面栈中只有一个页面（即该 tabBar 页面是栈顶页面），触发它的 `onHide` 生命周期；
       - 否则（路由事件开始时该 tabBar 页面不是栈顶页面），不触发它的任何生命周期；
     - 否则（这个页面为非 tabBar 页面时），销毁该页面，触发 `onUnload` 生命周期；
  3. - 如果目标 tabBar 页之前已经被创建过（现在是一个悬垂页面），将其推入页面栈，触发 `onShow` 生命周期；
     - 否则（目标 tabBar 页不存在实例），创建目标 tabBar 页并推入页面栈，依次触发 `onLoad`, `onShow` 生命周期。

### 6. 重加载

- openType: `reLaunch`, `autoReLaunch`

重加载路由 `reLaunch` 或 `autoReLaunch` 表示销毁当前所有的页面，并载入一个新页面。

重加载路由的两种 openType 的区别主要为是否由开发者主动触发（或是由用户触发），这两种 openType 的路由逻辑基本一致。

**触发方式**

1. （`reLaunch`）调用 API [`wx.reLaunch`](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.reLaunch.html), [`Router.reLaunch`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Router.html)
2. （`reLaunch`）使用组件 [``](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html)
3. （`autoReLaunch`）小程序处于后台时，用户从扫码或分享等场景重新进入小程序

`reLaunch` 可以指定任意页面作为目标页面，无论它是否是小程序的首页或是否 tabBar 页。

请注意：`reLaunch` 及 `autoReLaunch` 仅代表一种路由，**并不等于小程序重启，小程序会在当前的 AppService 上继续运行**，既不会重新启动 AppService 的 JavaScript 运行环境，也不会重新注入小程序代码或触发 `App.onLaunch` 生命周期，各种 JS 的全局变量或全局状态也不会被重置。

**页面栈及生命周期处理**

`reLaunch` 或 `autoReLaunch` 事件发生时，页面栈中的所有页面将由顶至底依次被弹出并销毁，触发 `onUnload` 生命周期；之后所有悬垂页面将以不确定的顺序逐个被销毁，触发 `onUnload` 生命周期。所有页面都被销毁后，目标页面将被创建，并推入页面栈成为栈中唯一的页面，依次触发 `onLoad` 和 `onShow` 两个生命周期。

### 7. 关闭小窗页面

- openType: `dismissPip`

关闭小窗页面路由 `dismissPip` 表示关闭一个正处于小窗模式的页面。

# 页面路由监听

> 基础库 3.5.5 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

这篇指南主要说明从基础库版本 [3.5.5](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 起可用的 *页面路由事件监听函数* 的使用方法。如果需要了解页面路由的类型及逻辑等基本信息，可以参考 [页面路由](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route)。

由于每次路由可能触发多个页面的多个页面生命周期，因此当某个页面的某个生命周期被触发时，小程序往往比较难判断它被触发的原因，从而难以做出一些针对路由（而非针对页面）的响应。一个例子是当小程序进行重加载 `reLaunch` 路由时，小程序可能需要重设一些全局状态来保证后续逻辑正常工作，或者模拟近似于重新启动的效果。然而从页面生命周期来反向推测 `reLaunch` 是比较难的，因为即使某一瞬间当前所有页面都被销毁，也不一定是由 `reLaunch` 引起的（也可能是在仅有单个页面的情况下进行了重定向 `redirectTo`）。这套接口可以帮助处理这样的场景。

## 所有监听及触发时序

| 页面路由监听                                                 | 触发时机                                       | 每次路由中的触发次数 |
| :----------------------------------------------------------- | :--------------------------------------------- | :------------------- |
| [`wx.onBeforeAppRoute`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforeAppRoute.html) | 路由事件下发到基础库，基础库执行路由逻辑前触发 | 一次                 |
| [`wx.onAppRoute`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAppRoute.html) | 路由事件下发到基础库，基础库执行路由逻辑后触发 | 一次                 |
| [`wx.onAppRouteDone`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAppRouteDone.html) | 路由对应的动画（页面推入、推出等）完成时触发   | 一次                 |
| [`wx.onBeforePageLoad`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforePageLoad.html) | 路由引发的页面创建之前触发                     | 不限                 |
| [`wx.onAfterPageLoad`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAfterPageLoad.html) | 路由引发的页面创建完成后触发                   | 不限                 |
| [`wx.onBeforePageUnload`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforePageUnload.html) | 路由引发的页面销毁之前触发                     | 不限                 |
| [`wx.onAfterPageUnload`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAfterPageUnload.html) | 路由引发的页面销毁完成后触发                   | 不限                 |

例如，在一次 `redirectTo` 中，监听和处理逻辑将按以下顺序触发：

1. [`wx.onBeforeAppRoute`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforeAppRoute.html)
2. [`wx.onBeforePageUnload`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforePageUnload.html)
3. 旧页面 [`onUnload`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#生命周期回调函数) 生命周期
4. 旧页面销毁，此过程中页面本身及页面中所有自定义组件的 [`detached`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Component.html) 生命周期被递归触发
5. 旧页面弹出页面栈，此时开始 [`getCurrentPages`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/getCurrentPages.html) 接口不再能获取到旧页面
6. [`wx.onAfterPageUnload`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAfterPageUnload.html)
7. [`wx.onBeforePageLoad`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onBeforePageLoad.html)
8. 创建新页面，此过程中页面本身及页面中所有自定义组件的 [`created`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Component.html) 生命周期被递归触发
9. 新页面压入页面栈，此时开始 [`getCurrentPages`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/getCurrentPages.html) 接口可以获取到新页面
10. 挂载新页面，此过程中页面本身及页面中所有自定义组件的 [`attached`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Component.html) 生命周期被递归触发
11. 新页面 [`onLoad`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#生命周期回调函数) 生命周期
12. 新页面 [`onShow`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#生命周期回调函数) 生命周期
13. [`wx.onAfterPageLoad`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAfterPageLoad.html)
14. [`wx.onAppRoute`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAppRoute.html)
15. （新页面推入动画完成时）[`wx.onAppRouteDone`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.onAppRouteDone.html)

对于其他路由，可以结合 [页面路由](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route) 中的具体路由逻辑进行类推。

## 路由事件 ID

为了在多次监听回调中识别同一个路由事件，框架会为每一次独立的路由事件生成一个在小程序实例中唯一的 ID，称为 *路由事件 ID*。在所有页面路由监听函数中，事件参数中都将携带一个字符串 `routeEventId`，表示这个路由事件 ID。小程序可以通过读取回调中的 `routeEventId`，来将同一个路由在不同时间节点触发的不同回调进行关联。例如：

```javascript
const redirectToContext = {};
wx.onBeforeAppRoute(res => {
  if (res.openType === "redirectTo") {
    redirectToContext[res.routeEventId] = { startTime: new Date() };
  }
});
wx.onBeforePageUnload(res => {
  const context = redirectToContext[res.routeEventId];
  if (context !== undefined) {
    context.from = res.page.is;
    context.data = res.page.data;
  }
});
wx.onAfterPageLoad(res => {
  const context = redirectToContext[res.routeEventId];
  if (context !== undefined) {
    console.log(
      `A "redirectTo" route replaced page "${context.from}" to "${
        res.page.is
      }", which is started at ${context.startTime.toString()}`
    );
    res.page.setData(context.data);
    delete redirectToContext[res.routeEventId];
  }
});
```

这个例子中，我们通过 `routeEventId` 关联了一次 `redirectTo` 中的页面创建和页面销毁：在页面销毁时记录了旧页面的数据，并将其应用到了新页面上。

## 可能的用例

1. 进行路由上报，方便还原用户使用路径：

   ```javascript
   wx.onAppRoute(res => {
     myReportAppRoute(res.timeStamp, res.openType, res.path, res.query);
   });
   ```

2. 小程序冷启动或热启动时，重置所有状态：

   ```javascript
   wx.onBeforeAppRoute(res => {
     if (["appLaunch", "reLaunch", "autoReLaunch"].includes(res.openType)) {
       myGlobalState.reset();
     }
   });
   ```

   这可以解决一些常见情景，例如小程序当前在后台，用户扫码热启动，触发 `autoReLaunch` 时进行状态清理。

3. 新页面创建前先进行网络请求，使页面首屏创建和等待网络请求并行进行：

   ```javascript
   const pageRequestData = {};
   wx.onBeforePageLoad(res => {
     pageRequestData[res.routeEventId] = new Promise((resolve, reject) => {
       wx.request({
         url: `https://mysite.wechat.qq.com/page-data?path=${res.path}&param=${res.query.param}`,
         success(res) {
           resolve(res);
         },
         fail(res) {
           reject(res);
         }
       });
     });
   });
   wx.onAfterPageLoad(res => {
     pageRequestData[res.routeEventId]
       .then(data => {
         res.page.setData(data);
       })
       .catch(err => {
         console.error("page data init error", err);
       });
   });
   ```

   当页面比较复杂时，页面创建需要一定时间。这个做法能充分利用页面的创建时间来等待网络请求返回，从而更快地将业务数据应用到页面上，展示给用户。

   # 路由事件重写

   从基础库 [3.8.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 起，小程序可以在路由事件下发到基础库但还未进行实际处理之前，改变这次路由事件的目标页面路径及参数。这有一点类似 HTTP 协议中 URL 重定向的效果，但为了不与现有的 *页面重定向* `redirectTo` 混淆，我们将这种新的特性称为 **路由重写（Route rewrite）**。

   > 为了更好地理解这个特性，你可能需要先了解 [路由事件](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route) 的相关机制

   ## 基本用法

   例如，我们可以通过这样的方式将所有跳转到页面 A 的路由都重写到页面 B：

   ```js
   // 添加路由事件处理前的监听
   wx.onBeforeAppRoute(res => {
     // 监听触发时，判断事件是否需要重写
     if (res.path === '/pages/A/A') {
       // 重写路由事件
       wx.rewriteRoute({
         url: '/pages/B/B',
         success(res) {
           console.info('Rewrite successfully from A to B')
         },
         fail(res) {
           console.error('Rewrite failed, reason: ' + res.errMsg)
           // 由于兼容性问题或场景不适用等原因重写失败，回退
           wx.redirectTo({
             url: '/pages/B/B',
             complete: console.info
           })
         }
       })
       return
     }
   })
   ```

   在这个例子中，如果有一个目标为 `/pages/A/A` 的路由事件（例如 `navigateTo`）下发到基础库，`wx.onBeforeAppRoute` 监听被触发，`wx.rewriteRoute` 执行重写后，`navigateTo` 的目标将变为 `/pages/B/B`。最终会有一个 B 页面被实例化并压入页面栈。

   ### 调用时机

   在上面的例子中，路由重写接口 `wx.rewriteRoute` 在 `wx.onBeforeAppRoute` 监听中执行。这是因为路由重写只能在路由事件下发到基础库，并且该路由事件还未被执行任何处理之前进行。换句话说，如果这次路由事件已经产生了实际影响（例如路由使旧页面被弹出销毁或者新页面被渲染），那我们就不能再重写这次路由事件了。因此目前有且只有 `wx.onBeforeAppRoute` 一个时机可以进行路由事件的重写，并且路由重写必须在这个监听的回调中 **同步** 进行。在 `wx.onBeforeAppRoute` 的回调以外的地方进行重写或者在回调中异步进行重写会导致重写失败。

   ### 目标限制

   由于路由重写是改变一个已有路由事件的目标路径，不能改变这个事件的事件类型，因此路由重写需要保证重写后新的目标路径和事件类型是匹配的。例如：`switchTab` 的目标必须是一个 Tab Bar 页面，因此重写也不能将 `switchTab` 事件重写到非 Tab Bar 页面。

   ### 常见用例

   > 此处的代码片段仅做简单的场景演示

   1. 页面未找到的情况下，回到小程序主页

      ```js
      wx.onBeforeAppRoute(res => {
        if (res.notFound) {
          wx.rewriteRoute({
            url: '/pages/index/index?from-not-found=' + encodeURIComponent(res.path),
          })
        }
      })
      ```

   2. 线下活动结束后，活动页面下线，用户扫描线下旧物料时引导到新活动页；或者线下物料中写错了路径 / 参数，小程序中进行兼容：

      ```js
      wx.onBeforeAppRoute(res => {
        if (res.path === '/pages/old-or-wrong/activity/page') {
          wx.rewriteRoute({
            url: '/pages/new/activity/page',
            preserveQuery: true,
          })
        }
      })
      ```

   3. 进入新任务页面时，判断用户是否有上次未完成的任务，继续处理：

      ```js
      wx.onBeforeAppRoute(res => {
        if (res.path === '/pages/task/new-task') {
          const unfinishedTaskId = globalStatus.unfinishedTaskId
          if (typeof unfinishedTaskId === 'string') {
            wx.rewriteRoute({
              url: '/pages/task/perform-task?taskId=' + unfinishedTaskId,
            })
          }
        }
      })
      ```

   4. 小程序从首页下拉冷启动时，读取 storage 中存储的不同用户身份（例如顾客与商家、学生与家长等），跳转到不同的首页

      ```js
      wx.onBeforeAppRoute(res => {
        if (res.openType === 'appLaunch') {
          const enterOptions = wx.getEnterOptionsSync()
          if (enterOptions.scene === 1089) {
            const userRole = wx.getStorageSync('user-role')
            if (userRole === 'customer') {
              wx.rewriteRoute({ url: '/pages/customer-index/index' })
            } else if (userRole === 'merchant') {
              wx.rewriteRoute({ url: '/pages/merchant-index/index' })
            } else { /* do nothing */ }
          }
        }
      })
      ```

   ### 常见问题

   1. **为什么我请求后台接口之后再执行 `rewriteRoute` 会失败？**

      目前小程序提供的网络请求接口都是异步接口，发起网络请求之后，JS 运行时会在等待服务器响应时执行其他任务。因此，请求后台并等待后台接口返回时，路由事件实际上已经被处理和执行了。

      理论上，我们也可以使路由事件的处理和执行等待网络请求返回。在等待期间，由于路由事件尚未处理，用户会持续停留在上一个页面（页面跳转的情况下）或者看到白屏（小程序启动的情况下），而这段时间的长短取决于网络请求的耗时，从而可能导致用户操作打开或跳转后持续没有响应。为了回避这种情况导致的体验恶化，现阶段我们只处理同步进行的路由重写。

   2. **为什么 `wx.rewriteRoute` 不像 `navigateTo` 一样可以直接调用，而是要放在监听的回调中？**

      因为相比于 `wx.navigateTo` 是一次路由请求，对应的 `navigateTo` 是一种路由事件类型，`rewriteRoute` 实际上并不是一种路由类型，它的作用是对一次已经存在的路由事件进行一些操作。`onBeforeAppRoute` 监听会在路由事件下发时触发，在这个回调中我们才能准确地对路由事件进行判断和处理。

   ### 常见失败及对应原因

   - `not supported`

     当前客户端平台或版本不支持路由重写能力

   - `rewriteRoute is only allowed in a onBeforeAppRoute callback`

     在不正确的时机调用 `wx.rewriteRoute`（见上方 [调用时机](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-rewrite.html#调用时机)）

   - `rewriteRoute can only be called once in a route event, this page hash been rewritten to "XXX"`

     多次重写了同一个路由事件。每一个路由事件只能被重写一次，可以先计算好最终的目标路径再调用。如果确实需要进行连续的重写，应该等待重写后的路由事件重新触发 `onBeforeAppRoute` 监听回调，再进行重写

   - `a "navigateBack" event is not allowed to be rewritten`

     页面返回 `navigateBack` 事件是不能被重写的（因为目标页面是已经存在的原有页面）

   - `rewriting a "XXX" event to to a non-tab page("YYY") is not allowed`

   - `rewriting a "XXX" event to a tab page("YYY") is not allowed`

     重写后的目标页面与路由事件类型不匹配（见上方 [目标限制](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route-rewrite.html#目标限制)）

   - `rewriting a route event that belongs to XXX is not allowed.`

     小程序不能重写目标为插件页面的路由事件，反之插件也不能重写目标为小程序或其他插件的路由事件

   ### 已知问题

   1. 目前仅能将路由事件重写到同一分包中的页面，暂不能重写到其他分包的页面。这个问题将在后续的客户端版本中修复