# 自定义组件

从小程序基础库版本 [1.6.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，小程序支持简洁的组件化编程。所有自定义组件相关特性都需要基础库版本 [1.6.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 或更高。

开发者可以将页面内的功能模块抽象成自定义组件，以便在不同的页面中重复使用；也可以将复杂的页面拆分成多个低耦合的模块，有助于代码维护。自定义组件在使用时与基础组件非常相似。

## 创建自定义组件

类似于页面，一个自定义组件由 `json` `wxml` `wxss` `js` 4个文件组成。要编写一个自定义组件，首先需要在 `json` 文件中进行自定义组件声明（将 `component` 字段设为 `true` 可将这一组文件设为自定义组件）：

```json
{
  "component": true
}
```

同时，还要在 `wxml` 文件中编写组件模板，在 `wxss` 文件中加入组件样式，它们的写法与页面的写法类似。具体细节和注意事项参见 [组件模板和样式](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/wxml-wxss.html) 。

**代码示例：**

```html
<!-- 这是自定义组件的内部WXML结构 -->
<view class="inner">
  {{innerText}}
</view>
<slot></slot>
/* 这里的样式只应用于这个自定义组件 */
.inner {
  color: red;
}
```

**注意：在组件wxss中不应使用ID选择器、属性选择器和标签名选择器。**

在自定义组件的 `js` 文件中，需要使用 `Component()` 来注册组件，并提供组件的属性定义、内部数据和自定义方法。

组件的属性值和内部数据将被用于组件 `wxml` 的渲染，其中，属性值是可由组件外部传入的。更多细节参见 [Component构造器](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/component.html) 。

**代码示例：**

```js
Component({
  properties: {
    // 这里定义了innerText属性，属性值可以在组件使用时指定
    innerText: {
      type: String,
      value: 'default value',
    }
  },
  data: {
    // 这里是一些组件内部数据
    someData: {}
  },
  methods: {
    // 这里是一个自定义方法
    customMethod: function(){}
  }
})
```

## 使用自定义组件

使用已注册的自定义组件前，首先要在页面的 `json` 文件中进行引用声明。此时需要提供每个自定义组件的标签名和对应的自定义组件文件路径：

```json
{
  "usingComponents": {
    "component-tag-name": "path/to/the/custom/component"
  }
}
```

这样，在页面的 `wxml` 中就可以像使用基础组件一样使用自定义组件。节点名即自定义组件的标签名，节点属性即传递给组件的属性值。

> 开发者工具 1.02.1810190 及以上版本支持在 app.json 中声明 usingComponents 字段，在此处声明的自定义组件视为全局自定义组件，在小程序内的页面或自定义组件中可以直接使用而无需再声明。

**代码示例：**

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/OMfVAKmZ6KZT)

```html
<view>
  <!-- 以下是对一个自定义组件的引用 -->
  <component-tag-name inner-text="Some text"></component-tag-name>
</view>
```

自定义组件的 `wxml` 节点结构在与数据结合之后，将被插入到引用位置内。

## 注意事项

一些需要注意的细节：

- 因为 WXML 节点标签名只能是小写字母、中划线和下划线的组合，所以自定义组件的标签名也只能包含这些字符。
- 自定义组件也是可以引用自定义组件的，引用方法类似于页面引用自定义组件的方式（使用 `usingComponents` 字段）。
- 自定义组件和页面所在项目根目录名不能以“wx-”为前缀，否则会报错。

注意，是否在页面文件中使用 `usingComponents` 会使得页面的 `this` 对象的原型稍有差异，包括：

- 使用 `usingComponents` 页面的原型与不使用时不一致，即 `Object.getPrototypeOf(this)` 结果不同。
- 使用 `usingComponents` 时会多一些方法，如 `selectComponent` 。
- 出于性能考虑，使用 `usingComponents` 时， `setData` 内容不会被直接深复制，即 `this.setData({ field: obj })` 后 `this.data.field === obj` 。（深复制会在这个值被组件间传递时发生。）

如果页面比较复杂，新增或删除 `usingComponents` 定义段时建议重新测试一下。

# 组件系统

小程序的组件系统与常见的前端框架有所不同，小程序的运行时组织结构包含了一些独特的设计和概念。

## Shadow 树与组件封装

小程序采用了类似 Shadow DOM 的概念来实现组件的封装。每个自定义组件都拥有自己的 Shadow 树，从而将组件的样式和结构与外部环境隔离。这种隔离机制使得组件更加模块化，可以独立管理自己的样式和逻辑，避免受到全局样式的干扰。

基本概念：

- Host Element: 即自定义组件本身，拥有一个 Shadow Root 节点。
- Shadow Root: Shadow 树的根节点，通常包含组件的 WXML 内容。
- Shadow Tree: 被 Shadow Root 包裹的子树，里面内容通常为 WXML 内写的内容。
- Slot Element: WXML 中写的 `<slot>` 节点，用于插入 Host 元素的子节点到 Shadow 树中的指定位置。

**代码示例：**

```html
<!-- 这是自定义组件 comp 的 WXML 结构 -->
<view class="inner">
  {{innerText}}
</view>
<slot></slot>
<!-- 这是使用 comp 的 WXML 结构 -->
<comp>
  <view class="outer"></view>
</comp>
```

最终所构造出的树结构为：

```html
<comp> <!-- 这是 Host Element -->
  #shadow-root <!-- 这里是 comp 组件的 Shadow 树 -->
    <view class="inner">{{innerText}}</view>
    <slot></slot> <!-- outer 会被插入到这里 -->
  <view class="outer"></view> <!-- outer 不属于 comp 组件的 Shadow 树 -->
</comp>
```

### Shadow 树的限制

通过 Shadow 树提供的封装能力，组件间的样式和逻辑得到了更明确的隔离，从而避免了外部的干扰。具体来说，Shadow 树有以下几个限制：

#### 1. 样式隔离

组件的样式被与其他组件的 WXSS 以及全局的 `app.wxss` 隔离开来，彼此间无法互相覆盖或影响，也无法直接使用全局的 `class`。

**提示:** 你可以通过 [组件样式隔离](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/wxml-wxss.html#组件样式隔离) 或 [外部样式类](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/wxml-wxss.html#外部样式类) 等方式，灵活地控制样式的隔离。

#### 2. 事件隔离

通过 [triggerEvent](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html#触发事件) 触发的事件会被限制在 Shadow 树内进行捕获和冒泡，外部组件无法直接监听这些事件。

**提示:** 你可以通过设置 `composed` 参数，改变事件的冒泡和捕获行为，从而允许外部监听。

#### 3. SelectQuery 隔离

使用 [SelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.html) 获取节点时，只能获取当前 Shadow 树内的节点，无法访问其他组件的 Shadow 树或外部元素。

#### 4. slot 状态

默认情况下，Host 节点的子节点的 `attached` 和 `detached` 状态仅与节点本身的挂载状态相关，而与 Shadow 树中的 `<slot>` 节点挂载状态无关。

```html
<comp> <!-- 这是 Host Element -->
  #shadow-root <!-- 这里是 comp 组件的 Shadow 树 -->
    <view class="inner">{{innerText}}</view>
    <slot wx:if="{{showSlot}}"></slot> <!-- outer 会被插入到这里 -->
  <view class="outer"></view> <!-- 即使 showSlot 为 false，outer 也是 attached 状态 -->
</comp>
```

**提示:** 你可以设置 [动态 slot](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/dynamic-slots.html) 改变此行为。

## Composed 树

在页面和组件渲染结构中，经过剔除虚拟节点和 Shadow Root 节点后，子节点会插入到对应的 `<slot>` 位置，最终形成 Composed 树。

它更加贴近实际的渲染结果，可以帮助开发者更清晰地看到组件和节点之间的真实关系。

**提示:** 你可以在调试面板中切换 Shadow 树和 Composed 树的展示

![alt text](https://res.wx.qq.com/wxdoc/dist/assets/img/custom-component-system.f754a0e6.png)

# 组件模板和样式

类似于页面，自定义组件拥有自己的 `wxml` 模板和 `wxss` 样式。

## 组件模板

组件模板的写法与页面模板相同。组件模板与组件数据结合后生成的节点树，将被插入到组件的引用位置上。

在组件模板中可以提供一个 `<slot>` 节点，用于承载组件引用时提供的子节点。

**代码示例：**

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/1udXLnmi6KY2)

```html
<!-- 组件模板 -->
<view class="wrapper">
  <view>这里是组件的内部节点</view>
  <slot></slot>
</view>
<!-- 引用组件的页面模板 -->
<view>
  <component-tag-name>
    <!-- 这部分内容将被放置在组件 <slot> 的位置上 -->
    <view>这里是插入到组件slot中的内容</view>
  </component-tag-name>
</view>
```

注意，在模板中引用到的自定义组件及其对应的节点名需要在 `json` 文件中显式定义，否则会被当作一个无意义的节点。除此以外，节点名也可以被声明为[抽象节点](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/generics.html)。

## 模板数据绑定

与普通的 WXML 模板类似，可以使用数据绑定，这样就可以向子组件的属性传递动态数据。

**代码示例：**

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/8ZhcXBme7djX)

```html
<!-- 引用组件的页面模板 -->
<view>
  <component-tag-name prop-a="{{dataFieldA}}" prop-b="{{dataFieldB}}">
    <!-- 这部分内容将被放置在组件 <slot> 的位置上 -->
    <view>这里是插入到组件slot中的内容</view>
  </component-tag-name>
</view>
```

在以上例子中，组件的属性 `propA` 和 `propB` 将收到页面传递的数据。页面可以通过 `setData` 来改变绑定的数据字段。

注意：这样的数据绑定只能传递 JSON 兼容数据。自基础库版本 [2.0.9](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始，还可以在数据中包含函数（但这些函数不能在 WXML 中直接调用，只能传递给子组件）。

## 组件 wxml 的 slot

在组件的 wxml 中可以包含 `slot` 节点，用于承载组件使用者提供的 wxml 结构。

默认情况下，一个组件的 wxml 中只能有一个 slot 。需要使用多 slot 时，可以在组件 js 中声明启用。

```js
Component({
  options: {
    multipleSlots: true // 在组件定义时的选项中启用多slot支持
  },
  properties: { /* ... */ },
  methods: { /* ... */ }
})
```

此时，可以在这个组件的 wxml 中使用多个 slot ，以不同的 `name` 来区分。

```html
<!-- 组件模板 -->
<view class="wrapper">
  <slot name="before"></slot>
  <view>这里是组件的内部细节</view>
  <slot name="after"></slot>
</view>
```

使用时，用 `slot` 属性来将节点插入到不同的 slot 上。

```html
<!-- 引用组件的页面模板 -->
<view>
  <component-tag-name>
    <!-- 这部分内容将被放置在组件 <slot name="before"> 的位置上 -->
    <view slot="before">这里是插入到组件slot name="before"中的内容</view>
    <!-- 这部分内容将被放置在组件 <slot name="after"> 的位置上 -->
    <view slot="after">这里是插入到组件slot name="after"中的内容</view>
  </component-tag-name>
</view>
```

## 组件样式

组件对应 `wxss` 文件的样式，只对组件wxml内的节点生效。编写组件样式时，需要注意以下几点：

- 组件和引用组件的页面不能使用id选择器（`#a`）、属性选择器（`[a]`）和标签名选择器，请改用class选择器。
- 组件和引用组件的页面中使用后代选择器（`.a .b`）在一些极端情况下会有非预期的表现，如遇，请避免使用。
- 子元素选择器（`.a>.b`）只能用于 `view` 组件与其子节点之间，用于其他组件可能导致非预期的情况。
- 继承样式，如 `font` 、 `color` ，会从组件外继承到组件内。
- 除继承样式外， `app.wxss` 中的样式、组件所在页面的的样式对自定义组件无效（除非更改组件样式隔离选项）。

```css
#a { } /* 在组件中不能使用 */
[a] { } /* 在组件中不能使用 */
button { } /* 在组件中不能使用 */
.a > .b { } /* 除非 .a 是 view 组件节点，否则不一定会生效 */
```

除此以外，组件可以指定它所在节点的默认样式，使用 `:host` 选择器（需要包含基础库 [1.7.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 或更高版本的开发者工具支持）。

**代码示例：**

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/jAgvwKm16bZD)

```css
/* 组件 custom-component.wxss */
:host {
  color: yellow;
}
<!-- 页面的 WXML -->
<custom-component>这段文本是黄色的</custom-component>
```

## 组件样式隔离

默认情况下，自定义组件的样式只受到自定义组件 wxss 的影响。除非以下两种情况：

- 指定特殊的样式隔离选项 `styleIsolation` 。
- webview 渲染下，在 `app.wxss` 或页面的 `wxss` 中使用标签名选择器（或一些其他特殊选择器）来直接指定样式会影响到页面和全部组件。通常情况下这是不推荐的做法。

```json
{
  "styleIsolation": "isolated"
}
```

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/xPQhJcm37e7h)

自定义组件 JSON 中的 `styleIsolation` 选项从基础库版本 [2.10.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 开始支持。它支持以下取值：

- `isolated` 表示启用样式隔离，在自定义组件内外，使用 class 指定的样式将不会相互影响（一般情况下的默认值）；
- `apply-shared` 表示页面 wxss 样式将影响到自定义组件，但自定义组件 wxss 中指定的样式不会影响页面；
- `shared` 表示页面 wxss 样式将影响到自定义组件，自定义组件 wxss 中指定的样式也会影响页面和其他设置了 `apply-shared` 或 `shared` 的自定义组件。（这个选项在插件中不可用。）

**使用后两者时，请务必注意组件间样式的相互影响。**

如果这个 [Component 构造器用于构造页面](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/component.html) ，则默认值为 `shared` ，且还有以下几个额外的样式隔离选项可用：

- `page-isolated` 表示在这个页面禁用 app.wxss ，同时，页面的 wxss 不会影响到其他自定义组件；
- `page-apply-shared` 表示在这个页面禁用 app.wxss ，同时，页面 wxss 样式不会影响到其他自定义组件，但设为 `shared` 的自定义组件会影响到页面；
- `page-shared` 表示在这个页面禁用 app.wxss ，同时，页面 wxss 样式会影响到其他设为 `apply-shared` 或 `shared` 的自定义组件，也会受到设为 `shared` 的自定义组件的影响。

<details style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34); font-family: -apple-system, BlinkMacSystemFont, &quot;SF UI Text&quot;, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><summary style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent;">其他不再推荐的配置方式</summary><p style="margin: 0px 0px 0.5em; padding: 0px; -webkit-tap-highlight-color: transparent;">从小程序基础库版本<span>&nbsp;</span><a href="https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; cursor: pointer; color: rgb(87, 107, 149); text-decoration: none;">2.6.5</a><span>&nbsp;</span>开始，<code style="margin: 0px; padding: 2px 0.4em; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 0.85em; border-radius: 2px; display: inline-block;">styleIsolation</code><span>&nbsp;</span>可以在 JS 文件的<span>&nbsp;</span><code style="margin: 0px; padding: 2px 0.4em; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 0.85em; border-radius: 2px; display: inline-block;">options</code><span>&nbsp;</span>中配置。例如：</p><div class="language-js extra-class" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; border-radius: 4px; background-color: rgb(249, 249, 250);"><pre class="language-js" style="margin: 1em 0px; padding: 30px; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; overflow: auto; background-color: rgb(249, 249, 250); border-radius: 4px;"><code style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 14px; border-radius: 0px; display: inline;"><span class="token function" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(35, 160, 255);">Component</span><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">(</span><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">{</span>
  <span class="token literal-property property" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(255, 77, 0);">options</span><span class="token operator" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(255, 77, 0);">:</span> <span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">{</span>
    <span class="token literal-property property" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(255, 77, 0);">styleIsolation</span><span class="token operator" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(255, 77, 0);">:</span> <span class="token string" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(7, 193, 96);">'isolated'</span>
  <span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">}</span>
<span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">}</span><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">)</span>
</code></pre></div><p style="margin: 0px 0px 0.5em; padding: 0px; -webkit-tap-highlight-color: transparent;">此外，小程序基础库版本<span>&nbsp;</span><a href="https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; cursor: pointer; color: rgb(87, 107, 149); text-decoration: none;">2.2.3</a><span>&nbsp;</span>以上支持<span>&nbsp;</span><code style="margin: 0px; padding: 2px 0.4em; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 0.85em; border-radius: 2px; display: inline-block;">addGlobalClass</code><span>&nbsp;</span>选项，即在<span>&nbsp;</span><code style="margin: 0px; padding: 2px 0.4em; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 0.85em; border-radius: 2px; display: inline-block;">Component</code><span>&nbsp;</span>的<span>&nbsp;</span><code style="margin: 0px; padding: 2px 0.4em; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 0.85em; border-radius: 2px; display: inline-block;">options</code><span>&nbsp;</span>中设置<span>&nbsp;</span><code style="margin: 0px; padding: 2px 0.4em; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 0.85em; border-radius: 2px; display: inline-block;">addGlobalClass: true</code><span>&nbsp;</span>。 这个选项等价于设置<span>&nbsp;</span><code style="margin: 0px; padding: 2px 0.4em; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 0.85em; border-radius: 2px; display: inline-block;">styleIsolation: apply-shared</code><span>&nbsp;</span>，但设置了<span>&nbsp;</span><code style="margin: 0px; padding: 2px 0.4em; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 0.85em; border-radius: 2px; display: inline-block;">styleIsolation</code><span>&nbsp;</span>选项后这个选项会失效。</p><p style="margin: 0px 0px 0.5em; padding: 0px; -webkit-tap-highlight-color: transparent;"><strong style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent;">代码示例：</strong></p><p style="margin: 0px 0px 0.5em; padding: 0px; -webkit-tap-highlight-color: transparent;"><a href="https://developers.weixin.qq.com/s/VkTd7Fm37ggl" title="在开发者工具中预览效果" target="_blank" rel="noopener noreferrer" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; cursor: pointer; color: rgb(87, 107, 149); text-decoration: none;">在开发者工具中预览效果<span style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent;"></span></a></p><div class="language-js extra-class" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; border-radius: 4px; background-color: rgb(249, 249, 250);"><pre class="language-js" style="margin: 1em 0px; padding: 30px; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; overflow: auto; background-color: rgb(249, 249, 250); border-radius: 4px;"><code style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 14px; border-radius: 0px; display: inline;"><span class="token comment" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.3);">/* 组件 custom-component.js */</span>
<span class="token function" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(35, 160, 255);">Component</span><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">(</span><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">{</span>
  <span class="token literal-property property" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(255, 77, 0);">options</span><span class="token operator" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(255, 77, 0);">:</span> <span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">{</span>
    <span class="token literal-property property" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(255, 77, 0);">addGlobalClass</span><span class="token operator" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(255, 77, 0);">:</span> <span class="token boolean" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(255, 77, 0);">true</span><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">,</span>
  <span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">}</span>
<span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">}</span><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">)</span>
</code></pre></div><div class="language-html extra-class" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; border-radius: 4px; background-color: rgb(249, 249, 250);"><pre class="language-html" style="margin: 1em 0px; padding: 30px; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; overflow: auto; background-color: rgb(249, 249, 250); border-radius: 4px;"><code style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 14px; border-radius: 0px; display: inline;"><span class="token comment" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.3);">&lt;!-- 组件 custom-component.wxml --&gt;</span>
<span class="token tag" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(180, 87, 255);"><span class="token tag" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(180, 87, 255);"><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">&lt;</span>text</span> <span class="token attr-name" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(255, 77, 0);">class</span><span class="token attr-value" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);"><span class="token punctuation attr-equals" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">=</span><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">"</span>red-text<span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">"</span></span><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">&gt;</span></span>这段文本的颜色由 `app.wxss` 和页面 `wxss` 中的样式定义来决定<span class="token tag" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(180, 87, 255);"><span class="token tag" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(180, 87, 255);"><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">&lt;/</span>text</span><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">&gt;</span></span>
</code></pre></div><div class="language-css extra-class" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; border-radius: 4px; background-color: rgb(249, 249, 250);"><pre class="language-css" style="margin: 1em 0px; padding: 30px; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; overflow: auto; background-color: rgb(249, 249, 250); border-radius: 4px;"><code style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; font-family: Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; direction: ltr; background-color: rgb(249, 249, 250); font-size: 14px; border-radius: 0px; display: inline;"><span class="token comment" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgba(0, 0, 0, 0.3);">/* app.wxss */</span>
<span class="token selector" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(180, 87, 255);">.red-text</span> <span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">{</span>
  <span class="token property" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(255, 77, 0);">color</span><span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">:</span> red<span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">;</span>
<span class="token punctuation" style="margin: 0px; padding: 0px; -webkit-tap-highlight-color: transparent; color: rgb(34, 34, 34);">}</span>
</code></pre></div></details>

