# 全局默认样式
## Body
`body` 元素具有以下默认样式：

 - `margin`：0
 - 字号：`--aw-font-size-s4` 或 `16px`（小四号）
 - 字体：`--aw-font-family`
 - 行距：1.5 倍行距

## 链接
`a` 元素具有以下默认样式：

 - 颜色：`--aw-color-blue-dark` 或 `#106ebe`
 - 下划线：正常状态无下划线，`hover` 状态有 `border` 形式的下划线。

```html
<a href="#">链接</a>
```

<div class="aw-p">
    <a href="#">链接</a>
</div>

## 代码
所有代码具有以下默认样式：

 - 字号：`--aw-font-size-c5` 或 `14px`（五号）
 - 字体：`--aw-font-family-code`
 - 颜色：`--aw-color-gray-1` 或 `#3f3f3f`
 - 背景：`--aw-color-gray-7` 或 `#f0f0f0`

`code` 元素（不在 `pre` 中）具有以下默认样式：

 - `padding: .2rem .4rem`

`pre` 元素具有以下默认样式：

 - `padding: 16px`
 - `margin-top: 16px`
 - `margin-bottom: 16px`
 - 超出父容器宽度自动显示滚动条
