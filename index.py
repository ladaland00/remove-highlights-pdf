import fitz


def remove_highlights(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)

    for page_number in range(len(doc)):
        page = doc[page_number]

        # Get the annotations on the page
        annotations = page.annots()

        # Remove annotations
        for annot in annotations:
            page.delete_annot(annot)

    doc.save(output_pdf)
    doc.close()


remove_highlights("Harrison Self Assessment, 17th.pdf",
                  "Harrison Self Assessment, 17th fix.pdf")

remove_highlights("Harrison Self Assessment, 18th Ed.pdf",
                  "Harrison Self Assessment, 18th Ed fix.pdf")

remove_highlights("Harrison Self Assessment, 19th.pdf",
                  "Harrison Self Assessment, 19th fix.pdf")
