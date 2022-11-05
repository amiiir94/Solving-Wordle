{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b6b44d80",
   "metadata": {},
   "outputs": [],
   "source": [
    "from english_words import english_words_lower_set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d5fd0c51",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mydic(n):\n",
    "    mywords = set()\n",
    "    for word in english_words_lower_set:\n",
    "        if len(word)==n:\n",
    "            mywords.add(word)\n",
    "    return mywords\n",
    "\n",
    "correct = dict()\n",
    "wrong=[]\n",
    "wrong_place = dict()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f9819af4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def wordfinder():\n",
    "     \n",
    "    allwords = mydic(5)\n",
    "    while(True):\n",
    "        print(\"give your guess:\")\n",
    "        guess = input().lower()\n",
    "        if(len(guess) == 5):\n",
    "            print(\"c:corrent , w:wrong , p:wrong place\")\n",
    "            result = input().lower()\n",
    "            possible_words = checker(allwords, guess , result)\n",
    "            print(possible_words)\n",
    "        else:\n",
    "            print(\"should be 5 elements!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "91fafd9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def checker(dic, guess , result):\n",
    "    new_dic= set()\n",
    "    #correct = dict()\n",
    "    #wrong=[]\n",
    "    #wrong_place = dict()\n",
    "    for i in range(0,5):\n",
    "        if result[i]=='c' :\n",
    "            correct[i] = guess[i]\n",
    "        if(result[i]=='p'):\n",
    "            wrong_place[i] = guess[i]\n",
    "    for i in range(0,5):\n",
    "        if(result[i] == 'w'):\n",
    "            if(guess[i] not in correct.values() and guess[i] not in wrong_place.values()):\n",
    "                wrong.append(guess[i])\n",
    "    for word in dic :\n",
    "        if correct_check(word , correct) and wrong_check(word ,wrong ) and place_check(word , wrong_place):\n",
    "            new_dic.add(word)\n",
    "            \n",
    "    return new_dic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "06d3847c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def correct_check(word , check_dict):\n",
    "    for key , value in check_dict.items() :\n",
    "        if(word[key]!= value):\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def wrong_check(word ,check_dict ):\n",
    "    for i in check_dict:\n",
    "        if i in word:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def place_check(word , check_dict):\n",
    "    for key , value in check_dict.items():\n",
    "        if word[key]==value or value not in word:\n",
    "            return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdecc6fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "give your guess:\n",
      "crown\n",
      "c:corrent , w:wrong , p:wrong place\n",
      "wwwww\n",
      "{'flush', 'fluke', 'shyly', 'midas', 'gummy', 'fiske', 'build', 'helix', 'yeats', 'tapis', 'laity', 'elegy', 'keats', 'livid', 'talky', 'miami', 'devil', 'jiffy', 'zeiss', 'might', 'shave', 'glide', 'balmy', 'medea', 'vivid', 'butyl', 'talus', 'tippy', 'madam', 'mazda', 'lethe', 'basil', 'beaux', 'split', 'fully', 'blade', 'dusky', 'apply', 'zesty', 'hamal', 'gluey', 'felix', 'sight', 'jazzy', 'dusty', 'duffy', 'plait', 'lithe', 'agate', 'papal', 'splat', 'heave', 'image', 'style', 'passe', 'pampa', 'pusey', 'emily', 'smile', 'gauge', 'pasty', 'usual', 'amble', 'depth', 'shelf', 'abuse', 'hague', 'petit', 'admix', 'amide', 'salad', 'stage', 'speak', 'blatz', 'gutsy', 'glyph', 'bella', 'gaffe', 'suite', 'sleet', 'shame', 'pique', 'stave', 'sleep', 'least', 'exult', 'adage', 'yaqui', 'italy', 'dhabi', 'islet', 'pupil', 'smell', 'usage', 'kathy', 'staff', 'sulfa', 'yates', 'ileum', 'pithy', 'spite', 'flail', 'filly', 'exalt', 'faust', 'stash', 'muggy', 'sable', 'haifa', 'tibet', 'blitz', 'abash', 'alley', 'midst', 'missy', 'spasm', 'tally', 'tepid', 'sushi', 'layup', 'shaft', 'alike', 'bleak', 'midge', 'dully', 'ideal', 'lymph', 'dealt', 'jaime', 'sleek', 'thumb', 'basis', 'salle', 'mauve', 'assai', 'title', 'gauss', 'slide', 'amass', 'mabel', 'susie', 'lapse', 'david', 'staid', 'stead', 'pease', 'fluff', 'glass', 'exist', 'blast', 'elves', 'magma', 'quiet', 'adieu', 'habib', 'adept', 'gully', 'timid', 'pixel', 'bezel', 'vague', 'fahey', 'paula', 'pauli', 'amaze', 'haley', 'selma', 'setup', 'bully', 'agave', 'leggy', 'aides', 'bambi', 'fight', 'theme', 'bliss', 'happy', 'fusty', 'sepia', 'milky', 'spill', 'aleph', 'essex', 'bette', 'sheet', 'latex', 'vault', 'shill', 'gibby', 'skill', 'saute', 'mummy', 'amiss', 'lemma', 'allay', 'jesus', 'gases', 'patty', 'smelt', \"she'd\", 'aegis', 'baste', 'elute', 'sheik', 'quill', 'blake', 'sheaf', 'exile', 'fetus', 'lykes', 'stilt', 'silky', 'edify', 'issue', 'state', 'delve', 'slake', 'hubby', 'impel', 'flame', 'beebe', 'sulky', 'alias', 'delhi', 'lydia', 'beady', 'leila', 'ethel', 'small', 'bulge', 'emile', 'dizzy', 'medal', 'stump', 'septa', 'vigil', 'adele', 'heavy', 'heath', 'betsy', 'teddy', 'fuzzy', 'plumb', 'shall', 'table', 'hedge', 'smash', 'kulak', 'shake', 'gemma', 'stupa', 'blush', 'spade', 'slush', 'levis', 'sieve', 'gypsy', 'bluet', 'tuple', 'patsy', 'legal', 'laugh', 'pause', 'abase', 'sault', 'melee', 'steve', 'meaty', 'pushy', 'guest', 'puffy', 'davit', 'sadie', 'salty', 'teeth', 'stahl', 'utile', 'these', 'datum', 'jesse', 'betty', 'guide', 'vitae', 'steal', 'shale', 'bizet', 'biggs', 'sepal', 'dulse', 'light', 'multi', 'steel', 'halma', 'jukes', 'lumpy', 'paste', 'addle', 'leigh', 'valet', 'islam', 'bushy', 'beast', 'steep', 'simla', 'buggy', 'mixup', 'daley', 'basel', 'humus', 'ladle', 'plush', 'tizzy', 'jelly', 'pleat', 'yeast', 'fifty', 'algae', 'axial', 'exude', 'atlas', 'baggy', 'styli', 'leeds', 'hasty', 'shiva', 'haste', 'tidal', 'degas', 'shady', 'taiga', 'metal', 'algal', 'yield', 'vella', 'field', 'quasi', 'sappy', 'judge', 'testy', 'phase', 'seedy', 'tease', 'sully', 'gules', 'mushy', 'messy', 'slave', 'skulk', 'salem', 'fussy', 'adult', 'plaid', 'filth', 'media', 'phyla', 'pupal', 'jules', 'stagy', 'aisle', 'puppy', 'empty', 'butte', 'theft', 'tibia', 'malta', 'diety', 'bassi', 'embed', 'vaduz', 'davis', 'leafy', 'elite', 'balky', 'mamma', 'assay', 'pussy', 'fugue', 'julie', 'situs', 'elate', 'bulky', 'flask', 'bathe', 'evade', 'beget', 'debut', 'patti', 'steam', 'lefty', 'degum', 'value', 'daffy', 'slimy', 'levee', 'essay', 'label', 'taffy', 'keyes', 'spiky', 'spike', \"he'll\", 'fatal', 'peale', 'guilt', 'tulip', 'eagle', 'etude', 'tampa', 'valid', \"it'll\", 'spume', 'della', 'petal', 'thigh', 'abbey', 'allis', 'abyss', 'kidde', 'eight', 'gassy', 'kafka', 'gaudy', 'dietz', 'giles', 'psalm', 'playa', 'sedge', 'hesse', 'tipsy', 'queue', 'gamut', 'flesh', 'deify', 'helga', 'abate', 'bleat', 'lease', 'quilt', 'veldt', 'digit', 'bleed', 'daddy', 'abbas', 'death', 'pygmy', 'fault', 'alibi', 'fudge', 'plate', 'malay', 'badge', 'geigy', 'delft', 'baldy', 'misty', 'gauzy', 'tight', 'fugal', 'hippy', 'delia', 'jimmy', 'heady', 'gamma', 'quaff', 'piggy', 'seize', 'muddy', 'mealy', 'bless', 'debit', 'ampex', 'mayst', 'beefy', 'amuse', 'kudzu', 'beset', 'bayda', 'begat', 'shape', 'adapt', 'lipid', 'splay', 'buzzy', 'flake', 'tulle', 'stile', 'easel', 'stale', 'pizza', 'fifth', 'false', 'hades', 'hayes', 'quell', 'slept', 'peste', 'meiji', 'filet', 'dubhe', 'steak', 'gibbs', 'maple', 'sixth', 'siege', 'vital', 'savvy', 'sixty', 'steed', 'titus', 'pabst', 'hiatt', 'stuff', 'judas', 'habit', 'peppy', 'suave', 'ellis', 'mavis', 'level', 'gusty', 'fetid', 'debug', 'pedal', 'stall', 'babel', 'bluff', 'glaze', 'shell', 'ababa', 'billy', 'equip', 'slate', 'plaza', 'julia', 'agile', 'belie', 'lilly', 'julep', 'musty', 'seamy', 'balsa', 'quail', 'villa', 'gauze', 'labia', 'quite', 'leave', 'elude', 'slump', 'squid', 'salve', 'shish', 'study', 'dixie', 'beige', 'estes', 'tulsa', 'sheep', 'apple', 'fetal', 'still', 'sammy', 'hilly', 'slash', 'katie', 'thief', 'sisal', 'budge', 'gleam', 'musky', 'dally', 'llama', 'squat', 'ahead', 'album', 'allyl', 'gates', 'hazel', 'tamil', 'blest', 'audit', 'james', 'hilum', 'taste', 'aphid', 'piety', 'admit', 'peaky', 'ample', 'hefty', 'phage', 'demit', 'flash', 'peggy', 'leapt', 'spitz', 'stake', 'bilge', 'silty', 'blaze', 'sibyl', 'telex', 'affix', 'eddie', 'plasm', 'delay', 'timex', 'smith', 'spate', 'speed', 'peepy', 'lapel', 'limit', 'u.s.a', 'quest', 'tempt', 'belly', 'giddy', 'flute', 'built', 'amity', 'thule', 'aside', 'sigma', 'edith', 'deity', 'tilde', 'gavel', 'guile', 'maybe', 'buddy', 'xylem', 'healy', 'dumpy', 'skate', 'saudi', 'texas', 'fable', 'leaky', 'filmy', 'batik', 'klaus', 'pasha', 'amply', 'putty', 'fluid', 'muzak', 'sybil', 'skiff', 'thyme', 'tappa', 'upset', 'skull', 'pepsi', 'belle', 'tatty', 'thump', 'allah', 'glade', 'latus', 'vista', 'kappa', 'samba', 'addis', 'blame', 'befit', 'staph', 'effie', 'stalk', 'bedim', 'stiff', 'plump', 'plume', 'debby', 'plead', 'stamp', 'shaky', 'yalta', 'lusty', 'halve', 'palsy', 'tepee', 'dummy', 'idyll', 'bumpy', 'pappy', 'haiti', 'faith', 'bevel', 'visit', 'kabul', 'bible', 'skimp', 'betel', 'egypt', 'humid', 'sally', 'miles', 'papua', 'pulse', 'hausa', 'feast', 'leash', 'basal', 'delta', 'fleet', 'paddy', 'fishy', 'gable', 'elsie', 'husky', 'gimpy', 'guild', 'silas', 'spilt', 'guess', 'geese', 'ditty', 'avail', 'daisy', 'matte', 'tithe', 'quash', 'elide', 'lisle', 'abide', 'kelly', 'bugle', 'khaki', 'petty', 'silly', 'libya', 'smite', 'expel', 'keith', 'mafia', 'kitty', 'biddy', 'haiku', 'guise', 'alpha', 'maxim', 'ledge', 'valve', 'iliad', 'qualm', 'spell', 'equal', 'alive', 'ethyl', 'imbue', 'getty', 'fatty', 'theta', 'libel', 'slime', 'sykes', 'sidle', 'jumpy', 'shift', 'squad', 'lathe', 'skeet', 'shade', 'blimp', 'heigh', 'asset', 'quake', 'assam', 'hetty', 'tasty', 'flaky', 'pupae', 'tilth'}\n",
      "give your guess:\n",
      "built\n",
      "c:corrent , w:wrong , p:wrong place\n",
      "wwwpw\n",
      "{'splay', 'elves', 'flake', 'lease', 'expel', 'easel', 'papal', 'slave', 'levee', 'false', 'leaky', 'palsy', 'salem', 'flash', 'leave', 'lykes', 'alpha', 'salve', 'legal', 'delve', 'slake', 'elegy', 'daley', 'alley', 'haley', 'flame', 'selma', 'melee', 'malay', 'valve', 'ledge', 'leggy', 'leash', 'plasm', 'delay', 'algae', 'allah', 'glyph', 'glade', 'lapel', 'slash', 'lymph', 'level', 'gleam', 'medal', 'llama', 'sleep', 'aleph', 'sleek', 'leeds', 'leafy', 'allyl', 'sepal', 'pedal', 'xylem', 'hamal', 'lapse', 'glaze', 'plead', 'halma', 'algal', 'hazel', 'flask', 'lemma', 'gavel', 'allay', 'playa', 'flaky', 'halve', 'plaza', 'glass', 'flesh', 'salad', 'helga'}\n",
      "give your guess:\n",
      "salve\n",
      "c:corrent , w:wrong , p:wrong place\n",
      "wppcc\n",
      "{'leave'}\n",
      "give your guess:\n"
     ]
    }
   ],
   "source": [
    "wordfinder()"
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
