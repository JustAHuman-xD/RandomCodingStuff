import turtle
import time
import random
import os

Options = {
    "Colors": {
        "red": ["red", "darkred", False],
        "orange": ["orange", "darkorange", False],
        "yellow": ["yellow", "gold", False],
        "green": ["lime", "green", False],
        "blue": ["blue", "darkblue", False],
        "purple": ["magenta", "purple", False],
        "white": ["white", "lightgray", False],
        "black": ["black", "darkgray", False],
        "brown": ["brown", "brown", False],
        "rainbow": ["black", "rainbow", True],
        "jack": ["darkgreen", "forest green", False],
        "custom": ["black", "custom", True]
    },
    "FruitTypes": {
        "apple": [1, "red", "circle"],
        "lemon": [2, "yellow", "circle"],
        "pear": [3, "lime", "triangle"],
        "mango": [4, "orange", "circle"],
        "watermelon": [5, "green", "square"]
    },
    "FruitLevels": {
        "low": 1,
        "medium": 3,
        "high": 5,
    },
    "SnakeTypes": {
        "blocky": "square",
        "circular": "circle",
        "pointed": "triangle",
        "arrow": "arrow"
    },
    "Modifiers": [
        "randomizer",
        "teleporter",
        "onechance",
    ],
    "ModifierInfo": {
        "randomizer": [
            "This modifier randomizes everything!",
            "Your snake, food, foodlevel are all randomized!"
            "If you don't know how you want to play this is a good fit!"
        ],
        "teleporter": [
            "This modifier is one of the hardest modifiers!",
            "This modifier makes the food randomly teleport!",
            "Staying alive is easy but increasing your score is not!"
        ],
        "onechance": [
            "This modifier is easy and hard, it depends on the player",
            "You have one chance. The first food you eat",
            "will increase your length enough to fill the entire screen.",
            "You have to not make a single wrong movement!"
        ]
    }
}
AvailibleColors = [
    "red", "darkred", "orange", "darkorange", "yellow", "gold", "lime",
    "green", "darkgreen", "cyan", "turquoise", "lightblue", "blue", "darkblue",
    "magenta", "purple", "violet", "black", "darkgray", "gray", "lightgray",
    "white", "brown"
]
ColorPatterns = {
    "rainbow": [
        "red",
        "orange",
        "yellow",
        "lime",
        "deepskyblue",
        "magenta",
    ],
    "custom": []
}


def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


#set up screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('white')
wn.setup(width=600, height=600)
wn.tracer(0)


