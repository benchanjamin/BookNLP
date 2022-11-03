if __name__ == '__main__':
    from booknlp.booknlp import BookNLP

    model_params = {
        "pipeline": "entity,quote,supersense,event,coref",
        "model": "big"
    }

    booknlp = BookNLP("en", model_params)

    input_file = "../book_txt_files/the_light_princess_and_other_fairy_stories.txt"

    output_directory = "../extracted_data/the_light_princess_and_other_fairy_stories"

    book_id = "the_light_princess_and_other_fairy_stories"

    booknlp.process(input_file, output_directory, book_id)
