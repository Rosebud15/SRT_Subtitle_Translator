#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import re
from pathlib import Path
from googletrans import Translator

def parse_srt(text: str):
    # Split on blank lines to get each block
    raw_entries = re.split(r'\n{2,}', text.strip())
    entries = []
    for entry in raw_entries:
        lines = entry.splitlines()
        idx       = lines[0]
        timestamp = lines[1]
        content   = ' '.join(lines[2:])  # collapse multi-line into one
        entries.append((idx, timestamp, content))
    return entries

def main(input_path, output_path):
    txt = Path(input_path).read_text(encoding='utf-8')
    entries = parse_srt(txt)

    translator = Translator()
    out_blocks = []
    for idx, ts, en_text in entries:
        # translate
        zh_text = translator.translate(en_text, src='en', dest='zh-cn').text
        # build bilingual block
        block = f"{idx}\n{ts}\n{en_text}\n{zh_text}"
        out_blocks.append(block)

    # write result
    Path(output_path).write_text("\n\n".join(out_blocks), encoding='utf-8')
    print(f"✔ Bilingual SRT saved to: {output_path}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate English+Chinese SRT via googletrans")
    p.add_argument("--input",  "-i", required=True, help="Path to original .srt")
    p.add_argument("--output", "-o", required=True, help="Path for bilingual .srt")
    args = p.parse_args()
    main(args.input, args.output)