def Game(Color, FruitLevel, FruitType, Shape, Modifier):
    global Count
    global delay

    Count = 0
    delay = 0.125

    segments = []
    foods = []
    headings = {"up": 90, "down": 270, "left": 180, "right": 0}

    #scores
    score = 0
    high_score = 0

    #snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape(Shape)
    head.color(Options["Colors"][Color][0])
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    #snake food
    for x in range(0, Options["FruitLevels"][FruitLevel]):
        food = turtle.Turtle()
        food.speed(0)
        food.shape(Options["FruitTypes"][FruitType][2])
        food.color(Options["FruitTypes"][FruitType][1])
        food.penup()
        food.goto(20 * round(random.randint(-280, 280) / 20),
                  20 * round(random.randint(-280, 280) / 20))
        foods.append(food)

    #scoreboards
    sc = turtle.Turtle()
    sc.speed(0)
    sc.shape("circle")
    sc.color("black")
    sc.penup()
    sc.hideturtle()
    sc.goto(0, 260)
    sc.write("Score: {}  High score: {}".format(score, high_score),
             align="center",
             font=("Comic Sans MS", 24, "normal"))

    if Modifier == "teleporter":
        Count = random.randint(1, 8)

    def Teleporter():
        global Count
        if Modifier == "teleporter" and Count > 0:
            Count = Count - 1
        elif Modifier == "teleporter" and Count == 0:
            for food in foods:
                Pos = GetPos(food)
                food.goto(Pos[0], Pos[1])
            Count = random.randint(1, 8)

    #Functions
    def go_up():
        if head.direction != "down":
            Teleporter()
            head.direction = "up"
            head.setheading(headings[head.direction])

    def go_down():
        if head.direction != "up":
            Teleporter()
            head.direction = "down"
            head.setheading(headings[head.direction])

    def go_left():
        if head.direction != "right":
            Teleporter()
            head.direction = "left"
            head.setheading(headings[head.direction])

    def go_right():
        if head.direction != "left":
            Teleporter()
            head.direction = "right"
            head.setheading(headings[head.direction])

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.setheading(headings[head.direction])
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.setheading(headings[head.direction])
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setheading(headings[head.direction])
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setheading(headings[head.direction])
            head.setx(x + 20)

    #keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "Right")

    #MainLoop
    while True:

        def GetPos(food):
            x = 20 * round(random.randint(-280, 280) / 20)
            y = 20 * round(random.randint(-280, 280) / 20)
            Hit = False
            if head.xcor() == x and head.ycor() == y:
                Hit = True
            for segment in segments:
                if segment.xcor() == x and segment.ycor() == y:
                    Hit = True
            for otherfood in foods:
                if not foods.index(otherfood) == foods.index(food):
                    if otherfood.xcor() == x and otherfood.ycor() == y:
                        Hit = True
            if Hit == False:
                return [x, y]
            else:
                return GetPos(food)

        wn.update()

        #check collision with border area
        if head.xcor() > 280 or head.xcor() < -280 or head.ycor(
        ) > 280 or head.ycor() < -280:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            #hide the segments of body
            for segment in segments:
                segment.goto(1000, 1000)  #out of range
            #clear the segments
            segments.clear()

            #reset score
            score = 0

            for food in foods:
                Pos = GetPos(food)
                food.goto(Pos[0], Pos[1])

            #reset delay
            delay = 0.125

            sc.clear()
            sc.write("Score: {}  High score: {}".format(score, high_score),
                     align="center",
                     font=("Comic Sans MS", 24, "normal"))

        #check collision with food
        for food in foods:
            if head.distance(food) < 20:
                if not Modifier == "onechance":
                    Pos = GetPos(food)
                    food.goto(Pos[0], Pos[1])
                RepeatAmount = Options["FruitTypes"][FruitType][0]
                if Modifier == "onechance":
                    RepeatAmount = 196
                for x in range(0, RepeatAmount):
                    new_segment = turtle.Turtle()
                    new_segment.speed(0)
                    new_segment.shape(Shape)
                    if len(segments) > 0:
                        new_segment.setheading(segments[len(segments) -
                                                        1].heading())
                    else:
                        new_segment.setheading(head.heading())
                    if not Options["Colors"][Color][2] == True:
                        new_segment.color(Options["Colors"][Color][1])
                    else:
                        ColorIndex = -1
                        for segment in segments:
                            ColorIndex = ColorPatterns[Color].index(
                                segment.color()[0])
                        if ColorIndex + 1 < len(ColorPatterns[Color]):
                            new_segment.color(ColorPatterns[Color][ColorIndex +
                                                                   1])
                        else:
                            new_segment.color(ColorPatterns[Color][0])
                    new_segment.penup()
                    segments.append(new_segment)
                    new_segment.goto(1000, 1000)
                if Modifier == "teleporter":
                    for food in foods:
                        Pos = GetPos(food)
                        food.goto(Pos[0], Pos[1])
                    Count = random.randint(1, 8)

                delay -= 0.001
                score += 10

                if score > high_score:
                    high_score = score
                sc.clear()
                sc.write("Score: {}  High score: {}".format(score, high_score),
                         align="center",
                         font=("Comic Sans MS", 24, "normal"))

        for index in range(len(segments) - 1, 0, -1):
            previous = segments[index - 1]
            x = previous.xcor()
            y = previous.ycor()
            segments[index].setheading(previous.heading())
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
            segments[0].setheading(headings[head.direction])
        move()

        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
                score = 0
                delay = 0.125

                for food in foods:
                    Pos = GetPos(food)
                    food.goto(Pos[0], Pos[1])

                sc.clear()
                sc.write("Score: {}  High score: {}".format(score, high_score),
                         align="center",
                         font=("Comic Sans MS", 24, "normal"))
        time.sleep(delay)
    wn.mainloop()


