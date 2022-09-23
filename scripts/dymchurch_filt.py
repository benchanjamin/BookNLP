if __name__ == '__main__':
    from booknlp.booknlp import BookNLP

    model_params = {
        "pipeline": "entity,quote,supersense,event,coref",
        "model": "big"
    }

    booknlp = BookNLP("en", model_params)

    input_file = "../book_txt_files/dymchurch_flit.txt"

    output_directory = "../extracted_data/dymchurch_filt"

    book_id = "dymchurch_filt"

    booknlp.process(input_file, output_directory, book_id)
