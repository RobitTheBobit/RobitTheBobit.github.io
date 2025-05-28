#### Description: This project is one born out of my own desire to have a customizable portfolio that serves itself as a piece of my own portfolio.
#### From this desire, I wanted to apply what I have learned over the past 2-3 weeks in the Web-Dev section of this course in a KISS manner (Keep it Simple Stupid).
#### Ultimately, I decided that I wanted to go back to the concept of a personal website shown in Week 8 and really make something professional.
#### From this desire to create a professional page to display my work, my project idea came: a personal website. I decided to stick with the same stack that was used in Week 8: HTML (+Bootstrap && Jinja), CSS (+Bootstrap), JS (+Popper), and Flask.
#### I wanted to recreate what I had previously made in HTML, but modernized it with the superior tools that I now had at my disposal.

#### I used Jinja to create templates and to automate what I otherwise would have had to have copied and pasted, or remade by hand;
#### I used Flask to avoid hard-coding the contents of my websites, and to instead store these contents in dicts server-side;
#### I used HTML for structuring each of my pages in unique ways that gave each subdomain a unique flair;
#### and I used CSS to make everything look as human-readable and user-friendly as I possibly could given my self-imposed design spec and deadline.
#### I didn't end up using JS due to time constraints and due to my own desire to keep things simple and elegant. While I certainly could have used JS--
#### and in the future will end up reconfiguring this website many times--I decided not to due to these previously mentioned concerns.
#### Furthermore; I did not end up using the full capabilities of Flask to interface with SQL databases since I wasn't allowing any kind of user-input on the server-side. Instead, I was building a nice little personal project that I could expand with some hardships.

### Tech Debt
#### In this project, I attempted to minimize the Tech Debt accumulated in creating this project. This meant looking to wikis on ways to avoid hard-coding in my template where loops could be used instead; leaving a smaller code footprint and less code for future me to maintain, further-develop, and reconfigure. This means that in the future, I could instead focus on creating new webpages or refining some other code that I messed up rather than having to sift through a bunch of copy-pasta.
#### One of my favorite examples of my eliminating of Technical Debt came in the form of creating a dictionary of dictionaries that would store strings, arrays of strings, or arrays of images that I could then loop through to create my webpages. This cut down on the amount of repository code a metric fuck ton, and I am very proud of my having thought of this. That being said, I do feel that I relied a bit too much on CHATGPT for help in realizing my idea of making a dictionary of dictionaries so that I could easily create 2D arrays of data to display on my webpages for this project.

### Compartmentalization
#### I tried to compartmentalize information in certain files to the best of my abilities given the time I had given myself. For me, this meant creating variables in routes.py that I could then pass to my .html pages for rendering, client-side storage, and ultimately displaying and the sort. I had considered using files to store text that could then be called from static and fed into the html file through a set of functions in python; however, I didn't know if Python had this capability and I figured that it would be rather easy to store strings in some kind of files going forward: cutting and pasting the string contents from routes.py to some set of YAML or JSON files. I avoided doing this in my project since I found that when I asked CHATGPT about storing such info in files to be accessed by Python, that I didn't really have a firm grasp of what it was suggesting. Due to this, I found that I would rather do what I knew how to rather than use something that CHATGPT suggested I use without understanding it all too well. I still don't get how JSON and YAML files store data, and what makes them a good choice here according to CHATGPT; however, if I were to take comparmentalization to the next level, I would move these strings and maybe the arrays and dicts I made in routes.py and move them either to lower-level python files or to static asset files of either the JSON, YAML, or TXT types.

### Grid Usage (HTML + Bootstrap)
#### In most of the webpages I built for this website/project, I used the grid system from Bootstrap as it was told in the docs. I used this system to create a Projects page that I could use to list all of the projects that I have worked on and documented in my life. I also used this grid system to create a Portfolio page where I could display projects, acomplishments, and milestones that others may look fondly upon such as my Building of my very own Personal Desktop, or the time I built this website after taking CS50x. I plan on creating a template at some point for a v2 of this website that I plan on using to develop a gallery page where I can post a bajilion photos of my super cute corgi :3. Overall, making the grid was a very fun thing to do, as was finding out how easy it was to cite the work of others in the comments of my code.

### Nav Bar
#### At first the most daunting part of this project, the navbar was something that I actually discovered how to create on my own using Bootstrap and the Bootstrap docs. Through these docs, I was able to make a superior version of what I had made in Week 8 where instead of using a few buttons I was able to instead create a fully-fledged navibar. My only qualm with my work here is that the text in my navbar is **noticably off-center from the rest of my page**. This deeply upsets my inner designer and symmetry lover, yet, it is something that I am willing to live with until I create a version 2 of this wonderful project. For this navbar, i used <a> tags with hrefs set equal to the other pages in my website that I wanted to display. From my index page to my portfolio page, all of my work is on display here! I even created an apology .html page that I could load with a custom message defined server-side. This allowed me to put in a TODO for my Gallery page until I get around to working out the kinks in this version and design this corgi fanboy page for the v2 launch.

### Footer
#### My footer is a sticky footer that admittedly I needed CHATGPT to let me know about so that I could use the proper Bootstrap class to create it. It contains some professional contact info and a link to both my Github and LinkedIn Accounts so that Employers can reach out to me if they see doing so fit! I also included my senior year-book HS quote, and my current college and my year of graduation in this footer.

### Index Page
#### My index page has text telling the visiter how happy I am that the site is getting used and two pictures of my corgi flanking the text on each side. My index page also has the navbar and footer that I created in my base.html file. This index page needed to use the grid system to get the images and text to display properly (as intented)

### About Page
#### My about page uses the grid system to have a nice format where a bunch of bulleted lists are shown on each row. These bulleted lists are great since they allow me to concisely express information about myself that I might not want to go into depth about, or just choose to format them similarly to paragraphs so I can express long-form, standard english information. I also utilized dictionaries and loops in creating this webpage to minimize the codebase future me would have to maintain. I also included a lot of basic information about myself, some of which I might remove when I make this site public. Overall, this was one of the most enjoyable and challenging sections for me to create.

### Projects Page
#### My projects page also uses the grid system to display the contents of the page in a scroll-down format. I find this format to be really hard to scale, so in the future I might make it a portal where I have a grid of projects on display or I might just fuse this page with the portfolio page I created later in development that has a format that is much easier to scale up to large sizes. Who knows! Later on, I might even create a filter feature so that people can sort my project my keywords or tags!

### Portfolio Page
#### My portfolio page uses the grid system alongside loops to create a visually pleasing array of cards. Each card has the ability to hold one image related to the project that their text describes. In the future, I might make it so that these cards can have a movie of images behind them, or that they might be linked with dynamically generated websites that talk about the project that the user clicks on. While I am unsure of how I would design such a website, I have some starting ideas and I think it would be a pretty badass move if I managed to pull it off!

### Apology Page
#### Since I haven't completed the Gallery Page, and since in the future I will have a website that is always in development, I decided that I would instead like to make an apology page with a message slot that could have anything loaded into it depending on the input that the developer associated with the flask route. While I could have used a text file or something as where the message would be pulled from, I instead just chose to hardcode it into the routes.py file. Currently, this page works great and can be reconfigured if needed in the future.

### AI USAGE && OUTSIDE CODE
#### Some code provided by Brave Search's AI and CHATGPT were used alongside outside sources that are mentioned in the comments of my code.

#### Be good to eachother and yourself. Remember...
> "the wisdom of a fool won't set you free" - World Order
