# 容器
为元素设置 `aw-vh-container` 类，使其最小高度（`min-height`）为 `100vh - (导航栏高度)`。

为了演示，容器的背景被设置成了 `#f0f0f0`，实际上是白色的。
```
<div class="aw-vh-container">
    ...
</div>
```
<div class="aw-p">
    <div class="aw-vh-container" style="background: #f0f0f0"></div>
</div>

## 响应式白边容器
为元素同时设置 `aw-vh-container` 和 `aw-vh-container-align-header` 类，使其两侧白边与导航栏对齐。由于导航栏的 `margin-left/right` 是响应式的，容器的 `margin-left/right` 也是响应式的。

```
<div class="aw-vh-container aw-vh-container-align-header">
    ...
</div>
```
调整窗口大小以观察下方 Demo 的变化。

<div class="aw-p">
    <div class="aw-vh-container aw-vh-container-align-header"
        style="background: #f0f0f0">
    </div>
</div>
