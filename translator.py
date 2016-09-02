# -*- coding: UTF-8 -*-
from mechanize import Browser
from bs4 import BeautifulSoup


dict = {"blank": 'whatever',
             "genitive_singular": 'blank',
             "dative_singular": 'blank',
             "accusative_singular": 'blank',
             "instrumental_singular": 'blank',
             "prepositional_singular": 'blank',
             "nominative_plural": 'blank',
             "genitive_plural": 'blank',
             "dative_plural": 'blank',
             "accusative_plural": 'blank',
             "instrumental_plural": 'blank',
             "prepositional_plural": 'blank',
             "nominative_singular": 'blank',
             "definition": 'blank',
             "alt_translations": "blank",
             "word_type": "blank"
            }



caseList = ["blank",
             "nominative_singular",
             "genitive_singular",
             "dative_singular",
             "accusative_singular",
             "instrumental_singular",
             "prepositional_singular",
             "nominative_plural",
             "genitive_plural",
             "dative_plural",
             "accusative_plural",
             "instrumental_plural",
             "prepositional_plural"
            ]

def analyseGrammar(searchterm):

#SUBMITS SEARCH
    br = Browser()
    br.set_handle_robots(False)
    br.open("http://www.multitran.ru/c/m.exe?a=1&SHL=2")
    br.select_form('translation')
    br.form['s'] = searchterm
    response1 = br.submit()
    soup = BeautifulSoup(response1, "html.parser")

#GET DEFINITION
    dict['definition'] = soup.findAll('a')[17].text
    dict['alt_translations'] = " " + soup.findAll('a')[18].text, " " + soup.findAll('a')[19].text, " " + soup.findAll('a')[20].text
#DETERMINES TYPE
    type = soup.findAll('em')[0].text
    if type == u"сущ.":
        wordtype = "noun."
    elif type == u"гл.":
        wordtype = "verb."
    elif type == u"прил.":
        wordtype = "adjective."
    else:
        wordtype = "word type unknown"

#WHEN NOUN

    if wordtype == "noun.":
        dict['word_type'] = "noun."
        response2 = br.follow_link(nr=13)
        soup2 = BeautifulSoup(response2, "html.parser")
        string = soup2.text
        counter = 0
        list = []
        for word in string.split():
            if counter <= 1:
                if searchterm.decode('utf-8')[0:3] in word:
                    dict[caseList[counter]] = word
                    counter = counter + 1
            elif counter < 13:
                if searchterm.decode('utf-8')[0:3] in word:
                    dict[caseList[counter]] = word[6:]
                    counter = counter + 1
                    if counter == 14:
                        break
        return dict


#WHEN VERB

    if wordtype == "verb.":
        dict['word_type'] = "verb."

        response2 = br.follow_link(nr=13)
        soup2 = BeautifulSoup(response2, "html.parser")
        string = soup2.text
        counter = 0
        list = []
        for word in string.split():
            if counter <= 1:
                if searchterm.decode('utf-8')[0:3] in word:
                    dict[caseList[counter]] = word
                    counter = counter + 1
            elif counter < 13:
                if searchterm.decode('utf-8')[0:3] in word:
                    dict[caseList[counter]] = word[6:]
                    counter = counter + 1
                    if counter == 14:
                        break
        return dict

