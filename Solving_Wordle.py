{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b6b44d80",
   "metadata": {},
   "outputs": [],
   "source": [
    "from english_words import english_words_lower_set\n",
    "# import a dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d5fd0c51",
   "metadata": {},
   "outputs": [],
   "source": [
    "# we find all the five-letter words in dictionary and make all the letters in lower\n",
    "def mydic(n):\n",
    "    mywords = set()\n",
    "    for word in english_words_lower_set:\n",
    "        if len(word)==n:\n",
    "            mywords.add(word)\n",
    "    return mywords\n",
    "# make dictionaries for correct letters in correct place , and the one in wrong places\n",
    "# male a list for wrong letters\n",
    "correct = dict() # using dict to show key as letter position and value as correct letter\n",
    "wrong=[]\n",
    "wrong_place = dict() # using dict to show value as letter, key as position, that letter can not be there"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f9819af4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def wordfinder():\n",
    "     \n",
    "    allwords = mydic(5)\n",
    "    while(True):\n",
    "        print(\"give your guess:\")\n",
    "        guess = input().lower() # hier we put out guess\n",
    "        if(len(guess) == 5):\n",
    "            print(\"c:corrent , w:wrong , p:wrong place\")# write the result in printed format\n",
    "            result = input().lower() # check our guess with result and write a 5-letter word in a format that is written up\n",
    "            possible_words = checker(allwords, guess , result) # check the guess with result and gives possible words back\n",
    "            print(possible_words)\n",
    "        else:\n",
    "            print(\"should be 5 elements!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "91fafd9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def checker(dic, guess , result): # generate new dictionary with possible letters and positions based on last guess and its result\n",
    "    new_dic= set()\n",
    "    #correct = dict()\n",
    "    #wrong=[]\n",
    "    #wrong_place = dict()\n",
    "    for i in range(0,5): # saving correct letters from guess\n",
    "        if result[i]=='c' : #if it was in the correct position save it in corrects\n",
    "            correct[i] = guess[i]\n",
    "        if(result[i]=='p'): #if it was in the wrong position save it in wrong_place\n",
    "            wrong_place[i] = guess[i]\n",
    "    for i in range(0,5):\n",
    "        if(result[i] == 'w'): # for saving wrong letters and not use them again\n",
    "            if(guess[i] not in correct.values() and guess[i] not in wrong_place.values()): \n",
    "                wrong.append(guess[i])\n",
    "    for word in dic :     \n",
    "        if correct_check(word , correct) and wrong_check(word ,wrong ) and place_check(word , wrong_place):\n",
    "            new_dic.add(word) # generate new dictionary, that contains words with possible letters and positions\n",
    "            \n",
    "    return new_dic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "06d3847c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# for generating new dictionary we should check each word in 5-letters-dictionary with correct letters and the wrong ones\n",
    "def correct_check(word , check_dict): # check with correct letters in correct position\n",
    "    for key , value in check_dict.items() :\n",
    "        if(word[key]!= value):\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def wrong_check(word ,check_dict ):   # check with wrong letters\n",
    "    for i in check_dict:\n",
    "        if i in word:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def place_check(word , check_dict):   # check with correct letters in wrong position\n",
    "    for key , value in check_dict.items():\n",
    "        if word[key]==value or value not in word:\n",
    "            return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63065507",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
