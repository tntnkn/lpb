import os

from docxtpl    import DocxTemplate


def makeDocument(from_id, user_info, user_document):
    print("makeDocument")
    tmp_dir  = os.path.join(os.getcwd(), 'tmp')
    f_name   = os.path.join(tmp_dir, str(from_id)) + ".docx"
    makeDocumentJinja(f_name, user_info, user_document)
    return f_name

def makeDocumentJinja(f_name, user_info, user_document):
    print("makeDocumentJinja")
    tags = { **vars(user_info), **vars(user_document) }
    try:
        doc = DocxTemplate("templates/summon_ags_template.docx")
        doc.render(tags)
    except Exception as e:
        print(e)
    print("after render")
    doc.save(f_name)