## 外部样式类

> 基础库 1.9.90 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

有时，组件希望接受外部传入的样式类。此时可以在 `Component` 中用 `externalClasses` 定义段定义若干个外部样式类。

这个特性可以用于实现类似于 `view` 组件的 `hover-class` 属性：页面可以提供一个样式类，赋予 `view` 的 `hover-class` ，这个样式类本身写在页面中而非 `view` 组件的实现中。

**注意：在同一个节点上使用普通样式类和外部样式类时，两个类的优先级是未定义的，因此最好避免这种情况。**

**代码示例：**

```js
/* 组件 custom-component.js */
Component({
  externalClasses: ['my-class']
})
<!-- 组件 custom-component.wxml -->
<custom-component class="my-class">这段文本的颜色由组件外的 class 决定</custom-component>
```

这样，组件的使用者可以指定这个样式类对应的 class ，就像使用普通属性一样。在 [2.7.1](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 之后，可以指定多个对应的 class 。

**代码示例：**

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/rbgNNKmE6bZK)

```html
<!-- 页面的 WXML -->
<custom-component my-class="red-text" />
<custom-component my-class="large-text" />
<!-- 以下写法需要基础库版本 2.7.1 以上 -->
<custom-component my-class="red-text large-text" />
.red-text {
  color: red;
}
.large-text {
  font-size: 1.5em;
}
```

