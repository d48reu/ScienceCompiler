from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess

ROOT = Path('/home/d48reu/science-compiler')
OUTDIR = ROOT / 'hackathon' / 'demo_video_original'
SLIDES = OUTDIR / 'slides'
OUTDIR.mkdir(parents=True, exist_ok=True)
SLIDES.mkdir(parents=True, exist_ok=True)

W, H = 1280, 720
BG = (17, 20, 26)
PANEL = (25, 29, 38)
TEXT = (235, 239, 244)
MUTED = (160, 174, 192)
ACCENT = (94, 234, 212)
ACCENT2 = (255, 184, 108)
RED = (255, 107, 107)
GREEN = (80, 250, 123)
BORDER = (63, 72, 87)

FONT_PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
TITLE_FONT = ImageFont.truetype(FONT_PATH, 42)
SUB_FONT = ImageFont.truetype(FONT_PATH, 24)
BODY_FONT = ImageFont.truetype(FONT_PATH, 22)
SMALL_FONT = ImageFont.truetype(FONT_PATH, 18)

slides = [
    {
        'name': '01_title',
        'duration': 6,
        'title': 'Science Compiler',
        'subtitle': 'AI as a scientific instrument, not a paper summarizer',
        'body': [
            ('Built for the Nous Research hackathon', ACCENT),
            ('Turns literature into claims, contradictions, weighted evidence,', TEXT),
            ('and experiment ideas.', TEXT),
        ],
        'footer': 'Raw papers -> structured scientific tension',
    },
    {
        'name': '02_problem',
        'duration': 7,
        'title': 'What problem are we solving?',
        'subtitle': 'Most AI-for-science tools flatten disagreement into summaries.',
        'body': [
            ('Bad output:', RED),
            ('  "The literature is mixed and context-dependent."', MUTED),
            ('', TEXT),
            ('Better output:', GREEN),
            ('  exact contradiction clusters', TEXT),
            ('  weighted evidence balance', TEXT),
            ('  candidate moderators', TEXT),
            ('  decisive follow-up experiments', TEXT),
        ],
        'footer': 'We want computable science, not vibes.',
    },
    {
        'name': '03_pipeline',
        'duration': 8,
        'title': 'Pipeline',
        'subtitle': 'Everything runs locally-first.',
        'body': [
            ('raw paper text', ACCENT),
            ('  -> first-pass extraction', TEXT),
            ('  -> second-pass refinement', TEXT),
            ('  -> curation / ranking', TEXT),
            ('  -> ontology / canonicalization', TEXT),
            ('  -> evidence weighting', TEXT),
            ('  -> contradiction + tradeoff analysis', TEXT),
            ('  -> review queue for human correction', TEXT),
        ],
        'footer': '/home/d48reu/science-compiler',
    },
    {
        'name': '04_butyrate_setup',
        'duration': 7,
        'title': 'Domain 1: butyrate / neuroinflammation',
        'subtitle': 'Question: when does butyrate help, and when might it worsen things?',
        'body': [
            ('Gold corpus:', ACCENT2),
            ('  14 curated claims', TEXT),
            ('  6 contradiction pairs', TEXT),
            ('  disease-family split', TEXT),
            ('', TEXT),
            ('Best current read:', GREEN),
            ('  mostly anti-neuroinflammatory outside parkinsonian context', TEXT),
            ('  but one MPTP Parkinson paper flips the sign', TEXT),
        ],
        'footer': 'compiler_report_gold.md',
    },
    {
        'name': '05_butyrate_results',
        'duration': 9,
        'title': 'Butyrate result',
        'subtitle': 'The family split is the point.',
        'body': [
            ('direct butyrate | alcohol_related | neuroinflammation  -> decrease  (+10.10)', GREEN),
            ('direct butyrate | alzheimer_related | neuroinflammation -> decrease  (+4.70)', GREEN),
            ('direct butyrate | acute_injury | neuroinflammation     -> decrease  (+4.20)', GREEN),
            ('direct butyrate | gut_inflammation | neuroinflammation -> decrease  (+5.50)', GREEN),
            ('direct butyrate | toxic_exposure | neuroinflammation   -> decrease  (+4.60)', GREEN),
            ('', TEXT),
            ('direct butyrate | parkinsonian | neuroinflammation    -> increase  (-5.70)', RED),
        ],
        'footer': 'Not universal benefit. Context-dependent effect heterogeneity.',
    },
    {
        'name': '06_butyrate_contradiction',
        'duration': 8,
        'title': 'What the compiler surfaces',
        'subtitle': 'A real contradiction cluster, not a fake average.',
        'body': [
            ('Negative anchor:', RED),
            ('  PMID 32556930  | MPTP Parkinson model', TEXT),
            ('', TEXT),
            ('Positive anchors:', GREEN),
            ('  PMID 33785315  | 5XFAD Alzheimer', TEXT),
            ('  PMID 36555338  | binge ethanol', TEXT),
            ('  PMID 36709599  | chronic alcohol', TEXT),
            ('  PMID 37665564  | DSS gut-brain spillover', TEXT),
            ('  PMID 38340407  | lead neurotoxicity', TEXT),
            ('  PMID 39962509  | cardiac arrest', TEXT),
        ],
        'footer': 'Better question: why does the sign flip in parkinsonian context?',
    },
    {
        'name': '07_senolytics',
        'duration': 8,
        'title': 'Domain 2: senolytics / aging',
        'subtitle': 'Generalization test: a different scientific structure emerges.',
        'body': [
            ('Not one clean contradiction — a tradeoff map.', ACCENT),
            ('', TEXT),
            ('Positive side:', GREEN),
            ('  D+Q improves function/lifespan/disc degeneration in some contexts', TEXT),
            ('  fisetin improves lifespan and vascular function', TEXT),
            ('', TEXT),
            ('Caution side:', RED),
            ('  navitoclax harms bone', TEXT),
            ('  D+Q fails in influenza and may worsen some liver contexts', TEXT),
            ('  D+Q can be detrimental in females in one study', TEXT),
        ],
        'footer': 'Different domain, different structure: tradeoffs instead of one sign-flip cluster.',
    },
    {
        'name': '08_why_it_matters',
        'duration': 7,
        'title': 'Why this matters',
        'subtitle': 'This is AI infrastructure for scientific reasoning.',
        'body': [
            ('Science Compiler helps researchers:', ACCENT2),
            ('  preserve disagreement instead of erasing it', TEXT),
            ('  compare rival mechanistic stories', TEXT),
            ('  compute over literature, not just read it', TEXT),
            ('  generate sharper next experiments', TEXT),
            ('', TEXT),
            ('It does not replace experts.', MUTED),
            ('It makes scientific tension legible.', TEXT),
        ],
        'footer': 'Science Compiler turns papers from things you read into things you can compute over.',
    },
    {
        'name': '09_close',
        'duration': 6,
        'title': 'Science Compiler',
        'subtitle': 'Hackathon demo complete',
        'body': [
            ('Two domains.', ACCENT),
            ('Two different scientific structures.', ACCENT),
            ('One reusable literature-compilation workflow.', TEXT),
        ],
        'footer': '@NousResearch hackathon submission',
    },
]


