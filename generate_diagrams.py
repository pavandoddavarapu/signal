import os
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, BoxStyle

output_dir = Path(__file__).resolve().parent / "assets" / "generated_diagrams"
output_dir.mkdir(parents=True, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

def create_dfd_diagram():
    fig, ax = plt.subplots(figsize=(6.5, 4.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Title
    ax.text(50, 95, "Level 0 & Level 1 Data Flow Diagrams (Signly)", fontsize=11, fontweight='bold', ha='center', color='#1E293B')
    
    # Level 0 Container
    ax.text(5, 84, "Level 0 DFD (Context Level):", fontsize=9, fontweight='bold', color='#334155')
    
    # Entities
    b1 = FancyBboxPatch((4, 66), 18, 12, boxstyle="round,pad=1,rounding_size=2", fc="#EFF6FF", ec="#3B82F6", lw=1.5)
    ax.add_patch(b1)
    ax.text(13, 72, "Signer / User\n(Video Input)", ha='center', va='center', fontsize=8, fontweight='bold', color='#1E3A8A')
    
    b2 = FancyBboxPatch((38, 66), 24, 12, boxstyle="round,pad=1,rounding_size=2", fc="#ECFDF5", ec="#10B981", lw=1.5)
    ax.add_patch(b2)
    ax.text(50, 72, "Signly Core System\n(0.0 Translation Engine)", ha='center', va='center', fontsize=8, fontweight='bold', color='#065F46')
    
    b3 = FancyBboxPatch((76, 66), 20, 12, boxstyle="round,pad=1,rounding_size=2", fc="#FAF5FF", ec="#8B5CF6", lw=1.5)
    ax.add_patch(b3)
    ax.text(86, 72, "Hearing User\n(Text & Speech Audio)", ha='center', va='center', fontsize=8, fontweight='bold', color='#5B21B6')
    
    ax.annotate("", xy=(38, 72), xytext=(22, 72), arrowprops=dict(arrowstyle="->", lw=1.5, color='#3B82F6'))
    ax.text(30, 75, "Raw Video", ha='center', fontsize=7, color='#1E3A8A')
    
    ax.annotate("", xy=(76, 72), xytext=(62, 72), arrowprops=dict(arrowstyle="->", lw=1.5, color='#10B981'))
    ax.text(69, 75, "Spoken Words", ha='center', fontsize=7, color='#065F46')

    # Separator line
    ax.plot([4, 96], [58, 58], color='#CBD5E1', lw=1, linestyle='--')

    # Level 1 DFD
    ax.text(5, 52, "Level 1 DFD (Decomposed Sub-Processes):", fontsize=9, fontweight='bold', color='#334155')
    
    procs = [
        ("1.0 Ingestion", "WebRTC Video", 4, 32, "#EFF6FF", "#3B82F6"),
        ("2.0 Localization", "YOLOv8 Hand Box", 28, 32, "#EFF6FF", "#3B82F6"),
        ("3.0 Extraction", "MediaPipe 21 Joint", 52, 32, "#EFF6FF", "#3B82F6"),
        ("4.0 Inference", "Keras Deep MLP", 76, 32, "#EFF6FF", "#3B82F6"),
        ("5.0 Stabilizer", "Hysteresis Window", 28, 8, "#ECFDF5", "#10B981"),
        ("6.0 Sentence", "State Machine", 52, 8, "#ECFDF5", "#10B981"),
        ("7.0 Synthesis", "ElevenLabs Neural", 76, 8, "#FAF5FF", "#8B5CF6"),
    ]
    
    for title, sub, x, y, fc, ec in procs:
        box = FancyBboxPatch((x, y), 20, 14, boxstyle="round,pad=1,rounding_size=2", fc=fc, ec=ec, lw=1.2)
        ax.add_patch(box)
        ax.text(x+10, y+8.5, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0F172A')
        ax.text(x+10, y+4.5, sub, ha='center', va='center', fontsize=6.5, color='#475569')

    # Connect top row
    ax.annotate("", xy=(28, 39), xytext=(24, 39), arrowprops=dict(arrowstyle="->", lw=1.2, color='#64748B'))
    ax.annotate("", xy=(52, 39), xytext=(48, 39), arrowprops=dict(arrowstyle="->", lw=1.2, color='#64748B'))
    ax.annotate("", xy=(76, 39), xytext=(72, 39), arrowprops=dict(arrowstyle="->", lw=1.2, color='#64748B'))
    
    # Down to row 2
    ax.annotate("", xy=(86, 22), xytext=(86, 32), arrowprops=dict(arrowstyle="->", lw=1.2, color='#64748B'))
    ax.annotate("", xy=(48, 15), xytext=(76, 22), arrowprops=dict(arrowstyle="->", lw=1.2, color='#64748B'))
    ax.annotate("", xy=(48, 15), xytext=(38, 15), arrowprops=dict(arrowstyle="<-", lw=1.2, color='#64748B'))
    ax.annotate("", xy=(76, 15), xytext=(72, 15), arrowprops=dict(arrowstyle="->", lw=1.2, color='#64748B'))

    plt.tight_layout()
    out = output_dir / "diagram_dfd.png"
    plt.savefig(out, bbox_inches='tight')
    plt.close()
    return out

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 105)
    ax.axis('off')
    
    ax.text(50, 100, "Signly End-to-End Pipeline Architecture", fontsize=11, fontweight='bold', ha='center', color='#0F172A')
    
    stages = [
        ("Input Source", "Webcam Video Stream\n(WebRTC 30 FPS / Video File)", "#F8FAFC", "#64748B"),
        ("Stage 1: Detection", "YOLOv8 Hand Localization\n(mAP@50 > 92%, Bounding Box)", "#EFF6FF", "#3B82F6"),
        ("Stage 2: Landmarks", "MediaPipe 21 Joint Extraction\n(3D Coordinates x, y, z)", "#EFF6FF", "#2563EB"),
        ("Stage 3: Normalization", "Wrist Origin & Knuckle Scale\n(Canonical 63-D Vector)", "#EEF2FF", "#4F46E5"),
        ("Stage 4: Classifier", "TensorFlow/Keras Deep MLP\n(29 Classes: 26 ASL + 3 Control)", "#F0FDF4", "#16A34A"),
        ("Stage 5: Stabilizer", "Temporal Consensus & Latch\n(5-Frame Filter, Tau >= 70%)", "#FEFCE8", "#CA8A04"),
        ("Stage 6: Composition", "Sentence Builder Engine\n(Append, Space, Delete, Clear)", "#FFF7ED", "#EA580C"),
        ("Stage 7: Audio Synth", "ElevenLabs Neural Speech\n(Natural Human Voice Playback)", "#FAF5FF", "#9333EA")
    ]
    
    # 2 columns layout
    # Left column: 0, 1, 2, 3
    # Right column: 4, 5, 6, 7
    y_starts = [80, 58, 36, 14]
    
    for i in range(4):
        title, desc, fc, ec = stages[i]
        b = FancyBboxPatch((4, y_starts[i]), 42, 16, boxstyle="round,pad=1,rounding_size=2", fc=fc, ec=ec, lw=1.4)
        ax.add_patch(b)
        ax.text(6, y_starts[i]+11.5, title, fontsize=8, fontweight='bold', color='#0F172A')
        ax.text(6, y_starts[i]+4.5, desc, fontsize=7, color='#334155')
        if i < 3:
            ax.annotate("", xy=(25, y_starts[i+1]+16), xytext=(25, y_starts[i]), arrowprops=dict(arrowstyle="->", lw=1.4, color='#3B82F6'))

    # Right column
    for i in range(4):
        title, desc, fc, ec = stages[4+i]
        b = FancyBboxPatch((54, y_starts[i]), 42, 16, boxstyle="round,pad=1,rounding_size=2", fc=fc, ec=ec, lw=1.4)
        ax.add_patch(b)
        ax.text(56, y_starts[i]+11.5, title, fontsize=8, fontweight='bold', color='#0F172A')
        ax.text(56, y_starts[i]+4.5, desc, fontsize=7, color='#334155')
        if i < 3:
            ax.annotate("", xy=(75, y_starts[i+1]+16), xytext=(75, y_starts[i]), arrowprops=dict(arrowstyle="->", lw=1.4, color='#16A34A'))

    # Arrow from Stage 3 to Stage 4 (Across columns)
    ax.annotate("", xy=(75, 96), xytext=(25, 14),
                arrowprops=dict(arrowstyle="->", lw=1.5, color='#4F46E5', connectionstyle="arc3,rad=-0.45"))
    ax.text(49, 52, "Normalized\n63-D Vector", fontsize=7.5, fontweight='bold', ha='center', color='#4F46E5',
            bbox=dict(boxstyle="round,pad=0.3", fc="#EEF2FF", ec="#818CF8", lw=1))

    plt.tight_layout()
    out = output_dir / "diagram_architecture.png"
    plt.savefig(out, bbox_inches='tight')
    plt.close()
    return out

def create_master_flowchart():
    fig, ax = plt.subplots(figsize=(6.5, 8.5), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 180)
    ax.axis('off')

    ax.text(50, 175, "Master System Flowchart (Signly Execution Flow)", fontsize=11, fontweight='bold', ha='center', color='#0F172A')

    def draw_oval(x, y, w, h, text, fc="#EFF6FF", ec="#2563EB"):
        b = FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=1,rounding_size=6", fc=fc, ec=ec, lw=1.5)
        ax.add_patch(b)
        ax.text(x, y, text, ha='center', va='center', fontsize=8, fontweight='bold', color='#1E293B')

    def draw_box(x, y, w, h, title, sub="", fc="#F8FAFC", ec="#64748B"):
        b = FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=1,rounding_size=2", fc=fc, ec=ec, lw=1.3)
        ax.add_patch(b)
        if sub:
            ax.text(x, y+2, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0F172A')
            ax.text(x, y-3, sub, ha='center', va='center', fontsize=6.5, color='#475569')
        else:
            ax.text(x, y, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#0F172A')

    def draw_diamond(x, y, w, h, text, fc="#FEFCE8", ec="#CA8A04"):
        diamond = patches.Polygon([[x, y+h/2], [x+w/2, y], [x, y-h/2], [x-w/2, y]], fc=fc, ec=ec, lw=1.3)
        ax.add_patch(diamond)
        ax.text(x, y, text, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#854D0E')

    # Steps from top to bottom
    draw_oval(50, 166, 32, 8, "START: Initialize System", "#EFF6FF", "#2563EB")
    ax.annotate("", xy=(50, 158), xytext=(50, 162), arrowprops=dict(arrowstyle="->", lw=1.2, color='#334155'))

    draw_box(50, 153, 44, 8, "Capture Frame via WebRTC", "RGB 640x480 @ 30 FPS")
    ax.annotate("", xy=(50, 145), xytext=(50, 149), arrowprops=dict(arrowstyle="->", lw=1.2, color='#334155'))

    draw_diamond(50, 137, 34, 12, "Hand Detected\nby YOLOv8?")
    
    # Hand NO branch
    ax.annotate("", xy=(84, 137), xytext=(67, 137), arrowprops=dict(arrowstyle="->", lw=1.2, color='#DC2626'))
    ax.text(73, 139, "No", fontsize=7.5, fontweight='bold', color='#DC2626')
    draw_box(84, 122, 26, 9, "Release Latch\n& Retain State", fc="#FEF2F2", ec="#EF4444")
    ax.annotate("", xy=(84, 126), xytext=(84, 137), arrowprops=dict(lw=1.2, color='#DC2626'))
    ax.annotate("", xy=(50, 24), xytext=(84, 117), arrowprops=dict(arrowstyle="->", lw=1.2, color='#DC2626', connectionstyle="arc3,rad=0.3"))

    # Hand YES branch
    ax.annotate("", xy=(50, 126), xytext=(50, 131), arrowprops=dict(arrowstyle="->", lw=1.2, color='#16A34A'))
    ax.text(53, 128, "Yes", fontsize=7.5, fontweight='bold', color='#16A34A')
    
    draw_box(50, 121, 46, 8, "Extract MediaPipe 21 3D Landmarks", "Wrist (p0) & Knuckles (p9)")
    ax.annotate("", xy=(50, 113), xytext=(50, 117), arrowprops=dict(arrowstyle="->", lw=1.2, color='#334155'))

    draw_box(50, 108, 48, 8, "Geometric Normalization", "Origin Centering + Knuckle Scale (63-D)")
    ax.annotate("", xy=(50, 100), xytext=(50, 104), arrowprops=dict(arrowstyle="->", lw=1.2, color='#334155'))

    draw_box(50, 95, 46, 8, "Deep Keras MLP Inference", "Softmax Probability across 29 Classes")
    ax.annotate("", xy=(50, 87), xytext=(50, 91), arrowprops=dict(arrowstyle="->", lw=1.2, color='#334155'))

    draw_diamond(50, 79, 36, 12, "Confidence >=\nThreshold (70%)?")
    
    # Confidence NO branch
    ax.annotate("", xy=(18, 79), xytext=(32, 79), arrowprops=dict(arrowstyle="->", lw=1.2, color='#DC2626'))
    ax.text(25, 81, "No", fontsize=7.5, fontweight='bold', color='#DC2626')
    draw_box(16, 68, 24, 8, "Reset Sliding\nBuffer", fc="#FEF2F2", ec="#EF4444")
    ax.annotate("", xy=(16, 72), xytext=(16, 79), arrowprops=dict(lw=1.2, color='#DC2626'))
    ax.annotate("", xy=(50, 24), xytext=(16, 64), arrowprops=dict(arrowstyle="->", lw=1.2, color='#DC2626', connectionstyle="arc3,rad=-0.3"))

    # Confidence YES branch
    ax.annotate("", xy=(50, 68), xytext=(50, 73), arrowprops=dict(arrowstyle="->", lw=1.2, color='#16A34A'))
    ax.text(53, 70, "Yes", fontsize=7.5, fontweight='bold', color='#16A34A')

    draw_diamond(50, 61, 38, 11, "5 Consecutive\nFrames Match?")

    # Match NO branch
    ax.annotate("", xy=(18, 61), xytext=(31, 61), arrowprops=dict(arrowstyle="->", lw=1.2, color='#CA8A04'))
    ax.text(25, 63, "No", fontsize=7.5, fontweight='bold', color='#CA8A04')
    ax.annotate("", xy=(16, 64), xytext=(18, 61), arrowprops=dict(arrowstyle="->", lw=1.2, color='#CA8A04'))

    # Match YES branch
    ax.annotate("", xy=(50, 51), xytext=(50, 55), arrowprops=dict(arrowstyle="->", lw=1.2, color='#16A34A'))
    ax.text(53, 53, "Yes", fontsize=7.5, fontweight='bold', color='#16A34A')

    draw_box(50, 46, 48, 8, "Fire Gesture: SentenceBuilder Action", "Append Letter / Space / Delete / Clear", fc="#F0FDF4", ec="#16A34A")
    ax.annotate("", xy=(50, 38), xytext=(50, 42), arrowprops=dict(arrowstyle="->", lw=1.2, color='#334155'))

    draw_diamond(50, 31, 36, 11, "User Pressed\n'Play Speech'?")

    # Speech YES
    ax.annotate("", xy=(82, 31), xytext=(68, 31), arrowprops=dict(arrowstyle="->", lw=1.2, color='#9333EA'))
    ax.text(72, 33, "Yes", fontsize=7.5, fontweight='bold', color='#9333EA')
    draw_box(82, 17, 26, 9, "ElevenLabs TTS\nSynthesize Audio", fc="#FAF5FF", ec="#9333EA")
    ax.annotate("", xy=(82, 21), xytext=(82, 31), arrowprops=dict(lw=1.2, color='#9333EA'))

    # Speech NO
    ax.annotate("", xy=(50, 21), xytext=(50, 25), arrowprops=dict(arrowstyle="->", lw=1.2, color='#334155'))
    ax.text(53, 23, "No", fontsize=7.5, fontweight='bold', color='#64748B')

    draw_oval(50, 15, 34, 8, "Update UI & Next Frame", "#EFF6FF", "#2563EB")
    ax.annotate("", xy=(67, 15), xytext=(69, 17), arrowprops=dict(arrowstyle="<-", lw=1.2, color='#9333EA'))

    plt.tight_layout()
    out = output_dir / "diagram_master_flowchart.png"
    plt.savefig(out, bbox_inches='tight')
    plt.close()
    return out

def create_usecase_diagram():
    fig, ax = plt.subplots(figsize=(6.5, 4.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Use Case Diagram (Signly System Actors & Actions)", fontsize=11, fontweight='bold', ha='center', color='#0F172A')

    # System boundary box
    box = FancyBboxPatch((30, 8), 65, 80, boxstyle="round,pad=1,rounding_size=3", fc="#F8FAFC", ec="#0EA5E9", lw=1.5, linestyle='--')
    ax.add_patch(box)
    ax.text(62.5, 84, "Signly Application Boundary", ha='center', fontsize=9, fontweight='bold', color='#0284C7')

    # Actor: User
    ax.plot([12, 12], [48, 60], color='#1E293B', lw=2) # body
    circle = patches.Circle((12, 66), 5, fc="#E2E8F0", ec="#1E293B", lw=2) # head
    ax.add_patch(circle)
    ax.plot([4, 20], [54, 54], color='#1E293B', lw=2) # arms
    ax.plot([12, 6], [48, 38], color='#1E293B', lw=2) # left leg
    ax.plot([12, 18], [48, 38], color='#1E293B', lw=2) # right leg
    ax.text(12, 32, "Deaf User / Signer\n(Actor)", ha='center', fontsize=8, fontweight='bold', color='#0F172A')

    use_cases = [
        ("UC-1: Start WebRTC Live Video Stream", 72),
        ("UC-2: Upload Recorded Sign Video", 58),
        ("UC-3: Perform Real-Time ASL Signs", 44),
        ("UC-4: Edit Sentence (Space/Delete/Clear)", 30),
        ("UC-5: Synthesize Speech via ElevenLabs", 16)
    ]

    for title, y in use_cases:
        oval = FancyBboxPatch((36, y-5), 54, 10, boxstyle="round,pad=1,rounding_size=5", fc="#EFF6FF", ec="#3B82F6", lw=1.2)
        ax.add_patch(oval)
        ax.text(63, y, title, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1E3A8A')
        ax.annotate("", xy=(36, y), xytext=(21, 54), arrowprops=dict(arrowstyle="->", lw=1.2, color='#64748B'))

    plt.tight_layout()
    out = output_dir / "diagram_usecase.png"
    plt.savefig(out, bbox_inches='tight')
    plt.close()
    return out

def create_class_diagram():
    fig, ax = plt.subplots(figsize=(6.5, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 105)
    ax.axis('off')

    ax.text(50, 100, "Class Diagram: Core OOP Architecture (signlens)", fontsize=11, fontweight='bold', ha='center', color='#0F172A')

    classes = [
        ("YOLOHandDetector", [
            "- model: YOLO",
            "- conf_threshold: float = 0.5",
            "+ detect(frame): (crop, bbox)"
        ], 4, 62, 42, 30, "#EFF6FF", "#3B82F6"),
        ("SignRecognizer", [
            "- model: tf.keras.Model",
            "- scaler_mean: ndarray(63,)",
            "- scaler_scale: ndarray(63,)",
            "+ predict(features): (str, float)"
        ], 54, 62, 42, 30, "#EFF6FF", "#3B82F6"),
        ("PredictionStabilizer", [
            "- window_size: int = 5",
            "- min_confidence: float = 0.70",
            "- waiting_for_release: bool",
            "+ update(letter, conf): str",
            "+ release(): void"
        ], 4, 16, 42, 38, "#ECFDF5", "#10B981"),
        ("SentenceBuilder", [
            "- text: str = ''",
            "+ add_letter(l: str): void",
            "+ add_space(): void",
            "+ backspace(): void",
            "+ clear(): void",
            "+ get_text(): str"
        ], 54, 16, 42, 38, "#FFF7ED", "#EA580C")
    ]

    for name, methods, x, y, w, h, fc, ec in classes:
        b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1,rounding_size=2", fc=fc, ec=ec, lw=1.4)
        ax.add_patch(b)
        ax.text(x+w/2, y+h-4.5, name, ha='center', fontsize=8, fontweight='bold', color='#0F172A')
        ax.plot([x, x+w], [y+h-8, y+h-8], color=ec, lw=1)
        for idx, m in enumerate(methods):
            ax.text(x+2, y+h-13-(idx*4.5), m, fontsize=6.8, fontfamily='monospace', color='#334155')

    # Connectors
    ax.annotate("", xy=(54, 77), xytext=(46, 77), arrowprops=dict(arrowstyle="<|-|>", lw=1.3, color='#475569'))
    ax.annotate("", xy=(25, 54), xytext=(25, 62), arrowprops=dict(arrowstyle="->", lw=1.3, color='#475569'))
    ax.annotate("", xy=(75, 54), xytext=(75, 62), arrowprops=dict(arrowstyle="->", lw=1.3, color='#475569'))
    ax.annotate("", xy=(54, 35), xytext=(46, 35), arrowprops=dict(arrowstyle="->", lw=1.3, color='#475569'))

    plt.tight_layout()
    out = output_dir / "diagram_class.png"
    plt.savefig(out, bbox_inches='tight')
    plt.close()
    return out

if __name__ == "__main__":
    print("Generating diagrams...")
    f1 = create_dfd_diagram()
    print("DFD generated:", f1)
    f2 = create_architecture_diagram()
    print("Architecture generated:", f2)
    f3 = create_master_flowchart()
    print("Flowchart generated:", f3)
    f4 = create_usecase_diagram()
    print("Use Case generated:", f4)
    f5 = create_class_diagram()
    print("Class Diagram generated:", f5)
    print("All diagrams generated successfully!")
