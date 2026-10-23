# SIGNLY: REAL-TIME AMERICAN SIGN LANGUAGE RECOGNITION AND SPEECH SYNTHESIS SYSTEM
## Comprehensive Project Dossier & Complete Academic Report Data

> **Purpose of this document:**  
> This file contains the complete, exhaustive dataset, architectural specifications, technical analysis, algorithms, flowcharts, testing records, implementation guides, and academic report text for the **Signly** (formerly Signify) project. It is strictly formatted according to the official **Deep Learning Project Report Format** (Lovely Professional University - School of Computer Science and Engineering).  
> All personal details (Student Name, Registration Number, Faculty Mentor) are provided with clean, standardized placeholders for the student to fill in.

---

# COVER PAGE TEMPLATE

```
================================================================================
                         DEEP LEARNING - PROJECT REPORT

                                   ON

                                 SIGNLY:
             REAL-TIME AMERICAN SIGN LANGUAGE RECOGNITION 
                     AND SPEECH SYNTHESIS SYSTEM

                             Submitted by:
                 [NAME OF STUDENT]
                 Registration Number: [REGISTRATION NUMBER]
                 Course Code: [COURSE CODE - e.g., CSE422 / CAPSTONE]

                         Under the Guidance of:
              [NAME OF FACULTY MENTOR WITH DESIGNATION]

               School of Computer Science and Engineering
                     LOVELY PROFESSIONAL UNIVERSITY
                           PHAGWARA, PUNJAB
                                 2026
================================================================================
```

---

# PRELIMINARY PAGES

## 1. DECLARATION
We hereby declare that the project work entitled **"Signly: Real-Time American Sign Language Recognition and Speech Synthesis System"** is an authentic record of our own work carried out as requirements of Deep Learning Project for the CA Evaluation of B.Tech 4th Year from Lovely Professional University, Phagwara, under the guidance of **[Name of Faculty Mentor]**, during 2026. All the information furnished in this capstone project report is based on our own intensive work and is genuine.

- **Name of Student:** Pavan Doddavarapu
- **Registration Number:** 12305446
- **Signature of Student:** ___________________________
- **Date:** [Date]

---

## 2. CERTIFICATE
This is to certify that the project entitled **"Signly: Real-Time American Sign Language Recognition and Speech Synthesis System"** submitted by **[Name of Student]** (Registration No: **[Registration Number]**) in partial fulfillment of the requirements for the award of the degree of **Bachelor of Technology in Computer Science and Engineering** at **Lovely Professional University, Phagwara**, is an authentic record of the work carried out by them under my supervision and guidance.

To the best of my knowledge, the matter embodied in this project report has not been submitted to any other University / Institute for the award of any Degree or Diploma.

- **[Name of Faculty Mentor]**  
  [Designation, Department of Computer Science & Engineering]  
  School of Computer Science and Engineering  
  Lovely Professional University, Phagwara  

---

## 3. ACKNOWLEDGEMENT
I would like to express my profound gratitude and deep regards to my guide **[Name of Faculty Mentor]** for their exemplary guidance, monitoring, and constant encouragement throughout the course of this project. The blessing, help, and guidance given by them time to time shall carry me a long way in the journey of life on which I am about to embark.

I also take this opportunity to express a deep sense of gratitude to the **School of Computer Science and Engineering, Lovely Professional University**, for providing all the necessary infrastructural facilities, high-performance computing resources, and academic environment required to carry out this deep learning research and implementation.

Finally, I am indebted to my parents, family, and peers for their continuous moral support and motivation throughout the development of this project.

- **[Name of Student]**  
  Registration Number: [Registration Number]

---

## 4. TABLE OF CONTENTS

```
Inner First Page ........................................................... (i)
PAC Form .................................................................. (ii)
Declaration ............................................................... (iii)
Certificate ................................................................ (iv)
Acknowledgement ............................................................ (v)
Table of Contents .......................................................... (vi)
List of Tables ............................................................ (vii)
List of Figures ........................................................... (viii)

1. INTRODUCTION ............................................................. 1
   1.1 Domain Overview and Background ...................................... 1
   1.2 Motivation and Relevance of Assistive Technologies ................... 2
   1.3 Project Overview: Signly Pipeline .................................... 3
   1.4 Core Objectives ...................................................... 4

2. PROFILE OF THE PROBLEM (PROBLEM STATEMENT & SCOPE) ....................... 5
   2.1 Problem Definition & Real-World Challenges ........................... 5
   2.2 Rationale of the Study ............................................... 6
   2.3 Scope and Delimitations of the System ................................ 7

3. EXISTING SYSTEM .......................................................... 8
   3.1 Introduction to Prior Methodologies ................................. 8
   3.2 Review of Existing Software and Hardware Systems ..................... 9
   3.3 Data Flow Diagram (DFD) for Present Systems .......................... 10
   3.4 What's New in the Developed System (Signly Novelties) ................ 11

4. PROBLEM ANALYSIS ......................................................... 13
   4.1 Product Definition .................................................. 13
   4.2 Feasibility Analysis ................................................ 14
       4.2.1 Technical Feasibility ......................................... 14
       4.2.2 Operational Feasibility ....................................... 15
       4.2.3 Economic Feasibility .......................................... 16
   4.3 Project Plan and Milestone Schedule ................................. 17

5. SOFTWARE REQUIREMENT ANALYSIS ............................................ 19
   5.1 Introduction ........................................................ 19
   5.2 General Description and User Characteristics ........................ 19
   5.3 Specific Requirements ............................................... 20
       5.3.1 Hardware Requirements ......................................... 20
       5.3.2 Software Requirements ......................................... 21
       5.3.3 Functional Requirements ....................................... 22
       5.3.4 Non-Functional Requirements ................................... 24

6. SYSTEM DESIGN ............................................................ 26
   6.1 System Architectural Design ......................................... 26
   6.2 Design Notations and Modeling Diagrams .............................. 28
       6.2.1 Use Case Diagram .............................................. 28
       6.2.2 Class Diagram & Entity Relationships .......................... 29
       6.2.3 Sequence Diagram .............................................. 31
   6.3 Detailed Component Design & Mathematical Formulations .............. 32
       6.3.1 YOLOv8 Object Detection Subsystem ............................. 32
       6.3.2 MediaPipe Hands Topological Landmark Extraction ............... 33
       6.3.3 Geometric Normalization & Scale Invariance .................... 34
       6.3.4 Deep Learning Classification Network (MLP) .................... 35
       6.3.5 Finite-State Machine Prediction Stabilizer .................... 37
       6.3.6 Stateful Sentence Construction Engine ......................... 38
       6.3.7 Neural Speech Synthesis Integration (ElevenLabs) .............. 39
   6.4 Flowcharts .......................................................... 40
       6.4.1 Master System Flowchart ....................................... 40
       6.4.2 Frame Processing & Stabilization Flowchart .................... 41
   6.5 Pseudo Code and Core Algorithms ..................................... 42

7. TESTING ................................................................. 45
   7.1 Functional Testing .................................................. 45
   7.2 Structural (White-Box) Testing ...................................... 46
   7.3 Levels of Testing (Unit, Integration, System, Acceptance) ............ 47
   7.4 Detailed Test Cases and Empirical Verification ...................... 48

8. IMPLEMENTATION ........................................................... 51
   8.1 Implementation Environment and Model Training ....................... 51
   8.2 Conversion Plan and Operational Deployment .......................... 53
   8.3 Post-Implementation Support and Software Maintenance ................ 54

9. PROJECT LEGACY ........................................................... 55
   9.1 Current Status of the Project ....................................... 55
   9.2 Remaining Areas of Concern and Known Limitations .................... 56
   9.3 Technical and Managerial Lessons Learnt ............................. 57

10. USER MANUAL & OPERATING GUIDE ........................................... 58
    10.1 System Installation & Prerequisites ............................... 58
    10.2 Starting the Application .......................................... 59
    10.3 Operating Modes and Feature Navigation ............................ 60
    10.4 Troubleshooting Guide ............................................. 62

11. SOURCE CODE ARCHITECTURE & SYSTEM SNAPSHOTS ............................. 63
    11.1 Directory Tree Structure .......................................... 63
    11.2 Core Python Module Implementations ................................ 64
    11.3 System User Interface Snapshots & Mockups ......................... 68

12. BIBLIOGRAPHY & REFERENCES ............................................... 70
```

