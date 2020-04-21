# 响应式网格
网格被分为 8 分，相关类用分数表示。父容器要先加上 `aw-g` 类。

`aw-g-w-` 开头为非响应式网格，`aw-g-w-s-` 开头为响应式网格。

IE 默认情况下，会回退到不支持网格的模式，解决方法见“IE 兼容性”节。

<style>
.demo-0, .demo-1 { padding: .5em; margin-bottom: 16px; text-align: center; }
.demo-0 { background-color: #ddd; }
.demo-1 { background-color: #999;  }
</style>

|非响应式|宽度|响应式<br>屏宽 0px-767px|响应式<br>屏宽 768px-1279px|响应式<br>屏宽 1279px+|
|-------------|-----|-----------------|-----------------|-----------------|
|`.aw-g-w-1-8`| 1/8 |`.aw-g-w-s-s-1-8`|`.aw-g-w-s-m-1-8`|`.aw-g-w-s-l-1-8`|
|`.aw-g-w-3-8`| 3/8 |`.aw-g-w-s-s-3-8`|`.aw-g-w-s-m-3-8`|`.aw-g-w-s-l-3-8`|
|`.aw-g-w-5-8`| 5/8 |`.aw-g-w-s-s-5-8`|`.aw-g-w-s-m-5-8`|`.aw-g-w-s-l-5-8`|
|`.aw-g-w-7-8`| 7/8 |`.aw-g-w-s-s-7-8`|`.aw-g-w-s-m-7-8`|`.aw-g-w-s-l-7-8`|
|`.aw-g-w-1-4`| 1/4 |`.aw-g-w-s-s-1-4`|`.aw-g-w-s-m-1-4`|`.aw-g-w-s-l-1-4`|
|`.aw-g-w-3-4`| 3/4 |`.aw-g-w-s-s-3-4`|`.aw-g-w-s-m-3-4`|`.aw-g-w-s-l-3-4`|
|`.aw-g-w-1-2`| 1/2 |`.aw-g-w-s-s-1-2`|`.aw-g-w-s-m-1-2`|`.aw-g-w-s-l-1-2`|
|`.aw-g-w-1`  |  1  |`.aw-g-w-s-s-1`  |`.aw-g-w-s-m-1`  |`.aw-g-w-s-l-1`  |

<div class="aw-p aw-g">
    <div class="aw-g-w-1-8 demo-0">1/8</div>
    <div class="aw-g-w-7-8 demo-1">7/8</div>
    <div class="aw-g-w-1-4 demo-0">1/4</div>
    <div class="aw-g-w-3-4 demo-1">3/4</div>
    <div class="aw-g-w-1-2 demo-0">1/2</div>
    <div class="aw-g-w-1-2 demo-1">1/2</div>
    <div class="aw-g-w-5-8 demo-0">5/8</div>
    <div class="aw-g-w-3-8 demo-1">3/8</div>
    <div class="aw-g-w-1   demo-0">1</div>
</div>

## IE 兼容性
为了使 IE 兼容网格，需要在添加 `aw-g` 类的基础上，增加 `aw-g-ie` 类。同时，由于 IE 不支持网格自动填充，需要自己设置网格位置（`-ms-grid-coloum` 和 `-ms-grid-row`）。

我们提供了以下工具类来帮助排版。请只把此工具类作修复 IE 问题用，不要用于其他用途，否则不保证其能在其他浏览器上正确显示。

注意，这些工具类也会影响 Edge（非 Chromium 内核的旧版）的显示。

|列号|非响应式     |屏宽 0px-767px  |屏宽 768px-1279px|屏宽 1279px+    |
|----|------------|----------------|----------------|----------------|
|   1|`.aw-g-ie-1`|`.aw-g-ie-s-s-1`|`.aw-g-ie-s-m-1`|`.aw-g-ie-s-l-1`|
|   2|`.aw-g-ie-2`|`.aw-g-ie-s-s-2`|`.aw-g-ie-s-m-2`|`.aw-g-ie-s-l-2`|
|   3|`.aw-g-ie-3`|`.aw-g-ie-s-s-3`|`.aw-g-ie-s-m-3`|`.aw-g-ie-s-l-3`|
|   4|`.aw-g-ie-4`|`.aw-g-ie-s-s-4`|`.aw-g-ie-s-m-4`|`.aw-g-ie-s-l-4`|
|   5|`.aw-g-ie-5`|`.aw-g-ie-s-s-5`|`.aw-g-ie-s-m-5`|`.aw-g-ie-s-l-5`|
|   6|`.aw-g-ie-6`|`.aw-g-ie-s-s-6`|`.aw-g-ie-s-m-6`|`.aw-g-ie-s-l-6`|
|   7|`.aw-g-ie-7`|`.aw-g-ie-s-s-7`|`.aw-g-ie-s-m-7`|`.aw-g-ie-s-l-7`|
|   8|`.aw-g-ie-8`|`.aw-g-ie-s-s-8`|`.aw-g-ie-s-m-8`|`.aw-g-ie-s-l-8`|

```html
<div class="aw-p aw-g aw-g-ie">
    <div class="aw-g-w-1-8 demo-0 aw-g-ie-1">w-1<br>ie-1</div>
    <div class="aw-g-w-1-8 demo-0 aw-g-ie-3">w-1<br>ie-3</div>
    <div class="aw-g-w-1-8 demo-0 aw-g-ie-5">w-1<br>ie-5</div>
    <div class="aw-g-w-1-8 demo-0 aw-g-ie-7">w-1<br>ie-7</div>
</div>
```

以下内容在 IE/Edge 浏览器上才会正确显示，在 Chrome 上，元素会堆叠在一起：

<div class="aw-p aw-g aw-g-ie">
    <div class="aw-g-w-1-8 demo-0 aw-g-ie-1">w-1<br>ie-1</div>
    <div class="aw-g-w-1-8 demo-0 aw-g-ie-3">w-1<br>ie-3</div>
    <div class="aw-g-w-1-8 demo-0 aw-g-ie-5">w-1<br>ie-5</div>
    <div class="aw-g-w-1-8 demo-0 aw-g-ie-7">w-1<br>ie-7</div>
</div>

如果不增加 `aw-g-ie` 类，那么将会所有网格子元素将会占满 100% 宽度（您可以用 IE 浏览器查看第一个 Demo）。
