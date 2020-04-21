# 背景颜色
背景颜色在支持 CSS 变量的浏览器上，由颜色变量确定；在不支持 CSS 变量的浏览器上，使用该颜色变量的默认值。详见：[全局默认值：颜色](global.html)。

为元素添加 `aw-bg-*` 类来设置其背景颜色。以下是背景颜色的预览、默认值和与其相关的变量值。如下图，第一行为类名，第二行为默认变量，第三行为在不支持 CSS 变量的浏览器上的默认值。

“按钮”和“提示框”依赖于“背景颜色”。

注：字体颜色需要另外自行设置。`aw-bg-white` 的 Demo 加上了黑色边框，以便演示，实际上并没有边框。

<style>
.demo { display: inline-block; padding: .5em; text-align: center; color: white; margin-bottom: 1em; width: 12em; }
</style>
<div class="aw-p">
    <div class="demo aw-bg-green">
        aw-bg-green<br>
        --aw-color-green<br>
        #498205
    </div>
    <div class="demo aw-bg-red">
        aw-bg-red<br>
        --aw-color-red<br>
        #a4262c
    </div>
    <div class="demo aw-bg-yellow" style="color: black;">
        aw-bg-yellow<br>
        --aw-color-yellow-light<br>
        #ffd56c
    </div>
    <div class="demo aw-bg-orange">
        aw-bg-orange<br>
        --aw-color-orange<br>
        #ca5010
    </div>
    <div class="demo aw-bg-blue">
        aw-bg-blue<br>
        --aw-color-blue-light<br>
        #0078d4
    </div>
    <div class="demo aw-bg-lightblue">
        aw-bg-lightblue<br>
        --aw-color-luotianyi<br>
        #66ccff
    </div>
    <div class="demo aw-bg-cyan">
        aw-bg-cyan<br>
        --aw-color-miku<br>
        #39c5bb
    </div>
    <div class="demo aw-bg-white" style="color: black;border: .5px solid black;">
        aw-bg-white<br>
        --aw-color-gray-9<br>
        #ffffff
    </div>
    <div class="demo aw-bg-gray" style="color: black;">
        aw-bg-gray<br>
        --aw-color-gray-6<br>
        #dddddd
    </div>
</div>