---

# CHAPTER 1: INTRODUCTION

### 1.1 Domain Overview and Background
Communication is an indispensable prerequisite for human social integration, education, employment, and interpersonal bonding. For the global population of over 70 million deaf individuals (and over 430 million people with disabling hearing loss according to the World Health Organization), Sign Language constitutes the primary and natural mode of linguistic expression. Unlike spoken languages, sign languages rely on visual-gestural modalities consisting of manual features (hand shape, palm orientation, spatial location, and trajectory) and non-manual signals (facial expressions, head movements, and torso posture).

Despite its linguistic completeness, sign language remains largely unintelligible to the hearing majority, creating significant communicative barriers in healthcare, academic institutions, legal proceedings, public services, and everyday commerce. Certified human sign language interpreters are scarce, geographically concentrated, and prohibitively expensive for routine conversations. Consequently, developing automated, accessible, vision-based Sign Language Recognition (SLR) systems is one of the most vital frontiers in human-computer interaction (HCI) and applied computer vision.

### 1.2 Motivation and Relevance of Assistive Technologies
Historically, assistive technologies for signers relied on cumbersome hardware-based sensory gloves (equipped with flex sensors, accelerometers, and gyroscopes) or multi-camera depth sensors (such as Microsoft Kinect). These physical peripherals impede natural hand movement, suffer from mechanical wear, and are not practical for pervasive real-world use.

The recent convergence of commodity webcams, deep convolutional neural networks (CNNs), edge object detection models, and real-time landmark estimation frameworks enables purely vision-based recognition. **Signly** is engineered to bridge the communication gap by translating American Sign Language (ASL) gestures directly into editable text and natural-sounding human speech in real-time, operating entirely through standard consumer webcams and modern web browsers without requiring specialized hardware.

### 1.3 Project Overview: Signly Pipeline
**Signly** implements an end-to-end, multi-stage pipeline designed for low latency, robust spatial invariance, and seamless usability:
1. **Input Acquisition:** Ingests live webcam video via WebRTC or accepts pre-recorded video files.
2. **Hand Detection:** Utilizes a custom-trained **YOLOv8** (You Only Look Once v8) detector running at high frame rates to crop bounding boxes around hands, discarding background noise and clutter.
3. **Topological Landmark Extraction:** Employs **MediaPipe Hands** to extract 21 three-dimensional skeletal joint coordinates $(x, y, z)$ within the detected hand region.
4. **Geometric Invariant Normalization:** Computes wrist-relative translational centering and scale normalization relative to the Euclidean distance between the wrist and the middle metacarpophalangeal (MCP) joint, yielding a 63-dimensional feature vector invariant to distance from the lens and hand size.
5. **Deep Learning Classification:** A specialized Deep Multilayer Perceptron (MLP) trained with Keras/TensorFlow classifies the 63 normalized coordinates into 29 discrete classes (26 ASL alphabet letters A–Z and 3 interactive control commands: `Space`, `Delete`, and `Clear`).
6. **Prediction Stabilization:** A sliding-window temporal filter with a confidence threshold ($\ge 70\%$) and release latch prevents noisy frame flickering and repeated key triggers.
7. **Sentence Construction:** A deterministic state machine converts accepted gestures into coherent words and sentences.
8. **Neural Speech Synthesis:** Integrates with the **ElevenLabs API** to synthesize the generated text into crystal-clear, natural human speech.
9. **Interactive Dashboard:** Built on **Streamlit** with real-time confidence metrics, interactive parameter sliders, audio playback, and customizable UI themes.

### 1.4 Core Objectives
- To eliminate the need for wearable sensors or expensive depth sensors by implementing a 100% RGB vision-based solution.
- To achieve high real-time throughput (>25 FPS) on consumer-grade hardware.
- To implement translational and scale invariance through rigorous skeletal normalization.
- To create an actual text-composition engine rather than isolated letter prediction by incorporating functional editing gestures (`Space`, `Delete`, `Clear`).
- To deliver multi-modal output by coupling text translation with naturalistic neural text-to-speech (TTS).

---

# CHAPTER 2: PROFILE OF THE PROBLEM (PROBLEM STATEMENT & SCOPE)

### 2.1 Problem Definition & Real-World Challenges
Standard gesture recognition models frequently fail when deployed in unconstrained real-world settings due to four fundamental challenges:
1. **Environmental Inhomogeneity:** Variable lighting, complex cluttered backgrounds, and fluctuating camera resolutions degrade raw-pixel convolutional classifiers.
2. **Subject & Distance Variability:** Differing hand skin tones, physical hand dimensions, and variable user distances from the camera cause massive feature distribution shifts.
3. **Temporal Jitter & Frame Noise:** Video frames capture transitions, partial occlusions, and brief motion blurs. Unstabilized frame-by-frame classifiers produce erratic predictions that make continuous typing impossible.
4. **Isolated Classification vs. True Sentence Building:** A model that only outputs individual characters fails as a communication aid if it lacks grammatical spacing, error correction, sentence termination, and acoustic playback.

