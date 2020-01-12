import re
from collections import namedtuple

# setup begin
Markdown_sub = namedtuple('Markdown_sub', 'pattern tags')

# substitutions must be checked in the following order
MD_SUBS = [
    Markdown_sub(pattern='^###### (.*)', tags=('h6',)),
    Markdown_sub(pattern='^##### (.*)', tags=('h5',)),
    Markdown_sub(pattern='^#### (.*)', tags=('h4',)),
    Markdown_sub(pattern='^### (.*)', tags=('h3',)),
    Markdown_sub(pattern='^## (.*)', tags=('h2',)),
    Markdown_sub(pattern='^# (.*)', tags=('h1',)),
    Markdown_sub(pattern='___(.*?)___', tags=('strong', 'em')),
    Markdown_sub(pattern='__(.*?)__', tags=('strong',)),
    Markdown_sub(pattern='_(.*?)_', tags=('em',)),
    Markdown_sub(pattern='`(.*?)`', tags=('code',)),
    Markdown_sub(pattern=r'^\* (.*)', tags=('ul', 'li')),
    Markdown_sub(pattern='^(?!<h|<ul|<p|<li)(.*)', tags=('p',)),
    ]
#setup end


def parse(markdown):
    '''
    Parse a given string with selected Markdown syntax and return the 
    associated HTML for that string.
    '''
    lines = markdown.splitlines()
    new_lines=[]
    for line in lines:
        for md_sub in MD_SUBS:
            line = re.sub(md_sub.pattern,
                          lambda line: surround_with_tags(line, md_sub.tags),
                          line, count=0)
        new_lines.append(line)

    res = "".join(new_lines)
    # post-processing fix for interior <ul>s
    res = res.replace('</ul><ul>', '')
    return res

def surround_with_tags(matchobj, tags):
    tags_open = ''.join(f'<{tag}>' for tag in tags)
    tags_close = ''.join(f'</{tag}>' for tag in reversed(tags))
    return f'{tags_open}{matchobj[1]}{tags_close}'
