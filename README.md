# Penstagram 2.0

$$\text{\textit{A fake social media app by MemoryOverload}}$$

## What is Penstagram 2.0?
In the Disney channel show *The Owl House*, Penstagram is a social media app that denizens of the Boiling Isles can use to talk about their day, rant about the atrocities committed by the Emperor's Coven, share cute pictures, stuff like that. This project aims to replicate the Penstagram experience for us mortals in the Human Realm through a story on AO3, which is unsurprisingly called [Penstagram 2.0 (but on AO3!)](https://archiveofourown.org/works/47292868/chapters/119167231).

![Darius' Penstagram, showing a post made by Raine Whispers (@rainey.day).](images/Darius-Penstagram.png)

$$\text{\small Photo: \textit{The Owl House}, "Any Sport In A Storm"}$$

## Okay, but why post this on AO3?
Why not?

## Can I Make My Own Version of Penstagram 2.0?
Be my guest! I'm making this under GPL 3.0, which means that anyone and everyone can copy, modify, or do whatever to this project.

## Code Breakdown
This project is written in Python, with the final output file being the incredibly creatively named [`penstagram_2.html`](/penstagram_2.html). In terms of actual executable code, the only file that really does anything when you run it is [html_generator.py](/html_generator.py). All the other files are basically just data storage, so running them doesn't really do anything. (Given, running one of the data files would define a dictionary, but then the program would terminate with no output.)

## html_generator.py
Since this is the only really interesting file, lets talk about it. The very first thing the program does is that it imports all the data from the other files. (Wouldn't be a good social media app if there weren't any posts, right?) The imports are broken into a couple big categories. First there is the actual user feeds. This is the first thing you see when you click on a profile to "log in" as. Then, there are the helper functions that make it easier to create a post or properly identify a tagged account, things like that. After that is the private messages and notifcations.Those are the two tabs on the right side of the navbar at the bottom of the "scroll". Finally, the trending posts are also imported for each user. Those are the posts that can be found by pressing the small magnifying class in the navbar.

Now that everything we need is imported, we can start putting together the HTML code. The HTML begins with a, you guessed it, `<HTML>` tag. It then links to the `penstagram.css` style sheet. (This is the same sheet that serves as the Work Skin on AO3.) Then comes the disclaimer to tell readers to turn on Creator Style.

Why should the reader turn on Creator Style? Because if they have it turned on, this is what they'll see when they load up the story.

![Yay this is what we want! :)](images/good%20scroll.jpg)

But if they have Creator Style off, then they see this monstrosity.

![AHH kill it with fire](images/bad%20scroll.jpg)
