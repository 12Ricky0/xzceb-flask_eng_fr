from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''Takes in a text english_text, returns the french_text of english_text'''
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text


def french_to_english(french_text):

    '''Takes in a text french_text, returns the english_text of french_text'''
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text