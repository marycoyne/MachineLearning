# MachineLearning

Download the assignment dataset from https://www.scss.tcd.ie/Doug.Leith/CSU44061/2021/supp.php. Important: You must fetch your own copy of the dataset, do not
use the dataset downloaded by someone else.

The data file consists of lines of json content. Each line contains data for one user
review gathered from the Steam online gaming platform. To read in the data you can
use:
    import j s o n l i n e s
    X= [ ] ; y = [ ] ; z =[]
    with open ( ’ r e vi e w s 0 . j l ’ , ’ rb ’ ) a s f :
      f o r item i n j s o n l i n e s . r e a d e r ( f ) :
      X. append ( item [ ’ te x t ’ ] )
      y . append ( item [ ’ voted up ’ ] )
      z . append ( item [ ’ e a r l y a c c e s s ’ ] )
The ’text’ field in the json gives the review text, the ’voted up’ field is true when the
reviewer recommends the game and otherwise ’false’, the ’early access’ field is true
when the review is for a beta version of the game (i.e. before full release).

Write a short report evaluating whether the review text can be used to (i) predict the review polarity (where a game has been “voted up” or not by the reviewer) and (ii) predict whether the review is for an “early access” version of a game or not. Hint: Select two or three machine learning approaches, apply them to the dataset and critically evaluate their classification performance. Remember it’s v important to clearly explain/justify any design choices that you make and any conclusions you arrive at. Include any code you use in an appendix. [75 marks: indicative breakdown (i) feature engineering 20 marks, (ii) machine learning methodology 20 marks, (iii) evaluation 25 marks, (iv) report presentation 10 marks]
