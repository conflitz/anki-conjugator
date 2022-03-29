## conjugations2csv

This is a Python script that converts a csv file of Spanish verbs to an [Anki](https://apps.ankiweb.net/)-importable text file for the conjugations of those verbs. It is essentially an Anki equivalent of [Maestro Spanish](https://maestrospanish.com/) that can be highly customized and used offline. Beyond just getting lists of conjugations, this script also allows the use of prompts that enhance learning (see [this](#but-why)).

### How to use

Create a csv file of Spanish verbs; remove whitespace and ensure that the delimiter is the symbol `,`. The [csv file](https://github.com/dtwil/conjugations2csv/blob/master/spa_verb_groups.csv) provided in thie repo covers every family of Spanish verb patterns, but you can provide your own. Line breaks in the csv are ignored.

### But why?

There are a freaking ton of conjugations to know in Spanish, but luckily there are only about [39 major conjugation patterns](https://www.hackettpublishing.com/spanish-grammar/VERBFORMS/verbsystem-list.htm#reg) - every word in that list appears in this deck except for parecer and esparcir. By learning to recognize these 39 groups you can conjugate almost any verb in Spanish. Pretty cool, right? I’m not the first one to notice or use this idea - sites like [Maestro Spanish](https://maestrospanish.com/) put it to good use. In fact, this deck is very much an Anki-fied version of that site.

[Anki](https://apps.ankiweb.net/) is open-source (translation: free!) flashcard software that uses a spaced repetition system (SRS). If you get a card right, you’ll see it less - if you get it wrong, you’ll see it more. This is excellent for reinforcing Spanish conjugations you need to know. Anki is available on iOS and Android, making it easy to practice on the go or offline. It also can sync your progress through AnkiWeb.

So why did I bother making this if Maestro Spanish already exists? First, although Maestro Spanish is excellent (I used it daily for months with great success), it doesn’t cover gerunds. Second, I wanted a tool I could be sure wouldn’t disappear in case the owner didn’t pay to keep it up. Third, if you choose to type in conjugations, mere typos will make the SRS think you didn’t know the conjugation when you really did. With Anki, you can judge for yourself. Also, with this deck it’s possible to customize which verbs appear and introduce helpful visual cues to reduce silly mistakes.

Here’s what I mean by that: say you’re being tested on the perfect present tense (one of the ways to use the past in Spanish). The card uses the symbol <- [like this](https://i.imgur.com/E6BMpqY.png) to make sure you realize it’s the past perfect. Here’s an example for a gerund (present progressive) that uses ... [like this](https://i.imgur.com/pXsGR8S.png). In all, the symbols I used were - for present, <- for present perfect, … for gerund, ↓ for preterite, ← for imperfect, → for future, ? for conditional, ~ for present subjunctive, ↜ for imperfect subjunctive, and ! for imperative. You’ll also notice the context clues for which tense to use. I give my thanks to /u/functools and their Italian conjugation deck for the idea.


As the title says, this deck is also sorted by frequency, so you’ll see more common conjugations before less common ones. This isn’t perfect (for example, como is the second most common conjugation because my program couldn’t distinguish between I eat and how), but these are only minor issues. As you become comfortable with conjugating in Spanish, I encourage you to change the deck options to introduce new cards at random (you don’t want to practice conjugating every form of zurcir over and over again, do you?).

I strongly encourage you to type each conjugation, which is why the deck is set up that way by default. You probably won’t really learn the conjugations otherwise. If you really don’t want to type, you can change this by (on the desktop version of Anki) clicking Add -> make sure type is “Conjugation” -> change {{type:Conjugation}} in the front template to just {{Conjugation}}. Also, be sure to do your reviews every day - Anki isn’t super useful if you don’t. 

Hope this deck helps you become a conjugation master! ¡Buena suerte!
