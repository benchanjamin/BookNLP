import shutil

def move(book_basename, entities_not_found, supersense_not_found):
    output_location_entity = f"../extracted_data/{book_basename}/{book_basename}.entities"
    output_location_supersense = f"../extracted_data/{book_basename}/{book_basename}.supersense"

    if entities_not_found:
        shutil.copy(output_location_entity, f"../tsv_files/entities_tsv_files/{book_basename}.tsv")

    if supersense_not_found:
        shutil.copy(output_location_supersense, f"../tsv_files/supersense_tsv_files/{book_basename}.tsv")


if __name__ == '__main__':
    import os
    import glob

    book_txt_files = glob.glob("../book_txt_files/*.txt")
    entities_files = glob.glob("../tsv_files/entities_tsv_files/*.tsv")
    supersense_files = glob.glob("../tsv_files/supersense_tsv_files/*.tsv")

    book_txt_files_basename = list(map(lambda x: os.path.basename(x).split(".")[0], book_txt_files))
    entities_files_basename = list(map(lambda x: os.path.basename(x).split(".")[0], entities_files))
    supersense_files_basename = list(map(lambda x: os.path.basename(x).split(".")[0], supersense_files))

    for f in book_txt_files_basename:
        if f not in entities_files_basename and f not in supersense_files_basename:
            move(f, True, True)
