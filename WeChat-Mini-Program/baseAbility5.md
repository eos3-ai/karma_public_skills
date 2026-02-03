# 使用分包

## 配置方法

假设支持分包的小程序目录结构如下：

```text
├── app.js
├── app.json
├── app.wxss
├── packageA
│   └── pages
│       ├── cat
│       └── dog
├── packageB
│   └── pages
│       ├── apple
│       └── banana
├── pages
│   ├── index
│   └── logs
└── utils
```

开发者通过在 app.json `subPackages` 字段声明项目分包结构：

> 写成 `subpackages` 也支持。

```json
{
  "pages":[
    "pages/index",
    "pages/logs"
  ],
  "subPackages": [
    {
      "root": "packageA",
      "pages": [
        "pages/cat",
        "pages/dog"
      ],
      "entry": "index.js"
    }, {
      "root": "packageB",
      "name": "pack2",
      "pages": [
        "pages/apple",
        "pages/banana"
      ]
    }
  ]
}
```

`subPackages` 中，每个分包的配置有以下几项：

| 字段        | 类型        | 说明                                                         |
| :---------- | :---------- | :----------------------------------------------------------- |
| root        | String      | 分包根目录                                                   |
| name        | String      | 分包别名，[分包预下载](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/preload.html)时可以使用 |
| pages       | StringArray | 分包页面路径，相对于分包根目录                               |
| independent | Boolean     | 分包是否是[独立分包](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/independent.html) |
| entry       | String      | 分包入口文件                                                 |

## 打包原则

- 声明 `subPackages` 后，将按 `subPackages` 配置路径进行打包，`subPackages` 配置路径外的目录将被打包到主包中
- 主包也可以有自己的 pages，即最外层的 pages 字段。
- `subPackages` 的根目录不能是另外一个 `subPackages` 内的子目录
- `tabBar` 页面必须在主包内

## 引用原则

- `packageA` 无法 require `packageB` JS 文件，但可以 require 主包、`packageA` 内的 JS 文件；使用 [分包异步化](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/async.html) 时不受此条限制
- `packageA` 无法 import `packageB` 的 template，但可以 require 主包、`packageA` 内的 template
- `packageA` 无法使用 `packageB` 的资源，但可以使用主包、`packageA` 内的资源

## 分包入口文件

每个分包的配置中，`entry` 字段可以指定该分包中的任意一个 JS 文件作为入口文件，该文件会在分包注入时首先被执行。

指定的 JS 文件应该填写相对于分包根目录的路径，例如需要指定 `/path/to/subPackage/src/index.js` 作为分包 `/path/to/subPackage` 的入口文件时，应填写 `src/index.js`。

调试这个功能需要 1.06.2406242 或以上版本的微信开发者工具，正式环境没有版本需求。

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/c5PkiKmv74S9)

## 示例项目

