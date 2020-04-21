# 按钮
为 `a` 或 `button` 元素设置 `aw-btn` 类来使其成为按钮。添加 `aw-bg-*` 类来设置按钮的颜色。关于背景颜色，详见：[背景颜色](bgcolor.html)；关于颜色变量，详见：[全局默认值：颜色](global.html)。

按钮在鼠标滑过或按下时，默认时没有效果的。添加 `aw-hov-dark` 类使其在鼠标滑过或按下时切换到深色。该功能基于 CSS 滤镜，故不支持滤镜的浏览器可能正常展示此效果。

在 IE 浏览器上，`button` 形式的按钮会有“按下”效果；`a` 形式的则没有。在其他浏览器上，两种形式都没有“按下”效果。

```html
<a href="#" class="aw-btn aw-bg-green aw-hov-dark">按钮</a>
<a href="#" class="aw-btn aw-bg-red aw-hov-dark">按钮</a>
<a href="#" class="aw-btn aw-bg-yellow aw-hov-dark">按钮</a>
<a href="#" class="aw-btn aw-bg-orange aw-hov-dark">按钮</a>
<button class="aw-btn aw-bg-blue aw-hov-dark">按钮</button>
<button class="aw-btn aw-bg-lightblue aw-hov-dark">按钮</button>
<button class="aw-btn aw-bg-cyan aw-hov-dark">按钮</button>
<a href="#" class="aw-btn aw-bg-green">无 hover 效果的按钮</a>
```

<div class="aw-p">
    <a href="#" class="aw-btn aw-bg-green aw-hov-dark">按钮</a>
    <a href="#" class="aw-btn aw-bg-red aw-hov-dark">按钮</a>
    <a href="#" class="aw-btn aw-bg-yellow aw-hov-dark">按钮</a>
    <a href="#" class="aw-btn aw-bg-orange aw-hov-dark">按钮</a>
    <button href="#" class="aw-btn aw-bg-blue aw-hov-dark">按钮</button>
    <button href="#" class="aw-btn aw-bg-lightblue aw-hov-dark">按钮</button>
    <button href="#" class="aw-btn aw-bg-cyan aw-hov-dark">按钮</button>
    <a href="#" class="aw-btn aw-bg-green">无 hover 效果的按钮</a>
</div>

## 幽灵按钮
幽灵按钮时背景或字体透明的按钮，常用于深色背景或图片上。设置幽灵按钮，无需添加 `aw-btn` 类。

为 `a` 或 `button` 元素设置 `aw-ghost-light` 类使其成为浅色（背景镂空）按钮。这种按钮可以放置在图片或深色背景上。此按钮的背景是真正透明的，因此可以放置在自定义元素上。

为 `a` 或 `button` 元素设置 `aw-ghost-dark` 类使其成为深色（字体镂空）按钮。这种按钮可以放置深色背景上；**放置在图片上时不起效果**。此按钮的字体 **不是真正透明** 的，它依赖于 `aw-bg-*` 类来确定字体的颜色，因此只能放置在设置了 `aw-bg-*` 的父容器内。

```html
<a href="#" class="aw-ghost-light aw-hov-dark">按钮</a>
<button class="aw-ghost-dark aw-hov-dark">按钮</button>
```

<div class="aw-p aw-bg-orange">
    <a href="#" class="aw-ghost-light aw-hov-dark">按钮</a>
    <button class="aw-ghost-dark aw-hov-dark">按钮</button>
</div>

## 按钮的禁用状态
如 [辅助类：禁用状态](utils.html) 所述，为按钮添加 `aw-disabled` 类即可使其应用禁用样式。

**警告：禁用样式只改变了显示形式，并没有实际禁用元素，并不能阻止点击事件的发生，也不能阻止 `a` 元素的 `href` 属性将网页导航到其他页面。开发者应自行编写 JavaScript 来完全地禁用元素。**

```html
<a href="#" class="aw-btn aw-bg-green">按钮</a>
<a href="#" class="aw-btn aw-bg-green aw-disabled">禁用按钮</a>
```

如下所示，当您点击禁用的按钮，页面依然会被导航到顶部：

<div class="aw-p">
    <a href="#" class="aw-btn aw-bg-green">按钮</a>
    <a href="#" class="aw-btn aw-bg-green aw-disabled">禁用按钮</a>
</div>