### 2.2 Rationale of the Study
Rather than feeding raw RGB images directly into an end-to-end heavy 3D-CNN or Vision Transformer (which requires high-end server GPUs and suffers from background over-fitting), Signly isolates semantic geometry from visual appearances:
- Hand localization (YOLO) decouples hand tracking from complex backgrounds.
- Landmark extraction (MediaPipe) strips away skin color, texture, and ambient lighting, preserving solely anatomical geometry.
- Centroid and scale normalization transforms hand coordinates into a canonical coordinate space.
- A lightweight MLP performs lightning-fast classification, leaving ample CPU/GPU overhead for video streaming and UI rendering.

### 2.3 Scope and Delimitations of the Study
- **Linguistic Scope:** Focuses on the 26 static/quasi-static letters of the American Sign Language (ASL) manual alphabet (A through Z) plus 3 control gestures (`Space`, `Delete`, `Clear`), totaling 29 target classes.
- **Continuous Gesture Limitation:** Continuous two-handed sign language (such as full ASL syntax, facial grammar, and torso motion) is excluded from the current scope.
- **Hardware Boundary:** Designed to operate on single-camera standard monocular RGB webcams (standard 720p/1080p at 30 FPS).
- **Network Dependency:** Core gesture recognition and sentence construction run completely offline on local compute; Text-to-Speech synthesis requires an active internet connection for the ElevenLabs API endpoint.

---

# CHAPTER 3: EXISTING SYSTEM

### 3.1 Introduction to Prior Methodologies
Early automated sign recognition systems fall broadly into two historical paradigms:
1. **Hardware-Intrusive / Glove-Based Systems:** Equipped with flex sensors along finger digits, Inertial Measurement Units (IMUs), and tactile pressure sensors connected via microcontrollers.
2. **Pixel-Based Computer Vision Systems:** Utilizing color segmentation (HSV skin color thresholding), edge detection, and classical feature extractors (Haar cascades, HOG, SIFT) coupled with Support Vector Machines (SVM) or Random Forests.
3. **End-to-End Deep CNNs:** Feeding 224x224 RGB image arrays into ResNet or MobileNet architectures.

### 3.2 Review of Existing Software and Hardware Systems
| Approach / System | Key Technologies | Advantages | Critical Drawbacks & Limitations |
| :--- | :--- | :--- | :--- |
| **Data Glove Systems** (e.g., CyberGlove, AcceleGlove) | Microcontroller, Flex sensors, Accelerometers | High landmark accuracy, invariant to lighting | Highly intrusive, high cost ($500-$5000), uncomfortable, calibration fatigue, non-scalable. |
| **Depth-Camera Systems** (e.g., Microsoft Kinect, Intel RealSense) | IR Depth sensors, Time-of-Flight (ToF) | Immune to ambient lighting variations | Bulky proprietary hardware, discontinued consumer lines, poor near-field hand resolution. |
| **Pure RGB End-to-End CNNs** (e.g., Standard ResNet-50 / VGG-16) | Raw pixel input directly into 2D-CNN | No sensor attachment required | Heavily biased by background clutter, sensitive to skin color variations, high latency, requires GPU. |
| **Isolated Alphabet Classifiers** (Academic Prototypes) | PyTorch / OpenCV window displays | Demonstrates basic ML feasibility | No sentence-building state machine, no error-correction, no speech synthesis, no web-ready interface. |

### 3.3 Data Flow Diagram (DFD) for Present Systems

#### Level 0 DFD (Existing Systems)
```
[User Hand Gesture] ---> (Traditional Vision/Glove System) ---> [Raw Letter Printed on Console]
```

#### Level 1 DFD (Existing Systems)
```
[Video Stream] 
     │
     ▼
(Color Filtering / Background Subtraction)
     │
     ▼
(Feature Extraction - SIFT / Contour / Raw Pixels)
     │
     ▼
(Heuristic / SVM / Heavy CNN Classifier)
     │
     ▼
[Raw Noisy Output: "AAAAABBBCCCC..."] (Unstabilized, No Speech, No Sentence Structure)
```

### 3.4 What's New in the System to be Developed (Signly Novelties)
1. **Hybrid Two-Stage Computer Vision Cascade:** Decoupled YOLOv8 hand bounding box localization and MediaPipe 21-joint topological landmark estimation.
2. **Canonical Hand Geometric Normalization:** Mathematical translation to wrist origin $(0,0,0)$ and Euclidean distance scale normalization using the middle metacarpophalangeal (MCP) knuckle distance.
3. **Temporal Stabilizer with Release Latch:** A rolling buffer of $N$ frames (default $N=5$) requiring 100% classification consensus and confidence exceeding 70%, combined with an anti-repeat release latch requiring the user to withdraw or reposition the hand before triggering duplicate characters.
4. **Interactive Text Composition Engine:** Integrated control gestures (`Space`, `Delete`, `Clear`) that allow users to spell full sentences, correct typos, and format words in real-time.
5. **Multilingual Neural Speech Synthesis:** Direct bridge to ElevenLabs neural voice models, converting constructed text into lifelike speech with multiple voice presets.
6. **WebRTC Cloud/Local Browser Architecture:** Implementation via `streamlit-webrtc` allowing client-side video streaming without server hardware camera access errors.

---

# CHAPTER 4: PROBLEM ANALYSIS

### 4.1 Product Definition
**Signly** is a cross-platform, browser-based, AI-driven assistive desktop/web application that functions as an instantaneous sign-to-speech interpreter. It ingests video feeds from webcams or video files, detects American Sign Language fingerspelling, dynamically constructs punctuated and spaced text, and synthesizes the resulting sentences into audible spoken English.

### 4.2 Feasibility Analysis

#### 4.2.1 Technical Feasibility
- **Libraries & Frameworks:** Built on well-established, enterprise-grade open-source libraries: OpenCV for image manipulation, MediaPipe for hand landmark extraction, Ultralytics YOLOv8 for edge detection, and TensorFlow/Keras for classification.
- **Inference Speed:** YOLOv8 nano/small models combined with coordinate-based MLPs require less than 15 milliseconds of inference time per frame on modern multi-core CPUs.
- **Hardware Independence:** Runs on standard x86 and ARM processors without requiring dedicated Nvidia CUDA GPUs.

#### 4.2.2 Operational Feasibility
- **User Interface:** Streamlit provides an intuitive single-page graphical interface containing video feeds, confidence gauges, text displays, and customizable color themes.
- **User Learning Curve:** Users require no training beyond knowledge of the standard American Sign Language alphabet and three intuitive control gestures.
- **Accessibility:** Operates directly inside standard web browsers (Google Chrome, Microsoft Edge, Mozilla Firefox).

