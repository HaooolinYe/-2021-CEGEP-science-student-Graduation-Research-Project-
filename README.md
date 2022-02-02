## Searching for Permutations of Strings
Searching for Strings with length over ten thousand... ...

Team members: Haolin Ye(1931141) and Xiaoming Zhang(1931049)

R. Vincent, instructor

420-LCU-05: Programming Techniques and Application

## About this project
This is third problem of the 2020 Canadian Computing Competition, Senior level. Following the instruction of this problem, “Search for Strings”,  the program is able to take two input strings and return an integer that is the times of the distinct permutations of the short string appearing in the long string.

## Sounds Easy, no...?
This problem may sounds easy the first time you see it, because it can be done nin just a few lines of code in the language you are familiar with. Yet, if you check the CCC contest website. We are expecting to have large input file...we are talking about <strong> ten thousand characters </strong>!
A program is said to be valid if it can return the correct output in less than 3 seconds. Spoiler,even if you realize the hash can be helpful for solving this problem, it is still really hard for a hashing method in Java or Python to get you into the 3 seconds!( We tried it in C, and (un)fortunately C wins again with the exact same algorithm using hash).
Our final version of the program satisty the 3-second rule however, and it explicitely returns the output in less than 1 second for every test cases CCC gives!! inclusing the 10 thousand one, haha.

## Ready to explore some hashing method?!
As we mentioned, we put our hope on improving the hash method. If you don't know about <a href="https://computersciencewiki.org/index.php/Hashing"> hash </a>, then there are tons of articles and videos out there that explains it well,so feel free to check those out. I <strong> strongly </strong>recommand this <a href="https://www.youtube.com/watch?v=FhNJ6aikTVI">Youtube Video</a> on the hash data structures, which helps you understand why hash and why it makes things fast.

The hash method we are using here, is call the rolling hash method. For this algorithm, if you want to know in details, you can check out the websites below or download the our python program to check it out. I do find some dynamic programming idea in this algorithm as we are building a table to store the information we want, rather than hash every strings we see. Once you have the table and the indices of a subsstring, knowing the hash value should just take O(1) time which is amazing! Leave an issue if what I said feels wrong to you; otherwise, enjoy the fun of the algorithm!

## Improvement, maybe??
* Calculating the upper and lower bound, be aware of the space of improvement
* Dynamic programming feels the right way to give us a same or more optimal solution

Websites that we found helpful:
* https://courses.csail.mit.edu/6.006/spring11/rec/rec06.pdf
* https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm

## Documentation
The improvements we made:

* First version: we implement the python list count() method, and we make a copy of every slice to store in the list containing existing permutations. This passes 96 tests in CCC 2020 Senior Problem 3.
* Second version: the only change is we make a copy of every slice but we compute the hash value of them and store in that list. But the improvement of efficiency is not obvious.This passes 114 tests in CCC 2020 Senior Problem 3.
* Third version: We replace the count() method with two histograms that only takes O(1) time to compute.This passes 117 tests in CCC 2020 Senior Problem 3.
* Final version: Based one the updated version of histogram, we implement the rolling hash method to get the hash values of all matched substrings and store these in that list. This passes all 127 tests in CCC 2020 Senior Problem 3 and each time returns the correct output in less then 0.4 second, thought some of the input has a length over ten thousand.

Check out <a href = "https://github.com/HaooolinYe/-2021-CEGEP-science-student-Graduation-Research-Project-/blob/main/Documentation.docx">this</a> if you are interested in the documentation of this project.
