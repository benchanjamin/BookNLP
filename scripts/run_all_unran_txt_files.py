import move_booknlp_output_to_tsv_files_directory as move

if __name__ == '__main__':
    import os
    import glob

    # book_txt_files = glob.glob("../book_txt_files/*.txt")
    book_txt_files = glob.glob("../literary_book_txt_files/*.txt")
    # entities_files = glob.glob("../tsv_files/entities_tsv_files-11-20/*.tsv")
    entities_files = glob.glob("../tsv_files/entities_tsv_files-02-25/*.tsv")
    # supersense_files = glob.glob("../tsv_files/supersense_tsv_files-11-20/*.tsv")
    supersense_files = glob.glob("../tsv_files/supersense_tsv_files-02-25/*.tsv")

    book_txt_files_basename = list(map(lambda x: os.path.basename(x).split(".")[0], book_txt_files))
    entities_files_basename = list(map(lambda x: os.path.basename(x).split(".")[0], entities_files))
    supersense_files_basename = list(map(lambda x: os.path.basename(x).split(".")[0], supersense_files))

    for f in book_txt_files_basename:
        if f not in entities_files_basename and f not in supersense_files_basename:
            from booknlp.booknlp import BookNLP

            print(f)
            model_params = {
                "pipeline": "entity,supersense",
                "model": "big"
            }

            booknlp = BookNLP("en", model_params)

            # input_file = f"../book_txt_files/{f}.txt"
            input_file = f"../literary_book_txt_files/{f}.txt"

            # output_directory = f"../extracted_data/{f}"
            output_directory = f"../literary_extracted_data/{f}"

            book_id = f"{f}"

            booknlp.process(input_file, output_directory, book_id)

            # move.move(output_directory, True, True)
            continue

        if f not in entities_files_basename:
            from booknlp.booknlp import BookNLP

            print(f)
            model_params = {
                "pipeline": "entity",
                "model": "big"
            }

            booknlp = BookNLP("en", model_params)

            # input_file = f"../book_txt_files/{f}.txt"
            input_file = f"../literary_book_txt_files/{f}.txt"

            # output_directory = f"../extracted_data/{f}"
            output_directory = f"../literary_extracted_data/{f}"

            book_id = f"{f}"

            booknlp.process(input_file, output_directory, book_id)

            # move.move(output_directory, True, True)
            continue

        if f not in supersense_files_basename:
            from booknlp.booknlp import BookNLP

            print(f)
            model_params = {
                "pipeline": "supersense",
                "model": "big"
            }

            booknlp = BookNLP("en", model_params)

            input_file = f"../literary_book_txt_files/{f}.txt"

            # output_directory = f"../extracted_data/{f}"
            output_directory = f"../literary_extracted_data/{f}"

            book_id = f"{f}"

            booknlp.process(input_file, output_directory, book_id)

            # move.move(output_directory, True, True)
            continue
