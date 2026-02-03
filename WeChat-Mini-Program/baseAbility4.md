# Canvas 画布

[canvas 组件](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) 提供了绘制界面，可以在之上进行任意绘制

## 基础使用

### 第一步：在 WXML 中添加 canvas 组件

```html
<!-- 2d 类型的 canvas -->
<canvas id="myCanvas" type="2d" style="border: 1px solid; width: 300px; height: 150px;" />
```

首先需要在 WXML 中添加 [canvas 组件](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html)。

指定 `id="myCanvas"` 唯一标识一个 canvas，用于后续获取 [Canvas 对象](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.html)。

指定 `type` 用于定义画布类型，本例子使用 `type="2d"` 示例。

### 第二步：获取 Canvas 对象和渲染上下文

```js
this.createSelectorQuery()
    .select('#myCanvas') // 在 WXML 中填入的 id
    .fields({ node: true, size: true })
    .exec((res) => {
        // Canvas 对象
        const canvas = res[0].node
        // 渲染上下文
        const ctx = canvas.getContext('2d')
    })
```

通过 [SelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.html) 选择上一步的 canvas，可以获取到 [Canvas 对象](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.html)。

再通过 [Canvas.getContext](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.getContext.html)，我们可以获取到 [渲染上下文 RenderingContext](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/RenderingContext.html)。

后续的画布操作与渲染操作，都需要通过这两个对象来实现。

### 第三步：初始化 Canvas

```js
this.createSelectorQuery()
    .select('#myCanvas') // 在 WXML 中填入的 id
    .fields({ node: true, size: true })
    .exec((res) => {
        // Canvas 对象
        const canvas = res[0].node
        // 渲染上下文
        const ctx = canvas.getContext('2d')

        // Canvas 画布的实际绘制宽高
        const width = res[0].width
        const height = res[0].height

        // 初始化画布大小
        const dpr = wx.getWindowInfo().pixelRatio
        canvas.width = width * dpr
        canvas.height = height * dpr
        ctx.scale(dpr, dpr)
    })
```

canvas 的宽高分为渲染宽高和逻辑宽高：

- 渲染宽高为 canvas 画布在页面中所实际占用的宽高大小，即通过对节点进行 [boundingClientRect](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/NodesRef.boundingClientRect.html) 请求获取到的大小。
- 逻辑宽高为 canvas 在渲染过程中的逻辑宽高大小，如绘制一个长方形与逻辑宽高相同，最终长方形会占满整个画布。逻辑宽高默认为 `300 * 150`。

不同的设备上，存在物理像素和逻辑像素不相等的情况，所以一般我们需要用 [wx.getWindowInfo](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getWindowInfo.html) 获取设备的像素比，乘上 canvas 的渲染大小，作为画布的逻辑大小。

### 第四步：进行绘制

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/smH8LGmn7Lz5)

```js
// 省略上面初始化步骤，已经获取到 canvas 对象和 ctx 渲染上下文

// 清空画布
ctx.clearRect(0, 0, width, height)

// 绘制红色正方形
ctx.fillStyle = 'rgb(200, 0, 0)';
ctx.fillRect(10, 10, 50, 50);

// 绘制蓝色半透明正方形
ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
ctx.fillRect(30, 30, 50, 50);
```

通过 [渲染上下文](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/RenderingContext.html) 上的绘图 api，我们可以在画布上进行任意的绘制。

## 进阶使用

### 绘制图片

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/2FHoZGmA7XzI)

```js
// 省略上面初始化步骤，已经获取到 canvas 对象和 ctx 渲染上下文

// 图片对象
const image = canvas.createImage()
// 图片加载完成回调
image.onload = () => {
    // 将图片绘制到 canvas 上
    ctx.drawImage(image, 0, 0)
}
// 设置图片src
image.src = 'https://open.weixin.qq.com/zh_CN/htmledition/res/assets/res-design-download/icon64_wx_logo.png'
```

通过 [Canvas.createImage](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.createImage.html) 我们可以创建图片对象并加载图片。当图片加载完成触发 `onload` 回调之后，使用 `ctx.drawImage` 即可将图片绘制到 canvas 上。

### 生成图片

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/FPIGmGmT7fzB)

```js
// 省略上面初始化步骤，已经获取到 canvas 对象和 ctx 渲染上下文

// 绘制红色正方形
ctx.fillStyle = 'rgb(200, 0, 0)';
ctx.fillRect(10, 10, 50, 50);

// 绘制蓝色半透明正方形
ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
ctx.fillRect(30, 30, 50, 50);

// 生成图片
wx.canvasToTempFilePath({
    canvas,
    success: res => {
        // 生成的图片临时文件路径
        const tempFilePath = res.tempFilePath
    },
})
```

通过 [wx.canvasToTempFilePath](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasToTempFilePath.html) 接口，可以将 canvas 上的内容生成图片临时文件。

