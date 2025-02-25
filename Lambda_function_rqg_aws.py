import random

def lambda_handler(event, context):
    quotes = [
        {"quote": "The trouble with programmers is that you can never tell what a programmer is doing until its too late.", "author": "Seymour Cray"},
        {"quote": "Programs must be written for people to read, and only incidentally for machines to execute.", "author": "Hal Abelson"},
        {"quote": "The best error message is the one that never shows up.", "author": "Thomas Fuchs"},
        {"quote": "Code is like humor. When you have to explain it, its bad.", "author": "Cory House"},
        {"quote": "The function of good software is to make the complex appear to be simple.", "author": "Grady Booch"},
        {"quote": "The most damaging phrase in the language is: 'Its always been done that way.'", "author": "Grace Hopper"},
        {"quote": "Truth can only be found in one place: the code.", "author": "Robert C. Martin"},
        {"quote": "Every great developer you know got there by solving problems they were unqualified to solve until they actually did it.", "author": "Patrick McKenzie"},
        {"quote": "It’s not at all important to get it right the first time. Its vitally important to get it right the last time.", "author": "Andrew Hunt and David Thomas"},
        {"quote": "Measuring programming progress by lines of code is like measuring aircraft building progress by weight.", "author": "Bill Gates"},
        {"quote": "The function of good software is to make the complex appear to be simple.", "author": "Grady Booch"},
        {"quote": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
        {"quote": "The most disastrous thing that you can ever learn is your first programming language.", "author": "Alan Kay"},
        {"quote": "The only language that looks the same before and after RSA encryption.", "author": "Keith Bostic"},
        {"quote": "It's harder to read code than to write it.", "author": "Joel Spolsky"},
        {"quote": "Programs must be written for people to read, and only incidentally for machines to execute.", "author": "Hal Abelson and Gerald Jay Sussman"},
        {"quote": "The best way to predict the future is to implement it.", "author": "David Heinemeier Hansson"},
        {"quote": "The next best thing to having good ideas is recognizing good ideas from your users. Sometimes the latter is better.", "author": "Eric S. Raymond"},
        {"quote": "The strength of JavaScript is that you can do anything. The weakness is that you will.", "author": "Reg Braithwaite"},
        {"quote": "Without requirements or design, programming is the art of adding bugs to an empty text file.", "author": "Louis Srygley"},
        {"quote": "Code never lies, comments sometimes do.", "author": "Ron Jeffries"},
        {"quote": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
        {"quote": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
        {"quote": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "author": "Martin Fowler"},
        {"quote": "Everybody in this country should learn to program a computer because it teaches you how to think.", "author": "Steve Jobs"},
        {"quote": "Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program.", "author": "Linus Torvalds"},
        {"quote": "Im not a great programmer. Im just a good programmer with great habits.", "author": "Kent Beck"},
        {"quote": "Programming isnt about what you know. its about what you can figure out.", "author": "Chris Pine"},
        {"quote": "The only way to learn a new programming language is by writing programs in it.", "author": "Dennis Ritchie"},
        {"quote": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
        {"quote": "Learning to write programs stretches your mind and helps you think better, creates a way of thinking about things that I think is helpful in all domains.", "author": "Bill Gates"},
        {"quote": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
        {"quote": "Programs are meant to be read by humans and only incidentally for computers to execute.", "author": "Donald Knuth"},
        {"quote": "Programming can be fun, so can cryptography; however, they should not be combined.", "author": "Kreitzberg and Shneiderman"},
        {"quote": "The only way to go fast, is to go well.", "author": "Robert C. Martin"},    {"quote": "To iterate is human, to recurse divine.", "author": "L. Peter Deutsch"},
        {"quote": "Code is poetry.", "author": "Automattic (Motto of WordPress)"},
        {"quote": "Before software can be reusable it first has to be usable.", "author": "Ralph Johnson"},
        {"quote": "The craft of programming begins with empathy, not formatting or languages or tools or algorithms or data structures.", "author": "Kent Beck"},
        {"quote": "The trouble with programmers is that you can never tell what a programmer is doing until its too late.", "author": "Seymour Cray"},
        {"quote": "Programs must be written for people to read, and only incidentally for machines to execute.", "author": "Hal Abelson and Gerald Jay Sussman"},
        {"quote": "Optimism is an occupational hazard of programming: feedback is the treatment.", "author": "Kent Beck"},
        {"quote": "In order to be irreplaceable, one must always be different.", "author": "Coco Chanel (adapted to a programming context)"},
        {"quote": "Good code is its own best documentation.", "author": "Steve McConnell"},
        {"quote": "Programming is the art of algorithm design and the craft of debugging errant code.", "author": "Ellen Ullman"},
        {"quote": "The best error message is the one that never shows up.", "author": "Thomas Fuchs"},
        {"quote": "A computer once beat me at chess, but it was no match for me at kickboxing.", "author": "Emo Philips"},
        {"quote": "I dont care if it works on your machine! We are not shipping your machine!", "author": "Vidiu Platon"},
        {"quote": "Every great developer you know got there by solving problems they were unqualified to solve until they actually did it.", "author": "Patrick McKenzie"},
        {"quote": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
        {"quote": "Coding is not just a career, its a craft.", "author": "Glenford Myers"},
        {"quote": "Programs are meant to be read by humans and only incidentally for computers to execute.", "author": "Donald Knuth"},
        {"quote": "In programming, as in everything else, to be in error is to be reborn.", "author": "Alan Perlis"},
        {"quote": "Programming is a skill best acquired by practice and example rather than from books.", "author": "Alan Turing"},
        {"quote": "The most secure computer is one thats unplugged, locked in a safe, and buried 20 feet under the ground in a secret location... and I'm not even too sure about that one.", "author": "Dennis Hughes"},
        {"quote": "One of the best programming skills you can have is knowing when to walk away for a while.", "author": "Oscar Godson"},
        {"quote": "The computer is incredibly fast, accurate, and stupid. Man is unbelievably slow, inaccurate, and brilliant. The marriage of the two is a force beyond calculation.", "author": "Leo Cherne"},
        {"quote": "Code is not just code, it is a story of understanding, told in a language that machines and humans can both understand.", "author": "Joshua Bloch"},
        {"quote": "I think Microsoft named .Net so it wouldn’t show up in a Unix directory listing.", "author": "Oktal"},
        {"quote": "One mans crappy software is another mans full-time job.", "author": "Jessica Gaston"},
        {"quote": "Bad code can always be improved; its the clever code that causes all the problems.", "author": "Pete Cordell"},
        {"quote": "Any application that can be written in JavaScript, will eventually be written in JavaScript.", "author": "Jeff Atwood"},
        {"quote": "A good programmer looks both ways before crossing a one-way street.", "author": "Doug Linder"},
        {"quote": "If you cant write it down in English, you cant code it.", "author": "Peter Halpern"},
        {"quote": "There are only two kinds of programming languages: those people always bitch about and those nobody uses.", "author": "Bjarne Stroustrup"},
        {"quote": "If debugging is the process of removing bugs, then programming must be the process of putting them in.", "author": "Edsger Dijkstra"}
    ]
    
    selected_quote = random.choice(quotes)
    
    # HTML template with embedded CSS for styling
    html_content = f"""
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }}
        .quote-container {{
            text-align: center;
            background-color: transparent; /* Transparent background */
            padding: 10px; /* Adjusted padding */
            border-radius: 8px;
            width: 80%;
            max-width: 600px;
            box-shadow: none; /* No box shadow */
            margin: auto; /* Center the container */
        }}
        .quote-text {{
            font-size: 24px;
            color: #9370db; /* Quote text color */
            margin-bottom: 5px; /* Adjusted margin */
        }}
        .quote-author {{
            font-size: 18px;
            color: #777; /* Author name color */
        }}
    </style>
</head>
<body>
    <div class="quote-container">
        <p class="quote-text">"{selected_quote['quote']}"</p>
        <p class="quote-author">- {selected_quote['author']}</p>
    </div>
</body>
</html>
"""

    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_content
    }
