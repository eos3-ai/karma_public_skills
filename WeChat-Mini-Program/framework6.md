# 简易双向绑定

> 基础库 2.9.3 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

## 双向绑定语法

在 WXML 中，普通的属性的绑定是单向的。例如：

```html
<input value="{{value}}" />
```

如果使用 `this.setData({ value: 'leaf' })` 来更新 `value` ，`this.data.value` 和输入框的中显示的值都会被更新为 `leaf` ；但如果用户修改了输入框里的值，却不会同时改变 `this.data.value` 。

如果需要在用户输入的同时改变 `this.data.value` ，需要借助简易双向绑定机制。此时，可以在对应项目之前加入 `model:` 前缀：

```html
<input model:value="{{value}}" />
```

这样，如果输入框的值被改变了， `this.data.value` 也会同时改变。同时， WXML 中所有绑定了 `value` 的位置也会被一同更新， [数据监听器](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/observer.html) 也会被正常触发。

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/8jXvobmV7vcj)

用于双向绑定的表达式有如下限制：

1. 只能是一个单一字段的绑定，如

```js
<input model:value="值为 {{value}}" />
<input model:value="{{ a + b }}" />
```

都是非法的；

1. 目前，尚不能 data 路径，如

```js
<input model:value="{{ a.b }}" />
```

这样的表达式目前暂不支持。

## 在自定义组件中传递双向绑定

双向绑定同样可以使用在自定义组件上。如下的自定义组件：

```js
// custom-component.js
Component({
  properties: {
    myValue: String
  }
})
<!-- custom-component.wxml -->
<input model:value="{{myValue}}" />
```

这个自定义组件将自身的 `myValue` 属性双向绑定到了组件内输入框的 `value` 属性上。这样，如果页面这样使用这个组件：

```html
<custom-component model:my-value="{{pageValue}}" />
```

当输入框的值变更时，自定义组件的 `myValue` 属性会同时变更，这样，页面的 `this.data.pageValue` 也会同时变更，页面 WXML 中所有绑定了 `pageValue` 的位置也会被一同更新。

## 在自定义组件中触发双向绑定更新

自定义组件还可以自己触发双向绑定更新，做法就是：使用 setData 设置自身的属性。例如：

```js
// custom-component.js
Component({
  properties: {
    myValue: String
  },
  methods: {
    update: function() {
      // 更新 myValue
      this.setData({
        myValue: 'leaf'
      })
    }
  }
})
```

如果页面这样使用这个组件：

```html
<custom-component model:my-value="{{pageValue}}" />
```

当组件使用 `setData` 更新 `myValue` 时，页面的 `this.data.pageValue` 也会同时变更，页面 WXML 中所有绑定了 `pageValue` 的位置也会被一同更新。

# 基础组件

