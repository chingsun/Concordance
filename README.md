# Python Concordance Script
### Description
  The concordance.py script will take in a input .txt file and print out  every word in the file in alphabetical order along with the number of times  each word occurs and which sentences the word occurs in
  1) Script will read in the file and turn it into a one line string<br />
  2) The pattern.en module will then parse the string into sentences<br />
  3) The sentences are lists the contain word objects, if a word object  is deemed to be an actual word, then it will be added the Concordance object<br />

### Running the script
You must install the python module pattern.en from http://www.clips.ua.ac.be/pattern                  
`python concordance.py <fileName>`

### Output
The program will print the contents of the concordance object to stdout i.e. <br />
The number before the colon is the number of occurences and the number after is the sentences it occurs in<br />

`a. a                      {2:1,1}`<br />
`b. all                    {1:1}`<br />
`c. alphabetical           {1:1}`<br />
`d. an                     {2:1,1}`<br />
`e. appeared               {1:2}`<br />
`f. arbitrary              {1:1}`<br />
`g. bonus                  {1:2}`<br />
`h. concordance            {1:1}`<br />
`i. document               {1:1}`<br />
`j. each                   {2:2,2}`<br />
`k. english                {1:1}`<br />
`l. frequencies            {1:1}`<br />
`m. generate               {1:1}`<br />
`n. given                  {1:1}`<br />
`o. i.e.                   {1:1}`<br />
`p. in                     {2:1,2}`<br />
`q. label                  {1:2}`<br />
`r. labeled                {1:1}`<br />
`s. list                   {1:1}`<br />
`t. numbers                {1:2}`<br />
`u. occurrence             {1:2}`<br />
`v. occurrences            {1:1}`<br />
`w. of                     {1:1}`<br />
`x. program                {1:1}`<br />
`y. sentence               {1:2}`<br />
`z. text                   {1:1}`<br />
`aa. that                  {1:1}`<br />
`bb. the                   {1:2}`<br />
`cc. which                 {1:2}`<br />
`dd. will                  {1:1}`<br />
`ee. with                  {2:1,2}`<br />
`ff. word                  {3:1,1,2}`<br />
`gg. write                 {1:1}`<br />
`hh. written               {1:1}`<br />

### Modules
Language parsing was done using the [pattern.en module](http://www.clips.ua.ac.be/pattern) from the [Computational Linguistics & Phycholingual Research Center](http://www.clips.ua.ac.be/)

### Authors

* **Ron Basumallik** - [Github](https://github.com/spothedog1)

### License

This project is licensed under the MIT License


