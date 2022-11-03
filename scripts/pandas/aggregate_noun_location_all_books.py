if __name__ == '__main__':
    import pandas as pd
    import os
    import glob
    import numpy as np

    # use glob to get all the csv files
    # in the folder
    tsv_files = glob.glob("../../tsv_files/entities_tsv_files/*.tsv")

    # create a main DataFrame object
    appended_data = []

    for f in tsv_files:
        book_df = pd.read_csv(f, sep="\t", header=0)
        book_df['book_title'] = os.path.basename(f).split(".")[0]
        book_df['count'] = 0
        book_df['total_count'] = 0
        appended_data.append(book_df)

    main_df = pd.concat(appended_data)
    main_df = main_df.filter(items=['cat', 'text', 'book_title', 'count', 'total_count'])
    main_df = main_df.loc[main_df['cat'] == 'LOC']

    # book_specific_noun_location_word_count
    main_df = main_df.groupby(["text", "total_count", "book_title"], as_index=False)["count"].count()
    # main_df = main_df.groupby(["text"], as_index=False)["total_count"].sum()
    main_df['total_count'] = main_df.groupby(["text"])['count'].transform('sum')


    # main_df = main_df.groupby(["text", "book_title", "total_count"], as_index=False).agg({'text': 'first', 'book_title': 'first', 'count': 'sum', 'total_count': 'first'})
    # main_df['count'] = main_df.groupby(['text'])['book_title'].transform('count')
    # main_df.drop_duplicates()
    # # main_df['total_count'] = main_df.groupby(["text"])['count'].transform('sum')
    # # main_df.drop_duplicates()

    # generalized_noun_location_word_count
    # main_df = main_df.groupby(["text"])["count"].sum()

    print(main_df.head())
    main_df.to_csv("noun_location_word_count_across_all_books_entities.csv")
