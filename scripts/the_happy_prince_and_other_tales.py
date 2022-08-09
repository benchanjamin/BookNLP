if __name__ == '__main__':
    from booknlp.booknlp import BookNLP

    model_params = {
        "pipeline": "entity,quote,supersense,event,coref",
        "model": "big"
    }

    booknlp = BookNLP("en", model_params)

    input_file = "../data/the_happy_prince_and_other_tales.py"

    output_directory = "../data/the_happy_prince_and_other_tales"

    book_id = "the_happy_prince_and_other_tales"

    booknlp.process(input_file, output_directory, book_id)
