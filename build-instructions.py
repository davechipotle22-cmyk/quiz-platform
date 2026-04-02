from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

doc = SimpleDocTemplate(
    "LockDown-Quiz-Build-Instructions.pdf",
    pagesize=letter,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch,
    leftMargin=0.85*inch,
    rightMargin=0.85*inch
)

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    'DocTitle',
    parent=styles['Title'],
    fontSize=24,
    textColor=HexColor('#1a1a2e'),
    spaceAfter=6,
))
styles.add(ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=12,
    textColor=HexColor('#666666'),
    alignment=TA_CENTER,
    spaceAfter=20,
))
styles.add(ParagraphStyle(
    'StepHeader',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=HexColor('#e94560'),
    spaceBefore=18,
    spaceAfter=8,
    fontName='Helvetica-Bold',
))
styles.add(ParagraphStyle(
    'StepDesc',
    parent=styles['Normal'],
    fontSize=11,
    textColor=HexColor('#333333'),
    spaceAfter=6,
    leading=16,
))
styles.add(ParagraphStyle(
    'CodeBlock',
    parent=styles['Normal'],
    fontName='Courier',
    fontSize=10.5,
    textColor=HexColor('#e0e0e0'),
    backColor=HexColor('#1a1a2e'),
    leading=16,
    leftIndent=12,
    rightIndent=12,
    spaceBefore=4,
    spaceAfter=10,
    borderPadding=(8, 8, 8, 8),
))
styles.add(ParagraphStyle(
    'Note',
    parent=styles['Normal'],
    fontSize=10,
    textColor=HexColor('#555555'),
    fontName='Helvetica-Oblique',
    leftIndent=16,
    spaceAfter=8,
    leading=14,
))
styles.add(ParagraphStyle(
    'SectionHeader',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=HexColor('#16213e'),
    spaceBefore=24,
    spaceAfter=10,
    fontName='Helvetica-Bold',
))
styles.add(ParagraphStyle(
    'WarningText',
    parent=styles['Normal'],
    fontSize=10,
    textColor=HexColor('#c0392b'),
    fontName='Helvetica-Bold',
    spaceAfter=8,
))

story = []

# Title
story.append(Paragraph("LockDown Quiz", styles['DocTitle']))
story.append(Paragraph("macOS Build Instructions", styles['Subtitle']))
story.append(HRFlowable(width="100%", thickness=2, color=HexColor('#e94560')))
story.append(Spacer(1, 16))

# Prerequisites
story.append(Paragraph("Prerequisites", styles['SectionHeader']))
story.append(Paragraph(
    "Before you begin, make sure the following are installed on your Mac. "
    "Open <b>Terminal</b> (Applications > Utilities > Terminal) and run each command below.",
    styles['StepDesc']
))

# Step 1
story.append(Paragraph("Step 1 - Install Homebrew (if not installed)", styles['StepHeader']))
story.append(Paragraph(
    "Homebrew is the macOS package manager. Check if it's installed first:",
    styles['StepDesc']
))
story.append(Paragraph("brew --version", styles['CodeBlock']))
story.append(Paragraph(
    "If you see a version number, skip to Step 2. If not, paste this into Terminal:",
    styles['StepDesc']
))
story.append(Paragraph(
    '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
    styles['CodeBlock']
))
story.append(Paragraph(
    "Follow the prompts. You may need to enter your Mac password.",
    styles['Note']
))

# Step 2
story.append(Paragraph("Step 2 - Install Node.js", styles['StepHeader']))
story.append(Paragraph(
    "Node.js is required to build the Electron app. Paste this into Terminal:",
    styles['StepDesc']
))
story.append(Paragraph("brew install node", styles['CodeBlock']))
story.append(Paragraph(
    "Verify it installed correctly:",
    styles['StepDesc']
))
story.append(Paragraph("node --version", styles['CodeBlock']))
story.append(Paragraph(
    "You should see a version number like v20.x.x or higher.",
    styles['Note']
))

# Step 3
story.append(Paragraph("Step 3 - Install Git (if not installed)", styles['StepHeader']))
story.append(Paragraph(
    "Check if Git is already installed:",
    styles['StepDesc']
))
story.append(Paragraph("git --version", styles['CodeBlock']))
story.append(Paragraph(
    "If not installed, paste this:",
    styles['StepDesc']
))
story.append(Paragraph("brew install git", styles['CodeBlock']))

