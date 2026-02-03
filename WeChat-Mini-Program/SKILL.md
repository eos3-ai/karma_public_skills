---
name: wechat-miniprogram
description: WeChat Mini Program development rules. Use this skill when developing WeChat mini programs, and deploying mini program projects.
---

## 微信小程序设计指南

在你刚开始开发新的一个小程序时，你应该阅读小程序设计指南，它旨在微信生态体系内，建立友好、高效、一致的用户体验，同时最大程度适应和支持不同需求，实现用户与小程序服务方的共赢。小程序设计指南分为小程序设计通用指南General.md、小程序大屏适配指南LargeScreen.md、小程序适老化设计指南SuitOldMan.md。通常情况下，你只需要阅读General.md。

## 开发指南

小程序提供了一个简单、高效的应用开发框架和丰富的组件及API，帮助开发者在微信中开发具有原生 APP 体验的服务。本章分主题的介绍了小程序的开发语言、框架、能力、调试等内容，帮助开发者快速全面的了解小程序开发的方方面面。当你开发的问题用到下面的知识的时候，你去阅读相应的md文档。

- 小程序与普通网页开发的区别：difference.md
- 小程序代码构成：compose.md
- 小程序宿主环境：HostEnvironment.md
- 目录结构：DirectoryStructure.md
- 小程序配置：configuration.md
- 小程序框架：小程序的框架提供了6个相关文档。分别为framework1.md，framework2.md，framework3.md，framework4.md，framework5.md，framework6.md，如果是框架介绍、场景值、逻辑层，请查看framework1.md，如果是逻辑层的页面路由问题，framework2.md；如果是模块化和API方面的问题，请查看framework3.md。如果是视图层的视图层介绍、WXML、WXSS、WXS，请查看framework4.md；如果是视图层的事件系统问题，请查看framework5.md，如果是简易双向绑定、基础组件、获取界面上的节点信息、响应显示区域变化、分栏模式、动画、初始渲染缓存问题，请查看framework6.md。
- 小程序运行时：runtime.md
- Skyline 渲染引擎：Skyline 渲染引擎提供了5个相关文档。分别为：Skyline1.md，Skyline2.md，Skyline3.md，Skyline4.md，Skyline5.md；如果是Skyline渲染引擎的概览，请查看Skyline1.md，如果是Skyline渲染引擎的支持与差异，请查看Skyline2.md，如果是Skyline渲染引擎的增强特性的Worklet 动画、手势系统，请查看Skyline3.md，如果是Skyline渲染引擎的增强特性的自定义路由，请查看的Skyline4.md，如果是Skyline渲染引擎的增强特性的共享元素动画、全局工具栏、滚动容器及其应用场景，请查看Skyline5.md；
- glass-easel 组件框架：glassEasel.md
- 自定义组件：自定义组件提供了14个相关文档，分别为：customComponent1.md，customComponent2.md，customComponent3.md，customComponent4.md，customComponent5.md，customComponent6.md，customComponent7.md，customComponent8.md，customComponent9.md，customComponent10.md，customComponent11.md，customComponent12.md，customComponent13.md，customComponent14.md；如果是自定义组件的介绍、组件系统、组件模板和样式，查看customComponent1.md；如果是自定义组件的Component 构造器，查看customComponent2.md；如果是自定义组件的组件间通信与事件，查看customComponent3.md；如果是自定义组件的组件生命周期，查看customComponent4.md；如果是自定义组件的behaviors，查看customComponent5.md；如果是自定义组件的组件间关系，查看customComponent6.md；如果是自定义组件的数据监听器，查看customComponent7.md；如果是自定义组件的纯数据字段，查看customComponent8.md；如果是自定义组件的抽象节点，查看customComponent9.md；如果是自定义组件的自定义组件扩展，查看customComponent10.md；如果是自定义组件的开发第三方自定义组件，查看customComponent11.md；如果是自定义组件的获取更新性能统计信息，查看customComponent12.md；如果是自定义组件的占位组件，查看customComponent13.md；如果是自定义组件的查看自定义组件数据，查看customComponent14.md；
- 插件：插件提供了6个相关的文档，分别为plugin1.md，plugin2.md，plugin3.md，plugin4.md，plugin5.md，plugin6.md。如果是插件的介绍，查看plugin1.md；如果是开发插件，查看plugin2.md；如果是使用插件，查看plugin3.md；如果是插件调用 API 的限制，查看plugin4.md；如果是插件使用组件的限制，查看plugin5.md；如果是插件功能页的介绍、用户信息功能页、支付功能页，查看plugin6.md；如果是插件功能页的收货地址功能页，查看plugin7.md；如果是插件功能页的发票功能页，查看plugin8.md；如果是插件功能页的发票抬头功能页，查看plugin9.md；
- 基础能力：基础能力提供了15个相关文档，分别为baseAbility1.md，baseAbility2.md，baseAbility3.md，baseAbility4.md，baseAbility5.md，baseAbility6.md，baseAbility7.md，baseAbility8.md，baseAbility9.md，baseAbility10.md，baseAbility11.md，baseAbility12.md，baseAbility13.md，baseAbility14.md；如果是基础能力的网络，查看baseAbility1.md；如果是基础能力的存储，查看baseAbility2.md；如果是基础能力的文件系统，查看baseAbility3.md；如果是基础能力的画布，查看baseAbility4.md；如果是基础能力的分包加载，查看baseAbility5.md；如果是基础能力的按需注入和用时注入，查看baseAbility6.md；如果是基础能力的多线程 Worker，查看baseAbility7.md；如果是基础能力的服务端能力，查看baseAbility8.md；如果是基础能力的自定义 tabBar，查看baseAbility9.md；如果是基础能力的周期性更新，查看baseAbility10.md；如果是基础能力的数据预拉取，查看baseAbility11.md；如果是基础能力的DarkMode 适配指南，查看baseAbility12.md；如果是基础能力的大屏适配指南，查看baseAbility13.md；如果是基础能力的HarmonyOS 适配指南，查看baseAbility14.md；
