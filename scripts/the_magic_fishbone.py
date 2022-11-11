if __name__ == '__main__':
    from booknlp.booknlp import BookNLP

    model_params = {
        "pipeline": "entity,quote,supersense,event,coref",
        "model": "big"
    }

    booknlp = BookNLP("en", model_params)

    book_name = "the_magic_fishbone"

    input_file = f"../book_txt_files/{book_name}.txt"

    output_directory = f"../extracted_data/{book_name}"

    book_id = f"{book_name}"

    booknlp.process(input_file, output_directory, book_id)
