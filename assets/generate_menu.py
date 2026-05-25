from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate,
                                 Table, TableStyle, Paragraph, Spacer, FrameBreak, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUTPUT = "C:/Users/inzra/OneDrive/Documents/GitHub/salon-uae/assets/Fade_and_Blade_Menu_Card_Print.pdf"

GOLD   = colors.HexColor("#B8960C")
BLACK  = colors.HexColor("#1A1A1A")
WHITE  = colors.white
DARK   = colors.HexColor("#111111")
LGREY  = colors.HexColor("#F5F5F0")
BGOLD  = colors.HexColor("#D4AF37")

styles = getSampleStyleSheet()

title_style = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=28,
                              textColor=WHITE, alignment=TA_CENTER, spaceAfter=2)
subtitle_style = ParagraphStyle("subtitle", fontName="Helvetica", fontSize=11,
                                 textColor=BGOLD, alignment=TA_CENTER, spaceAfter=4)
cat_style = ParagraphStyle("cat", fontName="Helvetica-Bold", fontSize=10,
                            textColor=WHITE, alignment=TA_CENTER)
svc_style = ParagraphStyle("svc", fontName="Helvetica", fontSize=8.5,
                            textColor=BLACK, leading=11)
dur_style = ParagraphStyle("dur", fontName="Helvetica", fontSize=8,
                            textColor=colors.HexColor("#555555"), alignment=TA_CENTER, leading=11)
price_style = ParagraphStyle("price", fontName="Helvetica-Bold", fontSize=9,
                              textColor=GOLD, alignment=TA_CENTER, leading=11)
footer_style = ParagraphStyle("footer", fontName="Helvetica-Oblique", fontSize=9,
                               textColor=WHITE, alignment=TA_CENTER)
note_style = ParagraphStyle("note", fontName="Helvetica", fontSize=7.5,
                             textColor=colors.HexColor("#888888"), alignment=TA_CENTER)

# ── data ────────────────────────────────────────────────────────────────────
SECTIONS = [
    {
        "title": "SIGNATURE HAIR",
        "cols": 2,
        "rows": [
            ("Haircut",                          "30 min",  "AED 120"),
            ("Haircut – Skin Fade",              "45 min",  "AED 140"),
            ("Hairstyling",                      "20 min",  "AED 75"),
            ("Toppik Hairstyling",               "20 min",  "AED 100"),
            ("Kidz Haircut (up to 12 yrs)",      "30 min",  "AED 80"),
            ("Head Clean Shave (Razor)",         "30 min",  "AED 100"),
            ("Snapshot Scalp Hair Treatment",    "15 min",  "AED 100"),
            ("Keratin Treatment – S/M  (1–12\")", "90 min", "AED 350"),
            ("Keratin Treatment – L  (12–16\")",  "120 min","AED 450"),
            ("Keratin Treatment – XL (16\"+)",    "180 min","AED 850"),
        ],
    },
    {
        "title": "BEARD GROOMING",
        "cols": 2,
        "rows": [
            ("Beard Clean Shave (Razor)",  "30 min", "AED 75"),
            ("Signature Clean Shave",      "45 min", "AED 100"),
            ("Beard Shaping",              "30 min", "AED 60"),
            ("Signature Beard",            "45 min", "AED 100"),
        ],
    },
    {
        "title": "COLOUR TREATMENTS",
        "cols": 2,
        "rows": [
            ("Hair Dye",                        "50 min",  "AED 160"),
            ("Beard Dye",                       "30 min",  "AED 100"),
            ("Fashion Colour",                  "240 min", "AED 500"),
            ("Snapshot Scalp Hair Treatment",   "15 min",  "AED 100"),
        ],
    },
    {
        "title": "FACIAL TREATMENTS",
        "cols": 2,
        "rows": [
            ("Face Cleansing",              "30 min", "AED 120"),
            ("Facial DeTan",                "45 min", "AED 160"),
            ("Signature Facial Treatment",  "60 min", "AED 200"),
            ("Charcoal Mask",               "20 min", "AED 50"),
            ("Casmara / Peel Off Mask",     "30 min", "AED 95"),
        ],
    },
    {
        "title": "WAXING & SPA",
        "cols": 2,
        "rows": [
            ("Ear Wax",                          "10 min", "AED 30"),
            ("Nose Wax",                         "10 min", "AED 30"),
            ("Ear & Nose Wax",                   "20 min", "AED 50"),
            ("Full Face Wax",                    "30 min", "AED 80"),
            ("Chest Wax",                        "30 min", "AED 100"),
            ("Back Wax",                         "30 min", "AED 100"),
            ("Back & Chest Wax",                 "50 min", "AED 175"),
            ("Chest Trimming",                   "15 min", "AED 50"),
            ("Back Trimming",                    "15 min", "AED 50"),
            ("Arms Wax",                         "30 min", "AED 99"),
            ("Under Arms Wax",                   "15 min", "AED 50"),
            ("Full Upper Body Wax",              "90 min", "AED 250"),
            ("Full Face Threading",              "20 min", "AED 60"),
            ("Eyebrow Shape Up",                 "15 min", "AED 30"),
            ("Head, Neck & Shoulder Massage",    "20 min", "AED 60"),
            ("Blackhead Removal Strips",         "10 min", "AED 20"),
        ],
    },
    {
        "title": "HAND & FOOT CARE",
        "cols": 2,
        "rows": [
            ("Manicure",                "30 min", "AED 90"),
            ("Pedicure",                "30 min", "AED 110"),
            ("Manicure & Pedicure",     "60 min", "AED 160"),
            ("Nails Express (Trim)",    "30 min", "AED 90"),
            ("Foot Massage",            "15 min", "AED 45"),
        ],
    },
    {
        "title": "SIGNATURE PACKAGES",
        "cols": 1,
        "rows": [
            ("4x Haircut / Skin Fade + 4x Signature Beard  (30-Day Rolling)",          "", "AED 800"),
            ("2x Manicure & Pedicure  (30-Day Rolling)",                                "", "AED 280"),
            ("1,000 AED Prepay Credit  +200 AED Bonus  (3 Months Validity)",          "", "AED 1,000"),
            ("2,000 AED Prepay Credit  +600 AED Bonus  (6 Months Validity)",          "", "AED 2,000"),
        ],
    },
]