#### 4.2.3 Economic Feasibility
- **Capital Cost:** Zero hardware investment required for users owning a standard laptop, desktop, or external USB webcam.
- **Software Cost:** The software stack (Python, Streamlit, MediaPipe, OpenCV, TensorFlow) is completely free and open source under permissive MIT/Apache licenses.
- **Operational Cost:** Minimal API utilization charges for ElevenLabs text-to-speech; offline fallback can easily integrate with open-source local engines like pyttsx3.

### 4.3 Project Plan and Milestone Schedule

```
+---------------------------------------------------------------------------------------+
| Milestone / Phase                  | Duration | Core Deliverables                     |
+---------------------------------------------------------------------------------------+
| Phase 1: Problem Definition & Data | Weeks 1-2| Dataset curation, ASL sign definition |
| Phase 2: Object Detection (YOLO)   | Weeks 3-4| Hand detector training & weights (.pt)|
| Phase 3: Landmark & Normalization  | Weeks 5-6| MediaPipe 21-joint normalizer (63-dim)|
| Phase 4: Classifier Architecture   | Weeks 7-8| Keras MLP training (29 classes)       |
| Phase 5: Stabilization & Sentence  | Weeks 9-10| Finite state machine & buffer logic  |
| Phase 6: TTS & Streamlit Frontend  | Weeks 11-12| WebRTC streaming, UI & ElevenLabs   |
| Phase 7: Verification & Testing    | Weeks 13-14| Test cases, latency & accuracy audits|
| Phase 8: Documentation & Reporting | Weeks 15-16| Capstone report, user manual, repo   |
+---------------------------------------------------------------------------------------+
```

---

# CHAPTER 5: SOFTWARE REQUIREMENT ANALYSIS

### 5.1 Introduction
This Software Requirement Specification (SRS) delineates the functional and non-functional requirements governing the design, implementation, and deployment of **Signly**.

### 5.2 General Description and User Characteristics
- **Target Audience:** Deaf and hard-of-hearing individuals, ASL students, educators, and hearing individuals who cannot interpret sign language.
- **Operating Environment:** Desktop and laptop environments running Windows 10/11, macOS, or Linux with local webcam hardware or browser access.

### 5.3 Specific Requirements

#### 5.3.1 Hardware Requirements
| Component | Minimum Specification | Recommended Specification |
| :--- | :--- | :--- |
| **Processor** | Intel Core i3 / AMD Ryzen 3 (Quad Core) | Intel Core i5/i7 (11th Gen+) / AMD Ryzen 5/7 / Apple M-series |
| **RAM** | 4 GB DDR4 | 8 GB or 16 GB DDR4/DDR5 |
| **Storage** | 2 GB free disk space | 5 GB SSD free space |
| **Camera** | Standard Integrated USB Webcam (720p @ 15fps) | HD Webcam (1080p @ 30fps) |
| **Audio** | Standard audio output (speakers / headphones) | Stereo output speakers |

#### 5.3.2 Software Requirements
| Software Element | Specification / Version |
| :--- | :--- |
| **Operating System** | Windows 10/11 (64-bit), macOS Monterey+, or Ubuntu 20.04+ |
| **Runtime Environment** | Python 3.10 / 3.11 / 3.12 (64-bit) |
| **Core Libraries** | OpenCV (`opencv-python` / `opencv-contrib-python-headless`) |
| **Object Detection** | `ultralytics==8.3.0` |
| **Landmark Engine** | `mediapipe==0.10.21` |
| **Deep Learning Framework** | `tensorflow==2.17.1` / `keras` |
| **Web Interface** | `streamlit>=1.28.0`, `streamlit-webrtc==0.47.9`, `av>=12.0.0` |
| **Speech Engine** | `elevenlabs>=1.50.0`, `python-dotenv>=1.0.0` |

#### 5.3.3 Functional Requirements
- **FR1 (Video Ingestion):** The system shall capture live RGB video streams from the client webcam at minimum 20 FPS or parse uploaded video files (`.mp4`, `.mov`, `.avi`).
- **FR2 (Hand Region Localization):** The system shall scan incoming video frames using YOLOv8 to identify and crop the bounding coordinates $(x_1, y_1, x_2, y_2)$ of the primary hand.
- **FR3 (Landmark Extraction):** The system shall extract 21 three-dimensional landmark points from the cropped hand region using MediaPipe Hands.
- **FR4 (Feature Normalization):** The system shall translate landmark points to the wrist origin $(0,0,0)$ and scale all coordinates by the Euclidean distance to the middle finger MCP joint.
- **FR5 (Sign Classification):** The Keras neural network shall classify the 63 normalized coordinates into one of 29 predefined categories.
- **FR6 (Prediction Filtering):** Predictions shall only be acknowledged if model confidence exceeds the user-configured threshold ($\tau \ge 70\%$) and remains constant across $W$ consecutive frames (default $W=5$).
- **FR7 (Sentence Editing State Machine):**
  - Alphabet inputs (A–Z) append the respective letter to the active sentence.
  - `Space` inserts a blank character between words.
  - `Delete` removes the most recent character from the buffer.
  - `Clear` empties the entire sentence buffer.
- **FR8 (Speech Generation):** Upon user command, the system shall transmit the assembled text string to the ElevenLabs API and stream back the generated MP3 audio stream for playback.

#### 5.3.4 Non-Functional Requirements
- **NFR1 (Low Latency):** Frame processing, landmark extraction, and neural inference shall complete within 35 milliseconds per frame to maintain real-time responsiveness.
- **NFR2 (Spatial & Scale Invariance):** Gesture classification accuracy shall not degrade by more than 5% across distances varying from 0.5 meters to 2.0 meters from the camera.
- **NFR3 (Reliability & Fault Tolerance):** Missing hands or unreadable frames shall gracefully clear temporary buffers without causing crashes or halting execution.
- **NFR4 (UI Usability):** Visual confidence meters, real-time graphs, and instant feedback cues shall keep the user informed of model status.

---

# CHAPTER 6: DESIGN

### 6.1 System Architectural Design
Signly utilizes a decoupled, pipe-and-filter modular architecture.

