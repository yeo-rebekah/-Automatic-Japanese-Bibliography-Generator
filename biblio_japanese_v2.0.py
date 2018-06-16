#function for book citation
def bookCitation(authorInput,yearInput,titleInput, publisherInput):
    print(str(authorInput)+'('+str(yearInput)+')'+'『'+str(titleInput)+'』'+str(publisherInput))
    print('')
    print(str(authorInput)+'('+str(yearInput)+')')
    
#function for a citation from a portion of a book
def bookPortionCitation(authorPortionInput,yearInput,titlePortionInput,authorInput,titleInput, publisherInput,pagesInput):
    print('')    
    print(str(authorPortionInput)+'('+str(yearInput)+')'+'「'+str(titlePortionInput)+'」'+str(authorInput)+'『'+str(titleInput)+'』'+str(publisherInput)+', '+str(pagesInput))
    print('')
    print(str(authorInput)+'('+str(yearInput)+')')
    
#function for citation from a translated book
def translatedCitation(authorForeignInput,yearPublishedInput,titleForeignInput,sourceForeignInput, translatorInput, titleInput, yearInput, publisherInput):
    print('')    
    print(str(authorForeignInput)+' ('+str(yearPublishedInput)+') '+str(titleForeignInput)+'. '+str(sourceForeignInput)+'. '+str(translatorInput)+'訳'+'『'+str(titleInput)+'』'+'('+str(yearInput)+')'+str(publisherInput))
    print('')
    print(str(authorInput)+'('+str(yearInput)+')')
    
#function for journal citations
def journalCitation(authorInput,yearInput,titleInput, journalInput, volumeInput,pagesInput):
    print('')    
    print(str(authorInput)+'('+str(yearInput)+')'+'「'+str(titleInput)+'」'+'『'+str(journalInput)+'』'+str(volumeInput)+', '+str(pagesInput))
    print('')
    print(str(authorInput)+'('+str(yearInput)+')')
    
#function for newspaper citations (print)
def newspaperCitation(authorInput,newspaperInput,yearInput, monthInput, dayInput, kanInput, hanInput, menInput):
    print('')    
    print(str(authorInput)+'「'+str(newspaperInput)+'」'+str(yearInput)+'年'+str(monthInput)+'月'+str(dayInput)+'日'+str(kanInput)+', '+str(hanInput)+'判'+str(menInput)+'面')
    print('')
    print(str(authorInput)+'('+str(yearInput)+')')
    
#function for internet articles citations
def websiteCitation(authorInput,titleInput, yearInput, monthInput,urlInput, accessedInput):
    print('')
    print(str(authorInput)+'「'+str(titleInput)+'('+str(yearInput)+'年'+str(monthInput)+'月'+')'+'」'+str(urlInput)+'　(参照'+str(accessedInput)+')')
    print('')
    print(str(authorInput)+'('+str(yearInput)+')')

print('参考文献')
print('1.書籍（本）Book')
print('2.書籍に載っている一部の章や論文 Portion of a Book')
print('3.書籍（翻訳書）Translated Book')
print('4.学会誌・雑誌掲載されている論文 Journal Article')
print('5.新聞記事 Newspaper Article (Print)')
print('6.インターネットの資料 Internet source')


print('Press enter to exit')
selection=int(input('Please input between 1-6: '))
if selection==1: #Book
    print('Book citation')
    print('e.g.中山・森本編(2018)『吾輩は猫』出版社')
    author=input('Author(s) (please separate by ・): ')
    year=input('Year: ')
    title=input('Title: ')
    publisher=input('Publisher: ')
    output=bookCitation(author,year,title,publisher)
elif selection==2: # Portion of a Book
    print('Portion of a book citation')
    print('e.g. 中山・森(2018)「猫のしっぽ」信長・しげしげ編『吾輩は猫』出版社, 82-91 ')
    authorPortion=input('Author(s) of portion (please separate by ・): ')
    year=input('Year: ')
    titlePortion=input('Title of portion: ')
    author=input('Book Author(s) (please separate by ・): ')
    title=input('Title: ')
    publisher=input('Publisher: ')
    pages=input('Pages: ')
    output=bookPortionCitation(authorPortion,year,titlePortion,author,title,publisher,pages)
elif selection==3: #Translated Book
    print('Translated literature citation')
    print('e.g. Tokugawa, Nobunobu (2017) Skiing with friends Daiedo Printing. 徳川繁々訳『スキー』(2018)出版社')
    authorForeign=input('Foreign Author(s) (please separate by , ): ')
    yearPublished=input('Year Published: ')
    titleForeign=input('Foreign Title: ')
    sourceForeign=input('Source (e.g. cambridge press): ')
    translator=input('Translator: ')
    title=input('Japanese title: ')
    year=input('Year translation was published: ')
    publisher=input('Japan Publisher: ')
    output=translatedCitation(authorForeign,yearPublished,titleForeign,sourceForeign, translator, title, year, publisher)
elif selection==4: #Journal Article
    print('Journal citation')
    print('e.g. 信長・しげしげ(2018)「なぜスキーが気持ちいいか」『大江戸大学紀要』32-1, 52-60')
    author=input('Author(s) (please separate by ・): ')
    year=input('Year: ')
    title=input('Title: ')
    journal=input('Journal: ')
    volume=input('Volume: ')
    pages=input('Pages: ')
    output=journalCitation(author,year,title, journal, volume,pages)
elif selection==5: #Newspaper Article
    print('Newspaper (print) citation')
    print('e.g. トトロ・メイ「となりのトトロ」2018年04月03日朝刊, 14判7面')
    author=input('Author(s) (please separate by ・): ')
    newspaper=input('Newspaper: ')
    year=input('Year: ')
    month=input('Month: ')
    day=input('Day: ')
    kan=input('刊: ')
    han=input('判: ')
    men=input('面: ')
    output=newspaperCitation(author,newspaper,year, month, day, kan, han, men)
elif selection==6: #Internet Source
    print('Internet source citation')
    print('e.g. ハウル・ソフィー「ハウルの動く城(2018年03日)」www.studioghibli .com　(参照2018-04-30)')
    author=input('Author(s) (please separate by ・): ')
    title=input('Title of article: ')
    year=input('Year: ')
    month=input('Month: ')
    url=input('URL: ')
    accessedDate=input('Accessed Date (YYYY-MM-DD): ')
    output=websiteCitation(author,title, year, month,url, accessedDate)
