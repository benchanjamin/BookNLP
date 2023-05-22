if __name__ == '__main__':
    import pandas as pd
    import os
    import glob
    import numpy as np

    # use glob to get all the csv files
    # in the folder
    # tsv_files = glob.glob("../../tsv_files/supersense_tsv_files-11-20/*.tsv")
    tsv_files = glob.glob("../../tsv_files/supersense_tsv_files-02-25/*.tsv")

    # create a main DataFrame object
    appended_data = []

    for f in tsv_files:
        book_df = pd.read_csv(f, sep="\t", header=0)
        book_df['book_title'] = os.path.basename(f).split(".")[0]
        book_df['count'] = 0
        book_df['total_count'] = 0
        appended_data.append(book_df)

    main_df = pd.concat(appended_data)
    main_df = main_df.filter(items=['supersense_category', 'text', 'book_title', 'count', 'total_count'])
    loc_df = main_df.loc[main_df['supersense_category'] == 'noun.location']
    group_df = main_df.loc[main_df['supersense_category'] == 'noun.group']
    main_df = pd.concat([loc_df, group_df])
    print(main_df)

    # book_specific_noun_location_word_count
    main_df = main_df.groupby(["text", "total_count", "book_title", "supersense_category"], as_index=False)["count"].count()
    # main_df = main_df.groupby(["text"], as_index=False)["total_count"].sum()
    main_df['total_count'] = main_df.groupby(["text"])['count'].transform('sum')


    print(main_df.head())
    main_df.to_csv("noun_location_word_count_across_all_books_supersense.csv")
