if __name__ == '__main__':
    from booknlp.booknlp import BookNLP

    model_params = {
        "pipeline": "entity,quote,supersense,event,coref",
        "model": "big"
    }

    booknlp = BookNLP("en", model_params)

    input_file = "data/harry_potter_cleaned.txt"

    output_directory = "data/harry_potter"

    book_id = "harry_potter"

    booknlp.process(input_file, output_directory, book_id)
