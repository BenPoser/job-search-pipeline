#!/usr/bin/env python3
"""Build an ATS-safe .docx from a JSON CV description.

Standard library only. A .docx is a zip of XML parts, and zipfile is built in.

    python3 scripts/build_docx.py out.docx < cv.json

Input JSON:

    {
      "name": "Jane Doe",
      "headline": "Service Manager",
      "contact": ["jane@example.com", "07700 900000", "Manchester"],
      "sections": [
        {"heading": "Summary", "paragraphs": ["..."]},
        {"heading": "Experience", "entries": [
            {"title": "Service Manager", "organisation": "Acme Trust",
             "dates": "Mar 2021 - Aug 2024", "location": "Manchester",
             "bullets": ["...", "..."]}
        ]},
        {"heading": "Skills", "paragraphs": ["..."]}
      ]
    }

Deliberately plain: single column, standard heading names, no tables, no text
boxes, no images, no headers or footers. Anything cleverer loses information
when an applicant tracking system parses the file.
"""

import json
import sys
import zipfile
from xml.sax.saxutils import escape

W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'


def para(text="", style=None, bold=False, size=None, space_after=0):
    """One paragraph. size is in half-points, Word's unit."""
    props = []
    if style:
        props.append(f'<w:pStyle w:val="{style}"/>')
    props.append(f'<w:spacing w:after="{space_after}"/>')
    ppr = f"<w:pPr>{''.join(props)}</w:pPr>"

    if not text:
        return f"<w:p>{ppr}</w:p>"

    rprops = []
    if bold:
        rprops.append("<w:b/>")
    if size:
        rprops.append(f'<w:sz w:val="{size}"/>')
    rpr = f"<w:rPr>{''.join(rprops)}</w:rPr>" if rprops else ""
    return f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'


def bullet(text):
    return (
        '<w:p><w:pPr><w:pStyle w:val="ListParagraph"/>'
        '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
        '<w:spacing w:after="40"/></w:pPr>'
        f'<w:r><w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>'
    )


def build_body(cv):
    out = []

    out.append(para(cv.get("name", ""), style="Heading1", size=36, space_after=40))
    if cv.get("headline"):
        out.append(para(cv["headline"], size=24, space_after=40))
    if cv.get("contact"):
        # One line, pipe separated. Parsers cope with this; multi-column does not.
        out.append(para(" | ".join(cv["contact"]), size=20, space_after=200))

    for section in cv.get("sections", []):
        out.append(para(section["heading"], style="Heading2", bold=True, size=26,
                        space_after=80))

        for text in section.get("paragraphs", []):
            out.append(para(text, size=20, space_after=120))

        for entry in section.get("entries", []):
            title_bits = [b for b in (entry.get("title"), entry.get("organisation")) if b]
            out.append(para(", ".join(title_bits), bold=True, size=22, space_after=0))

            meta = [b for b in (entry.get("dates"), entry.get("location")) if b]
            if meta:
                out.append(para(" | ".join(meta), size=18, space_after=60))

            for b in entry.get("bullets", []):
                out.append(bullet(b))

            out.append(para(space_after=100))

    return "".join(out)


STYLES = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles {W}>
  <w:docDefaults><w:rPrDefault><w:rPr>
    <w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="20"/>
  </w:rPr></w:rPrDefault></w:docDefaults>
  <w:style w:type="paragraph" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/>
    <w:pPr><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:sz w:val="36"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/>
    <w:pPr><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:b/><w:sz w:val="26"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="ListParagraph">
    <w:name w:val="List Paragraph"/></w:style>
</w:styles>"""

NUMBERING = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering {W}>
  <w:abstractNum w:abstractNumId="0"><w:lvl w:ilvl="0">
    <w:numFmt w:val="bullet"/><w:lvlText w:val="&#8226;"/>
    <w:pPr><w:ind w:left="360" w:hanging="360"/></w:pPr>
  </w:lvl></w:abstractNum>
  <w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>"""

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
</Relationships>"""


def build(cv, path):
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f"<w:document {W}><w:body>{build_body(cv)}"
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134"/>'
        "</w:sectPr></w:body></w:document>"
    )

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/document.xml", document)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/numbering.xml", NUMBERING)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: build_docx.py <output.docx>  (JSON on stdin)")
    build(json.load(sys.stdin), sys.argv[1])
    print(f"wrote {sys.argv[1]}")