# Building section
story.append(Paragraph("Building the Application", styles['SectionHeader']))
story.append(HRFlowable(width="100%", thickness=1, color=HexColor('#ddd')))

# Step 4
story.append(Paragraph("Step 4 - Clone the Repository", styles['StepHeader']))
story.append(Paragraph(
    "This downloads the quiz platform code to your Mac. Paste this into Terminal:",
    styles['StepDesc']
))
story.append(Paragraph(
    "git clone git@github.com:davechipotle22-cmyk/quiz-platform.git",
    styles['CodeBlock']
))
story.append(Paragraph(
    "If you get a permission error, use HTTPS instead:",
    styles['Note']
))
story.append(Paragraph(
    "git clone https://github.com/davechipotle22-cmyk/quiz-platform.git",
    styles['CodeBlock']
))

# Step 5
story.append(Paragraph("Step 5 - Navigate into the Project Folder", styles['StepHeader']))
story.append(Paragraph(
    "Move into the downloaded folder. Paste this:",
    styles['StepDesc']
))
story.append(Paragraph("cd quiz-platform", styles['CodeBlock']))

# Step 6
story.append(Paragraph("Step 6 - Install Dependencies", styles['StepHeader']))
story.append(Paragraph(
    "This downloads Electron and the build tools. Paste this and wait for it to finish:",
    styles['StepDesc']
))
story.append(Paragraph("npm install", styles['CodeBlock']))
story.append(Paragraph(
    "This may take 2-5 minutes depending on your internet speed. You'll see a progress bar.",
    styles['Note']
))

# Step 7
story.append(Paragraph("Step 7 - Test the App (Optional)", styles['StepHeader']))
story.append(Paragraph(
    "Before building, you can test that everything works. Paste this:",
    styles['StepDesc']
))
story.append(Paragraph("npm start", styles['CodeBlock']))
story.append(Paragraph(
    "The quiz app should open in a window. Press Ctrl+C in Terminal to close it when done.",
    styles['Note']
))

# Step 8
story.append(Paragraph("Step 8 - Build the macOS App", styles['StepHeader']))
story.append(Paragraph(
    "This creates the final .dmg installer file. Paste this:",
    styles['StepDesc']
))
story.append(Paragraph("npm run build:mac", styles['CodeBlock']))
story.append(Paragraph(
    "This takes 3-10 minutes. When finished, the installer will be in the <b>dist/</b> folder.",
    styles['StepDesc']
))

# Step 9
story.append(Paragraph("Step 9 - Find Your App", styles['StepHeader']))
story.append(Paragraph(
    "Open the dist folder to see your built app:",
    styles['StepDesc']
))
story.append(Paragraph("open dist/", styles['CodeBlock']))
story.append(Paragraph(
    "You will see a file called <b>LockDown Quiz-1.0.0-universal.dmg</b>. "
    "This is the installer you distribute to students.",
    styles['StepDesc']
))

# Distribution section
story.append(Paragraph("Distributing to Students", styles['SectionHeader']))
story.append(HRFlowable(width="100%", thickness=1, color=HexColor('#ddd')))
story.append(Spacer(1, 6))

story.append(Paragraph(
    "Share the <b>.dmg</b> file with students via email, Google Drive, or any file sharing service.",
    styles['StepDesc']
))
story.append(Spacer(1, 4))
story.append(Paragraph("Students install it by:", styles['StepDesc']))

steps_data = [
    ["1.", "Double-click the .dmg file"],
    ["2.", "Drag 'LockDown Quiz' into the Applications folder"],
    ["3.", "Open it from Applications"],
]
t = Table(steps_data, colWidths=[0.3*inch, 5*inch])
t.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 11),
    ('TEXTCOLOR', (0, 0), (0, -1), HexColor('#e94560')),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
story.append(t)

story.append(Spacer(1, 10))
story.append(Paragraph(
    "If macOS blocks the app: Go to System Settings > Privacy & Security > "
    "scroll down and click 'Open Anyway' next to the LockDown Quiz message.",
    styles['WarningText']
))