# ── helpers ──────────────────────────────────────────────────────────────────

def make_section_table(section, page_width):
    """Build a ReportLab Table for one section."""
    col_count = section["cols"]
    rows = section["rows"]

    # Header row spans full width
    header_para = Paragraph(section["title"], cat_style)

    # Determine column widths  (service | duration | price) repeated col_count times
    # With 2 columns: [svc, dur, price, svc, dur, price]
    available = page_width - 20 * mm
    if col_count == 2:
        col_widths = [available * 0.33, available * 0.10, available * 0.10,
                      available * 0.33, available * 0.10, available * 0.10]
        n_cols = 6
    else:
        col_widths = [available * 0.68, available * 0.16, available * 0.16]
        n_cols = 3

    # Sub-header
    if col_count == 2:
        sub = [Paragraph("Service", dur_style), Paragraph("Duration", dur_style),
               Paragraph("Price", dur_style),
               Paragraph("Service", dur_style), Paragraph("Duration", dur_style),
               Paragraph("Price", dur_style)]
    else:
        sub = [Paragraph("Service / Package", dur_style),
               Paragraph("Duration", dur_style),
               Paragraph("Price", dur_style)]

    data = []
    # header spanning all cols
    data.append([header_para] + [""] * (n_cols - 1))
    data.append(sub)

    if col_count == 2:
        # pair rows side by side
        pairs = [rows[i:i+2] for i in range(0, len(rows), 2)]
        for pair in pairs:
            left  = pair[0] if len(pair) > 0 else ("", "", "")
            right = pair[1] if len(pair) > 1 else ("", "", "")
            row = [Paragraph(left[0],  svc_style),
                   Paragraph(left[1],  dur_style),
                   Paragraph(left[2],  price_style),
                   Paragraph(right[0], svc_style),
                   Paragraph(right[1], dur_style),
                   Paragraph(right[2], price_style)]
            data.append(row)
    else:
        for r in rows:
            data.append([Paragraph(r[0], svc_style),
                         Paragraph(r[1], dur_style),
                         Paragraph(r[2], price_style)])

    tbl = Table(data, colWidths=col_widths, repeatRows=0)

    n_rows = len(data)
    style_cmds = [
        # Header row
        ("BACKGROUND",   (0, 0), (-1, 0), DARK),
        ("SPAN",         (0, 0), (-1, 0)),
        ("ALIGN",        (0, 0), (-1, 0), "CENTER"),
        ("TOPPADDING",   (0, 0), (-1, 0), 5),
        ("BOTTOMPADDING",(0, 0), (-1, 0), 5),
        # Sub-header
        ("BACKGROUND",   (0, 1), (-1, 1), colors.HexColor("#2A2A2A")),
        ("FONTNAME",     (0, 1), (-1, 1), "Helvetica-Bold"),
        ("FONTSIZE",     (0, 1), (-1, 1), 7.5),
        ("TEXTCOLOR",    (0, 1), (-1, 1), BGOLD),
        ("ALIGN",        (0, 1), (-1, 1), "CENTER"),
        ("TOPPADDING",   (0, 1), (-1, 1), 3),
        ("BOTTOMPADDING",(0, 1), (-1, 1), 3),
        # Data rows alternating
        ("ROWBACKGROUNDS", (0, 2), (-1, -1), [WHITE, LGREY]),
        ("ALIGN",        (1, 2), (1, -1), "CENTER"),
        ("ALIGN",        (2, 2), (2, -1), "CENTER"),
        ("TOPPADDING",   (0, 2), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 2), (-1, -1), 4),
        ("LEFTPADDING",  (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("GRID",         (0, 1), (-1, -1), 0.3, colors.HexColor("#DDDDDD")),
        ("LINEBELOW",    (0, 0), (-1, 0), 1.5, GOLD),
    ]
    if col_count == 2:
        # Vertical divider between left & right halves
        style_cmds += [
            ("ALIGN", (4, 2), (4, -1), "CENTER"),
            ("ALIGN", (5, 2), (5, -1), "CENTER"),
            ("LINEAFTER", (2, 1), (2, -1), 1.2, GOLD),
        ]
    tbl.setStyle(TableStyle(style_cmds))
    return tbl


def make_header_table(page_width):
    """Full-width title banner."""
    data = [
        [Paragraph("FADE &amp; BLADE — PRICE MENU", title_style)],
        [Paragraph("Premium Gents Grooming · Dubai  |  Tel: 058 588 7245  |  @fadeandbladedxb", subtitle_style)],
    ]
    tbl = Table(data, colWidths=[page_width])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LINEBELOW",     (0, -1), (-1, -1), 2, GOLD),
    ]))
    return tbl


