# 页脚
为 `footer` 元素添加 `aw-footer` 类，即可使其成为页脚。页脚也是响应式的。

```html
<footer class="aw-footer">
    ...
</footer>
```

<div class="aw-p">
    <footer class="aw-footer">
    </footer>
</div>

可以看到，空的页脚什么都没有。您可以给页脚添加两种元素：页脚导航和版权信息。

## 页脚导航
页脚的 `nav` 元素自动成为页脚导航的一栏。导航由多个栏目组成：
```html
<footer class="aw-footer">
    <div class="aw-g aw-g-ie">
        <nav class="aw-g-w-1-2 aw-g-w-s-s-1 aw-g-ie-1">
            <h2>栏目 1</h2>
            <ul>
                <li><a href="#">NavItem 1</a></li>
                <li><a href="#">NavItem 2</a></li>
                <li><a href="#">NavItem 3</a></li>
            </ul>
        </nav>
        <nav class="aw-g-w-1-2 aw-g-w-s-s-1 aw-g-ie-5">
            <h2>栏目 2</h2>
            <ul>
                <li><a href="#">NavItem 1</a></li>
                <li><a href="#">NavItem 2</a></li>
                <li><a href="#">NavItem 3</a></li>
            </ul>
        </nav>
    </div>
</footer>
```
<div class="aw-p">
    <footer class="aw-footer">
        <div class="aw-g aw-g-ie">
            <nav class="aw-g-w-1-2 aw-g-w-s-s-1 aw-g-ie-1">
                <h2>栏目 1</h2>
                <ul>
                    <li><a href="#">NavItem 1</a></li>
                    <li><a href="#">NavItem 2</a></li>
                    <li><a href="#">NavItem 3</a></li>
                </ul>
            </nav>
            <nav class="aw-g-w-1-2 aw-g-w-s-s-1 aw-g-ie-5">
                <h2>栏目 2</h2>
                <ul>
                    <li><a href="#">NavItem 1</a></li>
                    <li><a href="#">NavItem 2</a></li>
                    <li><a href="#">NavItem 3</a></li>
                </ul>
            </nav>
        </div>
    </footer>
</div>

## 版权信息
带有 `aw-footer-copyright` 的元素，成为页脚版权信息栏。

如果页脚只有版权信息，没用页脚导航，建议添加 `aw-footer-copyright-s` 类以补足 `padding-top` 使得页脚上下 `padding` 对称。
```html
<footer class="aw-footer">
    <div class="aw-footer-copyright aw-footer-copyright-s">
        <ul>
            <li>&copy; 2020</li>
            <li><a href="#">About</a></li>
            <li><a href="#">License</a></li>
            <li><a href="#">Privacy</a></li>
        </ul>
    </div>
</footer>
```

<div class="aw-p">
    <footer class="aw-footer">
        <div class="aw-footer-copyright aw-footer-copyright-s">
            <ul>
                <li>&copy; 2020</li>
                <li><a href="#">About</a></li>
                <li><a href="#">License</a></li>
                <li><a href="#">Privacy</a></li>
            </ul>
        </div>
    </footer>
</div>

## 组合
```html
<footer class="aw-footer">
    <div class="aw-g aw-g-ie">
        <nav class="aw-g-w-1-2 aw-g-w-s-s-1 aw-g-ie-1">
            <h2>栏目 1</h2>
            <ul>
                <li><a href="#">NavItem 1</a></li>
                <li><a href="#">NavItem 2</a></li>
                <li><a href="#">NavItem 3</a></li>
            </ul>
        </nav>
        <nav class="aw-g-w-1-2 aw-g-w-s-s-1 aw-g-ie-5">
            <h2>栏目 2</h2>
            <ul>
                <li><a href="#">NavItem 1</a></li>
                <li><a href="#">NavItem 2</a></li>
                <li><a href="#">NavItem 3</a></li>
            </ul>
        </nav>
    </div>
    <div class="aw-footer-copyright aw-footer-copyright-s">
        <ul>
            <li>&copy; 2020</li>
            <li><a href="#">About</a></li>
            <li><a href="#">License</a></li>
            <li><a href="#">Privacy</a></li>
        </ul>
    </div>
</footer>
```
<div class="aw-p">
    <footer class="aw-footer">
        <div class="aw-g aw-g-ie">
            <nav class="aw-g-w-1-2 aw-g-w-s-s-1 aw-g-ie-1">
                <h2>栏目 1</h2>
                <ul>
                    <li><a href="#">NavItem 1</a></li>
                    <li><a href="#">NavItem 2</a></li>
                    <li><a href="#">NavItem 3</a></li>
                </ul>
            </nav>
            <nav class="aw-g-w-1-2 aw-g-w-s-s-1 aw-g-ie-5">
                <h2>栏目 2</h2>
                <ul>
                    <li><a href="#">NavItem 1</a></li>
                    <li><a href="#">NavItem 2</a></li>
                    <li><a href="#">NavItem 3</a></li>
                </ul>
            </nav>
        </div>
        <div class="aw-footer-copyright aw-footer-copyright-s">
            <ul>
                <li>&copy; 2020</li>
                <li><a href="#">About</a></li>
                <li><a href="#">License</a></li>
                <li><a href="#">Privacy</a></li>
            </ul>
        </div>
    </footer>
</div>