def draw_terminal_slide(spec: dict, idx: int) -> Path:
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)

    margin = 48
    panel_x0, panel_y0 = 40, 36
    panel_x1, panel_y1 = W - 40, H - 36
    d.rounded_rectangle((panel_x0, panel_y0, panel_x1, panel_y1), radius=18, fill=PANEL, outline=BORDER, width=2)

    topbar_h = 42
    d.rounded_rectangle((panel_x0, panel_y0, panel_x1, panel_y0 + topbar_h), radius=18, fill=(33, 38, 48))
    d.rectangle((panel_x0, panel_y0 + topbar_h - 18, panel_x1, panel_y0 + topbar_h), fill=(33, 38, 48))
    for i, color in enumerate([(255,95,86), (255,189,46), (39,201,63)]):
        cx = panel_x0 + 22 + i * 20
        cy = panel_y0 + 21
        d.ellipse((cx-6, cy-6, cx+6, cy+6), fill=color)
    d.text((panel_x0 + 90, panel_y0 + 10), f' science_compiler_demo_{idx:02d}.md ', font=SMALL_FONT, fill=MUTED)

    y = panel_y0 + 70
    d.text((margin + 10, y), spec['title'], font=TITLE_FONT, fill=TEXT)
    y += 58
    d.text((margin + 12, y), spec['subtitle'], font=SUB_FONT, fill=ACCENT)
    y += 52

    for line, color in spec['body']:
        if line == '':
            y += 18
            continue
        d.text((margin + 16, y), line, font=BODY_FONT, fill=color)
        y += 34

    footer_y = panel_y1 - 48
    d.line((margin + 8, footer_y - 18, W - margin - 8, footer_y - 18), fill=BORDER, width=1)
    d.text((margin + 12, footer_y), spec['footer'], font=SMALL_FONT, fill=MUTED)

    path = SLIDES / f"{idx:02d}_{spec['name']}.png"
    img.save(path)
    return path


def build_ffmpeg_concat(slide_paths: list[Path]) -> Path:
    concat_path = OUTDIR / 'slides.txt'
    lines = []
    for slide, spec in zip(slide_paths, slides):
        lines.append(f"file '{slide}'")
        lines.append(f"duration {spec['duration']}")
    lines.append(f"file '{slide_paths[-1]}'")
    concat_path.write_text('\n'.join(lines) + '\n')
    return concat_path


def main() -> None:
    slide_paths = [draw_terminal_slide(spec, i + 1) for i, spec in enumerate(slides)]
    concat_path = build_ffmpeg_concat(slide_paths)
    out_video = ROOT / 'hackathon' / 'science_compiler_nous_demo_original_visuals.mp4'

    cmd = [
        'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', str(concat_path),
        '-vf', 'fps=24,format=yuv420p',
        '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
        str(out_video)
    ]
    subprocess.run(cmd, check=True)
    print(out_video)


if __name__ == '__main__':
    main()