play = input("Would you like to play the Snake Game? (yes/no) ").upper()
if play == "Y" or play == "YES":

    def Select(SelectType, InputMessage):
        Selection = input(InputMessage + " ").lower()
        if Selection in Options[SelectType]:
            print(Selection.capitalize() + " Selected!")
            return Selection
        else:
            print("Invalid Selection!")
            time.sleep(1)
            print("Did you spell it Right?")
            time.sleep(1)
            clear()
            Again = Select(SelectType, InputMessage)
            return Again

    print("Alright Lets Play!")
    time.sleep(1)
    clear()
    print("What Snake do you want?")
    time.sleep(1)
    print("The different snakes have a different Shape!")
    time.sleep(1)
    clear()
    print("You can pick one of These Types:")
    for Type, Table in Options["SnakeTypes"].items():
        print(Type.capitalize())
    Shape = Options["SnakeTypes"][Select("SnakeTypes",
                                         "Which Type would you like?")]
    time.sleep(1)
    clear()
    print("What color do you want your snake to be?")
    time.sleep(1)
    print("You can pick one of the Following:")
    for Color, Table in Options["Colors"].items():
        print(Color.capitalize())
    Color = Select("Colors", "Which Color would you like?")
    time.sleep(1)
    clear()
    if Color == "custom":
        print("Lets make your custom snake!")
        time.sleep(1)

        def getLength():
            clear()
            print("How long do you want the color pattern to be?")
            print("(If you input 3 it will be 3 colors long)")
            time.sleep(1)
            print("Type your number!")
            length = input("Pattern Length: ")
            if length.isdigit():
                return length
            else:
                print("Thats not a Valid Number!")
                time.sleep(1)
                return getLength()

        length = getLength()
        time.sleep(1)
        print("Lets pick our Colors!")
        for amount in range(1, int(length) + 1):
            amount = str(amount)
            clear()
            print("Here are your availible colors!")
            for color in AvailibleColors:
                print(color.capitalize())
            time.sleep(1)

            def getColor():
                print("What color do you want #" + amount + " Segment to be?")
                time.sleep(1)
                color = input("Color: ")
                if color in AvailibleColors:
                    return color
                else:
                    print("Thats not a valid color!")
                    time.sleep(1)
                    return getColor()

            color = getColor()
            ColorPatterns["custom"].append(color)
        print("We are done with our Custom Snake!")
        time.sleep(1)
    clear()
    print("What type of Fruit would you like?")
    time.sleep(1)
    print(
        "The different Fruit Types grant more or less length than the others!")
    time.sleep(1)
    print(
        "For example the Apple only grows your snake by 1 while the Pear grows by 3!"
    )
    time.sleep(1)
    clear()
    print("Here are the Fruit Types:")
    for FoodType, Table in Options["FruitTypes"].items():
        print(FoodType.capitalize() + "-" + str(Table[0]) + " Growth")
    FruitType = Select("FruitTypes", "Which Fruit would you like?")
    time.sleep(1)
    clear()
    print("What Fruit Level would you like?")
    time.sleep(1)
    print("The Fruit Level is the Amount of Fruit in the game at once!")
    time.sleep(1)
    print(
        "For Example if your Fruit Level is set to Low, there is only 1 Piece of Fruit on the Board at a time!"
    )
    time.sleep(1)
    clear()
    print("Here are the Following Fruit levels:")
    for FoodLevel, Amount in Options["FruitLevels"].items():
        print(FoodLevel.capitalize() + "-" + str(Amount) + " Fruits")
    time.sleep(1)
    Fruit = Select("FruitLevels", "What Fruit Level would you like?")
    time.sleep(1)
    clear()
    print("And Finally, would you like to add a Modifier?")
    time.sleep(1)
    print(
        "A modifier will drastically change the way you play, it sometimes ignores your previous choices"
    )
    time.sleep(1)
    print("It gives the game a new spin and makes it more challenging!")
    time.sleep(1)
    global AddMod
    AddMod = input("Do you want a modfifier? (yes/no) ").upper()
    if AddMod == "Y" or AddMod == "YES":

        def AddModifier():
            global AddMod

            def Select():
                global AddMod
                clear()
                print("Your availible Modifiers are:")
                for modifier in Options["Modifiers"]:
                    print(modifier.capitalize())
                time.sleep(1)
                Selected = input("What Modifier would you like?: ").lower()
                if Selected in Options["Modifiers"]:
                    return Selected
                else:
                    print("Invalid Selection!")
                    time.sleep(1)
                    print("Did you spell it right?")
                    time.sleep(1)
                    return Select()

            def Learn():
                global AddMod
                clear()
                print("Your availible Modifiers are:")
                for modifier in Options["Modifiers"]:
                    print(modifier.capitalize())
                LearnAbout = input(
                    "What Modifier would you like to learn about? ").lower()
                if LearnAbout in Options["Modifiers"]:
                    print(LearnAbout.capitalize() + ":")
                    for string in Options["ModifierInfo"][LearnAbout]:
                        print(string)
                        time.sleep(1)
                    input("Press Enter to Continue")
                    time.sleep(1)
                    AddModifier()
                else:
                    print("Invalid Selection!")
                    time.sleep(1)
                    print("Did you spell it right?")
                    time.sleep(1)
                    Learn()

            clear()
            print("Here is every Modifier:")
            for modifier in Options["Modifiers"]:
                print(modifier.capitalize())
            print(
                "Would you like to Select (1), learn more about a Modifier (2), or do Nothing (3)?"
            )
            Choice = input("Choice: ")
            if Choice == "1":
                AddMod = Select()
            elif Choice == "2":
                Learn()
            elif Choice == "3":
                print("Alright we won't have a modifier this time!")
            else:
                print("Invalid Choice")
                time.sleep(1)
                AddModifier()

        AddModifier()
        if AddMod == "onechance":
            Fruit = "low"
        elif AddMod == "randomizer":
            ShapeList = list(Options["SnakeTypes"].items())
            Shape = random.choice(ShapeList)[1]
            ColorList = list(Options["Colors"].items())
            Color = random.choice(ColorList)[0]
            ColorList = list(Options["FruitTypes"].items())
            FruitType = random.choice(ColorList)[0]
            ColorList = list(Options["FruitLevels"].items())
            Fruit = random.choice(ColorList)[0]
    Game(Color, Fruit, FruitType, Shape, AddMod)
    #love you!  you are crazy good at this game!!
