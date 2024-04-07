from text_classification.algo_manager import Spacy
from text_classification.model import Sentiment, SentimentAnalysis


def test_spacy_positive_sentiment():
    text = 'This tea is fun to watch as the flower expands in the water. Very smooth taste and can be used again and again in the same day. If you love tea, you gotta try these "flowering teas"'
    model = Spacy()
    positive_sentiment = SentimentAnalysis(sentiment=Sentiment.POSITIVE)
    assert positive_sentiment == model.predict(text)


def test_spacy_negative_sentiment():
    text = "I bought this product at a local store, not from this seller.  I usually use Wellness canned food, but thought my cat was bored and wanted something new.  So I picked this up, knowing that Evo is a really good brand (like Wellness).<br /><br />It is one of the most disgusting smelling cat foods I've ever had the displeasure of using.  I was gagging while trying to put it into the bowl.  My cat took one taste and walked away, and chose to eat nothing until I replaced it 12 hours later with some dry food.  I would try another flavor of their food - since I know it's high quality - but I wouldn't buy the duck flavor again."
    model = Spacy()
    negative_sentiment = SentimentAnalysis(sentiment=Sentiment.NEGATIVE)
    assert negative_sentiment == model.predict(text)