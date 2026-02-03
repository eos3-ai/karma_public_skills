# 预设路由

为降低开发成本，基础库预设了一批常见的路由动画效果。

| routeType                     | 最低基础库版本 |
| :---------------------------- | :------------- |
| `wx://bottom-sheet`           | 3.1.0          |
| `wx://upwards`                | 3.1.0          |
| `wx://zoom`                   | 3.1.0          |
| `wx://cupertino-modal`        | 3.1.0          |
| `wx://cupertino-modal-inside` | 3.1.0          |
| `wx://modal-navigation`       | 3.1.0          |
| `wx://modal`                  | 3.1.0          |

## 使用方法

仅需在路由跳转时，指定对应的 `routeType`。

注: 以上路由效果均可通过[自定义路由](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/custom-route.html)实现，可参考示例代码中的源码文件，自定义所需效果。

```js
wx.navigateTo({
  url: 'xxx',
  routeType: 'wx://modal'
})
```

## 示例代码

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/XC8BGymC7QMo)

## 效果演示

wx://bottom-sheet

半屏弹窗

wx://upwards

向上进入

wx://zoom

放大进入

wx://cupertino-modal-inside

wx-cupertino-modal 跳转到 wx-cupertino-modal-inside

wx://modal-navigation

wx-cupertino-modal 跳转到 wx-modal-navigation

wx://modal

wx-modal 跳转到 wx-modal-navigation

# 容器转场动画

通过将一个元素无缝地转换为另一个元素，可以加强两个元素间的关系，如常见的瀑布流中点击卡片跳转到详情页。

为降低开发成本，基础库提供了容器转场动画组件来实现该路由效果。

## 效果演示

<video id="video" autoplay="autoplay" loop="loop" controls="controls" preload="auto" width="800" height="400" poster="https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/open-container.html" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34); font-family: -apple-system, BlinkMacSystemFont, &quot;SF UI Text&quot;, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"></video>



## 使用方法

开发者工具需升级到 `Nightly` `1.06.2403222`，基础库选择 `3.4.0`

将需要进行过度的元素放置在 [``](https://developers.weixin.qq.com/miniprogram/dev/component/open-container.html) 组件内，点击 [``](https://developers.weixin.qq.com/miniprogram/dev/component/open-container.html)，当使用 `navigateTo` 跳转下一页面时，对其子节点和下一个页面进行过渡。

```html
<open-container
  closed-elevation="{{closedElevation}}"
  closed-border-radius="{{closedBorderRadius}}"
  open-elevation="{{openElevation}}"
  open-border-radius="{{openBorderRadius}}"
  transition-type="{{type}}"
  transition-duration="{{duration}}"
  bind:tap="goDetail"
>
  <card/>
</open-container>
Page({
   goDetail() {
    wx.navigateTo({
      url: 'nextPageUrl'
    })
  }
})
```

### 组件属性

| 属性                 | 类型   | 默认值 | 必填 | 说明                             |
| :------------------- | :----- | :----- | :--- | :------------------------------- |
| closed-color         | string | white  | 否   | 初始容器背景色                   |
| closed-elevation     | number | 0      | 否   | 初始容器影深大小                 |
| closed-border-radius | number | 0      | 否   | 初始容器圆角大小                 |
| middle-color         | string | ''     | 否   | `fadeThrough` 模式下的过渡背景色 |
| open-color           | string | white  | 否   | 打开状态下容器背景色             |
| open-elevation       | number | 0      | 否   | 打开状态下容器影深大小           |
| open-border-radius   | number | 0      | 否   | 打开状态下容器圆角大小           |
| transition-duration  | number | 300    | 否   | 动画时长                         |
| transition-type      | string | fade   | 否   | 动画类型                         |

## 示例代码片段

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/TMOyD8mB7YOB)

# 页面返回手势

默认情况下，小程序页面都是右滑返回。但在使用[自定义路由](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/custom-route.html)和[预设路由](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/preset-route.html)时，我们常常需要不同的手势返回效果。

例如使用 `wx://cupertino-modal` 路由效果时，下个页面自底向上出现，右滑返回并不符合视觉一致性。采用纵向的滑动返回（原路返回）会更合适一些。

## 使用方法

开发者工具需升级到 `Nightly` `1.06.2403222`，基础库选择 `3.4.0`。

### 一行代码配置

在[自定义路由配置](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/custom-route.html#默认路由配置)中，开发者可通过 `fullscreenDrag` 和 `popGestureDirection` 来定义手势返回效果。

| 属性                | 类型    | 默认值     | 说明                           |
| :------------------ | :------ | :--------- | :----------------------------- |
| popGestureDirection | string  | horizontal | 返回手势方向                   |
| fullscreenDrag      | boolean | false      | 右滑返回手势区域拓展到全屏范围 |

`popGestureDirection` 支持的枚举值如下

- horizontal：仅能横向拖动返回，fullscreenDrag 仅对横向拖动有效
- vertical: 仅能纵向拖动返回
- multi: 可以横向或纵向拖动返回

### 结合纵向滚动容器

当纵向拖动返回时，若页面内有纵向滚动的 `<scroll-view>`，默认在 `scroll-view` 上滑动无法触发页面返回。

此时可声明关联容器为 `pop-gesture`，此时滑动 [`scroll-view`](https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view.html) 至顶端后可继续触发页面返回。

```html
<scroll-view 
  type="custom"
  associative-container="pop-gesture"
>
  <!-- 页面内容 -->
</scroll-view>
```

### 结合预设路由

为增加路由配置的灵活性，`3.4.0` 版本起 [wx.navigateTo](https://developers.weixin.qq.com/miniprogram/dev/api/route/wx.navigateTo.html) 增加 `routeConfig` 和 `routeOptions` 两个属性。

#### routeConfig

[routeConfig 可配字段](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/custom-route.html#默认路由配置)。`navigateTo` 传入的 `routeConfig` 将会覆盖 `routeBuilder` 返回的配置项，开发者可借此更改 [预设路由](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/preset-route.html) 返回手势类型。

#### routeOptions

[routeBuilder 接口定义](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/custom-route.html#接口定义)。`routeOptions` 将作为 `routeBuilder` 的第二个参数传入，开发者可根据当前页面动态改变路由动画的内容。比如对 `BottomSheet` 更改高度、圆角等，以适应不同场景。

```js
interface INavigateToArg {
  url: string,
  routeType: string,
  routeConfig: CustomRouteConfig,
  routeOptions: Record<string, any>
}

wx.navigateTo({
  routeType: 'wx://bottom-sheet',
  routeConfig: {
    fullscreenDrag: true,
    popGestureDirection: 'multi'
  },
  routeOptions: {
    round: false,
  },
})
```

常用的 `wx://bottom-sheet` 预设路由 `routeOptions` 增加如下属性

| 属性   | 类型    | 默认值 | 说明                  |
| :----- | :------ | :----- | :-------------------- |
| round  | boolean | true   | 是否使用圆角          |
| height | number  | 60     | 弹窗页面高度，单位 vh |

## 示例代码片段

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/BGoSE0mS7KQS)