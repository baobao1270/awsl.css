# -*- coding: UTF-8 -*-
import markdown, os, json, shutil, rcssmin, htmlmin

root_dir = os.path.split(os.path.realpath(__file__))[0]
with open(root_dir + '/doc-src/_index.json', encoding='utf-8') as f:
    index_json = json.loads(f.read())

menu_html = ''
for doc_info in index_json:
    (slug, title), = doc_info.items()
    menu_html += '<li><a href="{}.html">{}</a></li>'.format(slug, title)

with open(root_dir + '/doc-src/_layout.html', encoding='utf-8') as f:
    layout = f.read()

with open(root_dir + '/doc-src/_inline.css', encoding='utf-8') as f:
    css_inline = rcssmin.cssmin(f.read())
    css_inline = '<style>' + css_inline + '</style>'

if not os.path.exists(root_dir + '/docs'):
    os.makedirs(root_dir + '/docs')

for doc_info in index_json:    
    (slug, title), = doc_info.items()
    if not (os.path.exists(root_dir + '/doc-src/' + slug + '.md')):
        print('Skipping: ' + slug + '.md')
        continue
    print('Rending: ' + slug + '.md')
    output = layout.replace('\r', '').replace('\n', '')
    output = output.replace('<insert-title></insert-title>', title)
    output = output.replace('<insert-index></insert-index>', menu_html)
    output = output.replace('<insert-style></insert-style>', css_inline)
    with open(root_dir + '/doc-src/' + slug + '.md', encoding='utf-8') as f:
        md_str = markdown.markdown(f.read(), extensions=['fenced_code', 'tables', 'codehilite'])
        output = output.replace('<insert-markdown></insert-markdown>', md_str)
        output = htmlmin.minify(output, remove_empty_space=True, keep_pre=True)
        output = '<!DOCTYPE html>' + output
        with open(root_dir + '/docs/' + slug + '.html', 'w+', encoding='utf-8') as outf:
            outf.write(output)

print('Builing and copying: awsl.min.css')
with open('awsl.css', 'r') as inf:
    raw = inf.read()
    copyright = raw[0:raw.find('**/') + 3] + '\n'
    copyright = copyright.replace('\r', '')
    out = rcssmin.cssmin(raw)
    with open('awsl.min.css', 'w+') as outf:
        outf.write(copyright + out)

shutil.copyfile(root_dir + '/awsl.min.css', root_dir + '/docs/awsl.min.css')
print('Builing and copying: codehilite.css')
shutil.copyfile(root_dir + '/doc-src/_codehilite.css', root_dir + '/docs/codehilite.css')
shutil.copyfile(root_dir + '/icon.ico', root_dir + '/docs/favicon.ico')
