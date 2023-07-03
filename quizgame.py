<!DOCTYPE html>
<html>
<head>
    <title>Marvel Quiz</title>
</head>
<body>
    <h1>Welcome to the Marvel quiz!</h1>

    <script>
        function checkAnswer(question, correctAnswer) {
            var answer = prompt(question);
            answer = answer.toUpperCase();
            
            if (answer === correctAnswer) {
                document.write("<p>Correct!</p>");
                return 1;
            } else {
                document.write("<p>Incorrect!</p>");
                return 0;
            }
        }

        var correctScore = 0;
        var playing = prompt("Do you want to play?");
        playing = playing.toUpperCase();

        if (playing !== "YES") {
            document.write("<p>Game over!</p>");
        } else {
            document.write("<p>Ok, let's play!</p>");

            correctScore += checkAnswer("What is Spider-Man's real name?\nA.)Peter Porker\nB.)Peter Parker\nC.)Tony Stark\nD.)Steve", "B");
            correctScore += checkAnswer("Is Iron Man rich or poor?\nA.)Rich\nB.)Poor", "A");
            correctScore += checkAnswer("Was Captain America ever an Avenger?\nA.)No\nB.)Definitely Not\nC.)Maybe\nD.)Yes", "D");
            correctScore += checkAnswer("Is Thor from Asgard or Earth?\nA.)Asgard\nB.)Earth", "A");
            correctScore += checkAnswer("Can any other Avenger lift Thor's hammer?\nA.)No\nB.)Yes", "B");
            correctScore += checkAnswer("Who fixed Ultron?\nA.)Spider Man\nB.)Tony Stark\nC.)Einstein\nD.)Brianna Caza", "B");
            correctScore += checkAnswer("In Spider-Man Homecoming, is Spider Man in High School, College, Middle School, or none?\nA.)High School\nB.)College\nC.)None\nD.)Middle School", "A");
            correctScore += checkAnswer("In Civil War, who's team does Spider Man join?\nA.)Aunt May\nB.)Hulk\nC.)Iron Man\nD.)Captain America", "C");
            correctScore += checkAnswer("Does Hawkeye have children?\nA.)Yes\nB.)No", "A");
            correctScore += checkAnswer("How long was Captain America frozen for?\nA.)12 years\nB.)4 years\nC.)300 years\nD.)66 years", "C");
            correctScore += checkAnswer("Who is Thor's brother?\nA.)Captain America\nB.)Captain Marvel\nC.)Loki\nD.)Odin", "C");
            correctScore += checkAnswer("What is Hulk's real name?\nA.)Bruce Banter\nB.)Bruce Baner\nC.)Bruce Banner\nD.)Bruce Bannner", "C");
            correctScore += checkAnswer("What color is Hulk's skin?\nA.)Green\nB.)Purple\nC.)Blue\nD.)Rainbow", "A");
            correctScore += checkAnswer("Does Captain America approve of curse words?\nA.)No\nB.)Yes\nC.)Sometimes", "A");
            correctScore += checkAnswer("How many Infinity Stones are there?\nA.)4\nB.)5\nC.)3\nD.)6", "D");

            document.write("<p>You got " + correctScore + " questions correct</p>");
            document.write("<p>You got " + (correctScore / 15 * 100) + "%</p>");