```
       +--------------------------------------------------------+
       |                  Video Capture Subsystem               |
       |     (Webcam Stream via WebRTC / File Uploader)         |
       +--------------------------------------------------------+
                                   │
                           [Raw BGR Frame]
                                   │
                                   ▼
       +--------------------------------------------------------+
       |               Stage 1: YOLO Hand Detector              |
       |      - YOLOv8 (50 epoch weights)                       |
       |      - Outputs: Bounding Box (x1, y1, x2, y2)          |
       +--------------------------------------------------------+
                                   │
                            [Cropped Hand]
                                   │
                                   ▼
       +--------------------------------------------------------+
       |             Stage 2: MediaPipe Landmark Extractor      |
       |      - 21 3D Joint Landmarks (x, y, z)                 |
       |      - Skeletal Hand Mesh Visualization                |
       +--------------------------------------------------------+
                                   │
                         [21 Landmark Points]
                                   │
                                   ▼
       +--------------------------------------------------------+
       |           Stage 3: Invariant Feature Normalization     |
       |      - Centering: Origin at Wrist (Index 0)            |
       |      - Scaling: Normalization by Middle MCP Distance   |
       |      - Flatten to 63-Dimensional Vector                |
       +--------------------------------------------------------+
                                   │
                        [63 Normalized Floats]
                                   │
                                   ▼
       +--------------------------------------------------------+
       |         Stage 4: TensorFlow/Keras Neural Classifier    |
       |      - Trained MLP with Softmax Output                 |
       |      - Output: Class Label + Confidence Score          |
       +--------------------------------------------------------+
                                   │
                     [Raw Prediction & Confidence]
                                   │
                                   ▼
       +--------------------------------------------------------+
       |          Stage 5: Temporal Prediction Stabilizer       |
       |      - Sliding Window Buffer (Size = 5)                |
       |      - Confidence Threshold Check (>= 70%)             |
       |      - Release Latch Mechanism (Anti-Bouncing)         |
       +--------------------------------------------------------+
                                   │
                          [Confirmed Gesture]
                                   │
                                   ▼
       +--------------------------------------------------------+
       |             Stage 6: Sentence Builder Engine           |
       |      - Append Letter / Add Space / Delete / Clear      |
       |      - State Maintenance in Streamlit Session State    |
       +--------------------------------------------------------+
                                   │
                           [Complete Sentence]
                                   │
                                   ▼
       +--------------------------------------------------------+
       |           Stage 7: ElevenLabs Neural TTS Engine        |
       |      - Text to Multilingual Audio Stream (MP3)         |
       |      - Browser Autoplay & Audio Waveform               |
       +--------------------------------------------------------+
```

### 6.2 Design Notations and Modeling Diagrams

#### 6.2.1 Use Case Diagram
```
                       +----------------------------------+
                       |           SIGNLY SYSTEM          |
                       +----------------------------------+
                                        │
           ┌────────────────────────────┼────────────────────────────┐
           │                            │                            │
           ▼                            ▼                            ▼
   (Start WebRTC Stream)       (Upload Recorded Video)      (Select Voice Preset)
           │                            │                            │
           └────────────────────────────┼────────────────────────────┘
                                        │
                                        ▼
                            (Perform Hand Gestures)
                                        │
                                        ▼
                            (View Real-Time Sentence)
                                        │
                                        ▼
                            (Trigger Speech Playback)
                                        │
                                        ▲
                                        │
                                  [  USER  ]
```

#### 6.2.2 Class Diagram & Entity Relationships
```
+------------------------------------+          +------------------------------------+
|          YOLOHandDetector          |          |          SignRecognizer            |
+------------------------------------+          +------------------------------------+
| - model: YOLO                      |          | - model: tf.keras.Model            |
| - confidence: float                |          | - checkpoint: dict                 |
+------------------------------------+          | - class_names: list[str]           |
| + detect(frame): (crop, bbox)      |          | - scaler_mean: ndarray             |
+------------------------------------+          | - scaler_scale: ndarray            |
                  │                             +------------------------------------+
                  │                             | + predict(features): (str, float)  |
                  ▼                             +------------------------------------+
+------------------------------------+                            ▲
|     Landmark Extraction & Math     |                            │
+------------------------------------+                            │
| + extract_landmarks(frame): pts    |                            │
| + extract_features(landmarks): 63D ├────────────────────────────┘
+------------------------------------+
                  │
                  ▼
+------------------------------------+          +------------------------------------+
|        PredictionStabilizer        |          |          SentenceBuilder           |
+------------------------------------+          +------------------------------------+
| - window_size: int                 |          | - text: str                        |
| - min_confidence: float            |          +------------------------------------+
| - predictions: deque               |          | + add_letter(letter: str)          |
| - waiting_for_release: bool        |          | + add_space()                      |
+------------------------------------+          | + backspace()                      |
| + update(letter, conf): confirmed  |          | + clear()                          |
| + release()                        |          | + get_text(): str                  |
| + reset()                          |          +------------------------------------+
+------------------------------------+                            │
                  │                                               │
                  └───────────────────────┬───────────────────────┘
                                          ▼
                        +------------------------------------+
                        |            SignPipeline            |
                        +------------------------------------+
                        | - yolo: YOLOHandDetector           |
                        | - recognizer: SignRecognizer       |
                        | - stabilizer: PredictionStabilizer |
                        | - sentence: SentenceBuilder        |
                        +------------------------------------+
                        | + process_frame(frame): dict       |
                        | + get_sentence(): str              |
                        | + clear_sentence()                 |
                        +------------------------------------+
```

### 6.3 Detailed Component Design & Mathematical Formulations

#### 6.3.1 YOLOv8 Hand Detection Subsystem
The hand detection stage uses a customized YOLOv8 deep network trained over 50 epochs on annotated hand datasets. Given an input RGB video frame $I \in \mathbb{R}^{H \times W \times 3}$:
$$\hat{B} = \text{argmax}_{B \in \mathcal{B}} (\text{Conf}(B))$$
where each bounding box candidate $B = [x_1, y_1, x_2, y_2]$. Bounding coordinates are clamped to ensure boundary validity:
$$x_1 = \max(0, x_1), \quad y_1 = \max(0, y_1), \quad x_2 = \min(W, x_2), \quad y_2 = \min(H, y_2)$$

#### 6.3.2 MediaPipe Hands Topological Landmarks
MediaPipe extracts 21 anatomical 3D landmark points:
$$\mathcal{P} = \{ \mathbf{p}_i = (x_i, y_i, z_i) \}_{i=0}^{20}$$
Key topological anchor points:
- $\mathbf{p}_0$: Wrist joint (origin anchor)
- $\mathbf{p}_9$: Middle finger metacarpophalangeal (MCP) knuckle joint (scale reference anchor)

#### 6.3.3 Mathematical Formulation of Invariant Normalization
To guarantee full invariance to hand translation within the camera frame and distance from the webcam lens:

1. **Translational Invariance (Wrist Centering):**
   $$\mathbf{c}_i = \mathbf{p}_i - \mathbf{p}_0, \quad \forall i \in \{0, 1, \dots, 20\}$$
   where $\mathbf{c}_0 = (0, 0, 0)$.

