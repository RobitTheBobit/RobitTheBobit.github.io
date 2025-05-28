from flask import Flask, render_template   # CONTRIBUTION -- Start of CHATGPT Contribution (imports flask as FLASK,
                                           # and the render_template funct)

portfolio = Flask(__name__)                # finds all needed folders relative to the position of routes.py


@portfolio.route('/')
def index():
    # Render a page that extends base.html
    return render_template('index.html')    # CONTRIBUTION -- End of CHATGPT Contribution

@portfolio.route('/about')                  #about route
def about():
    academics = [
        "Electrical Engineering Major at RIT — 2029",
        "The Clarkson School — 2024",
        "Millbrook High School — 2023"
    ]                                       #CHATGPT edit: give a reusable template INSTEAD of hardcoded plaintext
    professionalInterests = [
        "Computer Science, Hardware, && Software",
        "Current Events && The World Around Me",
        "Electrical Engineering && Electronics",
        "Education && Learning",
        "Mathematics && Statistics?*",
        "Physics"
    ]
    hobbies = [
        "Playing Video Games with friends",
        "Walking my precious lil corgi",
        "Borking SSDs by encrypting my Linux installs :(",
        "Listening to music*",
        "Reading books*"
    ]
    biography = [
        "My name is Matthew D. Hogencamp. I was born on April 20th, 2006 to a loving mother. "
        "I attended the Millbrook Central School District in Millbrook, NY: Getting my HS diploma from Millbrook HS. "
        "Due to being bullied and being academically excellent, I enrolled in The Clarkson School at Clarkson University. "
        "As of 2025, I am an Electrical Engineering student at RIT with a passion for technology. "
        "I have a sister, an adorable corgi, and a loving family."
    ]
    achievements = [
        "RIT - Dean's List",
        "The Clarkson School @CU - Graduation",
        "Millbrook High School - High School Algebra Award",
        "CS50x - Certificate of Completion"
    ]
    lifeGoals = [
        "Get involed in semi-conducters. ",
        "Build some really cool devices (like a microprocessor). ",
        "Have a Linux install last more than 2 years with no major issues. ",
        "Voluteer more",
        "Learn more about finance",
        "Learn more in general"
    ]
    aboutInfo = {
        "Row_1": {
            "Academics": academics,
            "Interests": professionalInterests,
            "Hobbies": hobbies
        },
        "Row_2": {
            "Biography": biography,
            "Achievements": achievements,
            "Life Goals": lifeGoals
        }
    }                       # Suggested by AI to avoid hardcoding multiple for loops, I was thinking along the same lines so I thought to ask CHATGPT.
    return render_template('about.html', aboutInfo=aboutInfo)    #returns the rendered about page, forwards variables to client