[下载 小程序示例（分包加载版）源码](https://res.wx.qq.com/wxdoc/dist/assets/media/demo-subpackages.b42a3adb.zip)

# 独立分包

> 微信客户端 6.7.2，基础库 [2.3.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 及以上版本开始支持。开发者工具请使用 1.02.1808300 及以上版本，可 [点此下载](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)。

独立分包是小程序中一种特殊类型的分包，可以独立于主包和其他分包运行。从独立分包中页面进入小程序时，不需要下载主包。当用户进入普通分包或主包内页面时，主包才会被下载。

开发者可以按需将某些具有一定功能独立性的页面配置到独立分包中。当小程序从普通的分包页面启动时，需要首先下载主包；而独立分包不依赖主包即可运行，可以很大程度上提升分包页面的启动速度。

一个小程序中可以有多个独立分包。

> 小游戏在基础库 v2.12.2 开始支持独立分包，详见 [小游戏独立分包指南](https://developers.weixin.qq.com/minigame/dev/guide/base-ability/independent-sub-packages.html)。

## 配置方法

假设小程序目录结构如下：

```text
├── app.js
├── app.json
├── app.wxss
├── moduleA
│   └── pages
│       ├── rabbit
│       └── squirrel
├── moduleB
│   └── pages
│       ├── pear
│       └── pineapple
├── pages
│   ├── index
│   └── logs
└── utils
```

开发者通过在`app.json`的`subpackages`字段中对应的分包配置项中定义`independent`字段声明对应分包为独立分包。

```json
{
  "pages": [
    "pages/index",
    "pages/logs"
  ],
  "subpackages": [
    {
      "root": "moduleA",
      "pages": [
        "pages/rabbit",
        "pages/squirrel"
      ]
    }, {
      "root": "moduleB",
      "pages": [
        "pages/pear",
        "pages/pineapple"
      ],
      "independent": true
    }
  ]
}
```

## 限制

独立分包属于分包的一种。普通分包的所有限制都对独立分包有效。独立分包中插件、自定义组件的处理方式同普通分包。

此外，使用独立分包时要注意：

- **独立分包中不能依赖主包和其他分包中的内容**，包括 js 文件、template、wxss、自定义组件、插件等（使用 [分包异步化](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/async.html) 时 js 文件、自定义组件、插件不受此条限制）
- 主包中的 `app.wxss` 对独立分包无效，应避免在独立分包页面中使用 `app.wxss` 中的样式；
- `App` 只能在主包内定义，独立分包中不能定义 `App`，会造成无法预期的行为；
- 独立分包中暂时不支持使用插件。

## 注意事项

### （1）关于 `getApp()`

与普通分包不同，独立分包运行时，`App` 并不一定被注册，因此 `getApp()` 也不一定可以获得 `App` 对象：

- 当用户从独立分包页面启动小程序时，主包不存在，`App`也不存在，此时调用 `getApp()` 获取到的是 `undefined`。 当用户进入普通分包或主包内页面时，主包才会被下载，`App` 才会被注册。
- 当用户是从普通分包或主包内页面跳转到独立分包页面时，主包已经存在，此时调用 `getApp()` 可以获取到真正的 `App`。

由于这一限制，开发者无法通过 `App` 对象实现独立分包和小程序其他部分的全局变量共享。

为了在独立分包中满足这一需求，基础库 [2.2.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 版本开始 `getApp` 支持 [`allowDefault`] 参数，在 `App` 未定义时返回一个默认实现。当主包加载，`App` 被注册时，默认实现中定义的属性会被覆盖合并到真正的 `App` 中。

**示例代码：**

- 独立分包中

```js
const app = getApp({allowDefault: true}) // {}
app.data = 456
app.global = {}
```

- app.js 中

```js
App({
  data: 123,
  other: 'hello'
})

console.log(getApp()) // {global: {}, data: 456, other: 'hello'}
```

### （2）关于 `App` 生命周期

当从独立分包启动小程序时，主包中 `App` 的 `onLaunch` 和首次 `onShow` 会在从独立分包页面首次进入主包或其他普通分包页面时调用。

由于独立分包中无法定义 `App`，小程序生命周期的监听可以使用 [wx.onAppShow](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAppShow.html)，[wx.onAppHide](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onAppHide.html) 完成。`App` 上的其他事件可以使用 [wx.onError](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onError.html)，[wx.onPageNotFound](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onPageNotFound.html) 监听。

## 低版本兼容

在低于 6.7.2 版本的微信中运行时，独立分包视为普通分包处理，不具备独立运行的特性。

**注意：在兼容模式下，主包中的 `app.wxss` 可能会对独立分包中的页面产生影响，因此应避免在独立分包页面中使用 `app.wxss` 中的样式。**

# 分包预下载

> 基础库 2.3.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。 开发者工具请使用 1.02.1808300 及以上版本，可[点此下载](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)。

开发者可以通过配置，在进入小程序某个页面时，由框架自动预下载可能需要的分包，提升进入后续分包页面时的启动速度。对于[独立分包](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/independent.html)，也可以预下载主包。

**分包预下载目前只支持通过配置方式使用，暂不支持通过调用API完成。**

> vConsole 里有`preloadSubpackages`开头的日志信息，可以用来验证预下载的情况。

## 配置方法

预下载分包行为在进入某个页面时触发，通过在 `app.json` 增加 `preloadRule` 配置来控制。

```json
{
  "pages": ["pages/index"],
  "subpackages": [
    {
      "root": "important",
      "pages": ["index"],
    },
    {
      "root": "sub1",
      "pages": ["index"],
    },
    {
      "name": "hello",
      "root": "path/to",
      "pages": ["index"]
    },
    {
      "root": "sub3",
      "pages": ["index"]
    },
    {
      "root": "indep",
      "pages": ["index"],
      "independent": true
    }
  ],
  "preloadRule": {
    "pages/index": {
      "network": "all",
      "packages": ["important"]
    },
    "sub1/index": {
      "packages": ["hello", "sub3"]
    },
    "sub3/index": {
      "packages": ["path/to"]
    },
    "indep/index": {
      "packages": ["__APP__"]
    }
  }
}
```

`preloadRule` 中，`key` 是页面路径，`value` 是进入此页面的预下载配置，每个配置有以下几项：

| 字段     | 类型        | 必填 | 默认值 | 说明                                                         |
| :------- | :---------- | :--- | :----- | :----------------------------------------------------------- |
| packages | StringArray | 是   | 无     | 进入页面后预下载分包的 `root` 或 `name`。`__APP__` 表示主包。 |
| network  | String      | 否   | wifi   | 在指定网络下预下载，可选值为： `all`: 不限网络 `wifi`: 仅wifi下预下载 |

## 限制

同一个分包中的页面享有共同的预下载大小限额 2M，限额会在工具中打包时校验。

如，页面 A 和 B 都在同一个分包中，A 中预下载总大小 0.5M 的分包，B中最多只能预下载总大小 1.5M 的分包。

# 分包异步化

在小程序中，不同的分包对应不同的下载单元；因此，除了非独立分包可以依赖主包外，分包之间不能互相使用自定义组件或进行 `require`。「分包异步化」特性将允许通过一些配置和新的接口，使部分跨分包的内容可以等待下载后异步使用，从而一定程度上解决这个限制。

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/6AYlPZmm7csW)

## 兼容性

该特性需要基础库版本 [2.11.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 或以上，使用该特性的小程序在 2.11.2 以下的基础库上可能无法工作，如果发布正式版本，可以考虑将最低基础库版本设置为 2.11.2 或以上。

<details style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34); font-family: -apple-system, BlinkMacSystemFont, &quot;SF UI Text&quot;, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><summary style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent;">点击展开各平台最低支持版本：</summary><ul style="margin: 0.8em 0px; padding: 0px 0px 0px 2em; -webkit-tap-highlight-color: transparent; list-style: none;"><li style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; list-style: disc;">安卓微信：7.0.13</li><li style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; list-style: disc;">iOS 微信：7.0.12</li><li style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; list-style: disc;">微信开发者工具：1.05.2104272</li><li style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; list-style: disc;">PC 微信：3.4.5</li><li style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; list-style: disc;">macOS 微信：3.4.1</li><li style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; list-style: disc;">安卓企业微信：3.1.23</li><li style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; list-style: disc;">iOS 企业微信：4.0.8</li></ul></details>

## 跨分包自定义组件引用

一个分包使用其他分包的自定义组件时，由于其他分包还未下载或注入，其他分包的组件处于不可用的状态。通过为其他分包的自定义组件设置 [占位组件](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/placeholder.html)，我们可以先渲染占位组件作为替代，在分包下载完成后再进行替换。例如：

```json
// subPackageA/pages/index.json
{
  "usingComponents": {
    "button": "../../commonPackage/components/button",
    "list": "../../subPackageB/components/full-list",
    "simple-list": "../components/simple-list",
    "plugin-comp": "plugin://pluginInSubPackageB/comp"
  },
  "componentPlaceholder": {
    "button": "view",
    "list": "simple-list",
    "plugin-comp": "view"
  }
}
```

在这个配置中，`button` 和 `list` 两个自定义组件是跨分包引用组件，其中 `button` 在渲染时会使用内置组件 `view` 作为替代，`list` 会使用当前分包内的自定义组件 `simple-list` 作为替代进行渲染；在这两个分包下载完成后，占位组件就会被替换为对应的跨分包组件。

在基础库 `2.24.3` 之后，可以使用 [`wx.onLazyLoadError`](https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-event/wx.onLazyLoadError) 监听加载事件。

## 跨分包 JS 代码引用

一个分包中的代码引用其它分包的代码时，为了不让下载阻塞代码运行，我们需要异步获取引用的结果。如：

```js
// subPackageA/index.js
// 使用回调函数风格的调用
require('../subPackageB/utils.js', utils => {
  console.log(utils.whoami) // Wechat MiniProgram
}, ({mod, errMsg}) => {
  console.error(`path: ${mod}, ${errMsg}`)
})
// 或者使用 Promise 风格的调用
require.async('../commonPackage/index.js').then(pkg => {
  pkg.getPackageName() // 'common'
}).catch(({mod, errMsg}) => {
  console.error(`path: ${mod}, ${errMsg}`)
})
```

在其它分包中的插件也可以通过类似的方法调用：

```js
// 使用回调函数风格的调用
requirePlugin('live-player-plugin', livePlayer => {
  console.log(livePlayer.getPluginVersion())
}, ({mod, errMsg}) => {
  console.error(`path: ${mod}, ${errMsg}`)
})
// 或者使用 Promise 风格的调用
requirePlugin.async('live-player-plugin').then(livePlayer => {
  console.log(livePlayer.getPluginVersion())
}).catch(({mod, errMsg}) => {
  console.error(`path: ${mod}, ${errMsg}`)
})
```

详情可参考 [require 文档](https://developers.weixin.qq.com/miniprogram/dev/reference/api/require)