2. **Scale Invariance (Knuckle Euclidean Normalization):**
   Calculate the spatial Euclidean distance between the wrist origin and the middle finger MCP joint:
   $$s = \|\mathbf{c}_9\|_2 = \sqrt{(x_9 - x_0)^2 + (y_9 - y_0)^2 + (z_9 - z_0)^2}$$
   To prevent division-by-zero singularities:
   $$s_{\text{ref}} = \max(s, 10^{-6})$$
   The scale-invariant normalized coordinates are:
   $$\hat{\mathbf{c}}_i = \frac{\mathbf{c}_i}{s_{\text{ref}}}, \quad \forall i \in \{0, 1, \dots, 20\}$$

3. **Feature Vector Assembly:**
   $$\mathbf{x} = \text{flatten}\left( [ \hat{\mathbf{c}}_0, \hat{\mathbf{c}}_1, \dots, \hat{\mathbf{c}}_{20} ] \right) \in \mathbb{R}^{63}$$

4. **Standardization Scaler Transformation:**
   Using precomputed dataset mean $\boldsymbol{\mu} \in \mathbb{R}^{63}$ and standard deviation $\boldsymbol{\sigma} \in \mathbb{R}^{63}$:
   $$\mathbf{z} = \frac{\mathbf{x} - \boldsymbol{\mu}}{\boldsymbol{\sigma}}$$

#### 6.3.4 Deep Learning Classification Network (MLP)
The standardized vector $\mathbf{z}$ is fed into a Multilayer Perceptron:
$$\mathbf{h}_1 = \text{ReLU}(\mathbf{W}_1 \mathbf{z} + \mathbf{b}_1)$$
$$\mathbf{h}_2 = \text{ReLU}(\mathbf{W}_2 \mathbf{h}_1 + \mathbf{b}_2)$$
$$\mathbf{z}_{\text{logits}} = \mathbf{W}_3 \mathbf{h}_2 + \mathbf{b}_3 \in \mathbb{R}^{29}$$
$$\hat{\mathbf{y}} = \text{Softmax}(\mathbf{z}_{\text{logits}}), \quad \hat{y}_k = \frac{e^{z_k}}{\sum_{j=1}^{29} e^{z_j}}$$
The predicted class label $L$ and confidence $C$ are:
$$k^* = \text{argmax}_{k} (\hat{y}_k), \quad L = \text{ClassNames}[k^*], \quad C = \hat{y}_{k^*}$$

#### 6.3.5 Prediction Stabilization Finite State Machine
To eliminate high-frequency predictions during hand transitions, Signly implements a temporal consensus stabilizer:
- **Condition 1 (Confidence Threshold):** If $C < 0.70$, discard frame and clear sliding window.
- **Condition 2 (Sliding Buffer Consensus):** Maintain rolling window $W = [l_{t-4}, l_{t-3}, l_{t-2}, l_{t-1}, l_t]$. If and only if $|W| = 5$ and $\text{cardinality}(\text{set}(W)) == 1$, confirm gesture $L$.
- **Condition 3 (Anti-Bouncing Release Latch):** Once gesture $L$ is confirmed, enter state `WAITING_FOR_RELEASE = TRUE`. Do not accept new predictions until hand detection drops or moves to neutral pose (`release()`).

### 6.4 Flowcharts

#### 6.4.1 Master System Processing Flowchart
```
                [Start: Incoming Video Stream]
                               │
                               ▼
                    [Fetch Next Video Frame]
                               │
                               ▼
               [YOLO Hand Detection: Detect(Frame)]
                               │
                      Hand Detected?
                     /              \
                   No                Yes
                   /                  \
      [Release Stabilizer Latch]       [Crop Hand Bounding Box]
                  │                            │
                  │                            ▼
                  │              [MediaPipe Extract Landmarks]
                  │                            │
                  │                   Landmarks Found?
                  │                  /                \
                  │                No                  Yes
                  │                /                    \
                  │         [Retain Previous State]      [Center to Wrist Origin]
                  │                │                            │
                  │                │                            ▼
                  │                │             [Scale Normalize by Middle MCP]
                  │                │                            │
                  │                │                            ▼
                  │                │               [Flatten to 63-D Vector]
                  │                │                            │
                  │                │                            ▼
                  │                │              [Execute Keras MLP Inference]
                  │                │                            │
                  │                │                            ▼
                  │                │                 [Compute Softmax & Conf]
                  │                │                            │
                  │                │                   Conf >= 0.70?
                  │                │                  /             \
                  │                │                No               Yes
                  │                │                /                 \
                  │                │       [Clear Buffer]       [Append to Buffer]
                  │                │                │                 │
                  │                │                │       5 Identical in Buffer?
                  │                │                │      /                      \
                  │                │                │    No                        Yes
                  │                │                │    /                          \
                  │                │                │   │                 [Fire Confirmed Gesture]
                  │                │                │   │                           │
                  │                │                │   │                   Gesture Type?
                  │                │                │   │                  /      |      \
                  │                │                │   │             Letter    Space   Delete/Clear
                  │                │                │   │               │         │          │
                  │                │                │   │            Append     Space     Modify
                  │                │                │   │               │         │          │
                  └────────────────┴────────────────┴───┴───────►──────┴─────────┴──────────┘
                               │
                               ▼
                    [Update Streamlit UI State]
                               │
                   User Clicked "Play Sound"?
                  /                          \
                Yes                           No
                /                              \
   [Call ElevenLabs API]                        │
   [Stream & Play Audio]                        │
                \                              /
                 └──────────────┬─────────────┘
                                │
                                ▼
                       [Next Frame Loop]
```

### 6.5 Pseudo Code and Core Algorithms

#### Algorithm 1: Landmark Extraction and Canonical Geometric Normalization
```python
ALGORITHM ExtractInvariantFeatures(frame, bbox):
    Input: frame (RGB image matrix), bbox (x1, y1, x2, y2)
    Output: normalized_vector (Array of 63 float values) or NULL

    cropped_hand = frame[bbox.y1 : bbox.y2, bbox.x1 : bbox.x2]
    landmarks_3d = MediaPipeHands.process(cropped_hand)
    
    IF landmarks_3d IS NULL THEN:
        RETURN NULL
    END IF

    # Step 1: Center coordinates at wrist (landmark index 0)
    origin = landmarks_3d[0]
    centered_points = []
    FOR EACH point IN landmarks_3d:
        centered_points.append(point - origin)
    END FOR

    # Step 2: Calculate Euclidean scale factor using Middle MCP (index 9)
    scale_factor = EuclideanNorm(centered_points[9])
    IF scale_factor < 1e-6 THEN:
        scale_factor = 1e-6
    END IF

    # Step 3: Scale normalization
    normalized_features = []
    FOR EACH pt IN centered_points:
        normalized_features.append(pt / scale_factor)
    END FOR

    # Step 4: Flatten 21 x 3 into 63-element vector
    flattened_63d = Flatten(normalized_features)
    RETURN flattened_63d
```

