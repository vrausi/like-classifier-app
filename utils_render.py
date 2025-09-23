# utils_render.py
import re
import html

def render_html(md_text: str, cls: str) -> str:
    """
    Escape user text, apply minimal markdown (links, inline code, bold, italics, underline),
    and wrap the result in a <div class="{cls}"> … </div>.
    """
    t = html.escape(md_text or "")

    # [text](https://link)
    t = re.sub(
        r'\[([^\]]+)\]\((https?://[^)]+)\)',
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        t,
        flags=re.S,
    )

    # `code`
    t = re.sub(r'`(.+?)`', r'<code>\1</code>', t, flags=re.S)

    # ++underline++
    t = re.sub(r'\+\+(.+?)\+\+', r'<u>\1</u>', t, flags=re.S)

    # **bold**
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t, flags=re.S)

    # _italics_  (avoid __underscores__ cases)
    t = re.sub(r'(?<!_)_(?!_)(.+?)(?<!_)_(?!_)', r'<em>\1</em>', t, flags=re.S)

    # Newlines → <br>
    t = t.replace("\n", "<br>")

    return f"<div class='{cls}'>" + t + "</div>"
