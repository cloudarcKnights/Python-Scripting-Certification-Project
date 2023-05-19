#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)

    elements = []
    elements.append(Paragraph(title, styles["Heading1"]))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(paragraph, styles["BodyText"]))

    report.build(elements)