## 引用页面或父组件的样式

> 基础库 2.9.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

即使启用了样式隔离 `isolated` ，组件仍然可以在局部引用组件所在页面的样式或父组件的样式。

例如，如果在页面 wxss 中定义了：

```css
.blue-text {
  color: blue;
}
```

在这个组件中可以使用 `~` 来引用这个类的样式：

```html
<view class="~blue-text"> 这段文本是蓝色的 </view>
```

如果在一个组件的父组件 wxss 中定义了：

```css
.red-text {
  color: red;
}
```

在这个组件中可以使用 `^` 来引用这个类的样式：

```html
<view class="^red-text"> 这段文本是红色的 </view>
```

也可以连续使用多个 `^` 来引用祖先组件中的样式。

**注意：如果组件是比较独立、通用的组件，请优先使用外部样式类的方式，而非直接引用父组件或页面的样式。**

## 虚拟化组件节点

> 基础库 2.11.2 开始支持，低版本需做[兼容处理](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)。

默认情况下，自定义组件本身的那个节点是一个“普通”的节点，使用时可以在这个节点上设置 `class` `style` 、动画、 flex 布局等，就如同普通的 view 组件节点一样。

```html
<!-- 页面的 WXML -->
<view style="display: flex">
  <!-- 默认情况下，这是一个普通的节点 -->
  <custom-component style="color: blue; flex: 1">蓝色、满宽的</custom-component>
</view>
```