### 帧动画

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/fmIKNGmF7tzV)

```js
// 省略上面初始化步骤，已经获取到 canvas 对象和 ctx 渲染上下文

const startTime = Date.now()

// 帧渲染回调
const draw = () => {
  const time = Date.now()
  // 计算经过的时间
  const elapsed = time - startTime

  // 计算动画位置
  const n = Math.floor(elapsed / 3000)
  const m = elapsed % 3000
  const dx = (n % 2 ? 0 : 1) + (n % 2 ? 1 : -1) * (m < 2500 ? easeOutBounce(m / 2500) : 1)
  const x = (width - 50) * dx

  // 渲染
  ctx.clearRect(0, 0, width, height)
  ctx.fillStyle = 'rgb(200, 0, 0)';
  ctx.fillRect(x, height / 2 - 25, 50, 50);

  // 注册下一帧渲染
  canvas.requestAnimationFrame(draw)
}

draw()
```

通过 [Canvas.requestAnimationFrame](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.requestAnimationFrame.html) 可以注册动画帧回调，在回调内进行动画的逐帧绘制。

### 自定义字体

通过 [wx.loadFontFace](https://developers.weixin.qq.com/miniprogram/dev/api/ui/font/wx.loadFontFace.html) 可以为 Canvas 加载自定义字体。

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/GAIwtGmB7Ez3)

### 录制视频

通过 [MediaRecorder](https://developers.weixin.qq.com/miniprogram/dev/api/media/media-recorder/MediaRecorder.html) 可以将 Canvas 内容录制为视频并保存。

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/MCz3kPmC7zpa)

### WebGL

