# 导航栏
为 `header` 元素添加 `aw-header` 类，使其成为导航栏。导航栏是响应式的。在 1279px 以下宽度的屏幕上，导航栏会以可折叠菜单的形式存在。

导航栏包含站点站点标题和链接。

导航栏在页面上只能存在一个，如果有多个，在窄屏幕状态下会造成折叠菜单冲突。（下面的 Demo 就是一个例子）

```html
<header class="aw-header">
    <h1>
        <a href="/">站点标题</a>
    </h1>
    <nav>
        <!-- 此处 label 和 input 不可删除 -->
        <label for="aw-header-nav-expend-doc-demo" class="aw-header-nav-expend"></label>
        <input id="aw-header-nav-expend-doc-demo" type="checkbox"/ class="aw-header-nav-expend">
        <ul>
            <li><a href="#">NavItem 1</a></li>
            <li><a href="#">NavItem 2</a></li>
            <li><a href="#">NavItem 3</a></li>
        </ul>
    </nav>
</header>
```

由于导航栏随着 viewport 大小变化而变化，因此你需要使用浏览器的“开发者工具”来查看下面 Demo 的变化。值得注意的是，由于导航栏在页面上只能存在一个，因此下面的 Demo 已经和本站的导航栏产生了冲突。

<div class="aw-p">
    <header class="aw-header">
        <h1>
            <a href="/">站点标题</a>
        </h1>
        <nav>
            <!-- 此处 label 和 input 不可删除 -->
            <label for="aw-header-nav-expend" class="aw-header-nav-expend"></label>
            <input id="aw-header-nav-expend" type="checkbox"/ class="aw-header-nav-expend">
            <ul>
                <li><a href="#">NavItem 1</a></li>
                <li><a href="#">NavItem 2</a></li>
                <li><a href="#">NavItem 3</a></li>
            </ul>
        </nav>
    </header>
</div>