框架为开发者提供了一系列基础组件，开发者可以通过组合这些基础组件进行快速开发。详细介绍请参考[组件文档](https://developers.weixin.qq.com/miniprogram/dev/component/)。

什么是组件：

- 组件是视图层的基本组成单元。
- 组件自带一些功能与微信风格一致的样式。
- 一个组件通常包括 `开始标签` 和 `结束标签`，`属性` 用来修饰这个组件，`内容` 在两个标签之内。

```html
<tagname property="value">
Content goes here ...
</tagname>
```

**注意：所有组件与属性都是小写，以连字符`-`连接**

## 属性类型

| 类型         | 描述           | 注解                                                         |
| :----------- | :------------- | :----------------------------------------------------------- |
| Boolean      | 布尔值         | 组件写上该属性，不管是什么值都被当作 `true`；只有组件上没有该属性时，属性值才为`false`。 如果属性值为变量，变量的值会被转换为Boolean类型 |
| Number       | 数字           | `1`, `2.5`                                                   |
| String       | 字符串         | `"string"`                                                   |
| Array        | 数组           | `[ 1, "string" ]`                                            |
| Object       | 对象           | `{ key: value }`                                             |
| EventHandler | 事件处理函数名 | `"handlerName"` 是 [Page](https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page.html) 中定义的事件处理函数名 |
| Any          | 任意属性       |                                                              |

## 公共属性

所有组件都有以下属性：

| 属性名         | 类型         | 描述           | 注解                                                         |
| :------------- | :----------- | :------------- | :----------------------------------------------------------- |
| id             | String       | 组件的唯一标示 | 保持整个页面唯一                                             |
| class          | String       | 组件的样式类   | 在对应的 WXSS 中定义的样式类                                 |
| style          | String       | 组件的内联样式 | 可以动态设置的内联样式                                       |
| hidden         | Boolean      | 组件是否显示   | 所有组件默认显示                                             |
| data-*         | Any          | 自定义属性     | 组件上触发的事件时，会发送给事件处理函数                     |
| bind* / catch* | EventHandler | 组件的事件     | 详见[事件](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/event.html) |

## 特殊属性

几乎所有组件都有各自定义的属性，可以对该组件的功能或样式进行修饰，请参考各个[组件](https://developers.weixin.qq.com/miniprogram/dev/component/)的定义。

# 获取界面上的节点信息

## WXML节点信息

节点信息查询 API (`createSelectorQuery`) 可以用于获取节点属性、样式、在界面上的位置等信息。

最常见的用法是使用这个接口来查询某个节点的当前位置，以及界面的滚动位置。

**示例代码：**

```js
const query = this.createSelectorQuery()
query.select('#the-id').boundingClientRect(function(res){
  res.top // #the-id 节点的上边界坐标（相对于显示区域）
})
query.selectViewport().scrollOffset(function(res){
  res.scrollTop // 显示区域的竖直滚动位置
})
query.exec()
```

上述示例中， `#the-id` 是一个节点选择器，与 CSS 的选择器相近但略有区别，请参见 [SelectorQuery.select](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.select.html) 的相关说明。

在自定义组件或包含自定义组件的页面中，推荐使用 `this.createSelectorQuery` 来代替 [wx.createSelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/wx.createSelectorQuery.html) ，这样可以确保在正确的范围内选择节点。

## WXML节点布局相交状态

节点布局相交状态 API (`createIntersectionObserver`) 可用于监听两个或多个组件节点在布局位置上的相交状态。这一组 API 常常可以用于推断某些节点是否可以被用户看见、有多大比例可以被用户看见。

这一组API涉及的主要概念如下。

- 参照节点：监听的参照节点，取它的布局区域作为参照区域。如果有多个参照节点，则会取它们布局区域的 **交集** 作为参照区域。页面显示区域也可作为参照区域之一。
- 目标节点：监听的目标，默认只能是一个节点（使用 `selectAll` 选项时，可以同时监听多个节点）。
- 相交区域：目标节点的布局区域与参照区域的相交区域。
- 相交比例：相交区域占目标节点的布局区域的比例。
- 阈值：相交比例如果达到阈值，则会触发监听器的回调函数。阈值可以有多个。

以下示例代码可以在目标节点（用选择器 `.target-class` 指定）每次进入或离开页面显示区域时，触发回调函数。

**示例代码：**

```js
Page({
  onLoad: function(){
    this.createIntersectionObserver().relativeToViewport().observe('.target-class', (res) => {
      res.id // 目标节点 id
      res.dataset // 目标节点 dataset
      res.intersectionRatio // 相交区域占目标节点的布局区域的比例
      res.intersectionRect // 相交区域
      res.intersectionRect.left // 相交区域的左边界坐标
      res.intersectionRect.top // 相交区域的上边界坐标
      res.intersectionRect.width // 相交区域的宽度
      res.intersectionRect.height // 相交区域的高度
    })
  }
})
```

以下示例代码可以在目标节点（用选择器 `.target-class` 指定）与参照节点（用选择器 `.relative-class` 指定）在页面显示区域内相交或相离，且相交或相离程度达到目标节点布局区域的20%和50%时，触发回调函数。

**示例代码：**

```js
Page({
  onLoad: function(){
    this.createIntersectionObserver({
      thresholds: [0.2, 0.5]
    }).relativeTo('.relative-class').relativeToViewport().observe('.target-class', (res) => {
      res.intersectionRatio // 相交区域占目标节点的布局区域的比例
      res.intersectionRect // 相交区域
      res.intersectionRect.left // 相交区域的左边界坐标
      res.intersectionRect.top // 相交区域的上边界坐标
      res.intersectionRect.width // 相交区域的宽度
      res.intersectionRect.height // 相交区域的高度
    })
  }
})
```

注意：与页面显示区域的相交区域并不准确代表用户可见的区域，因为参与计算的区域是“布局区域”，布局区域可能会在绘制时被其他节点裁剪隐藏（如遇祖先节点中 overflow 样式为 hidden 的节点）或遮盖（如遇 fixed 定位的节点）。

在自定义组件或包含自定义组件的页面中，推荐使用 `this.createIntersectionObserver` 来代替 [wx.createIntersectionObserver](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/wx.createIntersectionObserver.html) ，这样可以确保在正确的范围内选择节点。

# 响应显示区域变化

## 显示区域尺寸

显示区域指小程序界面中可以自由布局展示的区域。在默认情况下，小程序显示区域的尺寸自页面初始化起就不会发生变化。但以下三种方式都可以改变这一默认行为。

### 在手机上启用屏幕旋转支持

从小程序基础库版本 [2.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，小程序在手机上支持屏幕旋转。使小程序中的页面支持屏幕旋转的方法是：在 `app.json` 的 `window` 段中设置 `"pageOrientation": "auto"` ，或在页面 json 文件中配置 `"pageOrientation": "auto"` 。

以下是在单个页面 json 文件中启用屏幕旋转的示例。

**代码示例：**

```json
{
  "pageOrientation": "auto"
}
```

如果页面添加了上述声明，则在屏幕旋转时，这个页面将随之旋转，显示区域尺寸也会随着屏幕旋转而变化。

从小程序基础库版本 [2.5.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始， `pageOrientation` 还可以被设置为 `landscape` ，表示固定为横屏显示。

### 在 iPad 上启用屏幕旋转支持

从小程序基础库版本 [2.3.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，在 iPad 上运行的小程序可以支持屏幕旋转。使小程序支持 iPad 屏幕旋转的方法是：在 `app.json` 中添加 `"resizable": true` 。

**代码示例：**

```json
{
  "resizable": true
}
```

如果小程序添加了上述声明，则在屏幕旋转时，小程序将随之旋转，显示区域尺寸也会随着屏幕旋转而变化。注意：在 iPad 上不能单独配置某个页面是否支持屏幕旋转。

### 启用大屏模式

从小程序基础库版本 [2.21.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，在 Windows、Mac、车机、安卓 WMPF 等大屏设备上运行的小程序可以支持大屏模式。可参考[小程序大屏适配指南](https://developers.weixin.qq.com/miniprogram/design/adapt.html)。方法是：在 `app.json` 中添加 `"resizable": true` 。

**代码示例：**

```json
{
  "resizable": true
}
```

如果小程序添加了上述声明，在大屏设备上运行时，小程序的默认窗口尺寸将会变大，同时用户可以自由拉伸。

## Media Query

有时，对于不同尺寸的显示区域，页面的布局会有所差异。此时可以使用 media query 来解决大多数问题。

**代码示例：**

```css
.my-class {
  width: 40px;
}

@media (min-width: 480px) {
  /* 仅在 480px 或更宽的屏幕上生效的样式规则 */
  .my-class {
    width: 200px;
  }
}
```

在 WXML 中，可以使用 [match-media](https://developers.weixin.qq.com/miniprogram/dev/component/match-media.html) 组件来根据 media query 匹配状态展示、隐藏节点。

此外，可以在页面或者自定义组件 JS 中使用 `this.createMediaQueryObserver()` 方法来创建一个 [`MediaQueryObserver`](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/MediaQueryObserver.html) 对象，用于监听指定的 media query 的匹配状态。

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/TtFaFjmb7aiy)

## 屏幕旋转事件

有时，仅仅使用 media query 无法控制一些精细的布局变化。此时可以使用 js 作为辅助。

在 js 中读取页面的显示区域尺寸，可以使用 [selectorQuery.selectViewport](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.selectViewport.html) 。

页面尺寸发生改变的事件，可以使用页面的 `onResize` 来监听。对于自定义组件，可以使用 resize 生命周期来监听。回调函数中将返回显示区域的尺寸信息。（从基础库版本 [2.4.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始支持。）

**代码示例：**

```js
Page({
  onResize(res) {
    res.size.windowWidth // 新的显示区域宽度
    res.size.windowHeight // 新的显示区域高度
  }
})
Component({
  pageLifetimes: {
    resize(res) {
      res.size.windowWidth // 新的显示区域宽度
      res.size.windowHeight // 新的显示区域高度
    }
  }
})
```

此外，还可以使用 [wx.onWindowResize](https://developers.weixin.qq.com/miniprogram/dev/api/ui/window/wx.onWindowResize.html) 来监听（但这不是推荐的方式）。

## 注意事项

- Bug： Android 微信版本 6.7.3 中， `live-pusher` 组件在屏幕旋转时方向异常。

- # 分栏模式

  在 PC 等能够以较大屏幕显示小程序的环境下，小程序支持以分栏模式展示。分栏模式可以将微信窗口分为左右两半，各展示一个页面。

  ![frameset-screenshot](https://res.wx.qq.com/wxdoc/dist/assets/img/frameset.59c5e57e.png)

  目前， Windows 微信 3.3 以上版本支持分栏模式。对于其他版本微信，分栏模式不会生效。

  ## 启用分栏模式

  在 app.json 中同时添加 `"resizable": true` 和 `"frameset": true` 两个配置项就可以启用分栏模式。

  **代码示例：**

  ```json
  {
    "resizable": true,
    "frameset": true
  }
  ```

  启用分栏模式后，可以使用开发者工具的自动预览功能来预览分栏效果。

  ## 分栏占位图片

  当某一栏没有展示任何页面时，会展示一张图片在此栏正中央。

  如果代码包中的 `frameset/placeholder.png` 文件存在，这张图片将作为此时展示的图片。

  ## 分栏适配要点

  启用分栏模式后，一些已有代码逻辑可能出现问题。可能需要更改代码来使其能够在分栏模式下正确运行。

  ### 避免使用更改页面展示效果的接口

  更改当前页面展示效果的接口，总是对最新打开的页面生效。

  例如，在右栏打开一个新页面后，更改页面标题的接口 [wx.setNavigationBarTitle](https://developers.weixin.qq.com/miniprogram/dev/api/ui/navigation-bar/wx.setNavigationBarTitle.html) 即使是在左栏的页面中调用，也将更改右栏内页面的标题！

  因此，应当尽量避免使用这样的接口，而是改用 [page-meta](https://developers.weixin.qq.com/miniprogram/dev/component/page-meta.html) 和 [navigation-bar](https://developers.weixin.qq.com/miniprogram/dev/component/navigation-bar.html) 组件代替。

  ### 变更路由接口调用

  如果在路由接口中使用相对路径，总是相对于最新打开的页面路径。

  例如，在右栏打开一个新页面后，路由接口 [wx.navigateTo](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateTo.html) 即使是在左栏的页面中调用，跳转路径也将相对于右栏内页面的路径！

  因此，应当将这样的路由接口改成 [Router](https://developers.weixin.qq.com/miniprogram/dev/reference/api/Router.html) 接口调用，如 `this.pageRouter.navigateTo` 。

  ### 页面大小不是固定值

  启用分栏模式的同时，页面大小也是可能动态变化的了。请使用 [响应显示区域变化](https://developers.weixin.qq.com/miniprogram/dev/framework/view/resizable.html) 的方法来处理页面大小变化时的响应方式。

  # 动画

  ## 界面动画的常见方式

  在小程序中，通常可以使用 [CSS 渐变](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions) 和 [CSS 动画](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Animations/Using_CSS_animations) 来创建简易的界面动画。

  [在开发者工具中预览效果](https://developers.weixin.qq.com/s/oHKxDPm47h5k)

  动画过程中，可以使用 `bindtransitionend` `bindanimationstart` `bindanimationiteration` `bindanimationend` 来监听动画事件。

  | 事件名             | 含义                                                         |
  | :----------------- | :----------------------------------------------------------- |
  | transitionend      | CSS 渐变结束或 [wx.createAnimation](https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/wx.createAnimation.html) 结束一个阶段 |
  | animationstart     | CSS 动画开始                                                 |
  | animationiteration | CSS 动画结束一个阶段                                         |
  | animationend       | CSS 动画结束                                                 |

  注意：这几个事件都不是冒泡事件，需要绑定在真正发生了动画的节点上才会生效。

  同时，还可以使用 [wx.createAnimation](https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/wx.createAnimation.html) 接口来动态创建简易的动画效果。（新版小程序基础库中推荐使用下述的关键帧动画接口代替。）

  ## 关键帧动画

  > 基础库 2.9.0 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

  从小程序基础库 [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始支持一种更友好的动画创建方式，用于代替旧的 [wx.createAnimation](https://developers.weixin.qq.com/miniprogram/dev/api/ui/animation/wx.createAnimation.html) 。它具有更好的性能和更可控的接口。

  在页面或自定义组件中，当需要进行关键帧动画时，可以使用 `this.animate` 接口：

  ```js
  this.animate(selector, keyframes, duration, callback)
  ```

  **参数说明**

  | 属性      | 类型     | 默认值 | 必填 | 说明                                                         |
  | :-------- | :------- | :----- | :--- | :----------------------------------------------------------- |
  | selector  | String   |        | 是   | 选择器（同 [SelectorQuery.select](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.select.html) 的选择器格式） |
  | keyframes | Array    |        | 是   | 关键帧信息                                                   |
  | duration  | Number   |        | 是   | 动画持续时长（毫秒为单位）                                   |
  | callback  | function |        | 否   | 动画完成后的回调函数                                         |

  **keyframes 中对象的结构**

  | 属性            | 类型   | 默认值 | 必填                              | 说明                                    |
  | :-------------- | :----- | :----- | :-------------------------------- | :-------------------------------------- |
  | offset          | Number |        | 否                                | 关键帧的偏移，范围[0-1]                 |
  | ease            | String | linear | 否                                | 动画缓动函数                            |
  | transformOrigin | String | 否     | 基点位置，即 CSS transform-origin |                                         |
  | backgroundColor | String |        | 否                                | 背景颜色，即 CSS background-color       |
  | opacity         | Number |        | 否                                | 不透明度，即 CSS opacity                |
  | width           | String |        | 否                                | 宽度，即 CSS width                      |
  | height          | String |        | 否                                | 高度，即 CSS height                     |
  | left            | String |        | 否                                | 左边位置，即 CSS left                   |
  | top             | String |        | 否                                | 顶边位置，即 CSS top                    |
  | right           | String |        | 否                                | 右边位置，即 CSS right                  |
  | bottom          | String |        | 否                                | 底边位置，即 CSS bottom                 |
  | matrix          | Array  |        | 否                                | 变换矩阵，即 CSS transform matrix       |
  | matrix3d        | Array  |        | 否                                | 三维变换矩阵，即 CSS transform matrix3d |
  | rotate          | Number |        | 否                                | 旋转，即 CSS transform rotate           |
  | rotate3d        | Array  |        | 否                                | 三维旋转，即 CSS transform rotate3d     |
  | rotateX         | Number |        | 否                                | X 方向旋转，即 CSS transform rotateX    |
  | rotateY         | Number |        | 否                                | Y 方向旋转，即 CSS transform rotateY    |
  | rotateZ         | Number |        | 否                                | Z 方向旋转，即 CSS transform rotateZ    |
  | scale           | Array  |        | 否                                | 缩放，即 CSS transform scale            |
  | scale3d         | Array  |        | 否                                | 三维缩放，即 CSS transform scale3d      |
  | scaleX          | Number |        | 否                                | X 方向缩放，即 CSS transform scaleX     |
  | scaleY          | Number |        | 否                                | Y 方向缩放，即 CSS transform scaleY     |
  | scaleZ          | Number |        | 否                                | Z 方向缩放，即 CSS transform scaleZ     |
  | skew            | Array  |        | 否                                | 倾斜，即 CSS transform skew             |
  | skewX           | Number |        | 否                                | X 方向倾斜，即 CSS transform skewX      |
  | skewY           | Number |        | 否                                | Y 方向倾斜，即 CSS transform skewY      |
  | translate       | Array  |        | 否                                | 位移，即 CSS transform translate        |
  | translate3d     | Array  |        | 否                                | 三维位移，即 CSS transform translate3d  |
  | translateX      | Number |        | 否                                | X 方向位移，即 CSS transform translateX |
  | translateY      | Number |        | 否                                | Y 方向位移，即 CSS transform translateY |
  | translateZ      | Number |        | 否                                | Z 方向位移，即 CSS transform translateZ |

  ### 示例代码

  [在开发者工具中预览效果](https://developers.weixin.qq.com/s/P73kJ7mi7UcA)

  ```javascript
    this.animate('#container', [
      { opacity: 1.0, rotate: 0, backgroundColor: '#FF0000' },
      { opacity: 0.5, rotate: 45, backgroundColor: '#00FF00'},
      { opacity: 0.0, rotate: 90, backgroundColor: '#FF0000' },
      ], 5000, function () {
        this.clearAnimation('#container', { opacity: true, rotate: true }, function () {
          console.log("清除了#container上的opacity和rotate属性")
        })
    }.bind(this))
  
    this.animate('.block', [
      { scale: [1, 1], rotate: 0, ease: 'ease-out'  },
      { scale: [1.5, 1.5], rotate: 45, ease: 'ease-in', offset: 0.9},
      { scale: [2, 2], rotate: 90 },
    ], 5000, function () {
      this.clearAnimation('.block', function () {
        console.log("清除了.block上的所有动画属性")
      })
    }.bind(this))
  ```

  调用 animate API 后会在节点上新增一些样式属性覆盖掉原有的对应样式。如果需要清除这些样式，可在该节点上的动画全部执行完毕后使用 `this.clearAnimation` 清除这些属性。

  ```js
  this.clearAnimation(selector, options, callback)
  ```

  **参数说明**

  | 属性     | 类型     | 默认值 | 必填 | 说明                                                         |
  | :------- | :------- | :----- | :--- | :----------------------------------------------------------- |
  | selector | String   |        | 是   | 选择器（同 [SelectorQuery.select](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.select.html) 的选择器格式） |
  | options  | Object   |        | 否   | 需要清除的属性，不填写则全部清除                             |
  | callback | Function |        | 否   | 清除完成后的回调函数                                         |

  ## 滚动驱动的动画

  我们发现，根据滚动位置而不断改变动画的进度是一种比较常见的场景，这类动画可以让人感觉到界面交互很连贯自然，体验更好。因此，从小程序基础库 [2.9.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始支持一种由滚动驱动的动画机制。

  基于上述的关键帧动画接口，新增一个 `ScrollTimeline` 的参数，用来绑定滚动元素（目前只支持 scroll-view）。接口定义如下：

  ```javascript
  this.animate(selector, keyframes, duration, ScrollTimeline)
  ```

  **ScrollTimeline 中对象的结构**

  | 属性              | 类型   | 默认值   | 必填 | 说明                                                         |
  | :---------------- | :----- | :------- | :--- | :----------------------------------------------------------- |
  | scrollSource      | String |          | 是   | 指定滚动元素的选择器（只支持 scroll-view），该元素滚动时会驱动动画的进度 |
  | orientation       | String | vertical | 否   | 指定滚动的方向。有效值为 horizontal 或 vertical              |
  | startScrollOffset | Number |          | 是   | 指定开始驱动动画进度的滚动偏移量，单位 px                    |
  | endScrollOffset   | Number |          | 是   | 指定停止驱动动画进度的滚动偏移量，单位 px                    |
  | timeRange         | Number |          | 是   | 起始和结束的滚动范围映射的时间长度，该时间可用于与关键帧动画里的时间 (duration) 相匹配，单位 ms |

  ### 示例代码

  [在开发者工具中预览效果](https://developers.weixin.qq.com/s/994o8jmY7FcQ)

  ```javascript
    this.animate('.avatar', [{
      borderRadius: '0',
      borderColor: 'red',
      transform: 'scale(1) translateY(-20px)',
      offset: 0,
    }, {
      borderRadius: '25%',
      borderColor: 'blue',
      transform: 'scale(.65) translateY(-20px)',
      offset: .5,
    }, {
      borderRadius: '50%',
      borderColor: 'blue',
      transform: `scale(.3) translateY(-20px)`,
      offset: 1
    }], 2000, {
      scrollSource: '#scroller',
      timeRange: 2000,
      startScrollOffset: 0,
      endScrollOffset: 85,
    })
  
    this.animate('.search_input', [{
      opacity: '0',
      width: '0%',
    }, {
      opacity: '1',
      width: '100%',
    }], 1000, {
      scrollSource: '#scroller',
      timeRange: 1000,
      startScrollOffset: 120,
      endScrollOffset: 252
    })
  ```

  ## 高级的动画方式

  在一些复杂场景下，上述的动画方法可能并不适用。

  [WXS 响应事件](https://developers.weixin.qq.com/miniprogram/dev/framework/view/interactive-animation.html) 的方式可以通过使用 WXS 来响应事件的方法来动态调整节点的 style 属性。通过不断改变 style 属性的值可以做到动画效果。同时，这种方式也可以根据用户的触摸事件来动态地生成动画。

  连续使用 setData 来改变界面的方法也可以达到动画的效果。这样可以任意地改变界面，但通常会产生较大的延迟或卡顿，甚至导致小程序僵死。此时可以通过将页面的 setData 改为 [自定义组件](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/) 中的 setData 来提升性能。下面的例子是使用 setData 来实现秒表动画的示例。

  [在开发者工具中预览效果](https://developers.weixin.qq.com/s/cRTvdPmO7d5T)

  # 初始渲染缓存

  > 基础库 2.11.1 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

  ## 初始渲染缓存工作原理

  小程序页面的初始化分为两个部分。

  - 逻辑层初始化：载入必需的小程序代码、初始化页面 this 对象（也包括它涉及到的所有自定义组件的 this 对象）、将相关数据发送给视图层。
  - 视图层初始化：载入必需的小程序代码，然后等待逻辑层初始化完毕并接收逻辑层发送的数据，最后渲染页面。

  在启动页面时，尤其是小程序冷启动、进入第一个页面时，逻辑层初始化的时间较长。在页面初始化过程中，用户将看到小程序的标准载入画面（冷启动时）或可能看到轻微的白屏现象（页面跳转过程中）。

  启用初始渲染缓存，可以使视图层不需要等待逻辑层初始化完毕，而直接提前将页面初始 data 的渲染结果展示给用户，这可以使得页面对用户可见的时间大大提前。它的工作原理如下：

  - 在小程序页面第一次被打开后，将页面初始数据渲染结果记录下来，写入一个持久化的缓存区域（缓存可长时间保留，但可能因为小程序更新、基础库更新、储存空间回收等原因被清除）；
  - 在这个页面被第二次打开时，检查缓存中是否还存有这个页面上一次初始数据的渲染结果，如果有，就直接将渲染结果展示出来；
  - 如果展示了缓存中的渲染结果，这个页面暂时还不能响应用户事件，等到逻辑层初始化完毕后才能响应用户事件。

  利用初始渲染缓存，可以：

  - 快速展示出页面中永远不会变的部分，如导航栏；
  - 预先展示一个骨架页，提升用户体验；
  - 展示自定义的加载提示；
  - 提前展示广告，等等。

  ## 支持的组件

  在初始渲染缓存阶段中，复杂组件不能被展示或不能响应交互。

  目前支持的内置组件：

  - `<view />`
  - `<text />`
  - `<button />`
  - `<image />`
  - `<scroll-view />`
  - `<rich-text />`

  自定义组件本身可以被展示（但它们里面用到的内置组件也遵循上述限制）。

  ## 静态初始渲染缓存

  若想启用初始渲染缓存，最简单的方法是在页面的 `json` 文件中添加配置项 `"initialRenderingCache": "static"` ：

  ```json
  {
    "initialRenderingCache": "static"
  }
  ```

  如果想要对所有页面启用，可以在 `app.json` 的 `window` 配置段中添加这个配置：

  ```json
  {
    "window": {
      "initialRenderingCache": "static"
    }
  }
  ```

  添加这个配置项之后，在手机中预览小程序首页，然后杀死小程序再次进入，就会通过初始渲染缓存来渲染首页。

  注意：这种情况下，初始渲染缓存记录的是页面 data 应用在页面 WXML 上的结果，不包含任何 setData 的结果。

  例如，如果想要在页面中展示出“正在加载”几个字，这几个字受到 `loading` 数据字段控制：

  ```html
  <view wx:if="{{loading}}">正在加载</view>
  ```

  这种情况下， `loading` 应当在 `data` 中指定为 `true` ，如：

  ```js
  // 正确的做法
  Page({
    data: {
      loading: true
    }
  })
  ```

  而不能通过 `setData` 将 `loading` 置为 `true` ：

  ```js
  // 错误的做法！不要这么做！
  Page({
    data: {},
    onLoad: function() {
      this.setData({
        loading: true
      })
    }
  })
  ```

  换而言之，这种做法只包含页面 `data` 的渲染结果，即页面的纯静态成分。

  ## 自定义渲染缓存时机

  > 基础库 3.7.4 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

  静态初始渲染缓存只在页面首次渲染完成后生成渲染缓存，在 `onLoad` 或之后的生命周期新增的页面内容无法进入缓存中。如果想要在自定义的时机生成缓存，可以配置 `"initialRenderingCache": "capture"` ：

  ```json
  {
    "initialRenderingCache": "capture"
  }
  ```

  此时，初始渲染缓存不会被自动启用，还需要在页面中调用 `this.setInitialRenderingCache()` 才能启用。

  ```js
  Page({
    data: {
      loading: true
    },
    onLoad: function() {
      this.setData({
        loading: false
      })
      this.setInitialRenderingCache() // 渲染缓存会在此时生成
    }
  })
  ```

  ## 在初始渲染缓存中添加动态内容

  有些场景中，只是页面 `data` 的渲染结果会比较局限。有时会想要额外展示一些可变的内容。

  这种情况下可以使用“动态”初始渲染缓存的方式。首先，配置 `"initialRenderingCache": "dynamic"` ：

  ```json
  {
    "initialRenderingCache": "dynamic"
  }
  ```

  此时，初始渲染缓存不会被自动启用，还需要在页面中调用 `this.setInitialRenderingCache(dynamicData)` 才能启用。其中， `dynamicData` 是一组数据，与 `data` 一起参与页面 WXML 渲染。

  ```js
  Page({
    data: {
      loading: true
    },
    onReady: function() {
      this.setInitialRenderingCache({
        loadingHint: '正在加载' // 这一部分数据不会真的参与页面渲染，仅仅用于生成缓存。也并*不等价*于一次 setData 调用
      })
    }
  })
  <view wx:if="{{loading}}">{{loadingHint}}</view>
  ```

  从原理上说，在动态生成初始渲染缓存的方式下，页面会在后台使用动态数据重新渲染一次，因而开销相对较大。因而要尽量避免频繁调用 `this.setInitialRenderingCache` ，如果在一个页面内多次调用，仅最后一次调用生效。

  注意：

  - `this.setInitialRenderingCache` 调用时机不能早于 `Page` 的 `onReady` 或 `Component` 的 `ready` 生命周期，否则可能对性能有负面影响。
  - 如果想禁用初始渲染缓存，调用 `this.setInitialRenderingCache(null)` 。