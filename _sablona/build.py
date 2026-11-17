#!/usr/bin/env python3
"""Usage: python3 _sablona/build.py <slug> <data.json>
Creates <slug>/index.html from _sablona/template.html and the JSON data."""
import json, sys, html, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
slug, data_path = sys.argv[1], sys.argv[2]
data = json.loads(pathlib.Path(data_path).read_text(encoding="utf-8"))

required = ["firma", "mesto", "headline", "lead", "widget", "services", "steps"]
missing = [k for k in required if not data.get(k)]
if missing:
    sys.exit(f"Chybí pole: {missing}")
if data.get("logo_url") and not data["logo_url"].startswith("https://"):
    data["logo_url"] = ""  # http obrázky prohlížeč na https stránce zablokuje

tpl = (root / "_sablona" / "template.html").read_text(encoding="utf-8")
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
title = html.escape(f"{data['firma']} – {data['mesto']} (návrh webu)")
out = tpl.replace("__TITLE__", title).replace("__DATA__", blob)
(root / slug).mkdir(exist_ok=True)
(root / slug / "index.html").write_text(out, encoding="utf-8")
(root / slug / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"OK {slug}/index.html")
