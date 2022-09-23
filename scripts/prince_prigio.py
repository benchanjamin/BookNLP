if __name__ == '__main__':
    from booknlp.booknlp import BookNLP

    model_params = {
        "pipeline": "entity,quote,supersense,event,coref",
        "model": "big"
    }

    booknlp = BookNLP("en", model_params)

    input_file = "../book_txt_files/prince_prigio.txt"

    output_directory = "../extracted_data/prince_prigio"

    book_id = "prince_prigio"

    booknlp.process(input_file, output_directory, book_id)
