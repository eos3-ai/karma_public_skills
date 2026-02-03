# 介绍

小程序开发框架的目标是通过尽可能简单、高效的方式让开发者可以在微信中开发具有原生 APP 体验的服务。

整个小程序框架系统分为两部分：**[逻辑层](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/)**（App Service）和 **[视图层](https://developers.weixin.qq.com/miniprogram/dev/framework/view/)**（View）。小程序提供了自己的视图层描述语言 `WXML` 和 `WXSS`，以及基于 `JavaScript` 的逻辑层框架，并在视图层与逻辑层间提供了数据传输和事件系统，让开发者能够专注于数据与逻辑。

## 响应的数据绑定

框架的核心是一个响应的数据绑定系统，可以让数据与视图非常简单地保持同步。当做数据修改的时候，只需要在逻辑层修改数据，视图层就会做相应的更新。

通过这个简单的例子来看：

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/l0gLEKmv6gZa)

```html
<!-- This is our View -->
<view> Hello {{name}}! </view>
<button bindtap="changeName"> Click me! </button>
// This is our App Service.
// This is our data.
var helloData = {
  name: 'Weixin'
}

// Register a Page.
Page({
  data: helloData,
  changeName: function(e) {
    // sent data change to view
    this.setData({
      name: 'MINA'
    })
  }
})
```

- 开发者通过框架将逻辑层数据中的 `name` 与视图层的 `name` 进行了绑定，所以在页面一打开的时候会显示 `Hello Weixin!`；
- 当点击按钮的时候，视图层会发送 `changeName` 的事件给逻辑层，逻辑层找到并执行对应的事件处理函数；
- 回调函数触发后，逻辑层执行 `setData` 的操作，将 `data` 中的 `name` 从 `Weixin` 变为 `MINA`，因为该数据和视图层已经绑定了，从而视图层会自动改变为 `Hello MINA!`。

## 页面管理

框架 管理了整个**小程序**的页面路由，可以做到页面间的无缝切换，并给以页面完整的生命周期。开发者需要做的只是将页面的数据、方法、生命周期函数注册到 框架 中，其他的一切复杂的操作都交由 框架 处理。

## 基础组件

框架 提供了一套基础的组件，这些组件自带微信风格的样式以及特殊的逻辑，开发者可以通过组合基础组件，创建出强大的**微信小程序** 。

## 丰富的 API

框架 提供丰富的微信原生 API，可以方便的调起微信提供的能力，如获取用户信息，本地存储，支付功能等。

# 场景值

> 基础库 1.1.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

