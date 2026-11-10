from pathlib import Path
import hashlib, html, re
root = Path(__file__).resolve().parent
source = root / 'lesson.md'
text = source.read_text()
blocks=[]
for paragraph in text.strip().split('\n\n'):
    if paragraph.startswith('<!--'): continue
    if paragraph.startswith('!['):
        m=re.fullmatch(r'!\[([^]]*)\]\(([^)]+)\)',paragraph)
        if not m: raise ValueError('Unexpected image markup')
        blocks.append('<img alt="'+html.escape(m[1],quote=True)+'" src="'+html.escape(m[2],quote=True)+'">')
    elif paragraph.startswith('# '): blocks.append('<h1>'+html.escape(paragraph[2:])+'</h1>')
    elif paragraph.startswith('## '): blocks.append('<h2>'+html.escape(paragraph[3:])+'</h2>')
    elif paragraph.startswith('> '): blocks.append('<aside>'+html.escape(paragraph[2:])+'</aside>')
    else: blocks.append('<p>'+html.escape(paragraph)+'</p>')
digest=hashlib.sha256(source.read_bytes()).hexdigest()
page='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="source-sha256" content="'+digest+'"><title>Markdown 与 HTML 的分工</title><style>body{max-width:48rem;margin:auto;padding:1.5rem;font:18px/1.8 system-ui;color:#182331;background:#fff}h1{font-size:2rem;line-height:1.3}h2{margin-top:2rem}img{max-width:100%;height:auto}aside{border-left:3px solid #0969da;padding-left:1rem}p{overflow-wrap:anywhere}</style><main>'+''.join(blocks)+'</main></html>'
(root/'lesson.html').write_text(page)
print('Built lesson.html from lesson.md; no network, model calls or JavaScript.')
