# BeatFormatter
A script to format YouTube type beat titles &amp; descriptions. It also looks up the tags, that are going to create the best engagement on your video! Enjoy :)

---------

Run the script and give in, whats asked for. It will give you your description and title saved in a subdirectory, which is called the name of your beat. 
enjoy :) 

---------

To modify for your own kind of formatting: 
main.py: 
- In "Types" are all the types concerning licencing included 
  - If you have more than three, you need to add on the profit_types below
  
- In final_beat_name_var is the formatting of you title 
  - It is a combination of variables and text, so look out for ""

- In "description" is the formatting of your description 

- To change the tag-generator website, look into the TagScraping.py file 
  - Change Website and then inspect the new website for the following:
  - Input field (XPATH)
  - Possibly a cockie accept button (XPATH)
  - Search field (XPATH)
  - Copy button (XPATH)

---------