def make_footer_table(page_width):
    data = [[Paragraph(
        "Thank you for choosing Fade &amp; Blade Gents Salon  ·  All prices in UAE Dirhams (AED)  ·  Prices subject to change without prior notice",
        footer_style)]]
    tbl = Table(data, colWidths=[page_width])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), DARK),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LINEABOVE",     (0, 0), (-1, 0), 2, GOLD),
    ]))
    return tbl


def build_pdf():
    page_size = landscape(A4)
    PW, PH = page_size
    margin = 10 * mm
    col_gap = 5 * mm
    full_w = PW - 2 * margin
    half_w = (full_w - col_gap) / 2

    # Header/footer heights (approximate)
    hdr_h = 22 * mm
    ftr_h = 12 * mm
    body_h = PH - 2 * margin - hdr_h - ftr_h - 4 * mm   # usable body height

    # ── Page templates ────────────────────────────────────────────────────
    # One-column header/footer frame (full width) + two body frames
    def make_frames(top_y):
        """Return [left_frame, right_frame] starting at top_y from bottom."""
        left = Frame(margin, margin + ftr_h + 2 * mm,
                     half_w, body_h, leftPadding=0, rightPadding=2*mm,
                     topPadding=0, bottomPadding=0, id="left")
        right = Frame(margin + half_w + col_gap, margin + ftr_h + 2 * mm,
                      half_w, body_h, leftPadding=2*mm, rightPadding=0,
                      topPadding=0, bottomPadding=0, id="right")
        hdr_frame = Frame(margin, PH - margin - hdr_h,
                          full_w, hdr_h, leftPadding=0, rightPadding=0,
                          topPadding=0, bottomPadding=0, id="header")
        ftr_frame = Frame(margin, margin,
                          full_w, ftr_h, leftPadding=0, rightPadding=0,
                          topPadding=0, bottomPadding=0, id="footer")
        return [hdr_frame, left, right, ftr_frame]

    def on_page(canvas, doc):
        pass  # header/footer included in story via FrameBreak

    frames = make_frames(PH - margin - hdr_h)
    pt = PageTemplate(id="main", frames=frames, onPage=on_page)

    doc = BaseDocTemplate(OUTPUT, pagesize=page_size,
                          leftMargin=margin, rightMargin=margin,
                          topMargin=margin, bottomMargin=margin)
    doc.addPageTemplates([pt])

    story = []

    # ── Page 1 ────────────────────────────────────────────────────────────
    # header frame
    story.append(make_header_table(full_w))
    story.append(FrameBreak())   # move to left body frame

    # Left column: Hair, Beard, Colour, Facial
    for sec in SECTIONS[:4]:
        story.append(make_section_table(sec, half_w))
        story.append(Spacer(1, 3 * mm))
    story.append(FrameBreak())   # move to right body frame

    # Right column: Waxing & Spa, Hand & Foot, Packages
    for sec in SECTIONS[4:]:
        story.append(make_section_table(sec, half_w))
        story.append(Spacer(1, 3 * mm))
    story.append(FrameBreak())   # move to footer frame

    story.append(make_footer_table(full_w))

    doc.build(story)
    print(f"PDF saved: {OUTPUT}")


build_pdf()
