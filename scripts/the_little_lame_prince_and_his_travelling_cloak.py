if __name__ == '__main__':
    from booknlp.booknlp import BookNLP

    model_params = {
        "pipeline": "entity,quote,supersense,event,coref",
        "model": "big"
    }

    booknlp = BookNLP("en", model_params)

    input_file = "../book_txt_files/the_little_lame_prince_and_his_travelling_cloak.txt"

    output_directory = "../extracted_data/the_little_lame_prince_and_his_travelling_cloak"

    book_id = "the_little_lame_prince_and_his_travelling_cloak"

    booknlp.process(input_file, output_directory, book_id)
