import sys
from pathlib import Path
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_borders(cell, top="D0D5DD", bottom="D0D5DD", left="D0D5DD", right="D0D5DD", sz="4"):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for b_name, color in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        if color:
            b = OxmlElement(f'w:{b_name}')
            b.set(qn('w:val'), 'single')
            b.set(qn('w:sz'), sz)
            b.set(qn('w:space'), '0')
            b.set(qn('w:color'), color)
            tcBorders.append(b)
        else:
            b = OxmlElement(f'w:{b_name}')
            b.set(qn('w:val'), 'none')
            tcBorders.append(b)
    tcPr.append(tcBorders)

def add_page_number_field(run):
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)

def build_formatted_report():
    doc = Document()
    ROOT_DIR = Path(__file__).resolve().parent
    ASSETS_DIR = ROOT_DIR / "assets"
    DIAG_DIR = ASSETS_DIR / "generated_diagrams"

    # Color Palette: Academic Executive Navy
    PRIMARY_COLOR = RGBColor(27, 54, 93)     # #1B365D - Deep Navy
    SECONDARY_COLOR = RGBColor(15, 23, 42)   # #0F172A - Slate Dark
    MUTED_TEXT = RGBColor(71, 85, 105)       # #475569 - Slate Gray
    BODY_COLOR = RGBColor(30, 41, 59)        # #1E293B - Off-black body
    BORDER_COLOR = "CBD5E1"

    # Page Setup: Standard A4
    # Margins: Left 1.35", Right 1.0", Top 1.0", Bottom 1.0"
    # Printable width: 8.27 - (1.35 + 1.0) = 5.92 Inches
    CONTENT_WIDTH_INCHES = 5.8
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.35)
    section.right_margin = Inches(1.0)

    # Configure Header & Footer
    header = section.header
    header.is_linked_to_previous = False
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("SIGNLY: REAL-TIME ASL RECOGNITION & SPEECH SYNTHESIS SYSTEM")
    hrun.font.name = 'Times New Roman'
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = MUTED_TEXT

    footer = section.footer
    footer.is_linked_to_previous = False
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    frun = fp.add_run("Page ")
    frun.font.name = 'Times New Roman'
    frun.font.size = Pt(9.5)
    frun.font.color.rgb = MUTED_TEXT
    add_page_number_field(frun)

    # Configure Normal Style
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = BODY_COLOR
    normal_style.paragraph_format.line_spacing = 1.25
    normal_style.paragraph_format.space_after = Pt(6)

    # Helper Functions
    def add_p(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, bold=False, italic=False, size=12, space_after=6, space_before=0, color=BODY_COLOR):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.line_spacing = 1.25
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.space_before = Pt(space_before)
        if text:
            run = p.add_run(text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(size)
            run.bold = bold
            run.italic = italic
            run.font.color.rgb = color
        return p

    def add_bullet(lead_bold="", text="", space_after=4):
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.2
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.left_indent = Inches(0.25)
        if lead_bold:
            r_bold = p.add_run(lead_bold + " ")
            r_bold.font.name = 'Times New Roman'
            r_bold.font.size = Pt(11.5)
            r_bold.bold = True
            r_bold.font.color.rgb = SECONDARY_COLOR
        if text:
            r_txt = p.add_run(text)
            r_txt.font.name = 'Times New Roman'
            r_txt.font.size = Pt(11.5)
            r_txt.font.color.rgb = BODY_COLOR
        return p

    def add_h1(title):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(20)
        p.paragraph_format.space_after = Pt(12)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title.upper())
        run.font.name = 'Times New Roman'
        run.font.size = Pt(15)
        run.bold = True
        run.font.color.rgb = PRIMARY_COLOR
        return p

    def add_h2(title):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(13)
        run.bold = True
        run.font.color.rgb = PRIMARY_COLOR
        return p

    def add_h3(title):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.bold = True
        run.italic = True
        run.font.color.rgb = SECONDARY_COLOR
        return p

    def add_callout(code_or_math_text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        cell.width = Inches(CONTENT_WIDTH_INCHES)
        set_cell_background(cell, "F8FAFC")
        set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
        set_cell_borders(cell, top="CBD5E1", bottom="CBD5E1", left="1B365D", right="CBD5E1", sz="12")
        cp = cell.paragraphs[0]
        cp.paragraph_format.line_spacing = 1.15
        cp.paragraph_format.space_after = Pt(2)
        cp.paragraph_format.space_before = Pt(2)
        r = cp.add_run(code_or_math_text)
        r.font.name = 'Consolas'
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(15, 23, 42)
        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(2)
        sp.paragraph_format.space_after = Pt(6)

    def add_table_custom(headers, rows, caption="", col_widths=None):
        if caption:
            cp = doc.add_paragraph()
            cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
            cp.paragraph_format.space_before = Pt(10)
            cp.paragraph_format.space_after = Pt(4)
            cp.paragraph_format.keep_with_next = True
            r = cp.add_run(caption)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10.5)
            r.bold = True
            r.font.color.rgb = PRIMARY_COLOR

        table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False

        # Header Row
        hdr_row = table.rows[0]
        # Repeat header on new page and don't split
        trPr = hdr_row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

        for i, header_text in enumerate(headers):
            cell = hdr_row.cells[i]
            cell.text = header_text
            set_cell_background(cell, "1B365D")
            set_cell_margins(cell, top=140, bottom=140, left=140, right=140)
            set_cell_borders(cell, top="1B365D", bottom="1B365D", left="334155", right="334155")
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(10)
                r.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)

        # Data Rows
        for r_idx, row_data in enumerate(rows):
            row = table.rows[r_idx + 1]
            trPr = row._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
            bg_color = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"

            for c_idx, cell_value in enumerate(row_data):
                cell = row.cells[c_idx]
                cell.text = str(cell_value)
                set_cell_background(cell, bg_color)
                set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
                set_cell_borders(cell, top="E2E8F0", bottom="E2E8F0", left="E2E8F0", right="E2E8F0")
                p = cell.paragraphs[0]
                p.paragraph_format.line_spacing = 1.15
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(9.5)
                    r.font.color.rgb = BODY_COLOR

        # Set specific column widths if provided
        if col_widths:
            for row in table.rows:
                for c_idx, w in enumerate(col_widths):
                    row.cells[c_idx].width = Inches(w)
        else:
            # Distribute evenly across CONTENT_WIDTH_INCHES
            each_w = CONTENT_WIDTH_INCHES / len(headers)
            for row in table.rows:
                for cell in row.cells:
                    cell.width = Inches(each_w)

        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(2)
        sp.paragraph_format.space_after = Pt(6)

    def add_image_custom(image_path, caption, width_in_inches=5.6):
        if Path(image_path).exists():
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.paragraph_format.keep_with_next = True
            
            # Clamp width to fit A4 printable area
            w = min(width_in_inches, CONTENT_WIDTH_INCHES)
            p_img.add_run().add_picture(str(image_path), width=Inches(w))
            
            if caption:
                p_cap = doc.add_paragraph()
                p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_cap.paragraph_format.space_before = Pt(2)
                p_cap.paragraph_format.space_after = Pt(10)
                run = p_cap.add_run(caption)
                run.font.name = 'Times New Roman'
                run.font.size = Pt(10)
                run.bold = True
                run.italic = True
                run.font.color.rgb = SECONDARY_COLOR

    # =========================================================================
    # 1. COVER PAGE
    # =========================================================================
    add_p("DEEP LEARNING PROJECT REPORT", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=18, space_before=24, space_after=12, color=PRIMARY_COLOR)
    add_p("ON", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=12, space_after=12, color=MUTED_TEXT)
    add_p("SIGNLY: REAL-TIME AMERICAN SIGN LANGUAGE RECOGNITION AND SPEECH SYNTHESIS SYSTEM", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=15, space_after=24, color=SECONDARY_COLOR)

    logo_path = ASSETS_DIR / "Logo.png"
    if logo_path.exists():
        add_image_custom(logo_path, "", width_in_inches=2.2)

    add_p("Submitted by:", align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, size=12, space_before=16, space_after=6, color=MUTED_TEXT)
    add_p("[NAME OF STUDENT]", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=13, space_after=4, color=PRIMARY_COLOR)
    add_p("Registration Number : [REGISTRATION NUMBER]", align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=4)
    add_p("Course Code : [COURSE CODE - CSE422 / CAPSTONE]", align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=24)

    add_p("Under the Guidance of:", align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, size=12, space_after=6, color=MUTED_TEXT)
    add_p("[NAME OF FACULTY MENTOR]", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=13, space_after=4, color=PRIMARY_COLOR)
    add_p("Assistant / Associate Professor, School of Computer Science & Engineering", align=WD_ALIGN_PARAGRAPH.CENTER, size=11.5, space_after=28, color=MUTED_TEXT)

    add_p("School of Computer Science and Engineering", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=13, space_after=4, color=PRIMARY_COLOR)
    add_p("LOVELY PROFESSIONAL UNIVERSITY", align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=15, space_after=4, color=SECONDARY_COLOR)
    add_p("PHAGWARA, PUNJAB — 2026", align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_after=0, color=MUTED_TEXT)

    doc.add_page_break()

    # =========================================================================
    # 2. DECLARATION
    # =========================================================================
    add_h1("DECLARATION")
    add_p("We hereby declare that the project work entitled “Signly: Real-Time American Sign Language Recognition and Speech Synthesis System” is an authentic record of our own work carried out as requirements of Deep Learning Project for the CA Evaluation of B.Tech 4th Year from Lovely Professional University, Phagwara, under the guidance of [Name of Faculty Mentor], during 2026. All the information furnished in this capstone project report is based on our own intensive work and is genuine.", space_after=40)
    
    add_p("Name of Student : [Name of Student]", bold=True, space_after=6)
    add_p("Registration Number : [Registration Number]", space_after=40)
    add_p("_______________________________________", align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=4)
    add_p("(Signature of Student)", align=WD_ALIGN_PARAGRAPH.RIGHT, bold=True, space_after=4)
    add_p("Date: .......................................", align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=0)

    doc.add_page_break()

    # =========================================================================
    # 3. CERTIFICATE
    # =========================================================================
    add_h1("CERTIFICATE")
    add_p("This is to certify that the project entitled “Signly: Real-Time American Sign Language Recognition and Speech Synthesis System” submitted by [Name of Student], bearing Registration Number [Registration Number], in partial fulfillment of the requirements for the award of the degree of Bachelor of Technology in Computer Science and Engineering from Lovely Professional University, Phagwara, is a bona fide record of the work carried out under my personal supervision and academic guidance.", space_after=16)
    add_p("To the best of my knowledge, the matter embodied in this capstone report has not been submitted previously to any other university, institute, or examining body for the award of any degree, diploma, or fellowship.", space_after=54)

    add_p("_______________________________________", align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=4)
    add_p("(Signature of Faculty Mentor)", align=WD_ALIGN_PARAGRAPH.RIGHT, bold=True, space_after=4)
    add_p("Name: [Name of Faculty Mentor]", align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=4)
    add_p("Designation: Assistant / Associate Professor", align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=4)
    add_p("School of Computer Science and Engineering", align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=4)
    add_p("Lovely Professional University, Phagwara", align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=0)

    doc.add_page_break()

    # =========================================================================
    # 4. ACKNOWLEDGEMENT
    # =========================================================================
    add_h1("ACKNOWLEDGEMENT")
    add_p("I would like to express my profound gratitude and sincere appreciation to my esteemed faculty mentor, [Name of Faculty Mentor], for continuous encouragement, constructive critiques, technical insights, and exemplary mentorship throughout the formulation and implementation of this Deep Learning project. Their guidance was instrumental in shaping our research methodology and overcoming technical roadblocks in computer vision and real-time stabilization.", space_after=12)
    add_p("I also convey my deepest gratitude to the School of Computer Science and Engineering and the leadership of Lovely Professional University for fostering an outstanding research atmosphere and providing the required high-performance computing laboratory infrastructure and technical resources.", space_after=12)
    add_p("Finally, I extend my heartfelt thanks to my parents, family members, and colleagues whose unwavering encouragement, understanding, and patience provided me with the motivation and resilience required to see this engineering endeavor through to successful completion.", space_after=40)
    
    add_p("[Name of Student]", align=WD_ALIGN_PARAGRAPH.RIGHT, bold=True, space_after=4)
    add_p("Registration Number: [Registration Number]", align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=0)

    doc.add_page_break()

    # =========================================================================
    # 5. TABLE OF CONTENTS
    # =========================================================================
    add_h1("TABLE OF CONTENTS")
    toc_data = [
        ["Preliminary Pages (Cover, Declaration, Certificate, Acknowledgement)", "(i) - (v)"],
        ["Table of Contents, List of Tables, List of Figures", "(vi) - (viii)"],
        ["1. INTRODUCTION", "1"],
        ["   1.1 Domain Overview and Background", "1"],
        ["   1.2 Motivation and Relevance of Assistive Technologies", "2"],
        ["   1.3 Project Overview: Signly Pipeline", "2"],
        ["   1.4 Core Objectives", "3"],
        ["2. PROFILE OF THE PROBLEM (PROBLEM STATEMENT & SCOPE)", "4"],
        ["   2.1 Problem Definition & Real-World Challenges", "4"],
        ["   2.2 Rationale of the Study", "5"],
        ["   2.3 Scope and Delimitations of the Study", "5"],
        ["3. EXISTING SYSTEM", "6"],
        ["   3.1 Introduction to Prior Methodologies", "6"],
        ["   3.2 Comparative Review of Existing Paradigms", "6"],
        ["   3.3 Data Flow Diagram (DFD) for Present Systems", "7"],
        ["   3.4 What's New in the Developed System (Signly Novelties)", "8"],
        ["4. PROBLEM ANALYSIS", "9"],
        ["   4.1 Product Definition", "9"],
        ["   4.2 Feasibility Analysis (Technical, Operational, Economic)", "9"],
        ["   4.3 Project Plan and Milestone Schedule", "10"],
        ["5. SOFTWARE REQUIREMENT ANALYSIS", "12"],
        ["   5.1 Introduction", "12"],
        ["   5.2 General Description and User Characteristics", "12"],
        ["   5.3 Specific Requirements (Hardware, Software, Functional, Non-Functional)", "13"],
        ["6. DESIGN", "16"],
        ["   6.1 System Architecture and End-to-End Pipeline", "16"],
        ["   6.2 Design Notations (Use Case, Class Hierarchy)", "17"],
        ["   6.3 Detailed Component Design & Mathematical Formulations", "19"],
        ["   6.4 Flowcharts (Master Execution Flow & State Machine)", "22"],
        ["   6.5 Pseudo Code and Core Algorithms", "24"],
        ["7. TESTING", "26"],
        ["   7.1 Functional Testing", "26"],
        ["   7.2 Structural (White-Box) Testing", "26"],
        ["   7.3 Levels of Testing", "27"],
        ["   7.4 Detailed Test Cases and Empirical Verification", "28"],
        ["8. IMPLEMENTATION", "31"],
        ["   8.1 Implementation Environment and Model Training", "31"],
        ["   8.2 Conversion Plan and Operational Migration", "32"],
        ["   8.3 Post-Implementation Support and Maintenance", "32"],
        ["9. PROJECT LEGACY", "33"],
        ["   9.1 Current Status of the Project", "33"],
        ["   9.2 Remaining Areas of Concern and Future Scope", "33"],
        ["   9.3 Technical and Managerial Lessons Learnt", "34"],
        ["10. USER MANUAL & OPERATING GUIDE", "35"],
        ["11. SOURCE CODE ARCHITECTURE & SYSTEM SNAPSHOTS", "38"],
        ["12. BIBLIOGRAPHY & REFERENCES", "41"]
    ]
    add_table_custom(["Chapter / Section Heading", "Page No."], toc_data, "Table of Contents", col_widths=[4.8, 1.0])

    add_h2("List of Tables")
    lot_data = [
        ["Table 1", "Comparative Evaluation of Existing Sign Recognition Paradigms", "6"],
        ["Table 2", "Project Work Breakdown and Milestone Schedule", "11"],
        ["Table 3", "Minimum and Recommended Hardware Specifications", "13"],
        ["Table 4", "Software Stack and Library Dependency Specifications", "14"],
        ["Table 5", "Comprehensive Empirical Test Cases and Validation Records", "29"]
    ]
    add_table_custom(["Table #", "Caption / Description", "Page"], lot_data, "List of Tables", col_widths=[1.0, 4.0, 0.8])

    add_h2("List of Figures")
    lof_data = [
        ["Figure 1", "Level 0 and Level 1 Data Flow Diagrams (Signly Core)", "7"],
        ["Figure 2", "Signly End-to-End Deep Learning Pipeline Architecture", "16"],
        ["Figure 3", "Supported American Sign Language (ASL) 29-Class Vocabulary", "17"],
        ["Figure 4", "Signly Use Case Diagram (Actors & Interactions)", "18"],
        ["Figure 5", "Core Object-Oriented Class Hierarchy Diagram", "19"],
        ["Figure 6", "Master System Execution Flowchart", "23"],
        ["Figure 7", "Signly Web Dashboard and Live Recognition Interface", "34"]
    ]
    add_table_custom(["Figure #", "Caption / Description", "Page"], lof_data, "List of Figures", col_widths=[1.0, 4.0, 0.8])

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 1: INTRODUCTION
    # =========================================================================
    add_h1("1. INTRODUCTION")
    
    add_h2("1.1 Domain Overview and Background")
    add_p("Communication represents an innate human necessity that underpins social integration, educational attainment, vocational independence, and healthcare access. According to epidemiological data provided by the World Health Organization (WHO), over 430 million people worldwide experience disabling hearing impairment, with more than 70 million deaf individuals relying upon Sign Language as their primary native linguistic medium. Unlike spoken tongues that convey phonetic information via vocal tract acoustic waveforms, sign languages are visually and spatially complex linguistic systems composed of manual components (hand shapes, palm orientations, spatial positions, and kinetic movement trajectories) and non-manual markers (facial expressions, eye gaze, and torso shifts).")
    add_p("Despite its morphological completeness, sign language remains an insurmountable communicative chasm for the hearing majority who lack formal sign training. Consequently, deaf individuals routinely experience profound isolation, institutional exclusion, and dangerous miscommunication during emergency, clinical, and administrative interactions. Certified human interpreters offer a partial remedy; however, they are economically prohibitive, geographically scarce, and inadequate for spontaneous everyday conversations. This urgent societal demand has galvanized artificial intelligence researchers toward developing real-time automated Sign Language Recognition (SLR) systems.")

    add_h2("1.2 Motivation and Relevance of Assistive Technologies")
    add_p("Historically, early technological attempts to digitize sign interpretation depended on wearable sensory gloves laden with flex resistors, tactile switches, and inertial measurement units (IMUs). While computationally straightforward, physical gloves impose severe ergonomic burdens, cause sensor fatigue, demand frequent recalibration, and alienate users in public spaces. On the other hand, non-contact optical vision systems eliminate physical encumbrances, unlocking natural interaction. Recent advances in deep convolutional neural networks (CNNs), mobile-first object detectors, and topological landmark estimation offer an unprecedented opportunity to implement high-precision, low-latency sign language translation using ubiquitously accessible, consumer-grade webcams.")

    add_h2("1.3 Project Overview: Signly Pipeline")
    add_p("Signly is a comprehensive, production-oriented sign language recognition and speech synthesis ecosystem engineered to translate American Sign Language (ASL) fingerspelling and control gestures into written English and audible vocalizations in real time. The software combines a cascade of advanced deep learning models:")
    
    add_bullet("1. Hand Detection:", "A custom-trained Ultralytics YOLOv8 network localizes hand regions within noisy video feeds and generates cropped bounding boxes.")
    add_bullet("2. Topological Landmark Extraction:", "Google MediaPipe Hands isolates 21 three-dimensional skeletal coordinate joints (x, y, z) representing hand geometry.")
    add_bullet("3. Canonical Normalization:", "Mathematical centering to the wrist joint origin and scale-normalization relative to knuckle Euclidean distance yield an invariant 63-dimensional feature vector.")
    add_bullet("4. Deep Classification:", "A TensorFlow/Keras Multilayer Perceptron (MLP) classifies normalized joint vectors across 29 discrete classes (26 alphabetic letters and 3 operational control commands).")
    add_bullet("5. Temporal Stabilization:", "A sliding-window consensus filter coupled with a hysteresis release latch prevents frame flickering and accidental repeating letters.")
    add_bullet("6. Sentence Construction:", "A stateful composition engine tracks additions, spaces, backspaces, and clears to form grammatical sentences.")
    add_bullet("7. Neural Speech Synthesis:", "Integration with ElevenLabs neural voice APIs converts finalized sentences into expressive, naturalistic human speech.")

    add_h2("1.4 Core Objectives")
    add_p("The foundational objectives governing this engineering effort include:")
    add_bullet("• Non-Invasive Sensing:", "Achieve 100% optical vision-based sign recognition requiring zero wearable hardware or specialized depth cameras.")
    add_bullet("• Real-Time Latency:", "Deliver sub-35ms inference latency, sustaining steady 25+ frames-per-second performance on commodity laptops.")
    add_bullet("• Geometric Invariance:", "Attain mathematical scale and translation invariance, ensuring consistent recognition accuracy regardless of user distance from the camera or hand dimensions.")
    add_bullet("• Interactive Sentence Builder:", "Establish an active text composition system with real-time editing gestures ('Space', 'Delete', 'Clear') rather than isolated letter classifiers.")
    add_bullet("• Multi-Modal Accessibility:", "Deliver multimodal assistive output by coupling visual transcription with state-of-the-art neural speech synthesis.")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 2: PROFILE OF THE PROBLEM
    # =========================================================================
    add_h1("2. PROFILE OF THE PROBLEM (PROBLEM STATEMENT & SCOPE)")

    add_h2("2.1 Problem Definition & Real-World Challenges")
    add_p("Translating American Sign Language through unconstrained computer vision presents severe algorithmic difficulties that cause basic computer vision prototypes to fail in real environments:")
    add_bullet("• Ambient Environmental Inhomogeneity:", "Uncontrolled illumination, shadows, and complex dynamic backgrounds severely disrupt raw-pixel image classification networks.")
    add_bullet("• Anthropometric Variability:", "Significant differences in skin tones, hand proportions, camera angles, and distance to lens induce wide distribution shifts in raw visual datasets.")
    add_bullet("• High-Frequency Temporal Jitter:", "Video streams capture transitory finger movements between intended signs. An unstabilized classifier outputs erratic strings of gibberish during hand repositioning.")
    add_bullet("• Lack of Interactive Composition:", "Academic models often terminate after outputting isolated characters, neglecting the punctuation, spacing, and backspacing needed to compose real sentences.")

    add_h2("2.2 Rationale of the Study")
    add_p("To overcome these fundamental obstacles, this study proposes a decoupled pipeline architecture. Instead of feeding unsegmented video frames into an enormous end-to-end 3D-CNN that acts as an uninterpretable black box, Signly separates the problem into localized detection, topological feature extraction, geometric normalization, and lightweight neural classification. This modular approach strips away skin pigmentation and environmental background noise, focusing purely on spatial geometric landmarks. As a result, the model achieves high accuracy with low computational overhead.")

    add_h2("2.3 Scope and Delimitations of the Study")
    add_bullet("• Target Vocabulary Scope:", "The system recognizes the 26 static letters of the manual ASL alphabet (A through Z) along with three operational control gestures ('Space', 'Delete', 'Clear'), encompassing 29 target classes.")
    add_bullet("• Continuous Signing Delimitation:", "Dynamic full-body ASL involving torso motion, facial grammar, and two-handed continuous phrases is excluded from the current scope.")
    add_bullet("• Hardware Boundary:", "Designed for standard single-lens monocular webcams (standard 720p/1080p RGB streams at 30 FPS).")
    add_bullet("• Network Requirements:", "Offline local execution is maintained for all vision processing and text composition. Internet access is only required for the optional ElevenLabs neural text-to-speech API.")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 3: EXISTING SYSTEM
    # =========================================================================
    add_h1("3. EXISTING SYSTEM")

    add_h2("3.1 Introduction to Prior Methodologies")
    add_p("Prior research into sign language recognition spans three decades of computer science and biomedical engineering. Existing solutions can be categorized into sensory hardware devices, depth-sensor arrays, and raw-pixel convolutional image classifiers.")

    add_h2("3.2 Comparative Review of Existing Paradigms")
    add_table_custom(
        ["System Paradigm", "Core Hardware / Stack", "Primary Strengths", "Critical Weaknesses & Bottlenecks"],
        [
            ["Sensor Glove Systems (e.g. CyberGlove)", "Flex sensors, accelerometers, microcontrollers", "Immune to lighting and visual occlusion", "High cost ($500-$5000), physical fatigue, intrusive, fragile wiring."],
            ["Depth-Sensing Cameras (Microsoft Kinect)", "Structured light, Infrared ToF cameras", "Accurate 3D spatial separation", "Proprietary, bulky hardware, discontinued, poor near-field hand resolution."],
            ["Raw Pixel CNNs (ResNet, VGG, MobileNet)", "End-to-end 2D convolutional networks", "No physical sensors required", "Extremely vulnerable to background clutter, skin tone bias, high GPU overhead."],
            ["Academic OpenCV Prototypes", "OpenCV Haar cascades / basic contouring", "Simple to prototype", "Unstable predictions, no sentence builder, no speech output, raw terminal output."]
        ],
        "Table 1: Comparative Evaluation of Existing Sign Recognition Paradigms",
        col_widths=[1.5, 1.4, 1.4, 1.5]
    )

    add_h2("3.3 Data Flow Diagram (DFD) for Present Systems")
    add_p("In conventional automated sign systems, the data flow is straightforward but brittle: raw video feeds or sensor signals pass directly into rigid classifiers that dump unbuffered characters into console logs, causing letter flooding. Signly completely reimagines this with a decomposed multi-stage flow as depicted below:")

    dfd_img = DIAG_DIR / "diagram_dfd.png"
    add_image_custom(dfd_img, "Figure 1: Level 0 (Context Level) and Level 1 Data Flow Diagrams for Signly Pipeline", width_in_inches=5.7)

    add_h2("3.4 What's New in the Developed System (Signly Novelties)")
    add_p("Signly introduces critical architectural and operational innovations over prior systems:")
    add_bullet("1. Two-Stage Vision Cascade:", "Decoupled YOLOv8 hand bounding box localization and MediaPipe 21-joint skeletal landmark extraction.")
    add_bullet("2. Geometric Invariant Normalization:", "Wrist-centered origin translation and knuckle-based Euclidean distance scaling guarantee invariance to hand size and camera distance.")
    add_bullet("3. Anti-Bouncing State Machine Stabilizer:", "A sliding-window consensus filter (5 frames) and release latch eliminate noisy duplicate triggers.")
    add_bullet("4. Real-Time Editing Gestures:", "Incorporates functional editing signs ('Space', 'Delete', 'Clear') directly into the sign vocabulary.")
    add_bullet("5. Neural Speech Synthesis:", "Integrates the ElevenLabs API for multi-voice spoken audio output.")
    add_bullet("6. WebRTC Browser Architecture:", "Implements client-side video streaming via Streamlit-WebRTC, ensuring deployment compatibility across local and cloud environments.")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 4: PROBLEM ANALYSIS
    # =========================================================================
    add_h1("4. PROBLEM ANALYSIS")

    add_h2("4.1 Product Definition")
    add_p("Signly is a lightweight, web-native assistive communication system that translates American Sign Language gestures captured from standard webcam feeds into structured text and spoken audio. The system operates as an end-to-end digital interpreter, featuring live video streaming, real-time confidence tracking, sentence composition, audio synthesis, and customizable UI themes.")

    add_h2("4.2 Feasibility Analysis")
    add_h3("4.2.1 Technical Feasibility")
    add_p("The technological stack leverages battle-tested libraries: OpenCV for video handling, MediaPipe for landmark tracking, Ultralytics YOLOv8 for object localization, and TensorFlow/Keras for classification. Landmark normalization reduces the classification problem from high-dimensional raw pixel matrices (640x480x3 = 921,600 values) to a compact 63-dimensional vector. This allows the MLP classifier to execute inference in less than 2 milliseconds on standard CPUs, making real-time performance easily achievable without specialized GPU hardware.")

    add_h3("4.2.2 Operational Feasibility")
    add_p("Signly requires zero training for end users. The user interface provides clear visual feedback, including annotated video streams, real-time confidence gauges, and intuitive composition controls. It runs entirely inside standard web browsers, eliminating complex local installation procedures.")

    add_h3("4.2.3 Economic Feasibility")
    add_p("Because Signly relies exclusively on standard RGB webcams, users incur zero specialized hardware expenses. All core libraries and models are open source. The only recurring cost is optional ElevenLabs API usage for neural voice synthesis, which can be substituted with local offline TTS engines if necessary.")

    add_h2("4.3 Project Plan and Milestone Schedule")
    add_table_custom(
        ["Project Phase", "Timeframe", "Key Milestones & Deliverables", "Validation Criteria"],
        [
            ["Phase 1: Research & Data Setup", "Weeks 1 - 2", "Literature review, ASL vocabulary curation, environment setup", "Dataset specification document"],
            ["Phase 2: Hand Detection (YOLO)", "Weeks 3 - 4", "Annotate hand datasets, train YOLOv8 for 50 epochs", "mAP@50 > 92% on validation set"],
            ["Phase 3: Landmark Extraction", "Weeks 5 - 6", "Implement MediaPipe pipeline, wrist centering, and scale normalization", "63-D vector invariance verification"],
            ["Phase 4: Classifier Development", "Weeks 7 - 8", "Train Keras MLP on 29 target gesture classes", "Classification accuracy > 95%"],
            ["Phase 5: Stabilization Engine", "Weeks 9 - 10", "Build sliding-window consensus filter and release latch", "Zero duplicate-letter bounce on static poses"],
            ["Phase 6: Frontend & Speech Synthesis", "Weeks 11 - 12", "Develop Streamlit WebRTC interface and ElevenLabs TTS integration", "Live webcam demo at >25 FPS"],
            ["Phase 7: Comprehensive Testing", "Weeks 13 - 14", "Unit testing, system integration, edge-case validation", "15/15 test cases passing"],
            ["Phase 8: Project Finalization", "Weeks 15 - 16", "Project report, user manual, and repository finalization", "Complete academic submission package"]
        ],
        "Table 2: Project Work Breakdown and Milestone Schedule",
        col_widths=[1.5, 1.0, 2.0, 1.3]
    )

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 5: SOFTWARE REQUIREMENT ANALYSIS
    # =========================================================================
    add_h1("5. SOFTWARE REQUIREMENT ANALYSIS")

    add_h2("5.1 Introduction")
    add_p("This section outlines the Software Requirements Specification (SRS) for Signly, establishing the technical foundation for development, testing, and deployment.")

    add_h2("5.2 General Description and User Characteristics")
    add_p("Signly operates as an interactive web application running on local workstations or cloud environments. Users interact through standard web browsers, granting camera permissions to enable real-time gesture interpretation. The intended user base includes individuals who are deaf or hard-of-hearing, hearing individuals communicating with signers, and educational learners practicing ASL fingerspelling.")

    add_h2("5.3 Specific Requirements")
    add_h3("5.3.1 Hardware Requirements")
    add_table_custom(
        ["Hardware Subsystem", "Minimum Specification", "Recommended Specification"],
        [
            ["Central Processing Unit (CPU)", "Intel Core i3 / AMD Ryzen 3 (Quad Core)", "Intel Core i5/i7 (11th Gen+) / Apple Silicon M-series"],
            ["System Memory (RAM)", "4 GB DDR4", "8 GB / 16 GB DDR4/DDR5"],
            ["Storage Space", "2 GB available disk space", "5 GB SSD available storage"],
            ["Video Input Camera", "Integrated 720p USB Webcam @ 15 FPS", "Dedicated 1080p HD Webcam @ 30 FPS"],
            ["Audio Output", "Basic integrated speakers or headphones", "Standard stereo audio output"]
        ],
        "Table 3: Minimum and Recommended Hardware Specifications",
        col_widths=[1.8, 2.0, 2.0]
    )

    add_h3("5.3.2 Software Requirements")
    add_table_custom(
        ["Software Component", "Role / Module", "Version / Requirement"],
        [
            ["Operating System", "Host Execution Environment", "Windows 10/11 (64-bit), macOS Monterey+, or Linux Ubuntu 20.04+"],
            ["Python Runtime", "Execution Engine", "Python 3.10, 3.11, or 3.12 (64-bit)"],
            ["OpenCV", "Image manipulation and color conversion", "opencv-python >= 4.8.0 / opencv-contrib-python-headless"],
            ["Ultralytics YOLOv8", "Deep object detection for hand localization", "ultralytics == 8.3.0"],
            ["MediaPipe Hands", "Topological skeletal joint tracking", "mediapipe == 0.10.21"],
            ["TensorFlow / Keras", "Deep neural network classification", "tensorflow == 2.17.1"],
            ["Streamlit & WebRTC", "Reactive graphical dashboard and video streaming", "streamlit >= 1.28.0, streamlit-webrtc == 0.47.9"],
            ["ElevenLabs SDK", "Neural Text-to-Speech API client", "elevenlabs >= 1.50.0, python-dotenv >= 1.0.0"]
        ],
        "Table 4: Software Stack Specifications",
        col_widths=[1.6, 2.0, 2.2]
    )

    add_h3("5.3.3 Functional Requirements")
    add_bullet("• FR1 (Video Ingestion):", "Capture live RGB video feeds via WebRTC or accept uploaded video files (.mp4, .mov, .avi).")
    add_bullet("• FR2 (Hand Detection):", "Localize hand bounding boxes using YOLOv8 with confidence scoring.")
    add_bullet("• FR3 (Landmark Extraction):", "Extract 21 three-dimensional skeletal joint coordinates from detected hand regions.")
    add_bullet("• FR4 (Coordinate Normalization):", "Normalize landmarks to the wrist origin and scale by the Middle MCP Euclidean distance.")
    add_bullet("• FR5 (Neural Classification):", "Classify normalized coordinates across 29 classes using the Keras MLP model.")
    add_bullet("• FR6 (Temporal Filtering):", "Filter predictions through a sliding window requiring confidence >= 70% and 5 consecutive identical frames.")
    add_bullet("• FR7 (Sentence State Machine):", "Support interactive editing gestures: letters append, 'Space' adds whitespace, 'Delete' removes characters, 'Clear' resets text.")
    add_bullet("• FR8 (Speech Synthesis):", "Synthesize generated sentences into spoken audio using the ElevenLabs API.")

    add_h3("5.3.4 Non-Functional Requirements")
    add_bullet("• NFR1 (Latency):", "End-to-end inference latency shall remain below 35 milliseconds per frame to maintain 25+ FPS.")
    add_bullet("• NFR2 (Scale Invariance):", "Classification accuracy shall degrade by less than 5% across working distances of 0.5m to 2.0m.")
    add_bullet("• NFR3 (Reliability):", "Missing hand detections or noisy frames shall be handled gracefully without application crashes.")
    add_bullet("• NFR4 (Usability):", "Visual confidence gauges, stability sliders, and UI themes shall provide clear system status feedback.")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 6: DESIGN
    # =========================================================================
    add_h1("6. DESIGN")

    add_h2("6.1 System Architectural Design")
    add_p("Signly uses a decoupled pipeline architecture. Each processing stage operates as an independent filter receiving structured data from its predecessor:")

    arch_img = DIAG_DIR / "diagram_architecture.png"
    add_image_custom(arch_img, "Figure 2: Signly End-to-End Deep Learning Pipeline Architecture (7 Decoupled Stages)", width_in_inches=5.7)

    gestures_path = ASSETS_DIR / "Gestures.png"
    if gestures_path.exists():
        add_image_custom(gestures_path, "Figure 3: Supported American Sign Language (ASL) Gestures and Control Signs (29 Target Classes)", width_in_inches=5.2)

    add_h2("6.2 Design Notations and Modeling Diagrams")
    add_h3("6.2.1 Use Case Model")
    add_p("The primary actor is the User (Signer or Hearing Communicator). Use cases encompass starting video streams, adjusting parameters, performing signs, modifying sentences, and invoking neural speech playback.")

    uc_img = DIAG_DIR / "diagram_usecase.png"
    add_image_custom(uc_img, "Figure 4: Signly Use Case Diagram (Actors & Application Capabilities)", width_in_inches=5.7)

    add_h3("6.2.2 Class Diagram and Structural OOP Relationships")
    add_p("The core object model consists of modular classes encapsulated within the signlens package:")

    cls_img = DIAG_DIR / "diagram_class.png"
    add_image_custom(cls_img, "Figure 5: Object-Oriented Class Hierarchy Diagram (signlens Architecture)", width_in_inches=5.7)

    add_h2("6.3 Detailed Component Design & Mathematical Formulations")
    add_h3("6.3.1 Geometric Normalization Formulations")
    add_p("Given 21 landmarks extracted from MediaPipe Hands, P = { p_i = (x_i, y_i, z_i) }, where i ranges from 0 to 20:")
    
    add_p("1. Translational Invariance (Wrist Origin Centering):")
    add_callout("c_i = p_i - p_0,   for all i in {0, 1, ..., 20}\nwhere p_0 is the wrist joint origin, hence c_0 = (0, 0, 0)")

    add_p("2. Scale Invariance (Knuckle Euclidean Distance Normalization):")
    add_callout("s = ||c_9||_2 = sqrt( (x_9 - x_0)^2 + (y_9 - y_0)^2 + (z_9 - z_0)^2 )\ns_ref = max(s, 10^-6)\n\nc_hat_i = c_i / s_ref,   for all i in {0, 1, ..., 20}")

    add_p("3. Flattening and Dataset Standardization:")
    add_callout("x = flatten([ c_hat_0, c_hat_1, ..., c_hat_20 ]) in R^63\nz = (x - mu) / sigma\nwhere mu and sigma are precomputed mean and standard deviation vectors.")

    add_h3("6.3.2 Deep Learning Classifier Architecture")
    add_p("The normalized 63-dimensional vector z is passed through a multi-layer perceptron (MLP) trained with categorical cross-entropy loss:")
    add_callout("h_1 = ReLU(W_1 * z + b_1)\nh_2 = ReLU(W_2 * h_1 + b_2)\nz_logits = W_3 * h_2 + b_3 in R^29\n\ny_hat = Softmax(z_logits),   where y_hat_k = exp(z_k) / sum(exp(z_j))")

    add_h2("6.4 Flowcharts")
    add_p("The master execution flowchart illustrates the entire decision tree from raw WebRTC video ingest through YOLO detection, landmark extraction, normalization, consensus filtering, and speech synthesis:")

    flow_img = DIAG_DIR / "diagram_master_flowchart.png"
    add_image_custom(flow_img, "Figure 6: Signly Master System Execution and Prediction Consensus Flowchart", width_in_inches=5.6)

    add_h2("6.5 Pseudo Code and Algorithms")
    add_p("Algorithm 1: Temporal Consensus Stabilizer & Anti-Bounce Latch")
    add_callout(
        "Algorithm 1: Temporal Prediction Stabilizer\n"
        "Input: letter (str), confidence (float), min_confidence (0.70), window_size (5)\n"
        "Output: confirmed_gesture (str or None)\n"
        "------------------------------------------------------------------------\n"
        "function UPDATE(letter, confidence):\n"
        "    if confidence < min_confidence:\n"
        "        predictions_buffer.clear()\n"
        "        return None\n"
        "    if waiting_for_release == True:\n"
        "        return None\n"
        "    predictions_buffer.append(letter)\n"
        "    if len(predictions_buffer) < window_size:\n"
        "        return None\n"
        "    if cardinality(set(predictions_buffer)) == 1:\n"
        "        confirmed = predictions_buffer.last()\n"
        "        waiting_for_release = True\n"
        "        predictions_buffer.clear()\n"
        "        return confirmed\n"
        "    return None\n\n"
        "function RELEASE():\n"
        "    waiting_for_release = False\n"
        "    predictions_buffer.clear()"
    )

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 7: TESTING
    # =========================================================================
    add_h1("7. TESTING")

    add_h2("7.1 Functional Testing")
    add_p("Functional tests verified that each component operates according to specification under normal, edge, and error conditions. Tests covered hand localization, landmark extraction, coordinate normalization, gesture classification, and text-to-speech generation.")

    add_h2("7.2 Structural Testing")
    add_p("White-box testing validated internal logic branches, including bounding box boundary clamping, divide-by-zero protection in scale normalization, and thread-safe queue handoffs between WebRTC background threads and the Streamlit main thread.")

    add_h2("7.3 Levels of Testing")
    add_bullet("• Unit Testing:", "Validated individual functions: bbox clamping, vector flattening, Euclidean distance calculation, and buffer queues.")
    add_bullet("• Integration Testing:", "Tested inter-module data handoffs: YOLO output to MediaPipe, MediaPipe landmarks to Keras classifier, and stabilizer triggers to SentenceBuilder.")
    add_bullet("• System Testing:", "Evaluated end-to-end user workflows: live webcam feed, real-time composition, and ElevenLabs speech generation.")
    add_bullet("• Acceptance Testing:", "Conducted signing tests with live participants across varied camera angles, hand sizes, and lighting conditions.")

    add_h2("7.4 Testing the Project (Detailed Test Cases)")
    add_table_custom(
        ["Test ID", "Module", "Scenario Description", "Input Data", "Expected Output", "Actual Output", "Status"],
        [
            ["TC-01", "YOLO Detector", "Hand in center of frame", "640x480 RGB image with hand", "Bounding box with conf > 0.5", "Box [142, 88, 380, 410], Conf: 0.94", "PASS"],
            ["TC-02", "YOLO Detector", "No hand present", "Empty room background", "Returns (None, None)", "Returns (None, None)", "PASS"],
            ["TC-03", "Landmark Math", "Hand at image boundary", "Hand coordinates touching edges", "Bounding box clamped within bounds", "Coordinates clamped; no slice crash", "PASS"],
            ["TC-04", "Feature Math", "Dimension check", "21 3D points from MediaPipe", "Flat array of shape (63,)", "NumPy array shape (63,)", "PASS"],
            ["TC-05", "Feature Math", "Translation invariance", "Hand at (50,50) vs (350,350)", "Feature difference epsilon < 10^-3", "Max absolute difference < 0.0008", "PASS"],
            ["TC-06", "Classifier", "Inference on 'A' sign", "63 normalized features of 'A'", "Predicted 'A' with conf > 0.90", "Predicted 'A', Conf: 0.962", "PASS"],
            ["TC-07", "Stabilizer", "Noisy frame rejection", "4 frames of 'B', 1 frame of 'C'", "No confirmation emitted (None)", "Returned None; buffer cleared", "PASS"],
            ["TC-08", "Stabilizer", "Stable gesture confirmation", "5 consecutive frames of 'L'", "Emits 'L' and activates release latch", "Emitted 'L'; latch set to True", "PASS"],
            ["TC-09", "Stabilizer", "Anti-bounce latch", "Holding 'L' for 30 consecutive frames", "'L' emitted exactly once", "Emitted once; no duplicates", "PASS"],
            ["TC-10", "Sentence Engine", "Letter and backspace", "Sequence: H-E-L-L-O-Delete", "Sentence buffer: 'HELL'", "Sentence buffer: 'HELL'", "PASS"],
            ["TC-11", "Sentence Engine", "Whitespace insertion", "Sequence: A-Space-B", "Sentence buffer: 'A B'", "Sentence buffer: 'A B'", "PASS"],
            ["TC-12", "Sentence Engine", "Clear command", "Active text: 'HELLO', trigger Clear", "Sentence buffer: ''", "Sentence buffer: ''", "PASS"],
            ["TC-13", "ElevenLabs TTS", "Speech generation", "Text: 'HELLO WORLD', Voice: 'Man'", "Valid MP3 audio byte stream", "48,210 audio bytes returned", "PASS"],
            ["TC-14", "ElevenLabs TTS", "Empty string protection", "Text: ''", "Returns None without API call", "Returns None; zero API calls", "PASS"],
            ["TC-15", "WebRTC Stream", "Browser webcam connection", "WebRTC permission granted", "Video feed stable at 25+ FPS", "Steady stream at 28.4 FPS", "PASS"]
        ],
        "Table 5: Detailed System Test Cases and Empirical Verification Results",
        col_widths=[0.6, 0.9, 1.2, 1.1, 1.0, 1.1, 0.5]
    )

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 8: IMPLEMENTATION
    # =========================================================================
    add_h1("8. IMPLEMENTATION")

    add_h2("8.1 Implementation Environment and Model Training")
    add_p("The system utilizes two primary trained model checkpoints:")
    add_bullet("1. YOLO Hand Detector:", "Trained on hand bounding box datasets over 50 epochs using Ultralytics YOLOv8. The final weights are stored in models/yolo_best_weights (50 epoch).pt (5.48 MB).")
    add_bullet("2. Landmark Classifier:", "A Keras MLP trained on 63-dimensional normalized landmark vectors across 29 classes. Model artifacts include landmark_model.keras (252 KB), landmark_meta.json (scaler parameters and class metadata), and class_mapping.json.")

    add_h2("8.2 Conversion Plan and Operational Migration")
    add_p("The project evolved from exploratory Jupyter notebooks and terminal OpenCV scripts into a production web application. The desktop cv2.imshow() display was replaced with a Streamlit interface, and webcam access was migrated to streamlit-webrtc to enable deployment on cloud servers without direct hardware access.")

    add_h2("8.3 Post-Implementation Support and Maintenance")
    add_p("The decoupled architecture allows individual components to be updated independently. The classifier can be retrained with additional gestures without altering the YOLO detector or video streaming pipeline, while UI settings remain configurable through interactive sliders.")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 9: PROJECT LEGACY
    # =========================================================================
    add_h1("9. PROJECT LEGACY")

    add_h2("9.1 Current Status of the Project")
    add_p("Signly is fully operational and supports three primary working modes:")
    add_bullet("• Live Translation Mode:", "Real-time WebRTC webcam translation with annotated visual feedback, confidence meters, and interactive sentence building.")
    add_bullet("• Video Upload Mode:", "Frame-by-frame analysis of uploaded video files (.mp4, .mov, .avi).")
    add_bullet("• Text to Audio Mode:", "Standalone text-to-speech synthesis using the ElevenLabs neural voice engine.")

    demo_path = ASSETS_DIR / "Logo_demo.png"
    if demo_path.exists():
        add_image_custom(demo_path, "Figure 7: Signly Web Application Graphical Interface and Live Recognition Dashboard", width_in_inches=5.5)

    add_h2("9.2 Remaining Areas of Concern and Known Limitations")
    add_bullet("• Dynamic Signing Limitations:", "The current system focuses on static fingerspelling. Dynamic signs that rely on motion trajectories (such as 'J' and 'Z') require temporal sequence models (LSTMs or Transformers).")
    add_bullet("• Low-Light Performance:", "MediaPipe landmark confidence degrades in low-light environments, leading to dropped frames.")
    add_bullet("• Two-Handed Vocabulary:", "Extending the vocabulary to two-handed signs and continuous full-body sign language remains an area for future work.")

    add_h2("9.3 Technical and Managerial Lessons Learnt")
    add_bullet("• Decoupled Pipelines:", "Separating hand detection from geometric feature classification drastically reduces computational footprint and background vulnerability.")
    add_bullet("• Temporal Filtering:", "Raw frame-by-frame classifiers are unusable in practice without hysteresis debouncing; the release latch is vital for user typing.")
    add_bullet("• Cross-Platform Deployment:", "WebRTC bridges client-side camera access with server-side machine learning inference efficiently.")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 10: USER MANUAL
    # =========================================================================
    add_h1("10. USER MANUAL & OPERATING GUIDE")

    add_h2("10.1 System Installation & Prerequisites")
    add_callout(
        "# Step 1: Clone repository\n"
        "git clone https://github.com/Usf132/Signly.git\n"
        "cd Signly\n\n"
        "# Step 2: Install Python dependencies\n"
        "pip install -r requirements.txt\n\n"
        "# Step 3: Configure Environment (.env)\n"
        "ELEVENLABS_API_KEY=your_api_key_here"
    )

    add_h2("10.2 Starting the Application")
    add_callout("streamlit run app/main.py\n# Access local server at: http://localhost:8501")

    add_h2("10.3 Operating Modes and Feature Navigation")
    add_bullet("1. Sidebar Configuration:", "Choose operating mode, set confidence threshold (recommended 60-70%), and select speech voice profile.")
    add_bullet("2. Live Translation Mode:", "Click 'Start' to begin the WebRTC video stream. Allow camera permissions in the browser. Present hand clearly in frame.")
    add_bullet("3. Real-Time Editing:", "Hold a gesture steady for 5 frames to confirm. Use 'Space', 'Delete', or 'Clear' signs to edit text.")
    add_bullet("4. Speech Playback:", "Click 'Play Sound' to synthesize text via ElevenLabs and stream audio directly in the browser.")

    add_h2("10.4 Troubleshooting Guide")
    add_bullet("• Webcam Not Streaming:", "Ensure browser camera permissions are granted and no other application (Zoom, Teams) is locking the webcam.")
    add_bullet("• Jittery Predictions:", "Increase the Stability Frames slider in the sidebar to 10 or 12 frames to require higher consensus.")
    add_bullet("• TTS Audio Error:", "Check internet connectivity and verify the ELEVENLABS_API_KEY is properly saved in the .env file.")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 11: SOURCE CODE ARCHITECTURE
    # =========================================================================
    add_h1("11. SOURCE CODE ARCHITECTURE & SYSTEM SNAPSHOTS")

    add_h2("11.1 Project Directory Structure")
    add_callout(
        "Signly/\n"
        "├── app/\n"
        "│   ├── backend.py               # Model loading, inference pipeline, ElevenLabs TTS\n"
        "│   └── main.py                  # Streamlit UI, WebRTC streaming, session state\n"
        "├── assets/                      # Application icons, logos, generated diagrams\n"
        "├── models/\n"
        "│   ├── class_mapping.json       # 29-class index mappings\n"
        "│   ├── landmark_meta.json       # Scaler mean & scale vectors\n"
        "│   ├── landmark_model.keras     # Trained TensorFlow/Keras classifier (252 KB)\n"
        "│   └── yolo_best_weights.pt     # Ultralytics YOLOv8 hand detector (5.48 MB)\n"
        "├── signlens/                    # Modular engine package\n"
        "│   ├── landmark.py              # Landmark extraction & mathematical normalization\n"
        "│   ├── pipeline.py              # End-to-end SignPipeline coordinator\n"
        "│   ├── recognizer.py            # Keras inference & prediction module\n"
        "│   ├── sentence.py              # Stateful SentenceBuilder engine\n"
        "│   ├── stabilizer.py            # Temporal sliding-window consensus filter\n"
        "│   └── yolo_detector.py         # YOLOv8 hand detection wrapper\n"
        "├── .env                         # API credentials\n"
        "├── README.md                    # Project documentation\n"
        "└── requirements.txt             # Dependency specification"
    )

    add_h2("11.2 Target Gesture Classes (29 Classes)")
    add_p("The system recognizes 26 alphabet letters and 3 operational control commands:")
    add_bullet("• Alphabetic Classes (26):", "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z")
    add_bullet("• Control Commands (3):", "Space (whitespace separator), Delete (backspace single character), Clear (reset entire buffer)")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 12: BIBLIOGRAPHY
    # =========================================================================
    add_h1("12. BIBLIOGRAPHY & REFERENCES")
    add_bullet("[1]", "Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLOv8 (Version 8.0.0). Available at: https://github.com/ultralytics/ultralytics")
    add_bullet("[2]", "Zhang, F., Bazarevsky, V., Vakunov, A., Tkachenka, A., Sung, C., Chang, C. L., & Grundmann, M. (2020). MediaPipe Hands: On-device Real-time Hand Tracking. arXiv preprint arXiv:2006.10214.")
    add_bullet("[3]", "Abadi, M., et al. (2016). TensorFlow: A System for Large-Scale Machine Learning. 12th USENIX Symposium on Operating Systems Design and Implementation (OSDI 16), pp. 265-283.")
    add_bullet("[4]", "Chollet, F. (2018). Deep Learning with Python. Manning Publications Co., Shelter Island, NY.")
    add_bullet("[5]", "Bradski, G. (2000). The OpenCV Library. Dr. Dobb's Journal of Software Tools.")
    add_bullet("[6]", "Streamlit Inc. (2023). Streamlit: The fastest way to build and share data apps. Documentation available at: https://docs.streamlit.io/")
    add_bullet("[7]", "ElevenLabs Inc. (2024). ElevenLabs Neural Text-to-Speech API. Documentation available at: https://elevenlabs.io/docs")
    add_bullet("[8]", "World Health Organization (2023). Deafness and Hearing Loss. WHO Fact Sheets. Available at: https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss")
    add_bullet("[9]", "American Sign Language Linguistic Research Project (2021). ASL Handshape and Lexical Database. Boston University.")

    # Save to both target locations
    target_primary = ROOT_DIR / "Signly_Deep_Learning_Project_Report.docx"
    target_formatted = ROOT_DIR / "Signly_Formatted_Project_Report_A4.docx"

    saved_paths = []
    # Try primary
    try:
        doc.save(str(target_primary))
        saved_paths.append(str(target_primary))
        print(f"SUCCESS: Saved primary file -> {target_primary}")
    except PermissionError:
        print(f"NOTE: {target_primary.name} is currently open in Word. Saving to alternate path.")

    # Always save formatted A4 version
    try:
        doc.save(str(target_formatted))
        saved_paths.append(str(target_formatted))
        print(f"SUCCESS: Saved formatted A4 file -> {target_formatted}")
    except Exception as e:
        print(f"Error saving formatted docx: {e}")

    return saved_paths

if __name__ == "__main__":
    paths = build_formatted_report()
    print("Report build completed. Output files:", paths)
