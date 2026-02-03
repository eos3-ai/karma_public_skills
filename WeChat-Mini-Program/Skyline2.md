# Skyline 基础组件支持与差异

## 通用特性

| 特性       | 支持情况                                       |
| :--------- | :--------------------------------------------- |
| 无障碍访问 | 暂只支持 aria-role / label / hidden / disabled |
| DarkMode   | 支持                                           |
| 原生组件   | 均支持同层渲染                                 |
| WeUI v2    | 支持                                           |

## 组件支持情况

总体来说，高频组件基本已支持，已标记为废弃的特性在 Skyline 下不会考虑支持。以下列出基础组件的整体情况，具体细节可跳转到对应组件文档查看

| 组件                                                         | 支持情况 | 组件差异与备注                                               |
| :----------------------------------------------------------- | :------- | :----------------------------------------------------------- |
| [text](https://developers.weixin.qq.com/miniprogram/dev/component/text?property=skyline) | 基本支持 | 内联文本只能用 text 组件；可通过 span 组件与 text / image 内联； |
| [view](https://developers.weixin.qq.com/miniprogram/dev/component/view.html) / [cover-view](https://developers.weixin.qq.com/miniprogram/dev/component/cover-view.html) | 完全支持 | 涉及文本节点见 text 组件                                     |
| [image](https://developers.weixin.qq.com/miniprogram/dev/component/image?property=skyline) / [cover-image](https://developers.weixin.qq.com/miniprogram/dev/component/cover-image?property=skyline) | 基本支持 | SVG 支持度已完善；部分低频 mode 未支持                       |
| [button](https://developers.weixin.qq.com/miniprogram/dev/component/button?property=skyline) | 完全支持 |                                                              |
| [scroll-view](https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view?property=skyline) | 完全支持 | 需显式指定 `type="list"`；部分属性无需对齐；额外支持大量新特性 |
| [swiper](https://developers.weixin.qq.com/miniprogram/dev/component/swiper?property=skyline) / [swiper-item](https://developers.weixin.qq.com/miniprogram/dev/component/swiper-item?property=skyline) | 完全支持 | 增强大量特性                                                 |
| [input](https://developers.weixin.qq.com/miniprogram/dev/component/input?property=skyline) / [textarea](https://developers.weixin.qq.com/miniprogram/dev/component/textarea?property=skyline) | 完全支持 | 光标选区、菜单略有不同                                       |
| [navigator](https://developers.weixin.qq.com/miniprogram/dev/component/navigator.html) | 完全支持 | 只能嵌套 text 组件或文本节点；可通过 span 组件与 text/image 内联 |
| [map](https://developers.weixin.qq.com/miniprogram/dev/component/map.html) | 完全支持 | 开发者工具暂未支持调试，请使用真机预览                       |
| [canvas](https://developers.weixin.qq.com/miniprogram/dev/component/canvas.html) | 完全支持 | 开发者工具暂未支持调试，请使用真机预览                       |
| [radio](https://developers.weixin.qq.com/miniprogram/dev/component/label.html) / [radio-group](https://developers.weixin.qq.com/miniprogram/dev/component/radio-group.html) | 完全支持 |                                                              |
| [label](https://developers.weixin.qq.com/miniprogram/dev/component/label.html) | 完全支持 |                                                              |
| [video](https://developers.weixin.qq.com/miniprogram/dev/component/video?property=skyline) | 基本支持 | 全屏在 3.3.0 已支持，投屏暂未支持，开发者工具暂未支持调试，请使用真机预览 |
| [checkbox](https://developers.weixin.qq.com/miniprogram/dev/component/checkbox?property=skyline) / [checkbox-group](https://developers.weixin.qq.com/miniprogram/dev/component/checkbox-group?property=skyline) | 完全支持 |                                                              |
| [picker](https://developers.weixin.qq.com/miniprogram/dev/component/picker?property=skyline) | 完全支持 |                                                              |
| [camera](https://developers.weixin.qq.com/miniprogram/dev/component/camera?property=skyline) | 完全支持 | 开发者工具暂未支持调试，请使用真机预览                       |
| [root-portal](https://developers.weixin.qq.com/miniprogram/dev/component/root-portal?property=skyline) | 完全支持 |                                                              |
| [form](https://developers.weixin.qq.com/miniprogram/dev/component/form?property=skyline) | 完全支持 |                                                              |
| [ad](https://developers.weixin.qq.com/miniprogram/dev/component/ad?property=skyline) | 完全支持 |                                                              |
| [official-account](https://developers.weixin.qq.com/miniprogram/dev/component/official-account?property=skyline) | 完全支持 |                                                              |
| [functional-page-navigator](https://developers.weixin.qq.com/miniprogram/dev/component/functional-page-navigator?property=skyline) | 支持中   |                                                              |
| [live-player](https://developers.weixin.qq.com/miniprogram/dev/component/live-player?property=skyline) / [live-pusher](https://developers.weixin.qq.com/miniprogram/dev/component/live-pusher?property=skyline) | 完全支持 |                                                              |
| [picker-view](https://developers.weixin.qq.com/miniprogram/dev/component/picker-view?property=skyline) | 基本支持 | indicator-class/mask-style 属性暂未支持                      |
| [voip-room](https://developers.weixin.qq.com/miniprogram/dev/component/voip-room?property=skyline) | 完全支持 |                                                              |
| [rich-text](https://developers.weixin.qq.com/miniprogram/dev/component/rich-text?property=skyline) | 完全支持 | 渲染结果可能略为不同，涉及到样式支持度；mode=web 时则完全对齐 webview |
| [match-media](https://developers.weixin.qq.com/miniprogram/dev/component/match-media?property=skyline) | 待考虑   |                                                              |
| [keyboard-accessary](https://developers.weixin.qq.com/miniprogram/dev/component/keyboard-accessary?property=skyline) | 待考虑   | 可通过 input 的 worklet:onkeyboardheightchange 回调实现      |
| [page-meta](https://developers.weixin.qq.com/miniprogram/dev/component/page-meta?property=skyline) | 基本支持 | 与全局滚动相关的属性不支持                                   |
| [editor](https://developers.weixin.qq.com/miniprogram/dev/component/editor?property=skyline) | 暂不考虑 |                                                              |
| [web-view](https://developers.weixin.qq.com/miniprogram/dev/component/web-view?property=skyline) | 暂不考虑 | 建议承载 web-view 的页面单独配置 `"renderer": "webview"`     |
| [movable-area](https://developers.weixin.qq.com/miniprogram/dev/component/movable-area?property=skyline) / [movable-view](https://developers.weixin.qq.com/miniprogram/dev/component/movable-view?property=skyline) | 暂不考虑 | 可用手势 + worklet 动画方案替代                              |
| [page-container](https://developers.weixin.qq.com/miniprogram/dev/component/page-container?property=skyline) | 基本支持 |                                                              |
| [share-element](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/share-element) | 完全支持 | 与 WebView 使用方式有异，特性有所增强                        |
| [icon](https://developers.weixin.qq.com/miniprogram/dev/component/icon?property=skyline) | 完全支持 |                                                              |
| [progress](https://developers.weixin.qq.com/miniprogram/dev/component/progress?property=skyline) | 暂不考虑 |                                                              |
| [slider](https://developers.weixin.qq.com/miniprogram/dev/component/slider?property=skyline) | 完全支持 |                                                              |
| [switch](https://developers.weixin.qq.com/miniprogram/dev/component/switch?property=skyline) | 完全支持 |                                                              |
| [xr-frame](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/(xr-frame)) | 暂未支持 |                                                              |
| [navigation-bar](https://developers.weixin.qq.com/miniprogram/dev/component/navigation-bar?property=skyline) | 不考虑   | Skyline 只能用自定义导航                                     |
| [open-data](https://developers.weixin.qq.com/miniprogram/dev/component/open-data?property=skyline) | 完全支持 | 已废弃特性不支持                                             |

## Skyline 新增组件

| 组件                                                         | 组件说明                                                     |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [span](https://developers.weixin.qq.com/miniprogram/dev/component/span.html) | 用于支持内联文本和 image / navigator 的混排                  |
| [snapshot](https://developers.weixin.qq.com/miniprogram/dev/component/snapshot.html) | 截图组件                                                     |
| [sticky-header](https://developers.weixin.qq.com/miniprogram/dev/component/sticky-header.html)、[sticky-section](https://developers.weixin.qq.com/miniprogram/dev/component/sticky-section.html) | 吸顶布局容器                                                 |
| [nested-scroll-header](https://developers.weixin.qq.com/miniprogram/dev/component/nested-scroll-header.html)、[nested-scroll-body](https://developers.weixin.qq.com/miniprogram/dev/component/nested-scroll-body.html) | 嵌套 [scroll-view](https://developers.weixin.qq.com/miniprogram/dev/component/scroll-view.html) 场景中使用的节点，仅支持作为 `<scroll-view type="nested">` 模式的直接子节点 |
| [list-view](https://developers.weixin.qq.com/miniprogram/dev/component/list-view.html) | 列表布局容器，仅支持作为 `<scroll-view type="custom">` 模式的直接子节点或 [sticky-section](https://developers.weixin.qq.com/miniprogram/dev/component/sticky-section.html) 组件直接子节点 |
| [grid-view](https://developers.weixin.qq.com/miniprogram/dev/component/grid-view.html) | Skyline 下网格布局容器 和 瀑布流布局容器                     |
| [draggable-sheet](https://developers.weixin.qq.com/miniprogram/dev/component/draggable-sheet.html) | 半屏可拖拽组件                                               |
| [double-tap-gesture-handler](https://developers.weixin.qq.com/miniprogram/dev/component/double-tap-gesture-handler.html) | 双击时触发手势                                               |
| [force-press-gesture-handler](https://developers.weixin.qq.com/miniprogram/dev/component/force-press-gesture-handler.html) | iPhone 设备重按时触发手势                                    |
| [horizontal-drag-gesture-handler](https://developers.weixin.qq.com/miniprogram/dev/component/horizontal-drag-gesture-handler.html) | 横向滑动时触发手势                                           |
| [long-press-gesture-handler](https://developers.weixin.qq.com/miniprogram/dev/component/long-press-gesture-handler.html) | 长按时触发手势                                               |
| [pan-gesture-handler](https://developers.weixin.qq.com/miniprogram/dev/component/pan-gesture-handler.html) | 拖动（横向/纵向）时触发手势                                  |
| [scale-gesture-handler](https://developers.weixin.qq.com/miniprogram/dev/component/scale-gesture-handler.html) | 多指缩放时触发手势                                           |
| [tap-gesture-handler](https://developers.weixin.qq.com/miniprogram/dev/component/tap-gesture-handler.html) | 点击时触发手势                                               |
| [vertical-drag-gesture-handler](https://developers.weixin.qq.com/miniprogram/dev/component/vertical-drag-gesture-handler.html) | 纵向滑动时触发手势                                           |

# Skyline WXSS 样式支持与差异

## 模块支持

| 模块                     | 支持情况 | 备注                                                         |
| :----------------------- | :------- | :----------------------------------------------------------- |
| CSS Animation            | ✓        | 安卓 8.0.37，iOS 8.0.39，支持情况见下表                      |
| 背景与边框               | ✓        | 常用的基本支持，详见[属性支持](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#属性支持) |
| 盒子模型                 | ✓        | 支持 border-box 和 content-box，没有 BFC                     |
| Inline 布局              | ×        | 开发中                                                       |
| Inline-Block 布局        | ×        | 仅支持在 text 组件里的嵌套结构使用，完整版本开发中           |
| Block 布局               | ✓        | 详见[开启默认 Block 布局](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#开启默认Block布局) |
| Flex 布局                | ✓        | 包括 inline-flex 布局                                        |
| 字体                     | ✓        | 基本支持，也支持自定义字体                                   |
| Positioned 布局          | ✓        | 支持情况见下表。sticky 可使用 [sticky-header](https://developers.weixin.qq.com/miniprogram/dev/component/sticky-header.html)/[sticky-section](https://developers.weixin.qq.com/miniprogram/dev/component/sticky-section.html) 替代 |
| CSS Transition           | ✓        |                                                              |
| CSS Variable（CSS 变量） | ✓        | 安卓 8.0.35，iOS 8.0.38                                      |
| Media queries            | ✓        | 只支持 DarkMode                                              |
| Font-face                | ✓        | 只支持 ttf 格式                                              |

## 选择器支持

| 类别           | 示例        | 支持度 | 备注                                                         |
| :------------- | :---------- | :----- | :----------------------------------------------------------- |
| 通配选择器     | * {}        | ×      |                                                              |
| 元素选择器     | tag {}      | ✓      |                                                              |
| 类选择器       | .class {}   | ✓      |                                                              |
| ID 选择器      | #id {}      | ✓      |                                                              |
| 分组选择器     | a, b {}     | ✓      |                                                              |
| 直接子代选择器 | a > b {}    | ✓      |                                                              |
| 后代选择器     | a b {}      | ✓      |                                                              |
| 属性选择器     | [attr] {}   | ×      |                                                              |
| 一般兄弟选择器 | a ~ b {}    | ✓      | 8.0.49                                                       |
| 紧邻兄弟选择器 | a + b {}    | ✓      | 8.0.49                                                       |
| 伪类选择器     | :active {}  | ✓      | 支持 :first-child / :last-child；微信 8.0.49 起（对应 Skyline 1.3.0）支持 :not / :only-child / :empty；微信 8.0.50 起（对应 Skyline 1.3.3）支持 :nth-child |
| 伪元素选择器   | ::before {} | ✓      | 只支持 ::before 和 ::after                                   |

## 属性支持

| 样式属性                   | 支持格式                                                     | 默认值                                                       | 备注                                                         |
| :------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| display                    | none / flex / block                                          | flex                                                         | 默认值可通过[配置](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#开启默认Block布局)改成 block |
| position                   | relative / absolute / fixed                                  | relative                                                     | fixed 在微信客户端 8.0.43 版本开始支持，只支持相对于窗口 viewport 定位，不支持 top / left / bottom / right 默认值 auto 解析，z-index 只作用在兄弟节点；sticky 可使用 [sticky-header](https://developers.weixin.qq.com/miniprogram/dev/component/sticky-header.html)/[sticky-section](https://developers.weixin.qq.com/miniprogram/dev/component/sticky-section.html) 替代 |
| overflow                   | hidden / visible                                             | visible                                                      | scroll 不支持，只能通过 scroll-view 实现；不支持单独设置 overflow-x/y |
| pointer-events             | auto / none                                                  | auto                                                         |                                                              |
| box-sizing                 | border-box / content-box                                     | border-box                                                   |                                                              |
| transform                  | none / `<transform-function>`                                | none                                                         |                                                              |
| transform-origin           | left / center / right / top / bottom / [`{1, 2}`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 50% 50%                                                      |                                                              |
| z-index                    | `<float>`                                                    | 0                                                            | 不支持层叠上下文，只对兄弟节点生效；不支持在 scroll-view 下的直接子节点上应用 |
| visibility                 | visible / hidden                                             | visible                                                      |                                                              |
| color                      | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-color) | black                                                        |                                                              |
| opacity                    | `<float>`                                                    | 1                                                            |                                                              |
| align-items                | stretch / center / flex-start / flex-end / baseline          | stretch                                                      |                                                              |
| align-self                 | auto / stretch / center / flex-start / flex-end / baseline   | auto                                                         |                                                              |
| align-content              | stretch / center / flex-start / flex-end / space-between / space-around | auto                                                         |                                                              |
| justify-content            | center / flex-start / flex-end / space-between / space-around / space-evenly | flex-start                                                   |                                                              |
| flex-direction             | row / row-reverse / column / column-reverse                  | column                                                       |                                                              |
| flex-wrap                  | nowrap / wrap / wrap-reverse                                 | nowrap                                                       |                                                              |
| flex-grow                  | `<float>`                                                    | 0                                                            |                                                              |
| flex-shrink                | `<float>`                                                    | 1                                                            |                                                              |
| flex-basis                 | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | auto                                                         |                                                              |
| order                      | `<float>`                                                    | 0                                                            |                                                              |
| gap                        | `<length>`                                                   | 0                                                            |                                                              |
| flex                       |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| background-color           | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-color) | transparent                                                  |                                                              |
| background-image           | none / [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-image) | none                                                         | 不支持多张图片                                               |
| background-size            | contain / cover / [`[ | auto\]{1, 2}`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | auto                                                         |                                                              |
| background-position        | left / center / right / top / bottom / [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0 0                                                          | 完全支持 `<bg-position>`#，请参考 MDN                        |
| background-repeat          | repeat-x / repeat-y / repeat / no-repeat                     | repeat                                                       |                                                              |
| background                 |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| width                      | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | auto                                                         |                                                              |
| height                     | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | auto                                                         |                                                              |
| min-width                  | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | auto                                                         |                                                              |
| min-height                 | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | none                                                         |                                                              |
| max-width                  | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | auto                                                         |                                                              |
| max-height                 | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | none                                                         |                                                              |
| left                       | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | auto                                                         |                                                              |
| right                      | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | auto                                                         |                                                              |
| top                        | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | auto                                                         |                                                              |
| bottom                     | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | auto                                                         |                                                              |
| padding                    | [`{1,4}`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0 0 0 0                                                      |                                                              |
| padding-left               | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            |                                                              |
| padding-top                | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            |                                                              |
| padding-right              | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            |                                                              |
| padding-bottom             | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            |                                                              |
| margin                     | [`{1,4}`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0 0 0 0                                                      |                                                              |
| margin-left                | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            |                                                              |
| margin-top                 | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            |                                                              |
| margin-right               | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            |                                                              |
| margin-bottom              | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            |                                                              |
| border-left-width          | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 3                                                            |                                                              |
| border-left-style          | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-border-style) | none                                                         |                                                              |
| border-left-color          | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-color) | black                                                        | 默认值与 web 不同， web 默认值是 currentcolor                |
| border-top-width           | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 3                                                            |                                                              |
| border-top-style           | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-border-style) | none                                                         |                                                              |
| border-top-color           | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-color) | black                                                        | 默认值与 web 不同， web 默认值是 currentcolor                |
| border-right-width         | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 3                                                            |                                                              |
| border-right-style         | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-border-style) | none                                                         |                                                              |
| border-right-color         | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-color) | black                                                        | 默认值与 web 不同， web 默认值是 currentcolor                |
| border-bottom-width        | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 3                                                            |                                                              |
| border-bottom-style        | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-border-style) | none                                                         |                                                              |
| border-bottom-color        | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-color) | black                                                        | 默认值与 web 不同， web 默认值是 currentcolor                |
| border-width               |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| border-style               |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| border-color               |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| border-left                |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| border-right               |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| border-top                 |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| border-bottom              |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| border                     |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| box-shadow                 | none / inset? && [`{2,4}`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) && [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-color)? | none                                                         | 不支持多个叠加                                               |
| border-top-left-radius     | [`{1, 2}`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            | border-radius 非 0 时，四边的 border-width 可不一致，四边的 border-color 和 border-style 需一致 |
| border-top-right-radius    | [`{1, 2}`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            | border-radius 非 0 时，四边的 border-width 可不一致，四边的 border-color 和 border-style 需一致 |
| border-bottom-left-radius  | [`{1, 2}`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            | border-radius 非 0 时，四边的 border-width 可不一致，四边的 border-color 和 border-style 需一致 |
| border-bottom-right-radius | [`{1, 2}`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 0                                                            | border-radius 非 0 时，四边的 border-width 可不一致，四边的 border-color 和 border-style 需一致 |
| border-radius              |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| transition-property        | none / all / transform / opacity 等                          | all                                                          | 基本都支持，暂不一一列举                                     |
| transition-duration        | `<time>`                                                     | 0                                                            |                                                              |
| transition-timing-function | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-timing-function) | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-timing-function) |                                                              |
| transition-delay           | `<time>`                                                     | 0                                                            |                                                              |
| transition                 |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| font                       |                                                              |                                                              | 简写属性，支持解析但以展开属性为准；不支持 caption / icon 等系统字体; |
| font-size                  | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | 16px                                                         | 不支持百分比；不支持 keyword (smaller..)                     |
| line-height                | normal / `<number>` / [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) / `<percent>` | normal                                                       |                                                              |
| text-align                 | left / center / right / justify / start / end                | start                                                        |                                                              |
| font-weight                | normal / bold / `<float>`                                    | normal                                                       |                                                              |
| white-space                | normal / nowrap / normal                                     |                                                              |                                                              |
| text-overflow              | clip / ellipsis                                              | clip                                                         | 仅作用于 text 节点                                           |
| word-break                 | normal / break-all                                           | normal                                                       |                                                              |
| word-spacing               | normal / [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | normal                                                       |                                                              |
| letter-spacing             | normal / [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | normal                                                       |                                                              |
| font-family                | serif / sans-serif / monospace / cursive / fantasy / `<string>` |                                                              |                                                              |
| font-style                 | normal / italic                                              | normal                                                       |                                                              |
| text-decoration-line       | none / underline / overline / line-through                   | none                                                         | 仅作用于 text 节点                                           |
| text-decoration-style      | solid / double / dotted / dashed / wavy                      | solid                                                        | 仅作用于 text 节点                                           |
| text-decoration-color      | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-color) | black                                                        | 仅作用于 text 节点；默认值和 web 不同，web 默认值是 currentcolor |
| text-decoration            |                                                              |                                                              | 简写属性，支持解析但以展开属性为准；当前仅支持设置一种类型；暂不支持复合使用 text-decoration |
| text-shadow                | none / [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-color)? && [`{2,3}`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-length) | none                                                         |                                                              |
| backdrop-filter            | none / [`[\]`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-filter-function) | none                                                         | 不支持 multi function；不支持 drop-shadow；不支持 url；与 opacity 混合有问题；blur 某些情况表现不一致； |
| filter                     | none / [`[\]`](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-filter-function) | none                                                         | 不支持 multi function；不支持 drop-shadow；不支持 url；      |
| mask-image                 | none / [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-image) | none                                                         | 不支持多张图片                                               |
| animation-delay            | `<time>`                                                     | 0                                                            |                                                              |
| animation-direction        | normal / reverse / alternate / alternate-reverse             | normal                                                       |                                                              |
| animation-duration         | `<time>`                                                     | 0                                                            |                                                              |
| animation-fill-mode        | forwards / both                                              | none                                                         | none 与 backwards 暂未支持，表现均为 forwards                |
| animation-iteration-count  | infinite / `<number>`                                        | 1                                                            |                                                              |
| animation-name             | none / `<custom-ident>`                                      | none                                                         |                                                              |
| animation-timing-function  | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-timing-function) | [``](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/wxss.html#wxss-timing-function) |                                                              |
| animation                  |                                                              |                                                              | 简写属性，支持解析但以展开属性为准                           |
| will-change                | auto / contents                                              | auto                                                         | 声明绘制边界，优化渲染性能                                   |

## 类型支持列表

| 类别              | 格式              | 支持度                        | 备注                   |
| :---------------- | :---------------- | :---------------------------- | :--------------------- |
| <length>          | auto              | ✓                             |                        |
| px                | ✓                 |                               |                        |
| rem               | ✓                 |                               |                        |
| em                | ×                 |                               |                        |
| rpx               | ✓                 |                               |                        |
| vw                | ✓                 |                               |                        |
| vh                | ✓                 |                               |                        |
| vmin              | ✓                 |                               |                        |
| vmax              | ✓                 |                               |                        |
| ratio             | ✓                 |                               |                        |
| env()             | ✓                 | 只支持 safe-area-inset-* 系列 |                        |
| calc()            | ✓                 |                               |                        |
| <color>           | color keywords    | ✓                             |                        |
| transparent       | ✓                 |                               |                        |
| currentColor      | ×                 | 考虑支持                      |                        |
| rgb[a]            | ✓                 |                               |                        |
| #RRGGBB / #RGB    | ✓                 |                               |                        |
| hsl               | ✓                 |                               |                        |
| hsla              | ✓                 |                               |                        |
| <url>             | url()             | ✓                             |                        |
| <gradient>        | linear-gradient() | ✓                             |                        |
| radial-gradient() | ✓                 |                               |                        |
| conic-gradient()  | ✓                 |                               |                        |
| <image>           | <url>             | ✓                             |                        |
| <gradient>        | ✓                 |                               |                        |
| <border-style>    | none              | ✓                             |                        |
| hidden            | ✓                 |                               |                        |
| solid             | ✓                 |                               |                        |
| dashed            | ✓                 |                               |                        |
| dotted            | ✓                 |                               |                        |
| <filter-function> | brightness()      | ✓                             | 多个 function 暂不支持 |
| contrast()        | ✓                 |                               |                        |
| saturate()        | ✓                 |                               |                        |
| huerotate()       | ✓                 |                               |                        |
| invert()          | ✓                 |                               |                        |
| opacity()         | ✓                 |                               |                        |
| grayscale()       | ✓                 |                               |                        |
| specia()          | ✓                 |                               |                        |
| drop-shadow       | ×                 |                               |                        |
| <angle>           | deg               | ✓                             |                        |
| grad              | ✓                 |                               |                        |
| rad               | ✓                 |                               |                        |
| turn              | ✓                 |                               |                        |
| <timing-function> | ease              | ✓                             |                        |
| ease-in           | ✓                 |                               |                        |
| ease-out          | ✓                 |                               |                        |
| ease-in-out       | ✓                 |                               |                        |
| linear            | ✓                 |                               |                        |
| cubic-bezier      | ✓                 |                               |                        |
| steps             | ✓                 |                               |                        |
| step-start        | ✓                 |                               |                        |
| step-end          | ✓                 |                               |                        |

## 开启默认Block布局

Skyline 下节点默认为 flex 布局，可通过以下配置切换为默认 block 布局。

| 平台       | 最低版本                     |
| :--------- | :--------------------------- |
| Android    | 8.0.34                       |
| IOS        | 8.0.36                       |
| 开发者工具 | Nightly Build (1.06.2304262) |
| 基础库     | 2.31.1                       |

在 `app.json` 或 `page.json` 中配置：

```json
rendererOptions: {
  "skyline": {
    "defaultDisplayBlock": true,
  }
}
```

## 开启默认ContentBox盒模型

Skyline 下节点默认为 border-box 盒模型，可通过以下配置切换为默认 content-box 盒模型。

| 平台       | 最低版本                     |
| :--------- | :--------------------------- |
| Android    | 8.0.42                       |
| IOS        | 8.0.42                       |
| 开发者工具 | Nightly Build (1.06.2310092) |
| 基础库     | 3.1.0                        |

在 `app.json` 或 `page.json` 中配置：

```json
rendererOptions: {
  "skyline": {
    "defaultContentBox": true,
  }
}
```

## 开启tag选择器全局匹配

Skyline 下 tag 选择器遵循样式隔离机制，而 WebView 下不受样式隔离约束，可通过 `tagNameStyleIsolation: legacy` 配置对齐 WebView 表现，若指定 `tagNameStyleIsolation: isolated` 则遵循样式隔离机制。

| 平台       | 最低版本                     |
| :--------- | :--------------------------- |
| Android    | 8.0.51                       |
| IOS        | 8.0.51                       |
| 开发者工具 | Nightly Build (1.06.2409032) |
| 基础库     | 3.6.0                        |

在 `app.json` 或 `page.json` 中配置：

```json
rendererOptions: {
  "skyline": {
    "tagNameStyleIsolation": "legacy",
  }
}
```

## 开启scroll-view自动撑开

Skyline 下 scroll-view 默认需要指定宽高撑开，可通过以下配置切换为自动根据内容撑开。

| 平台    | 最低版本 |
| :------ | :------- |
| Android | 8.0.54   |
| IOS     | 8.0.54   |
| 基础库  | 3.7.2    |

在 `app.json` 或 `page.json` 中配置：

```json
rendererOptions: {
  "skyline": {
    "enableScrollViewAutoSize": true,
  }
}
```

## 开启keyframe样式全局共享

Skyline 下 @keyframe 规则遵循样式隔离机制，而 WebView 下不受样式隔离约束，可通过 `tagNameStyleIsolation: legacy` 配置对齐 WebView 表现，若指定 `tagNameStyleIsolation: isolated` 则遵循样式隔离机制。

| 平台    | 最低版本 |
| :------ | :------- |
| Android | 8.0.57   |
| IOS     | 8.0.57   |
| 基础库  | 3.8.0    |

在 `app.json` 或 `page.json` 中配置：

```json
rendererOptions: {
  "skyline": {
    "keyframeStyleIsolation": "legacy",
  }
}
```