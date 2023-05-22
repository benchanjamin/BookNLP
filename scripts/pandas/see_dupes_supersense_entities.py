if __name__ == '__main__':
    import pandas as pd
    entities = pd.read_csv("noun_location_word_count_across_all_books_entities.csv")
    supersense = pd.read_csv("noun_location_word_count_across_all_books_supersense.csv")
    df_all1 = entities.merge(supersense.drop_duplicates(), on=['text', 'text'],
                       how='left', indicator=True)
    df_all2 = entities.merge(supersense.drop_duplicates(), on=['text', 'text'],
                       how='right', indicator=True)
    df_all1.to_csv("has_entities_differences.csv")
    df_all2.to_csv("has_supersense_differences.csv")
