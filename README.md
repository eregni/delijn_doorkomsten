### Description
Script to show realtime info from De lijn. I wrote this thing because the official
(android) app works awefully slow on my phone. A solution is to make a terminal program with
(a lot) less feautures:

*   search realtime info for a specific bus stop. When there's no result search for
    a stop by name

*   Filter search results by line nr

I've used Dutch words in the code and comments because I kept the same variable names as found in
the api from De Lijn

usefull sources:  
API https://delijn.docs.apiary.io/


The user gets one input field:
    - type in a stop nr and get the (realtime) info
    - type a name and get a list with search results. each result is a link to the realtime info of that stop

### Usage:
run: python doorkomsten.py
On android:  
use termux on android + the termux-widgets addon. Put a bash script in the termux $HOME/.shortcuts folder who runs
python script  
https://termux.com/


### Idea:
 - GUI on android (beeware, kivy)
 - search for a specific time
 - sort data?
 - storingen?