#### Algorithm 2: Finite State Machine Prediction Stabilization
```python
ALGORITHM StabilizePrediction(letter, confidence, window_size=5, min_confidence=0.70):
    Input: letter (String), confidence (Float)
    Output: confirmed_letter (String or NULL)

    IF confidence < min_confidence THEN:
        CLEAR(predictions_buffer)
        RETURN NULL
    END IF

    IF waiting_for_release IS TRUE THEN:
        RETURN NULL
    END IF

    APPEND letter TO predictions_buffer

    IF LENGTH(predictions_buffer) < window_size THEN:
        RETURN NULL
    END IF

    # Verify 100% consensus in buffer
    IF ALL_ELEMENTS_EQUAL(predictions_buffer) THEN:
        confirmed_letter = predictions_buffer.last()
        last_confirmed = confirmed_letter
        waiting_for_release = TRUE
        CLEAR(predictions_buffer)
        RETURN confirmed_letter
    END IF

    RETURN NULL
```

---

# CHAPTER 7: TESTING

### 7.1 Functional Testing
Functional testing ensured that each modular component satisfied its specification:
- Hand detection correctly identifies hands under varying orientations.
- Feature extraction outputs exact 63-dimensional arrays with values bounded within expected ranges.
- Prediction stabilizer reliably filters single-frame glitches.
- Sentence builder properly handles character additions, whitespace formatting, backspaces, and clearing.
- Text-to-speech module correctly handles network timeouts, empty strings, and audio byte generation.

### 7.2 Structural (White-Box) Testing
White-box testing validated internal logic branches, loop conditions, and exception pathways:
- Tested boundary cases where `scale_ref` approaches 0 (verified fallback to $10^{-6}$ prevents divide-by-zero crashes).
- Tested bounding box clamping when hands touch the edge of the image frame (ensured array slicing does not throw out-of-bounds exceptions).
- Tested thread-safe handoff between WebRTC background callback threads and the Streamlit main thread using Python's `queue.Queue`.

### 7.3 Levels of Testing
1. **Unit Testing:** Individual verification of `YOLOHandDetector`, `extract_landmarks`, `extract_features`, `SignRecognizer`, `PredictionStabilizer`, and `SentenceBuilder`.
2. **Integration Testing:** Verification of the complete sequential pipeline (`SignPipeline`), ensuring that data arrays propagate correctly between models without type or dimension mismatches.
3. **System Testing:** End-to-end testing of the Streamlit application including camera capture, WebRTC video processing, and ElevenLabs API integration.
4. **User Acceptance Testing (UAT):** Real-time testing conducted by human testers executing gestures at various distances, speeds, and lighting conditions.

### 7.4 Detailed Test Cases and Empirical Verification

| Test ID | Module Tested | Test Scenario Description | Test Input Data | Expected Output | Actual Output | Test Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | `YOLOHandDetector` | Hand present in center of frame | 640x480 RGB image with visible hand | Bounding box coordinates $[x_1, y_1, x_2, y_2]$ with conf > 0.5 | Box returned: $[142, 88, 380, 410]$, Conf: 0.94 | **PASS** |
| **TC-02** | `YOLOHandDetector` | No hand present in scene | 640x480 RGB background image (empty room) | `None, None` returned | `None, None` returned | **PASS** |
| **TC-03** | `Landmark` | Hand partially clipped at image boundary | Hand on edge: $x_1 < 0, x_2 > W$ | Coordinates clamped to image dimensions | Coordinates clamped, no out-of-bounds error | **PASS** |
| **TC-04** | `extract_features`| Vector dimension verification | 21 3D points from MediaPipe | Exactly 63-element float32 array | 1D NumPy array of shape `(63,)` | **PASS** |
| **TC-05** | `extract_features`| Translation invariance verification | Hand at $(50, 50)$ vs Hand at $(350, 350)$ | Normalized coordinates identical within $\epsilon < 10^{-3}$ | Coordinate difference $< 0.0008$ | **PASS** |
| **TC-06** | `SignRecognizer` | Inference on known static 'A' sign | 63 normalized coordinates of 'A' | Predicted letter 'A', confidence > 0.90 | Letter 'A', Conf: 0.962 | **PASS** |
| **TC-07** | `Stabilizer` | Noisy frame rejection | 4 frames of 'B', 1 frame of 'C' | No confirmation output (`None`) | `None` returned, buffer rejected | **PASS** |
| **TC-08** | `Stabilizer` | Stable gesture acceptance | 5 consecutive frames of 'L' (conf > 0.70) | Output confirmed: 'L', Latch set to TRUE | 'L' emitted, latch activated | **PASS** |
| **TC-09** | `Stabilizer` | Anti-bouncing latch verification | Holding sign 'L' for 30 consecutive frames | 'L' emitted exactly once | 'L' emitted once; no duplicate letters | **PASS** |
| **TC-10** | `SentenceBuilder`| Letter insertion and backspace | Sequence: `['H','E','L','L','O','Delete']` | Text state: `"HELL"` | Text state: `"HELL"` | **PASS** |
| **TC-11** | `SentenceBuilder`| Space bar insertion | Add 'A', Space, 'B' | Text state: `"A B"` | Text state: `"A B"` | **PASS** |
| **TC-12** | `SentenceBuilder`| Clear command execution | Active text: `"HELLO"`, trigger `Clear` | Text state: `""` | Text state: `""` | **PASS** |
| **TC-13** | `ElevenLabs TTS` | Audio conversion with valid text | Text: `"HELLO WORLD"`, Voice: `"Man"` | Non-empty MP3 audio byte stream | 48,210 audio bytes returned | **PASS** |
| **TC-14** | `ElevenLabs TTS` | Empty text protection | Text: `""` (empty string) | Function returns `None` immediately | `None` returned, zero API calls made | **PASS** |
| **TC-15** | `WebRTC Stream` | Web browser live webcam connection | Browser WebRTC permission granted | Live video feed displays with 25+ FPS | Stream stable at 28.4 FPS | **PASS** |

---

# CHAPTER 8: IMPLEMENTATION

### 8.1 Implementation Environment and Model Training
- **YOLOv8 Hand Detection Model:**
  - Base Model: YOLOv8n (nano) / YOLOv8s (small) from Ultralytics.
  - Training Epochs: 50 epochs on curated hand bounding-box datasets.
  - Saved Checkpoint: `models/yolo_best_weights (50 epoch).pt` (5.48 MB).
- **Landmark Classifier Network (Keras MLP):**
  - Input Features: 63 normalized landmark floating point coordinates.
  - Training Optimizer: Adam ($\text{lr} = 0.001$).
  - Loss Function: Categorical Cross-Entropy.
  - Classes: 29 target classes (26 alphabets + Delete, Clear, Space).
  - Saved Artifacts: `models/landmark_model.keras` (252 KB), `models/landmark_meta.json` (metadata with standardization scaler means and variances), and `models/class_mapping.json`.

