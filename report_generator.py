from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class PDFReport:

    def generate(self, filename, sections):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>AI Resume Analyzer Report</b>",
                styles["Title"]
            )
        )

        story.append(
            Paragraph("<br/><br/>", styles["BodyText"])
        )

        for title, content in sections:

            story.append(
                Paragraph(
                    f"<b>{title}</b>",
                    styles["Heading2"]
                )
            )

            story.append(
                Paragraph(
                    content.replace("\n", "<br/>"),
                    styles["BodyText"]
                )
            )

            story.append(
                Paragraph("<br/>", styles["BodyText"])
            )

        doc.build(story)