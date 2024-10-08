import regex as re
#import nltk
#nltk.download('words')
#from nltk.corpus import words

# Load English words from NLTK corpus
#english_words = set(words.words())
def count_words(text):
    # Define special words that aren't part of nltk corpus
    #special_words = set([
        #'in', 'from', 'to', 'on', 'out', 'at', 'but', 'because', 'although', 'so', 'and',
        #'you', 'I', 'me', 'he', 'him', 'himself', 'ourselves', 'mine', 'hers', 'a', 'an', 'the',
        #'yipe', 'yum', 'yak', 'ugh', 'huh'
    #])
    name_list = [
        r"[(Ondra|Ondřej)]*\sMandík",
        r"[Alena]*\sReichlová",
        r"[(Jára|Jaroslav)]*\sCimrman"
    ]
    # Name censor
    for name in name_list:
        text = re.sub(name, " [AUTOMATICKYCENZUROVÁNO] ", text)

    # Replace dates
    text = re.sub(r'[\p{L}]+\s\d{1,2}(st|nd|rd|th)?\s\d{4}', "date", text)

    # Replace addresses
    text = re.sub(r'\d+\s[\p{L} ]+,(\s[\p{Lu}][\p{L}]+)+(?!\s[\p{Lu}][\p{L}]+)', "address", text)

    # Replace contractions
    contractions = { "'ll": "will", "'ve": "have", "'re": "are", "'m": "am", "'d": "would", "can't": "cannot","'t": "not"}
    for contraction, expanded_form in contractions.items():
        text = re.sub(re.escape(contraction), " " + expanded_form, text)

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Remove numbers
    text = re.sub(r'\b\d+\b', '', text)

    # Split text into words
    words_in_text = text.split()
    print(words_in_text)
    word_count = 0
    for word in words_in_text:
        word = word.lower()

        # Increment count for ordinal numbers
        if re.match(r'\d+(st|nd|rd|th)', word):
            word_count += 1
            continue
        word_count += 1
    return word_count
# Sample text
text = "I can't believe it 58! I live at 10 Broadway, New York City and visited on September 11th 2014. Mandík byl na konferenci s Alenou Reichlovou. Jára Cimrman přednesl svou teorii. Také se tam objevil Ondřej Mandík a Jaroslav Cimrman."
# Test function
print("count:", count_words(text))