[在开发者工具中预览效果](https://developers.weixin.qq.com/s/9gIuqGmN7QzX)

```html
<canvas type="webgl" id="myCanvas" />
// 省略上面初始化步骤，已经获取到 canvas 对象

const gl = canvas.getContext('webgl') // 获取 webgl 渲染上下文
```

# 旧版 Canvas 迁移指南

小程序的 [旧版 canvas 接口](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas-legacy.html) 已经不再维护，本指南将指引如何迁移至新版 [Canvas 2D 接口](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/canvas.html)。

## 特性差异

|          | 旧版 canvas 接口 | Canvas 2D 接口    |
| :------- | :--------------- | :---------------- |
| 同层渲染 | 不支持           | 支持              |
| api支持  | 部分支持         | 支持全部 Web 标准 |
| 绘制     | 异步绘制         | 同步绘制          |
| 性能     | 低               | 高                |

## 迁移步骤

### 第一步：修改 WXML

```html
<canvas canvas-id="myCanvas" />
<!-- 修改为以下 -->
<canvas id="myCanvas" type="2d" />
```

旧版 canvas 接口使用 `canvas-id` 属性唯一标识 canvas；新版 Canvas 2D 可直接使用 `id` 标识。

另外需要给 canvas 添加 `type="2d"` 属性标识为新版 Canvas 2D 接口。

### 第二步：修改获取 CanvasContext

```js
const context = wx.createCanvasContext('myCanvas')
//
// 修改为以下
//
this.createSelectorQuery()
    .select('#myCanvas') // 在 WXML 中填入的 id
    .node(({ node: canvas }) => {
        const context = canvas.getContext('2d')
    })
    .exec()
```

旧版 canvas 接口使用 [wx.createCanvasContext](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.createCanvasContext.html) **同步**获取 [CanvasContext](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.html)。

新版 Canvas 2D 接口需要先通过 [SelectorQuery](https://developers.weixin.qq.com/miniprogram/dev/api/wxml/SelectorQuery.html) **异步**获取 [Canvas 对象](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.html)，再通过 [Canvas.getContext](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.getContext.html) 获取渲染上下文 [RenderingContext](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/RenderingContext.html)。

### 第三步：画布大小初始化

```js
// 旧版 canvas 不能修改宽高
this.createSelectorQuery()
    .select('#myCanvas') // 在 WXML 中填入的 id
    .fields({ node: true, size: true })
    .exec((res) => {
        // Canvas 对象
        const canvas = res[0].node
        // Canvas 画布的实际绘制宽高
        const renderWidth = res[0].width
        const renderHeight = res[0].height
        // Canvas 绘制上下文
        const ctx = canvas.getContext('2d')

        // 初始化画布大小
        const dpr = wx.getWindowInfo().pixelRatio
        canvas.width = renderWidth * dpr
        canvas.height = renderHeight * dpr
        ctx.scale(dpr, dpr)
    })
```

旧版 canvas 接口的画布大小是根据实际渲染宽度决定的，开发者无法修改。

新版 Canvas 2D 接口允许开发者自由修改画布的逻辑大小，默认宽高为 300*150。

不同的设备上，存在物理像素和逻辑像素不相等的情况，所以一般我们需要用 [wx.getWindowInfo](https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.getWindowInfo.html) 获取设备的像素比，乘上 canvas 的实际大小。

### 第四步：修改绘制方法

```js
// 若干绘制调用
context.fillRect(0, 0, 50, 50)
context.fillRect(20, 20, 50, 50)

context.draw(false, () => {
    // 这里绘制完成
    console.log('draw done')
})

//
// 修改为以下
//

// 绘制前清空画布
context.clearRect(0, 0, canvas.width, canvas.height)
// 若干绘制调用
context.fillRect(0, 0, 50, 50)
context.fillRect(20, 20, 50, 50)

// 这里绘制完成
console.log('draw done')
```

旧版 canvas 接口绘制需要调用 [CanvasContext.draw](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.draw.html) 才会进行绘制，并且绘制过程是**异步**的，需要等待绘制完成回调才能进行下一步操作。

新版 Canvas 2D 接口不再需要调用 `draw` 函数，所有绘制方法都会**同步**绘制到画布上。

需要注意的是 [CanvasContext.draw](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.draw.html) 函数第一个参数控制在绘制前是否保留上一次绘制（默认值为 false，即不保留），若设置为 false，则迁移至新接口后，需要在绘制前通过 `clearRect` 清空画布。

### 第五步：修改图片绘制

```js
context.drawImage(
    'https://open.weixin.qq.com/zh_CN/htmledition/res/assets/res-design-download/icon64_wx_logo.png',
    0,
    0,
    150,
    100,
)
//
// 修改为以下
//
const image = canvas.createImage()
image.onload = () => {
    context.drawImage(
        image,
        0,
        0,
        150,
        100,
    )
}
image.src = 'https://open.weixin.qq.com/zh_CN/htmledition/res/assets/res-design-download/icon64_wx_logo.png'
```

旧版 canvas 接口 [CanvasContext.drawImage](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/CanvasContext.drawImage.html) 直接传入图片 url 进行绘制。

新版 Canvas 2D 接口需要先通过 [Canvas.createImage](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.createImage.html) 创建图片对象，`onload` 图片加载完成回调触发后，再将图片对象传入 `context.drawImage` 进行绘制。

## 其余接口调整

### [wx.canvasToTempFilePath](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasToTempFilePath.html)

```js
wx.canvasToTempFilePath({
    canvasId: 'myCanvas',
    success(res) {
        //
    }
})
//
// 修改为以下
//
wx.canvasToTempFilePath({
    canvas: canvas,
    success(res) {
        //
    }
})
```

旧版 canvas 接口传入 `canvas-id`。

新版 Canvas 2D 接口需要直接传入 [Canvas 实例](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/Canvas.html)

### [wx.canvasPutImageData](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasPutImageData.html)

```js
wx.canvasPutImageData({
    canvasId: 'myCanvas',
    x: 0,
    y: 0,
    width: 1,
    height: 1,
    data: data,
    success (res) {
        // after put image data
    }
})
//
// 修改为以下
//
const context = canvas.getContext('2d')
context.putImageData(data, 0, 0, 0, 0, 1, 1)
// after put image data
```

新版 canvas 不支持 [wx.canvasPutImageData](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasPutImageData.html)，应使用 `context.putImageData` 代替。

### [wx.canvasGetImageData](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasGetImageData.html)

```js
wx.canvasGetImageData({
    canvasId: 'myCanvas',
    x: 0,
    y: 0,
    width: 100,
    height: 100,
    success(res) {
        console.log(res.width) // 100
        console.log(res.height) // 100
        console.log(res.data instanceof Uint8ClampedArray) // true
        console.log(res.data.length) // 100 * 100 * 4
    }
})
//
// 修改为以下
//
const context = canvas.getContext('2d')
const imageData = context.getImageData(0, 0, 100, 100)
console.log(imageData.width) // 100
console.log(imageData.height) // 100
console.log(imageData.data instanceof Uint8ClampedArray) // true
console.log(imageData.data.length) // 100 * 100 * 4
```

新版 canvas 不支持 [wx.canvasGetImageData](https://developers.weixin.qq.com/miniprogram/dev/api/canvas/wx.canvasGetImageData.html)，应使用 `context.getImageData` 代替。

### [wx.loadFontFace](https://developers.weixin.qq.com/miniprogram/dev/api/ui/font/wx.loadFontFace.html)

```js
wx.loadFontFace({
  family: 'Bitstream Vera Serif Bold',
  source: 'url("https://sungd.github.io/Pacifico.ttf")',
  success: console.log
})
//
// 修改为以下
//
wx.loadFontFace({
  family: 'Bitstream Vera Serif Bold',
  source: 'url("https://sungd.github.io/Pacifico.ttf")',
  scopes: ['webview', 'native'],
  success: console.log
})
```

新版 Canvas 2D 接口需要为 `scopes` 设置 `native`。