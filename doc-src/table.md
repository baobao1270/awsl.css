# 表格
为 `table` 元素加入 `aw-table` 类使其应用表格样式。

```html
<table class="aw-table">
    <thead>
        <tr>
            <th>Header</th>
            <th>Header</th>
            <th>Header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Data</td>
            <td>Data</td>
            <td>Data</td>
        </tr>
        <tr>
            <td>Data</td>
            <td>Data</td>
            <td>Data</td>
        </tr>
        <tr>
            <td>Data</td>
            <td>Data</td>
            <td>Data</td>
        </tr>
    </tbody>
</table>
```

<div class="aw-p">
    <table class="aw-table">
        <thead>
            <tr>
                <th>Header</th>
                <th>Header</th>
                <th>Header</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Data</td>
                <td>Data</td>
                <td>Data</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Data</td>
                <td>Data</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Data</td>
                <td>Data</td>
            </tr>
        </tbody>
    </table>
</div>

## 定列宽表格
表格在使用 `aw-table` 类的基础上，加上 `aw-table-fixed` 使其能够固定列宽（您需要自己设置列宽）。
```html
<table class="aw-table aw-table-fixed">
    <thead>
        <tr>
            <th style="width: 50px;">Header</th>
            <th style="width: 100px;">Header</th>
            <th style="width: 150px;">Header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Data</td>
            <td>Data</td>
            <td>Data</td>
        </tr>
        <tr>
            <td>Data</td>
            <td>Data</td>
            <td>Data</td>
        </tr>
        <tr>
            <td>Data</td>
            <td>Data</td>
            <td>Data</td>
        </tr>
    </tbody>
</table>
```

<div class="aw-p">
    <table class="aw-table">
        <thead>
            <tr>
                <th style="width: 150px;">Header</th>
                <th style="width: 150px;">Header</th>
                <th style="width: 150px;">Header</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Data</td>
                <td>Data</td>
                <td>Data</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Data</td>
                <td>Data</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Data</td>
                <td>Data</td>
            </tr>
        </tbody>
    </table>
</div>

## 横向自动滚动条
如 [辅助类：横向自动滚动条](utils.html) 所述，为 `aw-table` 的父容器添加 `aw-scoll-x` 类，使其超过宽度时自动出现横向滚动条。

```html
<div class="aw-scoll-x">
    <table class="aw-table">
        <thead>
            <tr>
                <th>A Loooooooooooooooooooooooooooong Header</th>
                <th>Super Looo...ooong Header</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Data</td>
                <td>Data</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Data</td>
            </tr>
            <tr>
                <td>Data</td>
                <td>Data</td>
            </tr>
        </tbody>
    </table>
</div>
```

<div class="aw-p">
    <div class="aw-scoll-x">
        <table class="aw-table">
            <thead>
                <tr>
                    <th>A Loooooooooooooooooooooooooooong Header</th>
                    <th>Super Loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Header</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Data</td>
                    <td>Data</td>
                </tr>
                <tr>
                    <td>Data</td>
                    <td>Data</td>
                </tr>
                <tr>
                    <td>Data</td>
                    <td>Data</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
