if __name__ == '__main__':
    from booknlp.booknlp import BookNLP

    model_params = {
        "pipeline": "entity,quote,supersense,event,coref",
        "model": "big"
    }

    booknlp = BookNLP("en", model_params)

    input_file = "../book_txt_files/the_rose_and_the_ring.txt"

    output_directory = "../extracted_data/the_rose_and_the_ring"

    book_id = "the_rose_and_the_ring"

    booknlp.process(input_file, output_directory, book_id)
