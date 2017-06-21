# Python Concordance Script
## Synopsis
This Concordance Project contains 3 modules:
  1) multiConcordance.py<br />
  2) concordance.py<br />
  3) word.py<br />
  
  The goal of these modules is to create an object which stores each unique word, the number of times it was used, and the sentences it was used in for a single or multiple text files. The data for each text file is stored in a Concordance class. Multiple text files can be stored and aggregated using the MultipleConcordance class.
  
## Running the script
You must install the python module pattern.en from http://www.clips.ua.ac.be/pattern<br />
To run the script you have 2 options.
  1) On a single directory containing text files <br />
    `python main.py $DIR`
  2) On multiple files <br />
    `python main.py $FILE1 $FILE2`
    
To run the test script<br />
  `python test.py`

#### Output
The program will print the contents of the concordance object to stdout. It uses the writeMethod of the class.<br />
The output formats as below<br />
```
34. in
  input/description.txt   {2:1,2}
  input/semiColon.txt     {1:1}
```
**34** - The list is ordered in alphabetical order. This is the 34th unique word from all text files <br />
**in** - The word that is being described <br />
**input/description.txt** - This means the word *in* showed up in the file description.txt <br />
**{2:1,2}** - The number before the colon the word count, and the two numbers after are the sentences the word showed up in. The word *in* showed up in description.txt 2 times, and appeared in sentence 1 & 2 of description.txt <br />

## Modules

#### Pattern.en
Language parsing was done using the [pattern.en module](http://www.clips.ua.ac.be/pattern) from the [Computational Linguistics & Phycholingual Research Center](http://www.clips.ua.ac.be/)

#### Word
The Word class has 2 properties. <br />
1) `int count` - The number of times the word appears <br />
2) `int[] sentences` - An array containing the sentence numbers the word appears in <br />

###### Init
To initialize a word <br />
`wordObject = Word(int sentence)`
This will initialize the object to a count of 1 with the sentences array populated by the parameter <br />

###### Add
To add to the word <br />
`Word.add(wordObject, int sentence)`
This will add to the array that containes the sentence numbers as well as increment the count by 1 <br />

###### Get Count
Get Word Count - Returns int <br />
`Word.getWordCount(wordObject)`

###### Get Sentences
Get Sentences Array - Returns int array <br />
`Word.getSentences(wordObject)`

###### Get String
Get String of Word - Returns string <br />
`Word.writeword(wordObject)`

#### Concordance
The Concordance class has 2 properties. <br />
1) `String fileName` - The name of the Concordance <br />
2) `Dictionary<String word, Word wordObject> concordance` - A dictionary. The key is the word and the value is an instance of the Word Class <br />

###### Init
To initialize a concordance pass it a file name<br />
`concordanceObject = Concordance(String fileName)`
This will parse the file and create the object. The Dictionary will be populated.

###### Get Name
Get Name of Concordance - Returns String <br />
`Concordance.getFileName(concordanceObject)` 

###### Get Word Count
Get the total word count - Returns int <br />
`Concordance.getWordCount(concordanceObject)`

###### Get Dictionary
Get the dictionary property - Returns Dictionary<String word, Word wordObject> <br />
`Concordance.getConcordance(concordanceObject)`

###### Get String
Get String of Concordance - Returns string <br />
`Concordance.writeword(wordObject)`

The output formats as below<br />
```
5. in                   {2:1,2}
```
**5** - The list is ordered in alphabetical order. This is the 5th unique word from all this file <br />
**in** - The word that is being described <br />
**{2:1,2}** - The number before the colon the word count, and the two numbers after are the sentences the word showed up in. The word *in* showed up in this file 2 times, and appeared in sentence 1 & 2 <br />

#### MultipleConcordance
The MultipleConcordance class has 2 properties
1) `Dictionary<String fileName, Concordance concordanceObject> concordances` - This dictionary's key is the name of the file it is representing. The value is a Concordance Object that contains all the information about its words <br />
2) `Dictionary<String word, String[] files> allConcordances `- This dictionary's key is the unique word found in one of the many concordance objects. The value is an array of fileNames it appears in. The fileNames are used as the key for the concordances dictionary above.

###### Init
To initialize the MultipleConcordance. <br />
`multipleConcordanceObject = MultipleConcordance()`

###### Add File
To add a file to the concordance simple pass the file path <br />
`MultipleConcordance.add(multipleConcordanceObject, fileName)`

###### Get Concordance
To get a specific concordance pass the name of the file - Returns Concordance Object<br />
`MultipleConcordance.getConcordance(multipleConcordanceObject, fileName)`

###### Get String of Specific Concordance
To get a string of a specific concordance <br />
`MultipleConcordance.writeConcordance(multipleConcordanceObject, fileName)`

###### Get String of All Concordances
To get a string containing all the concordances information <br />
`MultipleConcordance.writeAllConcordances(multipleConcordanceObject)`

## Authors

* **Ron Basumallik** - [Github](https://github.com/spothedog1)

## License

This project is licensed under the MIT License