# Quick reference
story.append(Spacer(1, 12))
story.append(Paragraph("Quick Reference - All Commands", styles['SectionHeader']))
story.append(HRFlowable(width="100%", thickness=1, color=HexColor('#ddd')))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "Copy and paste these commands one at a time into Terminal:",
    styles['StepDesc']
))

commands = [
    "git clone git@github.com:davechipotle22-cmyk/quiz-platform.git",
    "cd quiz-platform",
    "npm install",
    "npm run build:mac",
    "open dist/",
]
for cmd in commands:
    story.append(Paragraph(cmd, styles['CodeBlock']))

# ========================================================
# SECRET KEYS ANSWER KEY — last page
# ========================================================
from reportlab.platypus import PageBreak
story.append(PageBreak())

story.append(Paragraph("Secret Keys - Answer Key", styles['SectionHeader']))
story.append(HRFlowable(width="100%", thickness=2, color=HexColor('#e94560')))
story.append(Spacer(1, 10))
story.append(Paragraph(
    "The following secret key combinations are built into the application. "
    "These are for the instructor/developer only. Do not share with students.",
    styles['WarningText']
))
story.append(Spacer(1, 12))

# Secret key table
secret_keys_data = [
    ["Secret Key", "Action", "How to Activate"],
    [
        "Developer\nPanel",
        "Opens the developer panel\nto edit questions and\nset question count",
        'Click the "Hide Time"\nbutton 3 times\nwithin 1 second'
    ],
    [
        "Lockdown\nMode",
        "Activates full kiosk mode.\nHides taskbar, notifications,\nand all other windows.\nOnly the quiz is visible.",
        'Press  S  key, then\npress  Enter  key, then\npress  Enter  key again\n(within 2 seconds)'
    ],
]

from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

key_table = Table(secret_keys_data, colWidths=[1.1*inch, 2.2*inch, 2.2*inch])
key_table.setStyle(TableStyle([
    # Header row
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('TOPPADDING', (0, 0), (-1, 0), 10),
    # Data rows
    ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f5f5f5')),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('TEXTCOLOR', (0, 1), (-1, -1), HexColor('#333333')),
    ('TOPPADDING', (0, 1), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 10),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    # First column bold
    ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
    ('TEXTCOLOR', (0, 1), (0, -1), HexColor('#e94560')),
    # Grid
    ('GRID', (0, 0), (-1, -1), 1, HexColor('#cccccc')),
    ('BOX', (0, 0), (-1, -1), 2, HexColor('#1a1a2e')),
]))
story.append(key_table)

story.append(Spacer(1, 20))

# Additional notes
story.append(Paragraph("Important Notes", styles['StepHeader']))

notes = [
    ["1.", "The Developer Panel secret key only works when NOT typing in an input field."],
    ["2.", "Lockdown Mode: press S then Enter then Enter in sequence (not held together). "
           "You have 2 seconds to complete the full sequence."],
    ["3.", "To EXIT lockdown mode, repeat the same key sequence: S > Enter > Enter."],
    ["4.", "In the Electron desktop app, lockdown mode hides the Windows taskbar, "
           "all notifications, and prevents Alt+Tab switching."],
    ["5.", "In a regular browser, lockdown mode uses fullscreen as a fallback."],
    ["6.", "A red border appears around the app when lockdown mode is active."],
]

notes_table = Table(notes, colWidths=[0.3*inch, 5.2*inch])
notes_table.setStyle(TableStyle([
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('TEXTCOLOR', (0, 0), (0, -1), HexColor('#e94560')),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TEXTCOLOR', (1, 0), (1, -1), HexColor('#444444')),
]))
story.append(notes_table)

story.append(Spacer(1, 24))
story.append(HRFlowable(width="100%", thickness=2, color=HexColor('#e94560')))
story.append(Spacer(1, 8))
story.append(Paragraph(
    "CONFIDENTIAL — For instructor use only. Do not distribute this page to students.",
    styles['WarningText']
))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "Generated for LockDown Quiz Platform v1.0.0",
    styles['Note']
))

doc.build(story)
print("PDF created: LockDown-Quiz-Build-Instructions.pdf")
