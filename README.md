This is an English to Chinese translation tool that accepts an srt file of subtitles in only English and adds translations (while preserving the English subtitles, indices, and timestamps as well)

To run the script as‐is, you’ll need:
1. Python 3.6 or newer; The #!/usr/bin/env python3 and f-strings require at least Python 3.6.
2. The googletrans library; I recommend the community-approved release candidate: bash: pip install googletrans==4.0.0-rc1

(Optional) A virtual environment to keep your dependencies isolated:
bash: python3 -m venv venv
	source venv/bin/activate     # on macOS/Linux
	venv\Scripts\activate.bat    # on Windows
  	pip install googletrans==4.0.0-rc1 

Everything else in the script—argparse, re, and pathlib—comes with Python’s standard library. Once you’ve got Python 3 and googletrans installed, the script should run without any further dependencies.

Bash line to run:
python3 generate_bilingual_srt.py \
  --input  "6月20日-采访C1.srt" \
  --output "6月20日-采访C1_bilingual_full.srt"

Wait until program outputs: “✔ Bilingual SRT saved to: 6月20日-采访C1_bilingual_full.srt”
