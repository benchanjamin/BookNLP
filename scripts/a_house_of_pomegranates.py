if __name__ == '__main__':
    from booknlp.booknlp import BookNLP

    model_params = {
        "pipeline": "entity,quote,supersense,event,coref",
        "model": "big"
    }

    booknlp = BookNLP("en", model_params)

    input_file = "../book_txt_files/a_house_of_pomegranates.txt"

    output_directory = "../extracted_data/a_house_of_pomegranates"

    book_id = "a_house_of_pomegranates"

    booknlp.process(input_file, output_directory, book_id)
