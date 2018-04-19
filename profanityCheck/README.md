# CoppinCS Challenge (Profanity Check)

Problem Statement:
---

Suppose that we are working for an online service that provides a bulletin board for its users. We would like to give our users the option of filtering out profanity. Suppose that we consider the word Cat. Write a program that reads a string from the keyboard and tests whether the string contains one of the profane words. Your program should find words like cAt that differ only in case.
Optional: As an extra challenge, have your program reject only lines that contain a profane word exactly. For example, Catmatic concatenation is a small category. This sentence should not be considered profane.

My Solution
---

* First step is to split the input string by a space, such that we obtain a list of words

* Use a nested loop to iterate over the profance data list and newly created list

* Campare the profane words with the words in the list

* Use flow contorl to determine whether the words in the list matches with the profance data words. If this is the case, the index value of that particular word is append to another array.

* We then remove the item whose index has been stored in the array (use loop to iterate)

* Finally, output the result

**Yadav, Anil (Coppin State University)**