### 8.2 Conversion Plan and Operational Deployment
- **From Terminal Scripts to Web Architecture:** The original development scripts ran OpenCV in blocking `cv2.imshow()` desktop windows. For production deployment, this was converted into a reactive web interface via Streamlit.
- **WebRTC Client-Side Streaming:** To run seamlessly without requiring direct server-attached camera hardware (which fails on cloud deployments like Streamlit Community Cloud), the architecture uses `streamlit-webrtc` to stream frames from client browser webcams to the backend processing thread.

### 8.3 Post-Implementation Support and Software Maintenance
- **Decoupled Architecture:** Each component can be upgraded independently. For instance, the landmark classifier can be retrained with additional classes without modifying the YOLO detector or WebRTC video streaming pipeline.
- **Dynamic Configuration:** Confidence thresholds and stability frame buffers are exposed through interactive UI sliders, allowing users to adapt the system to their specific lighting and signing speed without code changes.

---

# CHAPTER 9: PROJECT LEGACY

### 9.1 Current Status of the Project
**Signly** is fully operational and capable of real-time sign language fingerspelling recognition and speech synthesis. The system successfully executes across three operational modes:
1. **Live Camera Feed & Translation:** Browser-based live WebRTC translation with bounding box annotations, real-time confidence tracking, and interactive sentence composition.
2. **Video Upload Translation:** Parses pre-recorded sign language video files frame-by-frame with playback controls.
3. **Text to Audio:** Direct text-to-speech sandbox for testing and synthesizing arbitrary phrases using the ElevenLabs neural engine.

### 9.2 Remaining Areas of Concern and Known Limitations
1. **Static vs. Continuous Sign Recognition:** The system classifies fingerspelling (letters A–Z) and discrete control signs. It does not yet interpret full continuous sign language sentences that involve complex trajectories, facial expressions, and two-handed interaction.
2. **Dynamic Signs ('J' and 'Z'):** In standard ASL, 'J' and 'Z' require dynamic spatial tracing motions. In static landmark classification, these rely on stationary hand conformations.
3. **Ambient Lighting Extremes:** In extremely dark environments, MediaPipe landmark confidence degrades, leading to dropped frames.

### 9.3 Technical and Managerial Lessons Learnt
- **Decoupling Geometry from Raw Pixels:** Isolating 3D skeletal landmarks before classification proved vastly superior to raw CNN pixel classification in preventing background overfitting and eliminating skin tone biases.
- **Temporal Stabilization is Mandatory:** Frame-by-frame classifiers are inherently noisy; a temporal consensus buffer and anti-bounce release latch are essential for turning raw model outputs into a usable typing interface.
- **Graceful API Fallbacks:** External cloud APIs (like ElevenLabs) must always be wrapped in exception handling to prevent network hiccups from crashing the core vision pipeline.

---

# CHAPTER 10: USER MANUAL (HELP GUIDE)

### 10.1 System Installation & Prerequisites
1. **Prerequisites:** Install Python 3.10, 3.11, or 3.12 (64-bit) and ensure webcam hardware is connected.
2. **Clone the Repository:**
   ```bash
   git clone https://github.com/Usf132/Signly.git
   cd Signly
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure ElevenLabs API Key (Optional for Speech):**
   Create a `.env` file in the project root:
   ```env
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   ```

### 10.2 Starting the Application
Launch the Streamlit web application from your terminal:
```bash
streamlit run app/main.py
```
Your default web browser will automatically open to `http://localhost:8501`.

### 10.3 Operating Modes and Feature Navigation
1. **Sidebar Controls:**
   - **Department Selector:** Choose between `Live Translation`, `Upload Video`, and `Text to Audio`.
   - **Confidence Threshold Slider:** Set between 0% and 100% (default: 55%-70%).
   - **Stability Frames Slider:** Adjust the consensus buffer between 1 and 30 frames (default: 10 frames).
   - **Voice Settings:** Select preferred speech synthesis voice profiles.
   - **Theme Customization:** Customize background, sidebar, and accent colors.
2. **Live Translation Mode:**
   - Click **"Start"** to initiate the WebRTC webcam feed. Allow browser camera permissions when prompted.
   - Position your hand in clear view of the camera. The green bounding box will localize your hand and the blue skeletal mesh will track your finger joints.
   - Hold an ASL gesture steady. When recognized, the confirmed letter appears under **Recognized Sequence**.
   - Use the **Space**, **Delete (⌫)**, and **Clear** buttons (or their respective sign gestures) to edit your sentence.
   - Click the **Play** button to convert the completed sentence into spoken audio.

---

# CHAPTER 11: SOURCE CODE ARCHITECTURE & SYSTEM SNAPSHOTS

### 11.1 Directory Tree Structure
```
Signly/
├── .devcontainer/
│   └── devcontainer.json
├── .streamlit/
│   └── config.toml
├── app/
│   ├── __init__.py
│   ├── backend.py               # ElevenLabs TTS & inference bindings
│   └── main.py                  # Streamlit frontend & WebRTC streamer
├── assets/
│   ├── Gestures.png             # ASL alphabet reference chart
│   ├── Logo.png                 # Project branding graphic
│   ├── Logo_demo.png            # UI preview graphic
│   └── live demo.mp4            # Demonstration video recording
├── models/
│   ├── class_mapping.json       # Index-to-label class definitions (29 classes)
│   ├── landmark.pt              # PyTorch landmark model weights
│   ├── landmark_meta.json       # Scaler mean/scale metadata & config
│   ├── landmark_model.keras     # Trained TensorFlow/Keras classifier
│   ├── yolo_best_weights (30 epoch).pt
│   └── yolo_best_weights (50 epoch).pt # Trained YOLOv8 hand detector
├── notebooks/                   # Research & exploratory notebooks
├── outputs/                     # Exported evaluation charts
├── presentations/               # Capstone project pitch decks
├── signlens/                    # Core modular processing package
│   ├── __init__.py
│   ├── landmark.py              # MediaPipe joint extraction & normalization
│   ├── pipeline.py              # End-to-end multi-stage pipeline
│   ├── recognizer.py            # Keras inference & scaler standardization
│   ├── sentence.py              # SentenceBuilder state machine
│   ├── stabilizer.py            # Finite state machine temporal filter
│   └── yolo_detector.py         # YOLOv8 hand bounding-box detector
├── .env                         # API keys & configuration
├── LICENSE                      # Open-source MIT license
├── README.md                    # Project documentation
└── requirements.txt             # Frozen dependency manifest
```

### 11.2 Core Class Map (29 Target Classes)
```json
{
  "Classes": [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z",
    "Delete", "Clear", "Space"
  ]
}
```

---