场景值用来描述用户进入小程序的路径。完整场景值的含义请查看[场景值列表](https://developers.weixin.qq.com/miniprogram/dev/reference/scene-list.html)。

由于Android系统限制，目前还无法获取到按 Home 键退出到桌面，然后从桌面再次进小程序的场景值，对于这种情况，会保留上一次的场景值。

## 获取场景值

开发者可以通过下列方式获取场景值：

- 对于小程序，可以在 `App` 的 `onLaunch` 和 `onShow`，或[wx.getLaunchOptionsSync](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getLaunchOptionsSync.html) 中获取上述场景值。
- 对于小游戏，可以在 [wx.getLaunchOptionsSync](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getLaunchOptionsSync.html) 和 [wx.onShow](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/(wx.onShow)) 中获取上述场景值

## 返回来源信息的场景

部分场景值下还可以获取来源应用、公众号或小程序的appId。获取方式请参考对应API的参考文档。

| 场景值 | 场景                            | appId含义  |
| :----- | :------------------------------ | :--------- |
| 1020   | 公众号 profile 页相关小程序列表 | 来源公众号 |
| 1035   | 公众号自定义菜单                | 来源公众号 |
| 1036   | App 分享消息卡片                | 来源App    |
| 1037   | 小程序打开小程序                | 来源小程序 |
| 1038   | 从另一个小程序返回              | 来源小程序 |
| 1043   | 公众号模板消息                  | 来源公众号 |
| 1069   | 移动应用                        | 来源App    |

# 逻辑层 App Service

小程序开发框架的逻辑层使用 `JavaScript` 引擎为小程序提供开发 `JavaScript` 代码的运行环境以及微信小程序的特有功能。

逻辑层将数据进行处理后发送给视图层，同时接受视图层的事件反馈。

开发者写的所有代码最终将会打包成一份 `JavaScript` 文件，并在小程序启动的时候运行，直到小程序销毁。这一行为类似 [ServiceWorker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)，所以逻辑层也称之为 App Service。

在 `JavaScript` 的基础上，我们增加了一些功能，以方便小程序的开发：

- 增加 `App` 和 `Page` 方法，进行[程序注册](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/app.html)和[页面注册](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page.html)。
- 增加 `getApp` 和 `getCurrentPages` 方法，分别用来获取 `App` 实例和当前页面栈。
- 提供丰富的 [API](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/api.html)，如微信用户数据，扫一扫，支付等微信特有能力。
- 提供[模块化](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/module.html#模块化)能力，每个页面有独立的[作用域](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/module.html#文件作用域)。

**注意：小程序框架的逻辑层并非运行在浏览器中，因此 `JavaScript` 在 web 中一些能力都无法使用，如 `window`，`document` 等。**

# 注册小程序

每个小程序都需要在 `app.js` 中调用 `App` 方法注册小程序实例，绑定生命周期回调函数、错误监听和页面不存在监听函数等。

详细的参数含义和使用请参考 [App 参考文档](https://developers.weixin.qq.com/miniprogram/dev/reference/api/App.html) 。

```js
// app.js
App({
  onLaunch (options) {
    // Do something initial when launch.
  },
  onShow (options) {
    // Do something when show.
  },
  onHide () {
    // Do something when hide.
  },
  onError (msg) {
    console.log(msg)
  },
  globalData: 'I am global data'
})
```

整个小程序只有一个 App 实例，是全部页面共享的。开发者可以通过 `getApp` 方法获取到全局唯一的 App 实例，获取App上的数据或调用开发者注册在 `App` 上的函数。

```js
// xxx.js
const appInstance = getApp()
console.log(appInstance.globalData) // I am global data
```

# 注册页面

对于小程序中的每个页面，都需要在页面对应的 `js` 文件中进行注册，指定页面的初始数据、生命周期回调、事件处理函数等。

## 使用 Page 构造器注册页面

简单的页面可以使用 `Page()` 进行构造。

**代码示例：**

```js
//index.js
Page({
  data: {
    text: "This is page data."
  },
  onLoad: function(options) {
    // 页面创建时执行
  },
  onShow: function() {
    // 页面出现在前台时执行
  },
  onReady: function() {
    // 页面首次渲染完毕时执行
  },
  onHide: function() {
    // 页面从前台变为后台时执行
  },
  onUnload: function() {
    // 页面销毁时执行
  },
  onPullDownRefresh: function() {
    // 触发下拉刷新时执行
  },
  onReachBottom: function() {
    // 页面触底时执行
  },
  onShareAppMessage: function () {
    // 页面被用户分享时执行
  },
  onPageScroll: function() {
    // 页面滚动时执行
  },
  onResize: function() {
    // 页面尺寸变化时执行
  },
  onTabItemTap(item) {
    // tab 点击时执行
    console.log(item.index)
    console.log(item.pagePath)
    console.log(item.text)
  },
  // 事件响应函数
  viewTap: function() {
    this.setData({
      text: 'Set some data for updating view.'
    }, function() {
      // this is setData callback
    })
  },
  // 自由数据
  customData: {
    hi: 'MINA'
  }
})
```

详细的参数含义和使用请参考 [Page 参考文档](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html) 。

## 在页面中使用 behaviors

> 基础库 2.9.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

页面可以引用 behaviors 。 behaviors 可以用来让多个页面有相同的数据字段和方法。

```js
// my-behavior.js
module.exports = Behavior({
  data: {
    sharedText: 'This is a piece of data shared between pages.'
  },
  methods: {
    sharedMethod: function() {
      this.data.sharedText === 'This is a piece of data shared between pages.'
    }
  }
})
// page-a.js
var myBehavior = require('./my-behavior.js')
Page({
  behaviors: [myBehavior],
  onLoad: function() {
    this.data.sharedText === 'This is a piece of data shared between pages.'
  }
})
```

具体用法参见 [behaviors](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/behaviors.html) 。

## 使用 Component 构造器构造页面

> 基础库 1.6.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

`Page` 构造器适用于简单的页面。但对于复杂的页面， `Page` 构造器可能并不好用。

此时，可以使用 `Component` 构造器来构造页面。 `Component` 构造器的主要区别是：方法需要放在 `methods: { }` 里面。

**代码示例：**

```js
Component({
  data: {
    text: "This is page data."
  },
  methods: {
    onLoad: function(options) {
      // 页面创建时执行
    },
    onPullDownRefresh: function() {
      // 下拉刷新时执行
    },
    // 事件响应函数
    viewTap: function() {
      // ...
    }
  }
})
```

这种创建方式非常类似于 [自定义组件](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/) ，可以像自定义组件一样使用 `behaviors` 等高级特性。

# 生命周期

**以下内容你不需要立马完全弄明白，不过以后它会有帮助。**

下图说明了页面 `Page` 实例的生命周期。

![img](https://res.wx.qq.com/wxdoc/dist/assets/img/page-lifecycle.2e646c86.png)

