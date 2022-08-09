if __name__ == '__main__':
    from booknlp.booknlp import BookNLP

    model_params = {
        "pipeline": "entity,quote,supersense,event,coref",
        "model": "big"
    }

    booknlp = BookNLP("en", model_params)

    input_file = "../data/the_king_of_the_golden_river.txt"

    output_directory = "../data/the_king_of_the_golden_river"

    book_id = "the_king_of_the_golden_river"

    booknlp.process(input_file, output_directory, book_id)
