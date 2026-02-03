# glass-easel ：新版微信小程序组件框架

glass-easel 是小程序组件框架的核心实现。它实质上是一个 JavaScript 的组件化界面框架，用来进行组件化、定义式的界面开发。

glass-easel 是对旧版小程序组件框架的重写，保持对旧版小程序组件框架特性的兼容，并添加了一些新特性。它运行时并不依赖于小程序环境，可以独立运行在 web 或其他 JavaScript 环境下。

## 主要特点

glass-easel 可以让同样的组件代码运行在 web 、小程序等不同环境下。

**后端** 是 glass-easel 的一个重要概念，表示组件系统的运行环境。在 web 环境下运行时，后端是浏览器的 DOM 接口；在小程序环境下运行时，后端则是小程序环境接口。这使得（后端无关的）组件代码可以运行在不同环境下。

glass-easel 完整具备小程序自定义组件相关特性，如组件模板、通信与事件、生命周期等等。此外， glass-easel 还实现了一些实用的新特性，也具有更好的 TypeScript 支持。

glass-easel 采用单组件节点树更新算法（大体上沿用了旧版小程序组件框架的更新算法），具有均衡的性能表现，适合高度组件化开发。





glass-easel 组件框架在 [GitHub](https://github.com/wechat-miniprogram/glass-easel) 上开源，代码和更详细的文档、示例等可以在 GitHub 上找到。

## 适配指引

[glass-easel 适配指引](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/migration) 中列举了一些相较于现有组件框架 *exparser* 需要变更的逻辑，可以用于将现有的小程序迁移到新的框架，也可以用于快速了解新旧框架之间的差异。

# glass-easel 适配指引

[*glass-easel*](https://github.com/wechat-miniprogram/glass-easel) 是一个新的组件框架，是对旧版组件框架 *exparser* 的一个重写，拥有 **比旧版组件框架更好的性能和更多的特性**。

将现有的运行在 *exparser* 上的小程序迁移到 *glass-easel* 需要一些适配，下面的文档会为适配提供一些指引。

## 运行环境

对于 **[\*Skyline\* 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)**，版本 [3.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 起的基础库将全量运行在 *glass-easel* 上，因此页面 **必须** 适配 *glass-easel* 才能正常运行（在上传时会有相应的检查）；在 [3.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 以下版本基础库或不支持 *Skyline* 的运行环境中，页面将在 *exparser* 上以兼容模式运行。

*WebView* 后端暂不支持 *glass-easel*（进行中），但页面可以在 *exparser* 上以兼容模式运行。

使用微信开发者工具进行调试时，*glass-easel* 需要 1.06.2308142 或更高版本的工具；当工具版本不支持使用 *glass-easel* 时，基础库将中断渲染并提示升级。



在运行过程中，*vConsole* 内的路由日志可以协助确认当前正在使用的组件框架：

![AppRouteLog](https://res.wx.qq.com/wxdoc/dist/assets/img/app-route-log.c5fdb5c4.png)

## JSON 配置

通过在页面或自定义组件的 JSON 配置中添加以下配置开始适配：

```json
{ "componentFramework": "glass-easel" }
```

添加后，WXML 模板将被编译为适配 *glass-easel* 的新格式 *ProcGen*，并同时保持对旧版组件框架 *exparser* 兼容。

为一个页面或自定义组件添加这个配置后，所有它依赖的组件也将自动被标记为 *glass-easel* 适配（包括 `usingComponents` 依赖和 `componentGenerics#default` 依赖）

在 `app.json` 中添加这个配置可以全局开启 *glass-easel* 支持。但需要注意的是，配置后编译生成的模板虽然也能在 *exparser* 上运行，但兼容版本在 *exparser* 上有可能遇到边界情况下的兼容性问题，因此除非不需要兼容旧版本基础库或者小程序整体都以 *Skyline* 运行，否则应该更谨慎地使用全局配置。

插件暂未支持页面或自定义组件级别的 `componentFramework` 配置项，可以在 `plugin.json` 中添加这个配置项来开始适配。

## 变更点适配

*glass-easel* 在设计上兼容绝大多数的旧版组件框架 *exparser* 的接口，仅有少数地方需要变更：

1. [必须]

    

   模板中数据绑定外的转义改为标准 XML 转义，数据绑定内的转义现在无需转义

   - 兼容性：[需要手动兼容] *exparser* 上不能使用新的转义写法

   - 旧例：

     ```html
     <view prop-a="\"test\"" prop-b="{{ test === \"test\" }}" />
     ```

   - 新例：

     ```html
     <view prop-a="&quot;test&quot;" prop-b="{{ test === "test" }}" />
     ```

2. [必须]

    

   模板中不再支持

    

   ```
   wx-if
   ```

   ,

    

   ```
   wx-for
   ```

    

   两种写法，仅支持

    

   ```
   wx:if
   ```

   ,

    

   ```
   wx:for
   ```

   - 兼容性：[推荐直接变更] *exparser* 同样可以使用 `wx:if`, `wx:for`

   - 旧例：

     ```html
     <view wx-if="{{ arr }}" />
     ```

   - 新例：

     ```html
     <view wx:if="{{ arr }}" />
     ```

3. [必须]

    

   运行在

    

   exparser

    

   兼容模式上时，不支持 WXSS

    

   ```
   input
   ```

    

   标签选择器

   - 兼容性：[推荐直接变更]

   - 旧例：

     ```css
     input {
        height: 30px;
     }
     ```

   - 新例：

     ```css
     .my-input {
        height: 30px;
     }
     ```

4. [可选]

    

   由于兼容需要，

   ```
   wx.createSelectorQuery
   ```

    

   性能不如

    

   ```
   this.createSelectorQuery
   ```

   ，应尽量使用后者

   - 兼容性：[推荐直接变更] *exparser* 同样支持 `this.createSelectorQuery`

   - 旧例：

     ```typescript
     wx.createSelectorQuery()
       .in(this)
       .select('#webgl')
       .exec(res => { })
     ```

   - 新例：

     ```typescript
     this.createSelectorQuery()
       .select('#webgl')
       .exec(res => { })
     ```

5. [必须]

    

   ```
   SelectorQuery
   ```

    

   等接口中的选择器现在和 CSS 选择器一样，不再支持以数字开头

   - 兼容性：[推荐直接变更]

   - 旧例：

     ```typescript
     this.createSelectorQuery()
       .select('#1')
       .exec(res => { })
     ```

   - 新例：

     ```typescript
     this.createSelectorQuery()
       .select('#element-1')
       .exec(res => { })
     ```

6. [必须]

    

   Skyline 渲染后端上的 Worklet 回调函数名称变更

   - 兼容性：[推荐直接变更] 旧版本基础库同样支持这些事件名称

   - 变更对应：

     | 组件名                                                       | 原 Worklet 事件名                        | 新 Worklet 事件名                                            |
     | :----------------------------------------------------------- | :--------------------------------------- | :----------------------------------------------------------- |
     | [pan-gesture-handler](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/gesture.html#通用属性) | `on-gesture-event`                       | `worklet:ongesture`                                          |
     | [pan-gesture-handler](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/gesture.html#通用属性) | `should-response-on-move`                | `worklet:should-response-on-move`                            |
     | [pan-gesture-handler](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/gesture.html#通用属性) | `should-accept-gesture`                  | `worklet:should-accept-gesture`                              |
     | [scroll-view](https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view.html) | `bind:scroll-start`                      | `worklet:onscrollstart`                                      |
     | [scroll-view](https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view.html) | `bind:scroll`                            | `worklet:onscrollupdate`                                     |
     | [scroll-view](https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view.html) | `bind:scroll-end`                        | `worklet:onscrollend`                                        |
     | [scroll-view](https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view.html) | `adjust-deceleration-velocity`           | `worklet:adjust-deceleration-velocity`                       |
     | [swiper](https://developers.weixin.qq.com/miniprogram/dev/component/swiper.html) | `bind:transition` `bind:animationfinish` | `worklet:onscrollstart` `worklet:onscrollupdate` `worklet:onscrollend` |
     | [share-element](https://developers.weixin.qq.com/miniprogram/dev/component/share-element.html) | `on-frame`                               | `worklet:onframe`                                            |

   - 旧例：

     ```html
     <scroll-view bindscroll="onScrollWorklet" />
     <swiper bind:transition="onTransitionWorklet" />
     ```

   - 新例：

     ```html
     <scroll-view worklet:onscrollupdate="onScrollWorklet" />
     <swiper
        worklet:onscrollstart="onTransitionWorklet"
        worklet:onscrollupdate="onTransitionWorklet"
        worklet:onscrollend="onTransitionWorklet"
     />
     ```

7. [正在支持] Skyline 渲染后端上，IntersectionObserver 暂不支持 `relativeTo`, 仅支持 `relativeToViewport`

8. [正在支持]

    

   暂不支持以下组件实例方法：

   - `animate`
   - `applyAnimation`
   - `clearAnimation`
   - `setInitialRenderingCache`

## 已知问题

1. 运行在 `exparser` 兼容模式上时，`text` 组件无法换行

## 更新记录

1. ```
   2023-06-01
   ```

    

   支持 WXS

   - 重新预览或上传即可，无版本依赖

2. ```
   2023-06-02
   ```

    

   修复 嵌套的

    

   ```
   wx:for
   ```

    

   可能导致异常

    

   [wechat-miniprogram/glass-easel#45]

   - 重新预览或上传即可，无版本依赖

3. ```
   2023-06-02
   ```

    

   修复

    

   ```
   <template name>
   ```

    

   中使用的 WXS 在引用到其他文件中时可能失效

    

   [wechat-miniprogram/glass-easel#47]

   - 重新预览或上传即可，无版本依赖

4. ```
   2023-06-12
   ```

    

   修复

    

   ```
   <template>
   ```

   ,

    

   ```
   <include>
   ```

   ,

    

   ```
   <slot>
   ```

    

   节点上不支持

    

   ```
   wx:
   ```

    

   指令

    

   [wechat-miniprogram/glass-easel#30]

   - 重新预览或上传即可，无版本依赖

5. ```
   2023-07-28
   ```

    

   支持兼容模式下 WXS 事件响应中

    

   ```
   ComponentDescriptor
   ```

    

   的

    

   ```
   getState
   ```

    

   方法

   - 需要基础库版本 [3.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 或以上，正在逐步支持到版本 [2.19.2](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

6. ```
   2024-05-20
   ```

    

   支持全空的数据绑定

   - 重新预览或上传即可，无版本依赖

7. ```
   2024-10-18
   ```

    

   支持在组件 JS 的 options 中定义

    

   ```
   styleIsolation
   ```

    

   和

    

   ```
   addGlobalClass
   ```

   - 需要基础库版本 [3.6.3](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 或以上，后续争取兼容到版本 [3.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

8. ```
   2024-10-28
   ```

    

   支持 WXS 事件响应函数

   - 需要基础库版本 [3.6.4](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html) 或以上，后续争取兼容到版本 [3.0.0](https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html)

   # 适用于 glass-easel 组件框架的特性

   部分自定义组件特性仅适用于 [glass-easel 组件框架](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/introduction.html) 。

   由于目前 glass-easel 组件框架仅可用于 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)，因此这些特性也同样受此限制。

   # 在模板中调用 data 里的函数

   > 由于目前 glass-easel 组件框架仅可用于 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)，因此这些特性也同样受此限制。

   如果 data 中的某个字段是函数，在模板里可以直接调用它：

   ```js
   Component({
     data: {
       getDataField() {
         return 'someValue'
       },
     },
   })
   <view>{{ getDataField() }}</view>
   ```

   尽管这样做有时会很方便，在实践中依然不建议滥用。

   从代码可维护性的角度看， `data` 中的内容应当与数据内容强相关。如果函数的主要目的是对数据展示方面的预处理，推荐用 [WXS](https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxs/) 的方式，将函数实现内联在模版中。

   # Chaining API

   > 由于目前 glass-easel 组件框架仅可用于 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)，因此这些特性也同样受此限制。

   ## Chaining API 接口形式

   Chaining API 是一种新的页面和自定义组件定义形式。

   对于一个传统的自定义组件定义：

   ```js
   Component({
     properties: {
       myProperty: String,
       myAnotherProperty: String,
     },
     data: {
       myDataField: 'someValue',
     },
   })
   ```

   它可以被等价地写成以下 Chaining API 形式：

   ```js
   Component()
     .property('myProperty', String)
     .property('myAnotherProperty', String)
     .data(() => ({
       myDataField: 'someValue',
     }))
     .register()
   ```

   使用 Chaining API 的主要好处是它具有更好的 TypeScript 支持，且对于复杂组件更加友好，还可以配合 [init 函数](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/chaining-api-init.html) 来使用。但它也使得对简单组件的定义看起来稍显繁琐。

   因而，每个组件都可以分别选用传统的定义方式或者 Chaining API 来进行定义，可以对于每个组件都选用更合适它的定义方式。

   ## 常用的链式调用项

   以下是一些常用链式调用项。

   `.property` 用来定义单个属性，等价于传统形式的 `properties` 定义段中的单个项目。例如：

   ```js
   Component()
     .property('myProperty', {
       type: String
     })
     .register()
   ```

   `.data` 用来定义数据字段表，作用上相当于传统形式的 `data` 定义段，但它接受一个函数。这个函数在每次组件创建时执行一次，它的返回值被用作数据字段。例如：

   ```js
   Component()
     .data(() => ({
       myDataField: 'someValue',
     }))
     .register()
   ```

   `.externalClasses` 用来定义外部样式类，等价于传统形式的 `externalClasses` 定义段。例如：

   ```js
   Component()
     .externalClasses(['my-class'])
     .register()
   ```

   `.options` 用来指定组件选项，等价于传统形式的 `options` 定义段。（注意，如果多次调用，仅有最后一次调用有效。）例如：

   ```js
   Component()
     .options({
       multipleSlots: true,
     })
     .register()
   ```

   `.options` 用来指定组件选项，等价于传统形式的 `options` 定义段。（注意，如果多次调用，仅有最后一次调用有效。）例如：

   ```js
   Component()
     .options({
       multipleSlots: true,
     })
     .register()
   ```

   以下链式调用项也是可用的，但通过 [init 函数](https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/chaining-api-init.html) 来调用通常更加友好。

   `.methods` 用来定义一组方法，等价于传统形式的 `methods` 定义段。例如：

   ```js
   Component()
     .methods({
       myMethod() { /* ... */ }
     })
     .register()
   ```

   `.lifetime` 和 `.pageLifetime` 分别用来定义单个生命周期方法和组件所在页面的生命周期方法，等价于传统形式的 `lifetime` 和 `pageLifetime` 定义段中的单个项目。例如：

   ```js
   Component()
     .lifetime('attached', function () { /* ... */ })
     .pageLifetime('show', function () { /* ... */ })
     .register()
   ```

   `.observer` 用来定义单个数据监听器，类似于传统形式的 `observers` 定义段中的单个项目，但在同时监听多个数据字段时，应写成数组形式。例如：

   ```js
   Component()
     .data(() => ({
       a: 1,
       b: 2,
     }))
     .observer(['a', 'b'], function () { /* ... */ })
     .register()
   ```

   `.relation` 用来定义单个组件间关系项，等价于传统形式的 `relations` 定义段中的单个项目。例如：

   ```js
   Component()
     .relation('another-component', {
       type: 'parent',
     })
     .register()
   ```

   ## 在链式调用项中使用 behavior

   类似地， `Behavior` 也支持 Chaining API 。例如：

   ```js
   const beh = Behavior()
     .property('myProperty', String)
     .register()
   ```

   这样，在组件中，可以使用 `.behavior` 将其引入：

   ```js
   Component()
     .behavior(beh)
     .register()
   ```

   需要注意的是，引入 behavior 导致出现了重复的同名属性或同名数据字段时， TypeScript 将会报出类型错误。

   ## 重复使用链式调用项

   除了 `options` 和 `export` ，其他链式调用项都可以重复调用多次，调用结果会组合起来。

   这样可以把复杂的组件拆解成好几个部分来定义，对于很复杂的组件定义会有帮助。

   ```js
   Component()
     // 定义 myDataField 字段和相关的处理逻辑
     .data(() => ({
       myDataField: 'someValue',
     }))
     .lifetime('attached', function () {
       this.setData({ myDataField: updatedValue })
     })
     // 定义 anotherField 字段和相关的处理逻辑
     .data(() => ({
       anotherField: 1,
     }))
     .lifetime('attached', function () {
       this.setData({ anotherField: updatedValue })
     })
     .register()
   ```

   ## 非连续链式调用

   链式调用项也可以分开写。例如：

   ```js
   const componentDefinition = Component()
   componentDefinition.property('myProperty', String)
   componentDefinition.data(() => ({
     myDataField: 'someValue',
   }))
   componentDefinition.register()
   ```

   但这样写会丢失部分 TypeScript 类型信息。这种做法比较适合制作中间件、将 `Component()` 封装成别的形式的调用时。手工编写代码时并不建议这么做。

   # Chaining API 的 init 函数

   > 由于目前 glass-easel 组件框架仅可用于 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)，因此这些特性也同样受此限制。

   ## init 链式调用项

   在 Chaining API 中支持 `.init(...)` 链式调用项，可以以另一种方式进行组件创建：

   ```js
   Component()
     .data(() => ({
       myDataField: 'someValue',
     }))
     .init(function ({ lifetime }) {
       // 这里可以用 JavaScript 局部量
       const getUpdatedValue = () => {
         return 'updated'
       }
   
       // 定义一个生命周期方法
       lifetime('attached', () => {
         this.setData({ myDataField: getUpdatedValue() })
       })
     })
     .register()
   ```

   init 中定义的函数会在每次组件创建时被调用一次。

   这种方式的主要好处是在其内部可以自由使用 JavaScript 局部变量，减少对组件 `this` 的使用，有时会很方便。

   ## init 函数中的辅助方法

   init 的第一个参数包含多个辅助方法，可以用于组件定义。

   `method` 用来定义单个方法，等价于传统形式的 `methods` 定义段中的单个项目。不过，它通常只用来定义事件响应函数，而且在末尾需要返回出来。例如：

   ```js
   Component()
     .init(function ({ method }) {
       const tapHandler = method(() => {
         /* ... */
       })
       return { tapHandler }
     })
     .register()
   ```

   `lifetime` 和 `pageLifetime` 分别用来定义单个生命周期方法和组件所在页面的生命周期方法，等价于传统形式的 `lifetime` 和 `pageLifetime` 定义段中的单个项目。例如：

   ```js
   Component()
     .init(function ({ lifetime, pageLifetime }) {
       lifetime('attached', () => { /* ... */ })
       pageLifetime('show', () => { /* ... */ })
     })
     .register()
   ```

   `observer` 用来定义单个数据监听器，类似于传统形式的 `observers` 定义段中的单个项目，但在同时监听多个数据字段时，应写成数组形式。例如：

   ```js
   Component()
     .data(() => ({
       a: 1,
       b: 2,
     }))
     .init(function ({ observer }) {
       observer(['a', 'b'], () => { /* ... */ })
     })
     .register()
   ```

   `relation` 用来定义单个组件间关系项，等价于传统形式的 `relations` 定义段中的单个项目。例如：

   ```js
   Component()
     .init(function ({ relation }) {
       relation('another-component', {
         type: 'parent',
       })
     })
     .register()
   ```

   需要注意的是，上面这些方法都不能异步或延迟执行，否则会报错：

   ```js
   Component()
     .init(function ({ lifetime }) {
       setTimeout(() => {
         // 不能这么做！
         lifetime('attached', () => { /* ... */ })
       }, 0)
     })
     .register()
   ```

   此外，第一个参数中还包含有 `data` 和 `setData` ，可以用来快速访问和设置数据。例如：

   ```js
   Component()
     .data(() => ({
       myDataField: 'someValue',
     }))
     .init(function ({ lifetime, data, setData }) {
       lifetime('attached', () => {
         setData({
           myDataField: data.myDataField + ' updated',
         })
       })
     })
     .register()
   ```

   但要注意 data 和 setData 只应在各个回调函数中使用，下面这样做会报错：

   ```js
   Component()
     .init(function ({ setData }) {
       setData({ /* ... */ })
     })
     .register()
   ```

# 动态 slot

> 由于目前 glass-easel 组件框架仅可用于 [Skyline 渲染引擎](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)，因此这些特性也同样受此限制。

## 静态 slot 与动态 slot

简单的自定义组件 slot 类型有两种：单一 slot 和多 slot ，取决于自定义组件的 `multipleSlots` 选项。它们都属于静态 slot 。

它们都要求（相同 name 的） slot 节点只有一个，重复的 `<slot />` 中只有第一个会生效。

之所以称其为“静态”，是因为无论组件的实现如何， slot 的内容（由组件使用者提供）只会出现一次，不会因 `<slot />` 的重复而重复。这样组件的使用者更容易控制它自身的节点。

从性能上看，单一 slot 也具有相对最优的性能表现。

但有时需要在列表中使用 slot 使得 slot 的内容被重复多次。此时可以使用动态 slot 。

```js
Component({
  options: {
    dynamicSlots: true, // 启用动态 slot
  },
  data: {
    list: ['A', 'B', 'C'],
  },
})
```

然后，在模板中可以使 `<slot />` 重复多次：

```xml
<block wx:for="{{ list }}">
  <slot />
</block>
```

## 通过动态 slot 传递数据

在动态 slot 中，被重复的 `<slot />` 可以分别携带不同的数据。例如：

```xml
<block wx:for="{{ list }}">
  <slot list-index="{{ index }}" item="{{ item }}" />
</block>
```

上述的 slot 中携带有 `list-index` 和 `item` 两个数据项。

组件的使用者可以通过 `slot:` 来接收 slot 传递的任何数据项。例如：

```xml
<view>
  <child>
    <view slot:item>{{ item }}</view>
    <view slot:listIndex>{{ listIndex }}</view>
  </child>
</view>
```

组件的使用者在接收 slot 传递的数据项时，可以更改数据项的字段名。例如：

```xml
<view>
  <child>
    <view slot:listIndex="index">{{ index }}</view>
  </child>
</view>
```