但有些时候，自定义组件并不希望这个节点本身可以设置样式、响应 flex 布局等，而是希望自定义组件内部的第一层节点能够响应 flex 布局或者样式由自定义组件本身完全决定。

这种情况下，可以将这个自定义组件设置为“虚拟的”：

```js
Component({
  options: {
    virtualHost: true
  },
  properties: {
    style: { // 定义 style 属性可以拿到 style 属性上设置的值
      type: String,
    }
  },
  externalClasses: ['class'], // 可以将 class 设为 externalClasses
})
```

这样，可以将 flex 放入自定义组件内：

```html
<!-- 页面的 WXML -->
<view style="display: flex">
  <!-- 如果设置了 virtualHost ，节点上的样式将失效 -->
  <custom-component style="color: blue">不是蓝色的</custom-component>
</view>
<!-- custom-component.wxml -->
<view style="flex: 1">
  满宽的
  <slot></slot>
</view>
```

需要注意的是，自定义组件节点上的 `class` `style` 和动画将不再生效，但仍可以：

- 将 style 定义成 `properties` 属性来获取 style 上设置的值；
- 将 class 定义成 `externalClasses` 外部样式类使得自定义组件 wxml 可以使用 class 值。

**代码示例：**

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/AlV9fEmF7Dh8)