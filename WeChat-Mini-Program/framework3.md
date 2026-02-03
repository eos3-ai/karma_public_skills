## 模块化

可以将一些公共的代码抽离成为一个单独的 js 文件，作为一个模块。模块只有通过 [`module.exports`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/module.html) 或者 `exports` 才能对外暴露接口。

注意：

- `exports` 是 [`module.exports`](https://developers.weixin.qq.com/miniprogram/dev/reference/api/module.html) 的一个引用，因此在模块里边随意更改 `exports` 的指向会造成未知的错误。所以更推荐开发者采用 `module.exports` 来暴露模块接口，除非你已经清晰知道这两者的关系。
- 小程序目前不支持直接引入 `node_modules` , 开发者需要使用到 `node_modules` 时候建议拷贝出相关的代码到小程序的目录中，或者使用小程序支持的 [npm](https://developers.weixin.qq.com/miniprogram/dev/devtools/npm.html) 功能。

```javascript
// common.js
function sayHello(name) {
  console.log(`Hello ${name} !`)
}
function sayGoodbye(name) {
  console.log(`Goodbye ${name} !`)
}

module.exports.sayHello = sayHello
exports.sayGoodbye = sayGoodbye
```

在需要使用这些模块的文件中，使用 `require` 将公共代码引入

```javascript
var common = require('common.js')
Page({
  helloMINA: function() {
    common.sayHello('MINA')
  },
  goodbyeMINA: function() {
    common.sayGoodbye('MINA')
  }
})
```

## 文件作用域

在 JavaScript 文件中声明的变量和函数只在该文件中有效；不同的文件中可以声明相同名字的变量和函数，不会互相影响。

通过全局函数 `getApp` 可以获取全局的应用实例，如果需要全局的数据可以在 `App()` 中设置，如：

```javascript
// app.js
App({
  globalData: 1
})
// a.js
// The localValue can only be used in file a.js.
var localValue = 'a'
// Get the app instance.
var app = getApp()
// Get the global data and change it.
app.globalData++
// b.js
// You can redefine localValue in file b.js, without interference with the localValue in a.js.
var localValue = 'b'
// If a.js it run before b.js, now the globalData shoule be 2.
console.log(getApp().globalData)
```

# API

小程序开发框架提供丰富的微信原生 API，可以方便的调起微信提供的能力，如获取用户信息，本地存储，支付功能等。详细介绍请参考 [API 文档](https://developers.weixin.qq.com/miniprogram/dev/api/index.html)。

通常，在小程序 API 有以下几种类型：

## 事件监听 API

我们约定，以 `on` 开头的 API 用来监听某个事件是否触发，如：[wx.onSocketOpen](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.onSocketOpen.html)，[wx.onCompassChange](https://developers.weixin.qq.com/miniprogram/dev/api/device/compass/wx.onCompassChange.html) 等。

这类 API 接受一个回调函数作为参数，当事件触发时会调用这个回调函数，并将相关数据以参数形式传入。

**代码示例**

```js
wx.onCompassChange(function (res) {
  console.log(res.direction)
})
```

## 同步 API

我们约定，以 `Sync` 结尾的 API 都是同步 API， 如 [wx.setStorageSync](https://developers.weixin.qq.com/miniprogram/dev/api/storage/wx.setStorageSync.html)，[wx.getSystemInfoSync](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getSystemInfoSync.html) 等。此外，也有一些其他的同步 API，如 [wx.createWorker](https://developers.weixin.qq.com/miniprogram/dev/api/worker/wx.createWorker.html)，[wx.getBackgroundAudioManager](https://developers.weixin.qq.com/miniprogram/dev/api/media/background-audio/wx.getBackgroundAudioManager.html) 等，详情参见 API 文档中的说明。

同步 API 的执行结果可以通过函数返回值直接获取，如果执行出错会抛出异常。

**代码示例**

```js
try {
  wx.setStorageSync('key', 'value')
} catch (e) {
  console.error(e)
}
```

## 异步 API

大多数 API 都是异步 API，如 [wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html)，[wx.login](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html) 等。这类 API 接口通常都接受一个 `Object` 类型的参数，这个参数都支持按需指定以下字段来接收接口调用结果：

**Object 参数说明**

| 参数名   | 类型     | 必填 | 说明                                             |
| :------- | :------- | :--- | :----------------------------------------------- |
| success  | function | 否   | 接口调用成功的回调函数                           |
| fail     | function | 否   | 接口调用失败的回调函数                           |
| complete | function | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |
| 其他     | Any      | -    | 接口定义的其他参数                               |

**回调函数的参数**

`success`，`fail`，`complete` 函数调用时会传入一个 `Object` 类型参数，包含以下字段：

| 属性    | 类型   | 说明                                                         |
| :------ | :----- | :----------------------------------------------------------- |
| errMsg  | string | 错误信息，如果调用成功返回 `${apiName}:ok`                   |
| errCode | number | 错误码，仅部分 API 支持，具体含义请参考对应 API 文档，成功时为 `0`。 |
| 其他    | Any    | 接口返回的其他数据                                           |

异步 API 的执行结果需要通过 `Object` 类型的参数中传入的对应回调函数获取。部分异步 API 也会有返回值，可以用来实现更丰富的功能，如 [wx.request](https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html)，[wx.connectSocket](https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.connectSocket.html) 等。

**代码示例**

```js
wx.login({
  success(res) {
    console.log(res.code)
  }
})
```

## 异步 API 返回 Promise

基础库 [2.10.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 版本起，异步 API 支持 callback & promise 两种调用方式。当接口参数 Object 对象中不包含 success/fail/complete 时将默认返回 promise，否则仍按回调方式执行，无返回值。

### 注意事项

1. 部分接口如 `downloadFile`, `request`, `uploadFile`, `connectSocket`, `createCamera`（小游戏）本身就有返回值， 它们的 promisify 需要开发者自行封装。
2. 当没有回调参数时，异步接口返回 promise。此时若函数调用失败进入 fail 逻辑， 会报错提示 `Uncaught (in promise)`，开发者可通过 catch 来进行捕获。
3. [wx.onUnhandledRejection](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onUnhandledRejection.html) 可以监听未处理的 Promise 拒绝事件。

**代码示例**

```js
// callback 形式调用
wx.chooseImage({
  success(res) {
    console.log('res:', res)
  }
})

// promise 形式调用
wx.chooseImage().then(res => console.log('res: ', res))
```

## 云开发 API

开通并使用[微信云开发](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/basis/getting-started.html)，即可使用云开发API，在小程序端直接调用服务端的[云函数](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/guide/functions.html#云函数)。

**代码示例**

```js
wx.cloud.callFunction({
  // 云函数名称
  name: 'cloudFunc',
  // 传给云函数的参数
  data: {
    a: 1,
    b: 2,
  },
  success: function(res) {
    console.log(res.result) // 示例
  },
  fail: console.error
})

// 此外，云函数同样支持promise形式调用
```