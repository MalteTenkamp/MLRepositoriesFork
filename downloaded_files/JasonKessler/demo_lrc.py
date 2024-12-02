import spacy

from scattertext.CorpusFromParsedDocuments import CorpusFromParsedDocuments

from scattertext.SampleCorpora import ConventionData2012
from scattertext import produce_frequency_explorer
from scattertext.termscoring.lrc import LRC

nlp = spacy.blank('en')
nlp.add_pipe('sentencizer')

corpus = CorpusFromParsedDocuments(
    ConventionData2012.get_data().assign(
        Parse=lambda df: df.text.apply(nlp)
    ),
    category_col='party',
    parsed_col='Parse',
).build().get_unigram_corpus().remove_infrequent_words(5)

term_scorer = LRC(
    corpus=corpus,
).set_categories('democrat', ['republican']).use_token_counts_as_doc_sizes()

html = produce_frequency_explorer(
    corpus,
    category='democrat',
    category_name='Democratic',
    not_category_name='Republican',
    minimum_term_frequency=0,
    pmi_threshold_coefficient=0,
    width_in_pixels=1000,
    metadata=lambda c: c.get_df()['speaker'],
    term_scorer=term_scorer
)

open('./demo_lrc.html', 'wb').write(html.encode('utf-8'))
print('Open ./demo_lrc.html in Chrome or Firefox.')