@portfolio.route('/projects')
def projects():
    firstLinuxInstall = """In the 6th grade, I noticed that my computer wasn't able to install Windows Security Updates.
    I investigated and learned that this was due to my laptop being a pile of e-waste.

    The specs were abysmal (4GB DDR3 RAM, 32GB NAND Flash, Intel Celeron Inside), and all resources were eaten up by the OS and old Microsoft Edge.

    I wanted to learn more about why this machine sucked, so I did. I listened to tech influencers like LTT to learn about consumer hardware,
    and I began looking for ways to solve the issue of having no free storage on my PC. That’s when I stumbled across Linux Mint.

    Eventually, I found an old flash drive, installed Linux Mint on it, and painlessly installed it on my laptop—transforming it from an unusable
    machine into a usable one!

    Below is a picture of what this laptop (now unusable for my current purposes) looks like now!


    """

    firstDesktopComputer = """Over the summer between 9th and 10th grade, I fulfilled a longtime dream of mine—building my own desktop PC.

    I had bought all the parts 2 years earlier, but then the GPU cryptomining shortage hit and I couldn’t find an affordable GPU.

    Eventually, I scored a deal on a refurbished EVGA 3070TI near the end of the shortage. I followed LTT’s “How to Build a PC” guide and finally built it.
    It was hard work, and a dream come true.

    See below for some pictures of this desktop!
    """

    bitSerialFSM = """As the final project for Digital Systems I at RIT (EEEE120), I designed a 5-bit full adder and wrote documentation for it.

    The design had 4 major components:
    1. A control FSM (either Mealy or Moore),
    2. Two 5-bit accumulators,
    3. A 1-bit serial adder.

    I built this over the course of 1–2 weeks while also writing the documentation.

    By the time it was due, I had created a working machine that met the project specs, tested it in hardware, and documented simulated results
    (except timing simulations, which I forgot to include). It was a super fun project that helped solidify my understanding of FSMs and core digital design concepts!
    """

    firstWebsite = """After learning about web-development, Flask, Jinja, and Bootstrap in the second-to-last week of CS50x, I wanted to revisit Week 8 and
    build my own personal website: a website that I could update as time went on to display my skills in programming so that my friends and employers
    can see what I have been up to and the cool things that I have done!

    I also wanted to solidify the lessons I had learned through this course about writing clean code, reading documentation, and responsibly using AI.
    I am proud of this website for being the culmination of these efforts, and I am hopeful that future me will find any reconfigs of this codebase
    to be simple, easy, and overall straightforward!

    For any Harvard students reading this, you all are super lucky to have Malan as a CS professor! I'm Jealous!

    Quack
    Quack, Quack
    Quack, Quack Quack
    Quack, Quack, Quack, Quack
    """

    projectsInfo = {
        "Row_1projects": {
            "First Website": firstWebsite,
            "Bit Serial Finite State Machine": bitSerialFSM,
            "First Desktop Computer Build": firstDesktopComputer,
            "First Linux Installation": firstLinuxInstall
        }
    }

    return render_template('projects.html', projectsInfo=projectsInfo)

@portfolio.route('/portfolio')
def myportfolio():
    myRITExperience = "Through much hard work, I have completed my 1st year at RIT with a 3.6 cumulative GPA!"
    myClarksonSchoolGraduation = """Through a lot of hard work and some good fortune,
    I was able to attend and graduate from The Clarkson School at Clarkson University as a part of the Class of 2024!"""
    myMillbrookHSGraduation = """I endured many year at the Millbrook Central School District. I am glad that these days
    are in the past."""

    thisWebsite = "This website... no images needed! xp"
    myCS50xCertificate = "My CS50x Certificate: Proof that I successfully completed CS50x!"
    myBitSerialFSM = "Click on the above image to cycle between hardware tests of my Bit Serial FSM!"

    myDesktop = "Click on the above image to cycle between snapshots of my Desktop from components to completion!"
    my1stLinuxInstall = "Click on the above image to cycle between snapshots of my 1st Linux Install and its host machine!"
    myCatchAllUSBDrive = "Click the above image to cycle between snapshots of my all-purpose USB drive!"
    myRasPi4 = "Click the above image to cycle between snapshots of a RasPi4 that I setup!"

    portfolioInfo = {
        "Row_1": {
            "My RIT Experience": myRITExperience,
            "My Clarkson School Graduation": myClarksonSchoolGraduation,
            "My Millbrook High School Graduation": myMillbrookHSGraduation
        },
        "Row_2": {
            "This Website": thisWebsite,
            "My CS50x Certificate": myCS50xCertificate,
            "My BitSerialFSM": myBitSerialFSM
        },
        "Row_3": {
            "My Desktop": myDesktop,
            "My 1st Linux Install": my1stLinuxInstall,
            "My Catch All USB Drive": myCatchAllUSBDrive,
        },
        "Row_4": {
            "My Raspberry Pi 4": myRasPi4
        }
    }


    return render_template('portfolio.html', portfolioInfo=portfolioInfo)

@portfolio.route('/gallery')
def gallery():
    message = "TODO"
    return render_template('apology.html', message=message)

@portfolio.route('/media')
def media():
    message = "TODO"
    return render_template('apology.html', message=message)
