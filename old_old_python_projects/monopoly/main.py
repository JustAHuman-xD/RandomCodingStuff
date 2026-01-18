
import os
import time
from random import randint

global NumberOfPlayers
global Players
global PrintBoard

RunningGames = {}

images = [
    [
        "______________________", 
        "|        .---.        |",
        "|        |#__|        |", 
        "|       =;===;=       |",
        "|       / - - \       |", 
        "|      ( _'.'_ )      |",
        "|     .-`-'^'-`-.     |", 
        "|    |   `>o<'   |    |",
        "|    /     :     \    |", 
        "|   /  /\  :  /\  \   |",
        "| .-'-/ / .-. \ \-'-. |", 
        "|  |_/ /-'   '-\ \_|  |",
        "|     /|   |   |\     |", 
        "|    (_|  /^\  |_)    |",
        "|      |  | |  |      |", 
        "|      |  | |  |      |",
        "|____'==='= ='==='____|"
    ],
]
Board = [
    "————————————————————————————————————————————————————————————————————————————————————————————————————————",
    "|   Free   |Kentucky| Chance |Indiana |Illinois|H&O Rail|Atlantic|Ventnor | Water  | Marvin | Goto Jail|",
    "|  _|¯=\_  | Avenue |  ?     | Avenue | Avenue |  Road  | Avenue | Avenue |  Works | Gardens|  ╔═╦═╦═╗ |",
    "| /o____o_\|        |      ? |        |        |        |        |        |        |        |  ║ ║ ║ ║ |",
    "|  Parking |  $200  |  ?     |  $220  |  $240  |  $200  |  $260  |  $260  |  $150  |  $280  |  ║ ║ ║ ║ |",
    "————————————————————————————————————————————————————————————————————————————————————————————————————————",
    "| New York |                                                                                |  Pacific |",
    "|  Avenue  |   ________________                                                             |   Avenue |",
    "|   $200   |  |                |                                                            |    $300  |",
    "————————————  |                |                                                            ————————————",
    "| Tennessee|  |                |                                                            |NorthCarol|",
    "|  Avenue  |  |________________|                                                            |ina Avenue|",
    "|   $180   |   Community Chest                                                              |   $300   |",
    "————————————                                                                                ————————————",
    "|Community |                                                                                |Community |",
    "|   Chest  |                                                                                |   Chest  |",
    "|          |                                                                                |          |",
    "————————————                                                                                ————————————",
    "| St. James|                                                                                |Pennsylvan|",
    "|  Place   |                   __  __                               _                       |  Avenue  |",
    "|   $180   |                  |  \/  |                             | |                      |   $320   |",
    "————————————                  | \  / | ___  _ __   ___  _ __   ___ | |_   _                 ————————————",
    "|Pennsylvan|                  | |\/| |/ _ \| '_ \ / _ \| '_ \ / _ \| | | | |                |Short Line|",
    "| RailRoad |                  | |  | | (_) | | | | (_) | |_) | (_) | | |_| |                |          |",
    "|   $200   |                  |_|  |_|\___/|_| |_|\___/| .__/ \___/|_|\__, |                |   $200   |",
    "————————————                                           | |             __/ |                ————————————",
    "| Virginia |                                           |_|            |___/                 |  Chance  |",
    "|  Avenue  |                                                                                |  ?   ?   |",
    "|   $160   |                                                                                |    ?     |",
    "————————————                                                                                ————————————",
    "|  States  |                                                                                |Park Place|",
    "|  Avenue  |                                                                                |          |",
    "|   $140   |                                                                                |   $350   |",
    "————————————                                                                                ————————————",
    "| Electric |                                                       ________________         |Luxury Tax|",
    "|  Company |                                                      |      .-.       |        |          |",
    "|   $150   |                                                      |       .'       |        |   $75    |",
    "————————————                                                      |       .        |        ————————————",
    "|St.Charles|                                                      |________________|        | Boardwalk|",
    "|   Place  |                                                            Chance              |          |",
    "|   $140   |                                                                                |   $400   |",
    "————————————————————————————————————————————————————————————————————————————————————————————————————————",
    "| Vi|      |Connet- | Vermont| Chance |Oriental|Reading | Income | Baltic |Commun- |Mediter-|   $200   |",
    "| si|  In  |   -icut| Avenue | ?      | Avenue |RailRoad|   Tax  | Avenue |  -ity  | -ainian|_____  _  |",
    "| ti| Jail | Avenue |        |      ? |        |        | 10% or |        |        | Avenue ||  _  | | |",
    "| ng|      |  $120  |  $100  |   ?    |  $100  |  $200  |  $200  |  $60   | Chest  |  $60   ||___\ |_| |",
    "————————————————————————————————————————————————————————————————————————————————————————————————————————",
]
TradeBoard = [
    #012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012
    #0         1         2         3         4         5         6         7         8         9
    "             P1N                                                              P2N            ",  #0
    "—————————————————————————————                                   —————————————————————————————",  #1
    "|       Trading Deeds:      |      ______________________       |       Trading Deeds:      |",  #2
    "|                           |      |        .---.        |      |                           |",  #3
    "|                           |      |        |#__|        |      |                           |",  #4
    "|                           |      |       =;===;=       |      |                           |",  #5
    "|                           |      |       / - - \       |      |                           |",  #6
    "|                           |      |      ( _'.'_ )      |      |                           |",  #7
    "|                           |      |     .-`-'^'-`-.     |      |                           |",  #8
    "|                           |      |    |   `>o<'   |    |      |                           |",  #9
    "|                           |      |    /     :     \    |      |                           |",  #10
    "|                           |      |   /  /\  :  /\  \   |      |                           |",  #11
    "|                           |      | .-'-/ / .-. \ \-'-. |      |                           |",  #12
    "|                           |      |  |_/ /-'   '-\ \_|  |      |                           |",  #13
    "|                           |      |     /|   |   |\     |      |                           |",  #14
    "|                           |      |    (_|  /^\  |_)    |      |                           |",  #15
    "|                           |      |      |  | |  |      |      |                           |",  #16
    "|         Trading $:        |      |      |  | |  |      |      |         Trading $:        |",  #17
    "|                           |      |____'==='= ='==='____|      |                           |",  #18
    "—————————————————————————————                                   —————————————————————————————",  #19
    #012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012
    #0         1         2         3         4         5         6         7         8         9
]
Sets = {
    "Red": ["Kentucky", "Indiana", "Illinois"],
    "Yellow": ["Atlantic", "Ventnor", "Marvin"],
    "Greem": ["Pacific", "NorthCarolina", "Pennsylvania"],
    "Blue": ["ParkPlace", "BoardWalk"],
    "Brown": ["Mediterranean", "Baltic"],
    "LightBlue": ["Oriental", "Vermont", "Conneticut"],
    "DarkRed": ["StCharles", "States", "Virginia"],
    "Orange": ["StJames", "Tennessee", "NewYork"]
}
PrintBoard = []
Positions = {
    "Go": [42, 45, 94, 103],
    "Mediterranean": [42, 45, 85, 92],
    "Community1": [42, 45, 76, 83],
    "Baltic": [42, 45, 67, 74],
    "Income": [42, 45, 58, 65],
    "Reading": [42, 45, 49, 56],
    "Oriental": [42, 45, 40, 47],
    "Chance1": [42, 45, 31, 38],
    "Vermont": [42, 45, 22, 29],
    "Conneticut": [42, 45, 13, 20],
    "VisitJail": [42, 45, 2, 4],
    "InJail": [42, 45, 6, 11],
    "Parking": [1, 4, 2, 11],
    "Kentucky": [1, 4, 13, 20],
    "Chance2": [1, 4, 22, 29],
    "Indiana": [1, 4, 31, 38],
    "Illinois": [1, 4, 40, 47],
    "H&O": [1, 4, 49, 56],
    "Atlantic": [1, 4, 58, 65],
    "Ventnor": [1, 4, 67, 74],
    "Water": [1, 4, 76, 82],
    "Marvin": [1, 4, 85, 92],
    "GoJail": [1, 4, 94, 103],
    "Pacific": [6, 8, 94, 103],
    "NorthCarolina": [10, 12, 94, 103],
    "Community3": [14, 16, 94, 103],
    "Pennsylvania": [18, 20, 94, 103],
    "ShortLine": [22, 24, 94, 103],
    "Chance3": [26, 28, 94, 103],
    "ParkPlace": [30, 32, 94, 103],
    "Luxury": [34, 36, 94, 103],
    "BoardWalk": [38, 40, 94, 103],
    "NewYork": [6, 8, 2, 11],
    "Tennessee": [10, 12, 2, 11],
    "Community2": [14, 16, 2, 11],
    "StJames": [18, 20, 2, 11],
    "PennsylvaniaRoad": [22, 24, 2, 11],
    "Virginia": [26, 28, 2, 11],
    "States": [30, 32, 2, 11],
    "Electric": [34, 36, 2, 11],
    "StCharles": [38, 40, 2, 11],
}
PositionIndex = [
    "Go", "Mediterranean", "Community1", "Baltic", "Income", "Reading",
    "Oriental", "Chance1", "Vermont", "Conneticut", "Jail", "StCharles",
    "Electric", "States", "Virginia", "PennsylvaniaRoad", "StJames",
    "Community2", "Tennessee", "NewYork", "Parking", "Kentucky", "Chance2",
    "Indiana", "Illinois", "H&O", "Atlantic", "Ventnor", "Water", "Marvin",
    "GoJail", "Pacific", "NorthCarolina", "Community3", "Pennsylvania",
    "ShortLine", "Chance3", "ParkPlace", "Luxury", "BoardWalk"
]
PositionType = [
    "Go", "Deed", "Community", "Deed", "Taxes", "RailRoad", "Deed", "Chance",
    "Deed", "Deed", "Jail", "Deed", "Utility", "Deed", "Deed", "RailRoad",
    "Deed", "Community", "Deed", "Deed", "Parking", "Deed", "Chance", "Deed",
    "Deed", "RailRoad", "Deed", "Deed", "Utility", "Deed", "Jail", "Deed",
    "Deed", "Community", "Deed", "RailRoad", "Chance", "Deed", "Taxes", "Deed"
]
#Position = [1-LineStart 2-LineEnd 3-CharacterStart 4-CharacterEnd]
ImageIndex = ["monopolyman"]
Templates = {
    "Deed": [
        "—————————————————————————————", "|        Title Deed         |",
        "|                           |", "|                           |",
        "|___________________________|", "|                           |",
        "|  Rent: $                  |", "|  1 House: $               |",
        "|  2 Houses: $              |", "|  3 Houses: $              |",
        "|  4 Houses: $              |", "|      Hotel: $             |",
        "|   Morgage Value: $        |", "|   House Price: $          |",
        "|                           |", "|   PRICE: $                |",
        "|                           |", "—————————————————————————————"
    ],
    "RailRoad": [
        "—————————————————————————————", "|                           |",
        "|                           |", "|         RailRoad          |",
        "|___________________________|", "|                           |",
        "|  Rent: $25                |", "|  2 R.R.'s: $50            |",
        "|  3 R.R.'s: $100           |", "|  4 R.R.'s: $200           |",
        "|                           |", "|   Morgage Value: $        |",
        "|   Price: $                |", "|                           |",
        "|                           |", "|                           |",
        "—————————————————————————————"
    ],
    "Utility": [
        "—————————————————————————————", "|                           |",
        "|                           |", "|                           |",
        "|___________________________|", "|                           |",
        "|  If 1 Utility is owned    |", "|  rent is 4 times amount   |",
        "|  shown on dice.           |", "|                           |",
        "|  If both Utilities are    |", "|  owned rent is 10 times   |",
        "|  amount on dice.          |", "|                           |",
        "|   Morgage Value: $75      |", "|   PRICE: $150             |",
        "|                           |", "—————————————————————————————"
    ],
    "Taxes": [
        "—————————————————————————————", "|                           |",
        "|                           |", "|            Tax            |",
        "|___________________________|", "|                           |",
        "|   _________               |", "|  /_|_____|_\              |",
        "|  '. \   / .'              |", "|    '.\ /.'                |",
        "|      '.'                  |", "|                           |",
        "|                           |", "|                           |",
        "|                           |", "|                           |",
        "|                           |", "—————————————————————————————"
    ],
    "Chance": [
        "———————————————————————————————————————————————————",
        "|                   Chance                        |",
        "|                                      #######    |",
        "|                                     ##     ##   |",
        "|                                           ##    |",
        "|                                         ###     |",
        "|                                        ##       |",
        "|                                        ##       |",
        "|                                                 |",
        "|                                        ##       |",
        "|                                                 |",
        "———————————————————————————————————————————————————"
    ],
    "Community": [
        "———————————————————————————————————————————————————",
        "|          Community Chest                        |",
        "|                                    __________   |",
        "|                                   /\____;;___\  |",
        "|                                  | /         /  |",
        "|                                  `. ())oo() .   |",
        "|                                   |\(%()*^^()^\ |",
        "|                                   | |-%-------| |",
        "|                                   \ | %  ))   | |",
        "|                                    \|%________| |",
        "|                                                 |",
        "———————————————————————————————————————————————————"
    ],
}
Dice = [[
    "——————————————", "|            |", "|            |", "|     []     |",
    "|            |", "|            |", "——————————————"
],
        [
            "——————————————", "|  []        |", "|            |",
            "|            |", "|            |", "|        []  |",
            "——————————————"
        ],
        [
            "——————————————", "|  []        |", "|            |",
            "|     []     |", "|            |", "|        []  |",
            "——————————————"
        ],
        [
            "——————————————", "|  []    []  |", "|            |",
            "|            |", "|            |", "|  []    []  |",
            "——————————————"
        ],
        [
            "——————————————", "|  []    []  |", "|            |",
            "|     []     |", "|            |", "|  []    []  |",
            "——————————————"
        ],
        [
            "——————————————", "|  []    []  |", "|            |",
            "|  []    []  |", "|            |", "|  []    []  |",
            "——————————————"
        ]]
Cards = {
    "Deed": {
        "Mediterranean": {
            "Name": "Mediterranean Avenue",
            "Price": 60,
            "Rent": 2,
            "1House": 10,
            "2House": 30,
            "3House": 90,
            "4House": 160,
            "Hotel": 250,
            "Morgage": 30,
            "HouseCost": 50
        },
        "Baltic": {
            "Name": "Baltic Avenue",
            "Price": 60,
            "Rent": 4,
            "1House": 20,
            "2House": 60,
            "3House": 180,
            "4House": 320,
            "Hotel": 450,
            "Morgage": 30,
            "HouseCost": 50
        },
        "Oriental": {
            "Name": "Oriental Avenue",
            "Price": 100,
            "Rent": 6,
            "1House": 30,
            "2House": 90,
            "3House": 270,
            "4House": 400,
            "Hotel": 550,
            "Morgage": 50,
            "HouseCost": 50
        },
        "Vermont": {
            "Name": "Vermont Avenue",
            "Price": 100,
            "Rent": 6,
            "1House": 30,
            "2House": 90,
            "3House": 270,
            "4House": 400,
            "Hotel": 550,
            "Morgage": 50,
            "HouseCost": 50
        },
        "Conneticut": {
            "Name": "Conneticut Avenue",
            "Price": 120,
            "Rent": 8,
            "1House": 40,
            "2House": 100,
            "3House": 300,
            "4House": 450,
            "Hotel": 600,
            "Morgage": 60,
            "HouseCost": 50
        },
        "StCharles": {
            "Name": "St.Charles Place",
            "Price": 140,
            "Rent": 10,
            "1House": 50,
            "2House": 150,
            "3House": 450,
            "4House": 625,
            "Hotel": 750,
            "Morgage": 70,
            "HouseCost": 100
        },
        "States": {
            "Name": "States Avenue",
            "Price": 140,
            "Rent": 10,
            "1House": 50,
            "2House": 150,
            "3House": 450,
            "4House": 625,
            "Hotel": 750,
            "Morgage": 70,
            "HouseCost": 100
        },
        "Virginia": {
            "Name": "Virginia Avenue",
            "Price": 160,
            "Rent": 12,
            "1House": 60,
            "2House": 180,
            "3House": 500,
            "4House": 700,
            "Hotel": 900,
            "Morgage": 80,
            "HouseCost": 100
        },
        "Pennsylvania": {
            "Name": "Pennsylvania Avenue",
            "Price": 320,
            "Rent": 28,
            "1House": 150,
            "2House": 450,
            "3House": 1000,
            "4House": 1200,
            "Hotel": 1400,
            "Morgage": 160,
            "HouseCost": 200
        },
        "StJames": {
            "Name": "St.James Place",
            "Price": 180,
            "Rent": 14,
            "1House": 70,
            "2House": 200,
            "3House": 550,
            "4House": 750,
            "Hotel": 950,
            "Morgage": 90,
            "HouseCost": 100
        },
        "Tennessee": {
            "Name": "Tennessee Avenue",
            "Price": 180,
            "Rent": 14,
            "1House": 70,
            "2House": 200,
            "3House": 550,
            "4House": 750,
            "Hotel": 950,
            "Morgage": 90,
            "HouseCost": 100
        },
        "NewYork": {
            "Name": "New York Avenue",
            "Price": 200,
            "Rent": 16,
            "1House": 80,
            "2House": 220,
            "3House": 600,
            "4House": 800,
            "Hotel": 1000,
            "Morgage": 100,
            "HouseCost": 100
        },
        "Kentucky": {
            "Name": "Kentucky Avenue",
            "Price": 220,
            "Rent": 18,
            "1House": 90,
            "2House": 250,
            "3House": 700,
            "4House": 875,
            "Hotel": 1050,
            "Morgage": 110,
            "HouseCost": 150
        },
        "Indiana": {
            "Name": "Indiana Avenue",
            "Price": 220,
            "Rent": 18,
            "1House": 90,
            "2House": 250,
            "3House": 700,
            "4House": 875,
            "Hotel": 1050,
            "Morgage": 110,
            "HouseCost": 150
        },
        "Illinois": {
            "Name": "Illinois Avenue",
            "Price": 240,
            "Rent": 20,
            "1House": 100,
            "2House": 300,
            "3House": 750,
            "4House": 925,
            "Hotel": 1100,
            "Morgage": 120,
            "HouseCost": 150
        },
        "Atlantic": {
            "Name": "Atlantic Avenue",
            "Price": 260,
            "Rent": 22,
            "1House": 110,
            "2House": 330,
            "3House": 800,
            "4House": 975,
            "Hotel": 1150,
            "Morgage": 130,
            "HouseCost": 150
        },
        "Ventnor": {
            "Name": "Ventnor Avenue",
            "Price": 260,
            "Rent": 22,
            "1House": 110,
            "2House": 330,
            "3House": 800,
            "4House": 975,
            "Hotel": 1150,
            "Morgage": 130,
            "HouseCost": 150
        },
        "Marvin": {
            "Name": "Marvin Gardens",
            "Price": 280,
            "Rent": 24,
            "1House": 120,
            "2House": 360,
            "3House": 850,
            "4House": 1025,
            "Hotel": 1200,
            "Morgage": 140,
            "HouseCost": 150
        },
        "Pacific": {
            "Name": "Pacific Avenue",
            "Price": 300,
            "Rent": 26,
            "1House": 130,
            "2House": 390,
            "3House": 900,
            "4House": 1100,
            "Hotel": 1275,
            "Morgage": 150,
            "HouseCost": 200
        },
        "NorthCarolina": {
            "Name": "North Carolina Avenue",
            "Price": 300,
            "Rent": 26,
            "1House": 130,
            "2House": 390,
            "3House": 900,
            "4House": 1100,
            "Hotel": 1275,
            "Morgage": 150,
            "HouseCost": 200
        },
        "ParkPlace": {
            "Name": "Park Place",
            "Price": 350,
            "Rent": 35,
            "1House": 175,
            "2House": 500,
            "3House": 1100,
            "4House": 1300,
            "Hotel": 1500,
            "Morgage": 175,
            "HouseCost": 200
        },
        "BoardWalk": {
            "Name": "BoardWalk",
            "Price": 400,
            "Rent": 50,
            "1House": 200,
            "2House": 600,
            "3House": 1400,
            "4House": 1700,
            "Hotel": 2000,
            "Morgage": 200,
            "HouseCost": 100
        },
    },
    "RailRoad": {
        "H&O": {
            "Title": "H&O",
            "Morgage": 100,
            "Price": 200
        },
        "ShortLine": {
            "Title": "Short Line",
            "Morgage": 100,
            "Price": 200
        },
        "Reading": {
            "Title": "Reading",
            "Morgage": 100,
            "Price": 200
        },
        "PennsylvaniaRoad": {
            "Title": "Pennsylvania",
            "Morgage": 100,
            "Price": 200
        },
    },
    "Utility": {
        "Electric": {
            "Title1": "Electric",
            "Title2": "Company",
            "Price": 150,
            "Morgage": 75
        },
        "Water": {
            "Title1": "Water",
            "Title2": "Works",
            "Price": 150,
            "Morgage": 75
        },
    },
    "Taxes": {
        "Income": {
            "Title": "Income",
            "Text1": "Pay 10%",
            "Text2": "OR",
            "Text3": "$200"
        },
        "Luxury": {
            "Title": "Luxury",
            "Text1": "Pay",
            "Text2": "$75",
            "Text3": ""
        }
    },
    "Chance": [
        ["Position", "Go", "Advance to", "Go!"],
        ["Position", "Illinois", "Advance to", "Illinois Avenue!"],
        ["Position", "StCharles", "Advance to", "St. Charles Place!"],
        ["Nearest", "Utility", "Advance to", "Nearest Utility!"],
        ["Nearest", "RailRoad", "Advance to", "Nearest Railroad!"],
        ["Distance", -3, "Go Back", "3 Spaces!"],
        ["Card", "JailFree", "Get out of", "Jail Free Card!"],
        ["Position", "Jail", "Go Directly", "to Jail"],
        [
            "GeneralRepair", [25, 100], "General Repairs",
            "$25 a House, $100 a Hotel"
        ],
        ["Tax", 15, "Pay poor tax", "of $15"],
        ["Position", "Reading", "Take a trip to", "Reading Railroad!"],
        ["Position", "BoardWalk", "Take a trip to", "Boardwalk!"],
        [
            "EachPlayerG", 50, "Elected Chairman of the Board.",
            "Give $50 a Player"
        ],
        ["Recieve", 150, "Building loan matures.", "Collect $150"],
    ],
    "Community": [
        ["Position", "Go", "Advance to", "Go!"],
        ["Recieve", 200, "Bank Error in your favor!", "Collect $200"],
        ["Tax", 50, "Doctor's Fees,", "Pay $50"],
        ["Recieve", 50, "From sale of stock", "you get $50!"],
        ["Card", "JailFree", "Get out of Jail", "Free Card!"],
        ["Position", "Jail", "Go Directly", "to Jail"],
        ["EachPlayerR", 50, "Grand Opera Night!", "Collect $50 a Player"],
        ["Recieve", 100, "Holiday Funds matures!", "Collect $100"],
        ["Recieve", 20, "Income tax refund!", "Collect $20"],
        ["EachPlayerR", 10, "Your Birthday!", "Collect $10 a Player"],
        ["Recieve", 100, "Life Insurance matures!", "Collect $100"],
        ["Tax", 50, "Hospital Fees,", "Pay $50"],
        ["Tax", 50, "School Fees,", "Pay $50"],
        ["Recieve", 25, "Consultanty fee!", "Collect $25"],
        [
            "StreetRepair", [40, 115], "Road Repairs $40 a House,",
            "$115 a Hotel"
        ],
        ["Recieve", 100, "You collect your inheritance!", "Collect $100"],
        ["Recieve", 10, "2nd Place in Beauty Contest!", "Collect $10"],
    ],
}
Replacement = {
    "Deed": {
        "Name": 3,
        "Price": 15,
        "Rent": 6,
        "1House": 7,
        "2House": 8,
        "3House": 9,
        "4House": 10,
        "Hotel": 11,
        "Morgage": 12,
        "HouseCost": 13,
    },
    "RailRoad": {
        "Title": 2,
        "Morgage": 11,
        "Price": 12
    },
    "Utility": {
        "Title1": 2,
        "Title2": 3,
        "Morgage": 14,
        "Price": 15
    },
    "Taxes": {
        "Title": 3,
        "Text1": 12,
        "Text2": 13,
        "Text3": 14
    },
    "TradeBoard": {
        "P1N": [0, 0, 9, 19, 0],
        "P2N": [0, 0, 74, 84, 1],
        "P1B": [18, 18, 1, 27],
        "P2B": [18, 18, 65, 91],
        "P1D": [3, 12, 1, 27],
        "P2D": [3, 12, 65, 91],
    },
    "Chance": {},
    "Community": {},
    "Jail": {
        "Title": 1
    },
    "Go": {}
}
PlayerTemplate = {
    "Name": "NoOne",
    "Position": "Go",
    "Roll": 0,
    "Order": 0,
    "Letter": "Car",
    "Money": 1500,
    "InJail": False,
    "Deeds": [],
    "Cards": [],
    "Houses": {},
    "CompletedSets": [],
    "Go": True,
    "DoublesCount": 0,
    "Playing": True,
    "SaveGame": False
}
AvailibleDeeds = [
    "Mediterranean", "Baltic", "Reading", "Oriental", "Vermont", "Conneticut",
    "Kentucky", "Indiana", "Illinois", "H&O", "Atlantic", "Ventnor", "Water",
    "Marvin", "Pacific", "NorthCarolina", "Pennsylvania", "ShortLine",
    "ParkPlace", "BoardWalk", "NewYork", "Tennessee", "StJames",
    "PennsylvaniaRoad", "Virginia", "States", "Electric", "StCharles"
]
MorgagedDeeds = []
TakenLetters = []
TakenNames = []
Players = {}
NumberOfPlayers = 0
Ended = False


def MonopolyMan():
    MonopolyMan = images[0]
    for string in MonopolyMan:
        print(string)


def CenterText(Text, TextToCenter):
    remainder = (len(Text) - len(TextToCenter)) % 2
    sidelength = int((len(Text) - len(TextToCenter)) / 2)
  
    if not remainder == 0:
        sidelength = int((len(Text) - len(TextToCenter)) / 2 - 0.5)
    
    side1 = Text[0:sidelength]
    side2 = Text[sidelength + len(TextToCenter):]
    return side1 + TextToCenter + side2


def ReplaceText(Text, TextToReplace, ReplaceWith):
    position = Text.find(TextToReplace)
    leftIndex = int(position - len(ReplaceWith) / 2)
    rightIndex = int(position + len(TextToReplace) - 1 + len(ReplaceWith) / 2)
  
    if (len(ReplaceWith) % 2) == 0:
        leftIndex = position - leftIndex + 1
      
    LeftHalf = Text[:leftIndex]
    RightHalf = Text[rightIndex:]
    return LeftHalf + ReplaceWith + RightHalf


def fillprice(Text, TextToFill):
    position = Text.find("$") + 1
    return Text[:position] + str(TextToFill) + Text[position + len(str(TextToFill)):]


def CreateCard(CardName, CardType):
    CardTable = Cards[CardType][CardName]
    DeedTable = [] + Templates[CardType]
    for ValueIndex, Value in CardTable.items():
        Position = Replacement[CardType][ValueIndex]
        if type(Value) == int:
            DeedTable[Position] = fillprice(DeedTable[Position], Value)
        else:
            DeedTable[Position] = CenterText(DeedTable[Position], Value)
    return DeedTable


def GetPlayers():
    global NumberOfPlayers
    global Players
    print("Lets Meet our Players!")
    time.sleep(1)
    print("Each Player will Have a Letter Representing them on the Board!")
    NumberOfPlayers = input("How many Players? (1-4) ")
    if not NumberOfPlayers.isdigit():
        print("Thats not a Number between 1 and 4!")
        time.sleep(1)
        print("Try Again!")
        time.sleep(1)
        clear()
        MonopolyMan()
        GetPlayers()
    elif NumberOfPlayers.isdigit(
    ) and int(NumberOfPlayers) > 4 or NumberOfPlayers.isdigit(
    ) and int(NumberOfPlayers) < 1:
        print("Thats not a Number between 1 and 4!")
        time.sleep(1)
        print("Try Again!")
        time.sleep(1)
        clear()
        MonopolyMan()
        GetPlayers()
    time.sleep(1)
    for x in range(0, int(NumberOfPlayers)):

        def AddPlayer():
            clear()
            MonopolyMan()
            print("Lets Meet our Players!")
            print(
                "Each Player will Have a Letter Representing them on the Board!"
            )
            PlayerName = input("Name of Player " + str(x + 1) +
                               ": ").lower().capitalize()
            PlayerName = PlayerName.replace(" ", "")
            if PlayerName in TakenNames:
                print("That name is already Taken, try again!")
                time.sleep(1)
                AddPlayer()
            PlayerLetter = input(PlayerName + "'s Letter: ").upper()
            if PlayerLetter in TakenLetters and len(PlayerLetter) == 1:
                print("That Letter is already Taken, try again!")
                time.sleep(1)
                AddPlayer()
            elif not len(PlayerLetter) == 1:
                print("Thats not a single letter!")
                time.sleep(1)
                AddPlayer()
            PlayerTable = PlayerTemplate.copy()
            PlayerTable["Name"] = PlayerName
            PlayerTable["Letter"] = PlayerLetter
            TakenLetters.insert(0, PlayerLetter)
            TakenNames.insert(0, PlayerName)
            Players[PlayerName] = PlayerTable

        AddPlayer()


def ResetBoard():
    global PrintBoard
    PrintBoard = [] + Board


def SeeBoard():
    clear()
    for string in PrintBoard:
        print(string)


def UpdateBoard():
    global PrintBoard
    global Players
    global Locations
    Locations = []
    ResetBoard()
    for Place in PositionIndex:
        Locations.insert(PositionIndex.index(Place), [])
    for Key, Player in Players.items():
        Locations[PositionIndex.index(Player["Position"])].insert(
            0, Player["Letter"])
    for Letters in Locations:
        for doesntmatter in Letters:

            def LoopBoard(Position):
                PosValues = Positions[Position]
                LetterString = ""
                for Letter in Letters:
                    LetterString = LetterString + Letter
                for x in range(PosValues[0], PosValues[1] + 1):
                    GetFrom = "" + PrintBoard[x]
                    LeftHalf = GetFrom[:PosValues[2] - 1]
                    RightHalf = GetFrom[PosValues[3]:]
                    NewSection = "".ljust(PosValues[3] - PosValues[2] + 1)
                    if x == PosValues[0] + 1:
                        NewSection = CenterText(NewSection, LetterString)
                    PrintBoard[x] = LeftHalf + NewSection + RightHalf

            Position = PositionIndex[Locations.index(Letters)]
            if Position == "Jail":
                VisitJail = ""
                InJail = ""
                for Letter in Letters:
                    for name, t in Players.items():
                        if t["Letter"] == Letter:
                            if t["InJail"] == False:
                                VisitJail = VisitJail + Letter
                            else:
                                InJail = InJail + Letter
                if not InJail == "":
                    LoopBoard("InJail")
                if not VisitJail == "":
                    LoopBoard("VisitJail")
            else:
                LoopBoard(Position)


def MoveLetter(PlayerName, Distance):
    global Players
    Player = Players[PlayerName]
    Pos = Player["Position"]
    PosIndex = PositionIndex.index(Pos)
    NewPosIndex = PosIndex + Distance + 1
    for x in range(PosIndex, NewPosIndex):
        if x > 39:
            x = x - 40
        Player["Position"] = PositionIndex[x]
        UpdateBoard()
        SeeBoard()
        if Player["Position"] == "Go" and Player["Go"] == False:
            print("You just passed Go!")
            time.sleep(1)
            print("You Collect $200!")
            Player["Money"] = Player["Money"] + 200
            time.sleep(1)
            Balance(Player["Name"])
            time.sleep(2)
            Player["Go"] == True
        elif Player["Position"] == "Mediterranean" and Player["Go"] == True:
            Player["Go"] = False
        time.sleep(0.5)


def Move(PlayerName):
    global Players
    Player = Players[PlayerName]
    clear()
    MonopolyMan()
    print(PlayerName + "'s Turn!")
    print(PlayerName + " Roll the Dice!")
    input("Press Enter to Roll!")
    Results = Roll(PlayerName)
    Distance = Results[0]
    Player["Roll"] = Results[0]
    Double = Results[1]
    if Double == True:
        Player["DoublesCount"] = Player["DoublesCount"] + 1
        time.sleep(1)
        print(PlayerName + " Rolled Doubles!")
        time.sleep(1)
        print("That means they will go twice!")
        time.sleep(1)
        if Player["InJail"] == True:
            time.sleep(1)
            print("You are out of Jail!")
            Player["InJail"] = False
            time.sleep(1)
    else:
        Player["DoublesCount"] = 0
        time.sleep(1)
    if Player["InJail"] == False:
        if Player["DoublesCount"] == 3:
            print("Uh Oh!")
            time.sleep(1)
            print("You rolled doubles 3 times!")
            time.sleep(1)
            print("You have to go to Jail!")
            Player["Position"] = "Jail"
            Player["InJail"] = True
            UpdateBoard()
            SeeBoard()
        else:
            MoveLetter(PlayerName, Distance)
            input("Press Enter to Continue....")
            Land(PlayerName)
            input("Press Enter to Continue....")
    else:
        print("You are in Jail!")
        time.sleep(1)
        print("To get out you need to Roll doubles or pay $50!")
        time.sleep(1)
    if Double == True and Player["InJail"] == False:
        Move(Player["Name"])


def Morgage(PlayerName):
    clear()
    MonopolyMan()
    global Players
    Player = Players[PlayerName]
    Deeds = [] + list(Player["Deeds"])
    Balance(Player["Name"])
    print("Here is a list of your owned Deeds!")
    for Deed in Deeds:

        def PrintMorgageDeed(Name, DeedM):
            if Deed in MorgagedDeeds:
                print(
                    str(Deeds.index(Deed)) + ". " + Name + " - Morgaged - $" +
                    str(DeedM))
            else:
                print(
                    str(Deeds.index(Deed)) + ". " + Name +
                    " - Not Morgaged - $" + str(DeedM))

        DeedType = PositionType[PositionIndex.index(Deed)]
        DeedT = Cards[DeedType][Deed]
        Name = ""
        DeedM = DeedT["Morgage"]
        if DeedType == "Deed":
            Name = "" + DeedT["Name"]
        elif DeedType == "RailRoad":
            Name = "" + DeedT["Title"] + " RailRoad"
        elif DeedType == "Utility":
            Name = "" + DeedT["Title1"] + "" + DeedT["Title2"]
        PrintMorgageDeed(Name, DeedM)
    ToDo = input(
        "Would you like to Morgage (1), UnMorgage(2), or do Nothing (3)? ")
    if ToDo == "1":
        ToMorgage = input(
            "Which Deed would you like to Morgage? (Type the Number) ")
        if ToMorgage.isdigit() and len(Deeds) - 1 >= int(
                ToMorgage) and not Deeds[int(ToMorgage)] in MorgagedDeeds:
            ToMorgage = Deeds[int(ToMorgage)]
            print("Okay Morgaging " + ToMorgage + "!")
            MorgagedDeeds.insert(0, ToMorgage)
            Player["Money"] = Player["Money"] + Cards[PositionType[
                PositionIndex.index(ToMorgage)]][ToMorgage]["Morgage"]
            time.sleep(1)
            Morgage(Player["Name"])
        else:
            print("You don't own that deed! Did you type the right number?")
            time.sleep(1)
            Morgage(Player["Name"])
    elif ToDo == "2":
        ToUnMorgage = input(
            "Which Deed would you like to UnMorgage? (Type the Number) ")
        if ToUnMorgage.isdigit() and len(Deeds) - 1 >= int(
                ToUnMorgage) and Deeds[int(ToUnMorgage)] in MorgagedDeeds:
            ToUnMorgage = Deeds[int(ToUnMorgage)]
            print("Okay UnMorgaging " + ToUnMorgage + "!")
            MorgagedDeeds.remove(ToUnMorgage)
            Player["Money"] = Player["Money"] - Cards[PositionType[
                PositionIndex.index(ToUnMorgage)]][ToUnMorgage]["Morgage"]
            time.sleep(1)
            Morgage(Player["Name"])
        else:
            print("You don't own that deed! Did you type the right number?")
            time.sleep(1)
            Morgage(Player["Name"])
    elif ToDo == "3":
        print("Alright!")
    else:
        print("Looks like you didn't type a Valid Option!")
        time.sleep(1)
        print("Pick Either 1, 2, or 3!")
        time.sleep(1)
        Morgage(Player["Name"])


def CalculateRent(OwnerName, PlayerName):
    global Players
    Player = Players[PlayerName]
    Deed = "" + Player["Position"]
    DeedIndex = PositionIndex.index(Deed)
    DeedType = PositionType[DeedIndex]
    DeedTable = Cards[DeedType][Deed]
    if DeedType == "Deed":
        Owner = Players[OwnerName]
        Houses = Owner["Houses"][Deed]
        if not Houses == 0:
            if Houses < 5:
                Rent = DeedTable[str(Houses) + "House"]
                return Rent
            else:
                return DeedTable["Hotel"]
        else:
            Rent = DeedTable["Rent"]
            return Rent
    elif DeedType == "RailRoad":
        Owner = Players[OwnerName]
        Rent = 25
        for RoadName, Table in Cards[DeedType].items():
            if not RoadName == Deed and RoadName in Owner["Deeds"]:
                Rent = Rent * 2
        return Rent
    elif DeedType == "Utility":
        Owner = Players[OwnerName]
        global Multiplier
        Multiplier = 4
        for UtilityName, Table in Cards[DeedType].items():
            if not UtilityName == Deed and UtilityName in Owner["Deeds"]:
                Multiplier = 10
        return Player["Roll"] * Multiplier


def CardSpots(PlayerName):
    global Players
    Player = Players[PlayerName]
    Pos = Player["Position"]
    PosIndex = PositionIndex.index(Pos)
    PosType = PositionType[PosIndex]
    ThingsToDo = Cards[PosType]
    RandomCard = ThingsToDo[randint(0, len(ThingsToDo) - 1)]
    ActionType = RandomCard[0]
    ActionVariable = RandomCard[1]
    ActionMessage = RandomCard[2]
    ActionMessage2 = RandomCard[3]
    PrintCard = [] + Templates[PosType]
    ChangeString = "" + PrintCard[5]
    LeftHalf = "|"
    RightHalf = ChangeString[33:]
    Middle = CenterText(ChangeString[1:33], ActionMessage)
    PrintCard[5] = LeftHalf + Middle + RightHalf
    ChangeString = "" + PrintCard[6]
    Right2 = ChangeString[33:]
    Middle2 = CenterText(ChangeString[1:33], ActionMessage2)
    PrintCard[6] = LeftHalf + Middle2 + Right2
    print("You picked:")
    for string in PrintCard:
        print(string)
    input("Press Enter to do what the Card says!")
    if ActionType == "Position":
        print("Advance to " + ActionVariable)
        if ActionVariable == "Go":
            CurrentPosIndex = PositionIndex.index(Player["Position"])
            MoveLetter(Player["Name"], 40 - CurrentPosIndex)
            Land(Player["Name"])
        elif ActionVariable == "Jail":
            Player["InJail"] = True
            Player["Position"] = "Jail"
            UpdateBoard()
            SeeBoard()
            print(
                "You are in Jail! You need to Roll Doubles or Pay $50 to get out!"
            )
            time.sleep(3)
        else:
            NewPosIndex = PositionIndex.index(ActionVariable)
            CurrentPosIndex = PositionIndex.index(Player["Position"])
            if NewPosIndex > CurrentPosIndex:
                Distance = NewPosIndex - CurrentPosIndex
                MoveLetter(Player["Name"], Distance)
                Land(Player["Name"])
            else:
                FirstMove = 40 - CurrentPosIndex
                MoveLetter(Player["Name"], FirstMove)
                MoveLetter(Player["Name"], NewPosIndex)
                Land(Player["Name"])
    elif ActionType == "Recieve":
        print("Collected $" + str(ActionVariable) + "!")
        time.sleep(1)
        Player["Money"] = Player["Money"] + ActionVariable
        Balance(Player["Name"])
        time.sleep(1)
    elif ActionType == "Tax":
        if Player["Money"] >= ActionVariable:
            print("Payed $" + str(ActionVariable) + "!")
            time.sleep(1)
            Player["Money"] = Player["Money"] - ActionVariable
            Balance(Player["Name"])
            time.sleep(1)
        else:
            print("You don't have enough Money!")
            time.sleep(1)
            print("You need to morgage!")
            time.sleep(1)
            Morgage(Player["Name"])
    elif ActionType == "Distance":
        print("Move backwards 3 spaces!")
        time.sleep(1)
        PosIndex = PositionIndex.index(Player["Position"])
        Player["Position"] = PositionIndex[PosIndex - 1]
        UpdateBoard()
        SeeBoard()
        time.sleep(0.5)
        Player["Position"] = PositionIndex[PosIndex - 2]
        UpdateBoard()
        SeeBoard()
        time.sleep(0.5)
        Player["Position"] = PositionIndex[PosIndex - 3]
        UpdateBoard()
        SeeBoard()
        time.sleep(0.5)
        Land(Player["Name"])
    elif ActionType == "Nearest":
        Pos = Player["Position"]
        NearType = ActionVariable
        StartIndex = PositionIndex.index(Pos)
        NewIndex = 0 + StartIndex
        Nearest = ""
        while not Nearest == NearType:
            NewIndex = NewIndex + 1
            if NewIndex > 39:
                NewIndex = 40 - NewIndex
            Nearest = "" + PositionType[NewIndex]
        if NewIndex > StartIndex:
            Distance = NewIndex - StartIndex
            MoveLetter(Player["Name"], Distance)
            Land(Player["Name"])
        else:
            FirstMove = 40 - StartIndex
            MoveLetter(Player["Name"], FirstMove)
            MoveLetter(Player["Name"], NewIndex)
            Land(Player["Name"])
    elif ActionType == "EachPlayerG":
        print("Payed Each Player $" + str(ActionVariable) + "!")
        time.sleep(1)
        Player["Money"] = Player["Money"] - ActionVariable * (NumberOfPlayers -
                                                              1)
        for PlayerName, Table in Players.items():
            if not PlayerName == Player["Name"]:
                Table["Money"] = Table["Money"] + ActionVariable
        Balance(Player["Name"])
        time.sleep(1)
    elif ActionType == "EachPlayerR":
        print("Gain $" + str(ActionVariable) + " from each Player!")
        time.sleep(1)
        Player["Money"] = Player["Money"] + ActionVariable * (
            int(NumberOfPlayers) - 1)
        for PlayerName, Table in Players.items():
            if not PlayerName == Player["Name"]:
                Table["Money"] = Table["Money"] - ActionVariable
        Balance(Player["Name"])
        time.sleep(1)
    elif ActionType == "Card":
        if ActionVariable == "JailFree":
            print("You have got a get out of Jail Free Card!")
            time.sleep(1)
            Player["Cards"].insert(0, "JailFree")


def Balance(PlayerName):
    global Players
    Players[PlayerName]["Money"] = int(Players[PlayerName]["Money"])
    print(PlayerName + "'s Balance: $" + str(Players[PlayerName]["Money"]))


def AuctionDeed(DeedName):
    clear()
    MonopolyMan()
    print("Welcome Players to the Auction!")
    time.sleep(1)
    AuctionFinished = False
    if not AuctionFinished == False:
        DeedIndex = PositionIndex.index(DeedName)
        DeedType = PositionType[DeedIndex]
        DeedTable = Cards[DeedType][DeedName]
        Card = CreateCard(DeedName, DeedType)

        def SeeCard():
            for string in Card:
                print(string)

        print("Here everybody has a Chance to buy the deed " +
              DeedTable["Name"] + "!")
        SeeCard()
        time.sleep(1)
        print("Lets Get to Bidding!")
        time.sleep(1)
        clear()
        SeeCard()
        print("The bid starts at $10")
        TopBid = 10
        TopBidder = "NoOne"
        AuctionEnded = False

        def Bid():
            clear()
            SeeCard()
            print("Top Bid: " + str(TopBid))
            print("TopBidder: " + TopBidder)
            print("Who would like to Bid?")
            Bidder = input("Player Letter: ").upper()
            FoundBidder = False
            for name, table in Players.items():
                if table["Letter"] == Bidder:
                    FoundBidder = name
            if not FoundBidder == False:
                Bidder = Players[FoundBidder]
                print("Bid")
            else:
                print("Not a valid Player Letter!")
                time.sleep()
                Bid()

        while AuctionEnded == False:
            Bid()
    else:
        print("Auctioning isnt Finished yet!")
        time.sleep(1)
        input("Press Enter to Continue...")


def Land(PlayerName):
    clear()
    MonopolyMan()
    global Players
    Player = Players[PlayerName]
    Pos = Player["Position"]
    PosIndex = PositionIndex.index(Pos)
    PosType = PositionType[PosIndex]
    if PosType == "Deed" or PosType == "RailRoad" or PosType == "Utility":
        CardName = ""
        if PosType == "Deed":
            CardName = Cards[PosType][Pos]["Name"]
            print("You landed on " + Cards[PosType][Pos]["Name"] + "!")
        elif PosType == "RailRoad":
            CardName = Cards[PosType][Pos]["Title"] + " RailRoad"
            print("You landed on " + Cards[PosType][Pos]["Title"] +
                  " RailRoad!")
        elif PosType == "Utility":
            CardName = Cards[PosType][Pos]["Title1"] + " " + Cards[PosType][
                Pos]["Title2"]
            print("You landed on " + Cards[PosType][Pos]["Title1"] + " " +
                  Cards[PosType][Pos]["Title2"] + "!")
        Card = CreateCard(Pos, PosType)
        for string in Card:
            print(string)
        if Pos in MorgagedDeeds:
            print("This spot is Morgaged so you don't Need to do anything!")
            time.sleep(1)
        elif not Pos in MorgagedDeeds:
            if Pos in AvailibleDeeds:
                print("This Deed is Availible!")
                time.sleep(1)
                Balance(Player["Name"])
                Purchase = input(
                    "Would you like to purchase it?! (yes/no) ").upper()
                if Purchase == "Y" or Purchase == "YES":
                    Money = Player["Money"]
                    CardTable = Cards[PosType][Pos]
                    Price = CardTable["Price"]
                    if Money >= Price:
                        print("You have bought " + CardName + "!")
                        Player["Money"] = Player["Money"] - Price
                        time.sleep(1)
                        Balance(Player["Name"])
                        Deeds = [] + Player["Deeds"]
                        Deeds.insert(0, Pos)
                        Player["Deeds"] = Deeds
                        Player["Houses"][Pos] = 0
                        AvailibleDeeds.remove(Pos)
                        time.sleep(1)
                        for Color, TitleDeeds in Sets.items():
                            if Pos in TitleDeeds:
                                owned = 0
                                total = len(TitleDeeds)
                                for Deed in TitleDeeds:
                                    if Deed in Player["Deeds"]:
                                        owned = owned + 1
                                if owned == total:
                                    Player["CompletedSets"].insert(0, Color)
                                    print("You have the Entire " + Color +
                                          " Set!")
                                    time.sleep(2)
                    else:
                        print("You don't have enough Money!")
                        Balance(Player["Name"])
                        time.sleep(1)
                        WillMorgage = input(
                            "Would you like to Morgage? (yes/no) ").upper()
                        if WillMorgage == "YES" or WillMorgage == "Y":
                            Morgage(Player["Name"])
                            if Player["Money"] > Price:
                                print("After Morgaging you have enough Money!")
                                print("You have bought " + Pos + "!")
                                Player["Money"] = Player["Money"] - Price
                                time.sleep(1)
                                Balance(Player["Name"])
                                Deeds = [] + Player["Deeds"]
                                Deeds.insert(0, Pos)
                                Player["Deeds"] = Deeds
                                Player["Houses"][Pos] = [0]
                                AvailibleDeeds.remove(Pos)
                                time.sleep(1)
                                for Color, TitleDeeds in Sets.items():
                                    if Pos in TitleDeeds:
                                        owned = 0
                                        total = len(TitleDeeds)
                                        for Deed in TitleDeeds:
                                            if Deed in Player["Deeds"]:
                                                owned = owned + 1
                                        if owned == total:
                                            Player["CompletedSets"].insert(
                                                Color)
                                            print("You have the Entire " +
                                                  Color + " Set!")
                                            time.sleep(2)
                            else:
                                print(
                                    "Even after Morgaging you still don't have enough money!"
                                )
                                time.sleep(1)
                                print("Lets Auction It!")
                                time.sleep(1)
                                AuctionDeed(Pos)
                        else:
                            print("Lets Auction It!")
                            time.sleep(1)
                            AuctionDeed(Pos)
                else:
                    print("Lets Auction It!")
                    time.sleep(1)
                    AuctionDeed(Pos)
            elif Pos in Player["Deeds"]:
                print("You own this already, so you can just relax!")
                time.sleep(1)
            else:
                Owner = ""
                for Name, Table in Players.items():
                    if Pos in Table["Deeds"]:
                        Owner = Table["Name"]
                print(Owner + " Owns this deed already, you have to pay rent!")
                time.sleep(1)
                Rent = CalculateRent(Owner, Player["Name"])
                print("The Rent is $" + str(Rent))
                input("Press Enter to Pay")
                if Player["Money"] > Rent:
                    Players[Owner]["Money"] = Players[Owner]["Money"] + Rent
                    Player["Money"] = Player["Money"] - Rent
                    Balance(Player["Name"])
                    Balance(Owner)
                else:

                    def SellLoop():
                        clear()
                        MonopolyMan()
                        print("You don't have enough Money!")
                        time.sleep(1)
                        print("Looks like you need to Morgage or Sell Houses!")
                        time.sleep(1)
                        print(
                            "Would you like to Morgage (1) or Sell Houses (2) "
                        )
                        Option = input("Option (1/2): ")
                        if Option == "1":
                            Morgage(Player["Name"])
                        elif Option == "2":
                            if not Player["CompletedSets"] == []:
                                BuyHouses(Player["Name"])
                            else:
                                print("You don't have any Houses to Sell!")
                                time.sleep(1)
                                SellLoop()
                        else:
                            time.sleep("Invalid Option!")
                            time.sleep(1)
                            SellLoop()
                        if Player["Money"] < Rent:
                            time.sleep(1)
                            AvailibleSell = False
                            for Deed in Player["Deeds"]:
                                if not Deed in MorgagedDeeds:
                                    AvailibleSell = True
                            for Houses in Player["Houses"]:
                                if Houses > 0:
                                    AvailibleSell = True
                            if AvailibleSell == True:
                                print("You can still Sell something!")
                                time.sleep(1)
                                SellLoop()
                            else:
                                clear()
                                MonopolyMan()
                                print(
                                    "Looks like you are completely out of Money & Property"
                                )
                                time.sleep(1)
                                print("You are out of the game!")
                                Player["Playing"] = False
                        else:
                            clear()
                            MonopolyMan()
                            print("You have enough Money now!")
                            time.sleep(1)
                            print("Paying Rent!")
                            time.sleep(1)
                            Players[Owner][
                                "Money"] = Players[Owner]["Money"] + Rent
                            Player["Money"] = Player["Money"] - Rent
                            Balance(Player["Name"])
                            Balance(Owner)

                time.sleep(2)
    elif PosType == "Taxes":
        if Pos == "Income":
            Card = CreateCard(Pos, PosType)
            for string in Card:
                print(string)
            print("You landed on Income Tax!")
            time.sleep(1)
            print("You have two Options:")
            time.sleep(1)
            print("1. Pay 10% of your total Balance ")
            time.sleep(1)
            print("2. Pay $200 ")
            time.sleep(1)
            Balance(Player["Name"])
            Choice = input("Type your option! (1/2) ")
            if Choice == "1":
                print("You have selected paying 10% of your Balance.")
                time.sleep(1)
                Player["Money"] = int(Player["Money"] - Player["Money"] / 10)
                Balance(Player["Name"])
                time.sleep(1)
            else:
                print("You have selected paying $200.")
                time.sleep(1)
                Player["Money"] = Player["Money"] - 200
                Balance(Player["Name"])
                time.sleep(1)
        elif Pos == "Luxury":
            Card = CreateCard(Pos, PosType)
            for string in Card:
                print(string)
            print("You landed on Luxury Tax!")
            time.sleep(1)
            print("You have to Pay $75")
            time.sleep(1)
            input("Press Enter to Pay the Tax")
            Player["Money"] = Player["Money"] - 75
            Balance(Player["Name"])
            time.sleep(1)
    elif PosType == "Go":
        print("You landed on Go!")
        time.sleep(1)
        print("You already collected your $200!")
        time.sleep(1)
    elif PosType == "Jail":
        if Pos == "Jail" and Player["InJail"] == False:
            print("You landed on Jail!")
            time.sleep(1)
            print("Don't Worry though, you are just Visiting!")
            time.sleep(1)
        elif Pos == "GoJail":
            Player["InJail"] = True
            Player["Position"] = "Jail"
            UpdateBoard()
            SeeBoard()
            print(
                "You are in Jail! You need to Roll Doubles or Pay $50 to get out!"
            )
            time.sleep(1)
    elif PosType == "Parking":
        print("You landed on Free Parking!")
        time.sleep(1)
        print("That means you get $500!")
        Player["Money"] = Player["Money"] + 500
        Balance(Player["Name"])
        time.sleep(1)
    elif PosType == "Chance":
        print("You landed on Chance!")
        time.sleep(1)
        input("Press Enter to Draw a Chance Card!")
        CardSpots(Player["Name"])
    elif PosType == "Community":
        print("You landed on Community Chest!")
        time.sleep(1)
        input("Press Enter to Draw a Community Chest Card!")
        CardSpots(Player["Name"])


def Tutorial():
    clear()
    Banker()


def Roll(PlayerName):
    clear()
    global dice1
    global dice2
    dice1 = 0
    dice2 = 0
    for roll in range(39, -1, -1):
        clear()
        MonopolyMan()
        print(PlayerName + " is Rolling!")
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        d1 = Dice[dice1 - 1]
        d2 = Dice[dice2 - 1]
        for i, string in enumerate(d1):
            print(string + "    " + d2[i])
        time.sleep(1 / (roll + 1))
    print("Its a " + str(dice1 + dice2) + "!")
    if dice1 == dice2:
        return [dice1 + dice2, True]
    else:
        return [dice1 + dice2, False]


def BuyHouses(PlayerName):
    global Players
    clear()
    MonopolyMan()
    Player = Players[PlayerName]
    Balance(Player["Name"])
    print("(Note a set with a morgaged Property cannot be built on)")
    print("Here is a list of the Sets you can Built on!:")
    time.sleep(1)
    for Name in Player["CompletedSets"]:
        Morgaged = False
        for Deed in Sets[Name]:
            if Deed in MorgagedDeeds:
                Morgaged = True
        if Morgaged == False:
            SetIndex = Player["CompletedSets"].index(Name)
            print(str(SetIndex) + ". " + Name)
        else:
            SetIndex = Player["CompletedSets"].index(Name)
            print("*Morgaged* " + str(SetIndex) + ". " + Name)
    time.sleep(1)
    print("Which Set would you like to Edit? (Ex. 0) ")
    SellectedSet = input("Or Type Finished to Exit! ").lower().capitalize()
    Morgaged = False
    if SellectedSet.isdigit() and len(
            Player["CompletedSets"]) - 1 >= int(SellectedSet):
        for Deed in Sets[Player["CompletedSets"][int(SellectedSet)]]:
            if Deed in MorgagedDeeds:
                Morgaged = True
    if SellectedSet.isdigit() and len(Player["CompletedSets"]) - 1 >= int(
            SellectedSet) and Morgaged == False:
        print("Selected " + Player["CompletedSets"][int(SellectedSet)] +
              " Set!")
        time.sleep(1)
        clear()
        MonopolyMan()
        Action = input(
            "Would you like to 1. Buy Houses/a Hotel or 2. Sell Houses/a Hotel? (1/2) "
        )
        if Action == "1":
            clear()
            MonopolyMan()
            Balance(Player["Name"])
            for Deed in Sets[Player["CompletedSets"][int(SellectedSet)]]:
                SetIndex = Sets[Player["CompletedSets"][int(SellectedSet)]]
                DeedIndex = SetIndex.index(Deed)
                DeedType = PositionType[PositionIndex.index(Deed)]
                DeedT = Cards[DeedType][Deed]
                if Player["Houses"][Deed] < 5:
                    print(
                        str(DeedIndex) + ". " + DeedT["Name"] +
                        " - House Cost: " + str(DeedT["HouseCost"]) + " - " +
                        str(Player["Houses"][Deed]) + " Houses")
                else:
                    print(
                        str(DeedIndex) + ". " + DeedT["Name"] +
                        " - House Cost: " + str(DeedT["HouseCost"]) + " - " +
                        "Hotel")
            SelectedDeed = input(
                "What Deed would you like to get Houses/a Hotel for? ")
            if SelectedDeed.isdigit() and len(Sets[Player["CompletedSets"][int(
                    SellectedSet)]]) - 1 >= int(SelectedDeed):
                Deed = Sets[Player["CompletedSets"][int(SellectedSet)]][int(
                    SelectedDeed)]
                DeedIndex = PositionIndex.index(Deed)
                DeedType = PositionType[DeedIndex]
                DeedT = Cards[DeedType][Deed]
                HouseCost = DeedT["HouseCost"]
                clear()
                MonopolyMan()
                Balance(Player["Name"])
                print("Prices: ")
                print("1 House: $" + str(HouseCost))
                print("Hotel: $" + str(HouseCost * 5))
                time.sleep(1)
                print("How many Houses would you like to Buy? (1-4)")
                print("Or would you like to Buy a Hotel (H)")
                print(
                    "(If you changed your mind and don't want to Buy Press Enter)"
                )
                ToBuy = input("Option: ").upper()
                if ToBuy.isdigit() and int(
                        ToBuy) < 5 and int(ToBuy) + Player["Houses"][Deed] < 6:
                    if Player["Houses"][Deed] + int(ToBuy) > 4:
                        print(
                            "The amount of Houses you have Bought is equal to a Hotel, buying a Hotel!"
                        )
                    else:
                        print("Buying " + ToBuy + " House(s)")
                    if Player["Money"] > HouseCost * int(ToBuy):
                        Player[
                            "Money"] = Player["Money"] - HouseCost * int(ToBuy)
                        Player["Houses"][Deed] = Player["Houses"][Deed] + int(
                            ToBuy)
                        time.sleep(1)
                        print("Succesfully Purchased!")
                        Balance(Player["Name"])
                        time.sleep(1)
                        BuyHouses(Player["Name"])
                    else:
                        time.sleep(1)
                        Balance(Player["Name"])
                        print("You do not have enough Money for that!")
                        time.sleep(1)
                        ToMorgage = input(
                            "Would you like to Morgage? (yes/no) ").upper()
                        if ToMorgage == "Y" or ToMorgage == "YES":
                            print("Okay!")
                            time.sleep(1)
                            Morgage(Player["Name"])
                            time.sleep(1)
                            clear()
                            MonopolyMan()
                            Balance(Player["Name"])
                            time.sleep(1)
                            if Player["Money"] < HouseCost * int(ToBuy):
                                print("You still do not have enough Money!")
                                time.sleep(1)
                                BuyHouses(Player["Name"])
                            else:
                                Player["Money"] = Player[
                                    "Money"] - HouseCost * int(ToBuy)
                                Player["Houses"][
                                    Deed] = Player["Houses"][Deed] + ToBuy
                                print("Succesfully Purchased!")
                                Balance(Player["Name"])
                                time.sleep(1)
                                BuyHouses(Player["Name"])
                        else:
                            print("Okay, Cancelling Purchase!")
                            time.sleep(1)
                            BuyHouses(Player["Name"])
                elif ToBuy.isdigit() and int(ToBuy) > 5:
                    print("You cannot buy that many Houses, try again!")
                    time.sleep(1)
                    BuyHouses(Player["Name"])
                elif ToBuy == "Hotel" or ToBuy == "H":
                    print("Buying Hotel")
                    HousesRemaining = 5 - Player["Houses"][Deed]
                    time.sleep(1)
                    if Player["Money"] > HouseCost * HousesRemaining:
                        Player["Money"] = Player[
                            "Money"] - HouseCost * HousesRemaining
                        Player["Houses"][Deed] = 5
                        print("Successfully Purchased!")
                        Balance(Player["Name"])
                        time.sleep(1)
                        BuyHouses(Player["Name"])
                    else:
                        print("You do not have enough Money!")
                        time.sleep(1)
                        ToMorgage = input(
                            "Would you like to Morgage? (yes/no) ").upper()
                        if ToMorgage == "Y" or ToMorgage == "YES":
                            print("Okay!")
                            time.sleep(1)
                            Morgage(Player["Name"])
                            time.sleep(1)
                            clear()
                            MonopolyMan()
                            Balance(Player["Name"])
                            time.sleep(1)
                            if Player["Money"] > HouseCost * HousesRemaining:
                                print("Successfully Purchased!")
                                Player["Money"] = Player[
                                    "Money"] - HouseCost * HousesRemaining
                                Balance(Player["Name"])
                                Player["Houses"][Deed] = 5
                                time.sleep(1)
                                BuyHouses(Player["Name"])
                            else:
                                print("You still do not have enough Money!")
                                Balance(Player["Name"])
                                time.sleep(1)
                                BuyHouses(Player["Name"])
                time.sleep(1)
        elif Action == "2":
            clear()
            MonopolyMan()
            Balance(Player["Name"])
            for Deed in Sets[Player["CompletedSets"][int(SellectedSet)]]:
                SetIndex = Sets[Player["CompletedSets"][int(SellectedSet)]]
                DeedIndex = SetIndex.index(Deed)
                DeedType = PositionType[PositionIndex.index(Deed)]
                DeedT = Cards[DeedType][Deed]
                if Player["Houses"][Deed] < 5:
                    print(
                        str(DeedIndex) + ". " + DeedT["Name"] +
                        " - House Cost: " + str(DeedT["HouseCost"]) + " - " +
                        str(Player["Houses"][Deed]) + " Houses")
                else:
                    print(
                        str(DeedIndex) + ". " + DeedT["Name"] +
                        " - House Cost: " + str(DeedT["HouseCost"]) + " - " +
                        "Hotel")
            SelectedDeed = input(
                "What Deed would you like to sell Houses/a Hotel from? ")
            if SelectedDeed.isdigit() and len(Sets[Player["CompletedSets"][int(
                    SellectedSet)]]) - 1 >= int(SelectedDeed):
                Deed = Sets[Player["CompletedSets"][int(SellectedSet)]][int(
                    SelectedDeed)]
                DeedIndex = PositionIndex.index(Deed)
                DeedType = PositionType[DeedIndex]
                DeedT = Cards[DeedType][Deed]
                HouseCost = DeedT["HouseCost"]
                clear()
                MonopolyMan()
                Balance(Player["Name"])
                print("Each House Morgages For $" + str(HouseCost / 2))
                print("How many Houses would you like to Sell? (1-4)")
                print("Or Would you like to Sell a Hotel? (H)")
                ToSell = input("Option: ").upper()
                if ToSell.isdigit() and Player["Houses"][Deed] >= int(ToSell):
                    if int(ToSell) > 4:
                        print(
                            "The amount of Houses you are Selling is equal to Selling an Hotel!"
                        )
                    else:
                        print("Selling " + ToSell + " Houses!")
                    Player["Money"] = Player["Money"] + HouseCost * int(
                        ToSell) / 2
                    Player["Houses"][Deed] = Player["Houses"][Deed] - int(
                        ToSell)
                    time.sleep(1)
                    print("Successfully Sold!")
                    Balance(Player["Name"])
                    time.sleep(1)
                    BuyHouses(Player["Name"])
                elif ToSell.isdigit() and Player["Houses"][Deed] < int(ToSell):
                    print("You can't Sell that Many Houses")
                    time.sleep(1)
                    BuyHouses(Player["Name"])
                elif ToSell == "H" and Player["Houses"][
                        Deed] == 5 or ToSell == "HOTEL" and Player["Houses"][
                            Deed] == 5:
                    print("Selling Hotel!")
                    time.sleep(1)
                    Player["Money"] = Player["Money"] + HouseCost * 5 / 2
                    Player["Houses"][Deed] = 0
                    print("Successfully Sold!")
                    Balance(Player["Name"])
                    time.sleep(1)
                    BuyHouses(Player["Name"])
                elif ToSell == "H" and not Player["Houses"][Deed] == 5:
                    print("You dont have a Hotel on this Property!")
                    time.sleep(1)
                    BuyHouses(Player["Name"])
        else:
            print("You didnt type a valid Answer. Restarting!")
            time.sleep(1)
            BuyHouses(Player["Name"])
    elif Morgaged == True:
        print("That Set is Morgaged!")
        time.sleep(1)
        BuyHouses(Player["Name"])
    elif SellectedSet == "Finished":
        print("Alright!")
        time.sleep(1)
    else:
        print(
            "You don't own that Set or it Doesn't Exsist, did you spell it right?"
        )
        BuyHouses(Player["Name"])


def Trade(PlayerName):
    global Players
    global NewTradeBoard
    global TradeData
    Player = Players[PlayerName]
    clear()
    MonopolyMan()
    NewTradeBoard = [] + TradeBoard
    TradeData = {
        "P1D": [],
        "P2D": [],
        "P1B": 0,
        "P2B": 0,
    }

    def ShowTrade():
        for string in NewTradeBoard:
            print(string)

    print("Lets get to Trading!")
    time.sleep(1)

    def SelectTrader():
        global Players
        clear()
        MonopolyMan()
        print("What Player would you like to trade with?")
        print("Here are all of the Players!:")
        for tradername, table in Players.items():
            if not tradername == PlayerName:
                print(tradername)
        tradewith = input("Which Player would you like to Trade with? ").lower(
        ).capitalize()
        if tradewith in Players and not tradewith == PlayerName:
            clear()
            MonopolyMan()
            Trade = input(tradewith + " Would you like to Trade with " +
                          PlayerName + "? (yes/no) ").upper()
            if Trade == "Y" or Trade == "YES":
                return Players[tradewith]
            else:
                print("Looks like " + tradewith +
                      " doesn't want to trade with you!")
                time.sleep(1)
                newtrader = input(
                    PlayerName +
                    " would you like to trade with someone else? (yes/no) "
                ).upper()
                if newtrader == "Y" or newtrader == "YES":
                    print("Alright!")
                    time.sleep(1)
                    return SelectTrader()
                else:
                    print("Alright no more trading!")
                    time.sleep(1)
                    return "Nope"
        elif tradewith == PlayerName:
            print("You can't trade with Yourself!")
            time.sleep(1)
            print("Try again!")
            time.sleep(1)
            return SelectTrader()
        else:
            print("That's not a real player!")
            time.sleep(1)
            print("Try again!")
            return SelectTrader()

    def UpdateTradeBoard(Traders):
        global NewTradeBoard
        global TradeData
        global Players
        NewTradeBoard = [] + TradeBoard
        for ReplacementType, Values in Replacement["TradeBoard"].items():
            if ReplacementType == "P1N" or ReplacementType == "P2N":
                x = Values[0]
                print(x)
                Player = Traders[Values[4]]
                print(Player)
                UpdatedString = ReplaceText(NewTradeBoard[x], ReplacementType,
                                            Player["Name"])
                NewTradeBoard[x] = UpdatedString
            elif ReplacementType == "P1B" or ReplacementType == "P2B":
                x = Values[0]
                Section = NewTradeBoard[x][Values[2]:Values[3] + 1]
                NewSection = CenterText(Section,
                                        str(TradeData[ReplacementType]))
                LeftSection = NewTradeBoard[x][:Values[2]]
                RightSection = NewTradeBoard[x][Values[3] + 1:]
                UpdatedString = LeftSection + NewSection + RightSection
                NewTradeBoard[x] = UpdatedString
            elif ReplacementType == "P1D" or ReplacementType == "P2D":
                for deed in TradeData[ReplacementType]:
                    PosIndex = TradeData[ReplacementType].index(
                        deed) + Values[0]
                    NewString = CenterText(NewTradeBoard[PosIndex], deed)
                    NewTradeBoard[PosIndex] = NewString

    Trader = SelectTrader()

    def EditOffer(Player, PNum):
        clear()
        ShowTrade()
        print(Player["Name"] +
              " What would you like to add/remove from your Offer?")
        time.sleep(1)
        print("Deeds (1), Money (2) or Nothing (3) ?")
        ToDo = input("Number: ")
        if ToDo == "1":
            clear()
            ShowTrade()
            print("Here is a list of All of your Deeds!")
            print("Select Which ones you want to Trade!")
            for Deed in Player["Deeds"]:
                InTrade = "NotTrading"
                if Deed in TradeData[PNum + "D"]:
                    InTrade = "Trading"
                DeedIndex = PositionIndex.index(Deed)
                DeedType = PositionType[DeedIndex]
                DeedTable = Cards[DeedType][Deed]
                NameString = ""
                if DeedType == "Deed":
                    NameString = str(
                        DeedIndex) + ". " + DeedTable["Name"] + " - " + InTrade
                elif DeedType == "RailRoad":
                    NameString = str(DeedIndex) + ". " + DeedTable[
                        "Title"] + "RailRoad - " + InTrade
                elif DeedType == "Utility":
                    NameString = str(DeedIndex) + ". " + DeedTable[
                        "Title1"] + " " + DeedTable["Title2"] + " - " + InTrade
                print(NameString)
            print("Which deed would you like to Add/Remove? ")
            ToTrade = input("Deed Number: ")
            if ToTrade.isdigit() and PositionIndex[int(
                    ToTrade)] in Player["Deeds"] and not PositionIndex[int(
                        ToTrade)] in MorgagedDeeds:
                DeedIndex = int(ToTrade)
                DeedType = PositionType[DeedIndex]
                DeedName = PositionIndex[int(ToTrade)]
                DeedTable = Cards[DeedType][DeedName]
                NameString = ""
                if DeedType == "Deed":
                    NameString = DeedTable["Name"] + " - " + InTrade
                elif DeedType == "RailRoad":
                    NameString = DeedTable["Title"] + "RailRoad - " + InTrade
                elif DeedType == "Utility":
                    NameString = DeedTable["Title1"] + " " + DeedTable[
                        "Title2"] + " - " + InTrade
                if DeedName in TradeData[PNum + "D"]:
                    print("Removing " + NameString + " From your Offer!")
                    TradeData[PNum + "D"].remove(ToTrade)
                    time.sleep(1)
                    again = input(
                        "Would you like to continue editing your offer? (yes/no) "
                    ).upper()
                    if again == "YES" or again == "Y":
                        EditOffer(Player, PNum)
                    else:
                        print("Alright!")
                else:
                    print("Adding " + NameString + " to your Offer!")
                    TradeData[PNum + "D"].append(ToTrade)
                    again = input(
                        "Would you like to continue editing your offer? (yes/no) "
                    ).upper()
                    if again == "YES" or again == "Y":
                        EditOffer(Player, PNum)
                    else:
                        print("Alright!")
            elif ToTrade.isdigit() and PositionIndex[int(
                    ToTrade)] in MorgagedDeeds:
                print("That Deed is Morgaged!")
                time.sleep(1)
                print("You need to UnMorgage it to Trade it!")
                time.sleep(1)
                input("Press Enter to Continue...")
                EditOffer(Player, PNum)
            elif not ToTrade.isdigit():
                print("Thats not a Number!")
                time.sleep(1)
                print("Try Again!")
                time.sleep(1)
                input("Press Enter to Continue...")
                EditOffer(Player, PNum)
            else:
                print("You don't own this deed!")
                time.sleep(1)
                print("Did you put the right number?")
                time.sleep(1)
                input("Press Enter to Continue...")
                EditOffer(Player, PNum)
        elif ToDo == "2":
            clear()
            ShowTrade()
            Balance(Player["Name"])
            Key = "P1B"
            if PNum == "P2":
                Key = "P2B"
            Change = input(
                "Would you like to Add(A) or Subtract(S) from the money you are trading? "
            ).lower()
            if Change == "add" or Change == "a" or Change == "subtract" or Change == "s":
                if Change == "a":
                    Change = "add"
                if Change == "s":
                    Change = "subtract"
                ToChange = input("How much money would you like to " + Change +
                                 "? ")
                if ToChange.isdigit(
                ) and int(ToChange) <= Player["Money"] and int(
                        ToChange) + TradeData[Key] <= Player["Money"]:
                    print(Change.capitalize() + "ing $" + str(int(ToChange)))
                    if Change == "add":
                        TradeData[Key] = TradeData[Key] + int(ToChange)
                    elif Change == "subtract":
                        TradeData[Key] = TradeData[Key] - int(ToChange)
                    time.sleep(1)
                    again = input(
                        "Would you like to continue editing your offer? (yes/no) "
                    ).upper()
                    if again == "YES" or again == "Y":
                        EditOffer(Player, PNum)
                    else:
                        print("Alright!")
                elif ToChange.isdigit(
                ) and int(ToChange) > Player["Money"] or ToChange.isdigit(
                ) and int(ToChange) + TradeData[Key] > Player["Money"]:
                    print("You don't have enough money for that!")
                    time.sleep(1)
                    input("Press Enter to Continue...")
                    EditOffer(Player, PNum)
                else:
                    print("Thats not a valid number!")
                    time.sleep(1)
                    input("Press Enter to Continue...")
                    EditOffer(Player, PNum)
            else:
                print("Invalid Selection!")
                time.sleep(1)
                print("Did you spell it right?")
                time.sleep(1)
                input("Press Enter to Continue...")
                EditOffer(Player, PNum)
        elif ToDo == "3":
            print("Nothing")
        else:
            print("Invalid Selection!")
            time.sleep(1)
            print("That isnt one of the Availible Numbers (1,2,3)")
            time.sleep(1)
            print("Restarting!")
            EditOffer(Player, PNum)

    if not Trader == "Nope":
        clear()
        MonopolyMan()
        print(
            "Before we start please not that you can only trade 10 deeds at a time!"
        )
        time.sleep(1)
        print("However there is no limit on how money you can trade!")
        time.sleep(1)
        print("Lets Trade!")
        time.sleep(2)

        def Confirm():
            clear()
            ShowTrade()
            P1Okay = input(Player["Name"] +
                           " Do you confirm the Trade? (yes/no) ").upper()
            if P1Okay == "Y" or P1Okay == "YES":
                print(Player["Name"] + " Accepted!")
                time.sleep(1)
                clear()
                ShowTrade()
                P2Okay = input(Trader["Name"] +
                               " Do you confirm the trade? (yes/no) ").upper()
                if P2Okay == "Y" or P2Okay == "YES":
                    print(Trader["Name"] + " Accepted!")
                    time.sleep(1)
                    print("Trade Commensing!")
                    time.sleep(1)
                    Trader["Money"] = Trader["Money"] - TradeData[
                        "P2B"] + TradeData["P1B"]
                    Player["Money"] = Player["Money"] - TradeData[
                        "P1B"] + TradeData["P2B"]
                    for deed in TradeData["P1D"]:
                        Player["Deeds"].remove(deed)
                        Player["Houses"][deed] = 0
                        Trader["Deeds"].append(deed)
                    for deed in TradeData["P2D"]:
                        Trader["Deeds"].remove(deed)
                        Trader["Houses"][deed] = 0
                        Player["Deeds"].append(deed)
                    Balance(Trader["Name"])
                    Balance(Player["Name"])
                    input("Press Enter to Continue...")
                else:
                    print(Trader["Name"] + " Denied!")
                    time.sleep(1)
                    clear()
                    ShowTrade()
                    P1Continue = input(
                        Player["Name"] +
                        " Would you like to continue Trading? ").upper()
                    if P1Continue == "Y" or P1Continue == "YES":
                        print("Alright!")
                        time.sleep(1)
                        clear()
                        ShowTrade()
                        P2Continue = input(
                            Trader["Name"] +
                            " Would you like to continue Trading? ")
                        if P2Continue == "YES" or P2Continue == "Y":
                            print("Alright!")
                            time.sleep(1)
                            TradeLoop()
                        else:
                            print(Trader["Name"] + " Declinced the Trade!")
                            time.sleep(1)
                            print("Ending the Trade!")
                    else:
                        print(Player["Name"] + " Declined the Trade!")
                        time.sleep(1)
                        print("Ending the Trade!")
            else:
                print(Player["Name"] + " Denied!")
                time.sleep(1)
                clear()
                ShowTrade()
                P1Continue = input(
                    Player["Name"] +
                    " Would you like to continue Trading? ").upper()
                if P1Continue == "Y" or P1Continue == "YES":
                    print("Alright!")
                    time.sleep(1)
                    clear()
                    ShowTrade()
                    P2Continue = input(Trader["Name"] +
                                       " Would you like to continue Trading? ")
                    if P2Continue == "YES" or P2Continue == "Y":
                        print("Alright!")
                        time.sleep(1)
                        TradeLoop()
                    else:
                        print(Trader["Name"] + " Declinced the Trade!")
                        time.sleep(1)
                        print("Ending the Trade!")
                else:
                    print(Player["Name"] + " Declined the Trade!")
                    time.sleep(1)
                    print("Ending the Trade!")

        def TradeLoop():
            global Players
            Traders = [Player, Trader]
            UpdateTradeBoard(Traders)
            clear()
            ShowTrade()
            Turn1 = input(
                Player["Name"] +
                " Would you like to edit your Offer? (yes/no) ").upper()
            if Turn1 == "Y" or Turn1 == "YES":
                EditOffer(Player, "P1")
                clear()
                ShowTrade()
                time.sleep(1)
                Turn2 = input(
                    Trader["Name"] +
                    " Would you like to edit your Offer? (yes/no) ").upper()
                if Turn2 == "Y" or Turn2 == "YES":
                    EditOffer(Trader, "P2")
                    time.sleep(1)
                    Confirm()
                else:
                    print("Alright!")
                    time.sleep(1)
                    Confirm()
            else:
                print("Alright!")
                time.sleep(1)
                Turn2 = input(
                    Trader["Name"] +
                    " Would you like to edit your Offer? (yes/no) ").upper()
                if Turn2 == "Y" or Turn2 == "YES":
                    EditOffer(Trader, "P2")
                    time.sleep(1)
                    Confirm()
                else:
                    print("Alright!")
                    time.sleep(1)
                    print("Neither Sides want to add to their Offer!")
                    time.sleep(1)
                    Confirm()

        TradeLoop()


def Start():
    MonopolyMan()
    play = input("Would you like to play a game of Monopoly? (yes/no) ")
    if (play.upper() == "Y" or play.upper() == "YES"):
        print("Alright Lets Get Started!")
        time.sleep(1)
        print("Monopoly is a long playing Game")
        print("I Hope if you are starting this you have enough time!")
        tutorial = input("Do all of your Players know how to play? (yes/no) ")
        if (tutorial.upper() == "Y" or tutorial.upper() == "YES"):
            print("Then Lets Play!")
            time.sleep(1)
            Game()
        else:
            print("Okay here is a tutorial!")
            time.sleep(1)
            Tutorial()
    else:
        print("I spent a really long time on this...")
        time.sleep(1)
        print("You're Mean")


def Turn(PlayerName):
    global Players
    Player = Players[PlayerName]
    clear()
    MonopolyMan()
    print(PlayerName + "'s Turn!")
    time.sleep(1)
    Move(PlayerName)
    if Player["SaveGame"] == True:
        SaveGame()
    Result = CheckEnd()

    def Options():
        clear()
        MonopolyMan()
        Balance(Player["Name"])
        print("What would you like to do? (1-3)")
        print("1: Morgage/UnMorgage")
        print("2: Buy Houses")
        print("3: Trade Deeds!")
        print("4: End Turn")
        if Player["InJail"] == True:
            print("5: Pay $50 to get out of Jail")
            print("6: Use Get Out of Jail Free Card")
        Action = input("Option: ")
        if Action == "1":
            if not Player["Deeds"] == []:
                Morgage(PlayerName)
                time.sleep(1)
                Options()
            else:
                print("You don't Own any Deeds!")
                time.sleep(1)
                Options()
        elif Action == "2":
            if not Player["CompletedSets"] == []:
                BuyHouses(PlayerName)
                time.sleep(1)
                Options()
            else:
                print("You don't have any Completed Sets!")
                time.sleep(1)
                Options()
        elif Action == "5" and Player["InJail"] == True:
            if Player["Money"] > 50 and Player["InJail"] == True:
                print("Alright!")
                time.sleep(1)
                Player["Money"] = Player["Money"] - 50
                Balance(Player["Name"])
                Player["InJail"] = False
                Options()
        elif Action == "6" and Player["InJail"] == True:
            if "JailFree" in Player["Cards"]:
                print("Alright!")
                time.sleep(1)
                print("You have used your get out of Jail free card!")
                Player["InJail"] = False
                time.sleep(1)
                Options()
            else:
                print("You don't Have one!")
                time.sleep(1)
                print("Looks like you need to roll doubles or pay $50!")
                Options()
        elif Action == "3":
            Trade(Player["Name"])
        elif Action == "4":
            print("Turn Over!")
            time.sleep(1)
            SaveGame()
        else:
            print("Invalid Option")
            time.sleep(1)
            Options()

    if Result == "Running":
        Options()
    else:
        print("The Game is Over!")
        time.sleep(1)
        print(Result + " Has Won!")
        time.sleep(1)
        print("Congradulations on a well Played Game!")
        for game in RunningGames:
            FoundPlayers = 0
            for playername, table in game.items():
                if playername in Players:
                    FoundPlayers = FoundPlayers + 1
            if FoundPlayers == len(table):
                RunningGames.remove(game)


def SaveGame():
    global Players
    SaveGame = False
    PlayerTable = {}
    for PlayerName, Table in Players.items():
        PlayerTable[PlayerName] = Table
        SaveGame = Table["SaveGame"]
    for game in RunningGames:
        FoundPlayers = 0
        for playername, table in game.items():
            if playername in PlayerTable:
                FoundPlayers = FoundPlayers + 1
        if FoundPlayers == len(PlayerTable):
            RunningGames.remove(game)
    if SaveGame == True:
        RunningGames.append(PlayerTable)
        db["RunningGames"] = RunningGames


def CheckEnd():
    global Players
    StillPlaying = 0
    for PlayerName, Table in Players.items():
        if Table["Playing"] == True:
            StillPlaying = StillPlaying + 1
    if StillPlaying < 2:
        print("The Game is Over!")
        Winner = ""
        for PlayerName, Table in Players.items():
            if Table["Playing"] == True:
                Winner = PlayerName
        time.sleep(1)
        print(Winner + " Has Won!")
        time.sleep(1)
        print("Congradulations!")
        return Winner
    else:
        return "Running"


def Banker():
    clear()
    MonopolyMan()
    print("Unlike normal Monpoly you don't need someone to be a Banker!")
    time.sleep(1)
    print("It is done Automatically!")
    time.sleep(1)
    print("That also means you dont have to")
    print("keep track of your Deeds & Money")


def Game():
    global Players
    global NumberOfPlayers
    clear()
    MonopolyMan()
    Resumed = False
    if not RunningGames == []:
        print("There is atleast one previous game paused!")
        time.sleep(1)
        resume = input("Would you like to resume a game? (yes/no) ").upper()
        if resume == "Y" or resume == "YES":
            Resumed = True
            print("Alright!")
            time.sleep(1)

            def ResumeGame():
                clear()
                MonopolyMan()
                print("Here is a list of paused games!")
                for game in RunningGames:
                    print()
                    PlayerString = ""
                    for playername, playertable in game.items():
                        PlayerString = PlayerString + playername + "(" + playertable[
                            "Letter"] + ")" + " "
                    print("Game " + str(RunningGames.index(game)) + ":")
                    print(PlayerString)
                print("Which game would you like to resume?")
                Selection = input("Game Number: ")
                if Selection.isdigit(
                ) and len(RunningGames) - 1 >= int(Selection):
                    print(Selection + " Selected!")
                    for Name, Table in RunningGames[int(Selection)].items():
                        Players[Name] = Table
                else:
                    print("Thats not a valid Selection!")
                    time.sleep(1)
                    print("Make sure you type the number!")
                    time.sleep(1)
                    ResumeGame()

            ResumeGame()
        else:
            deletesave = input(
                "Would you like to delete a Game? (yes/no) ").upper()
            if deletesave == "Y" or deletesave == "YES":
                for game in RunningGames:
                    PlayerString = ""
                    for playername, playertable in game.items():
                        PlayerString = PlayerString + playername + "(" + playertable[
                            "Letter"] + ")" + " "
                    print("Game " + str(RunningGames.index(game)) + ":")
                    print(PlayerString)
                    print()
                time.sleep(1)
                print("What save would you like to delete?")
                todelete = input("Game Number: ")
                if todelete.isdigit(
                ) and len(RunningGames) - 1 >= int(todelete):
                    print(todelete + " Deleting!")
                    RunningGames.remove(RunningGames[int(todelete)])
                    time.sleep(1)
                    print("Deleted")
                    time.sleep(1)
                else:
                    print("Thats not a valid Selection!")
                    time.sleep(1)
                    print("Next time type the correct number!")
                    time.sleep(1)
            clear()
            MonopolyMan()
            print("Alright! Lets start a new game!")
            time.sleep(1)
            clear()
            MonopolyMan()
            GetPlayers()
    else:
        GetPlayers()
    if Resumed == False:
        clear()
        MonopolyMan()
        print("Would you like to Auto Save your Game?")
        time.sleep(1)
        print(
            "If you want to resume your game later then autosave is the way to do it!"
        )
        time.sleep(1)
        Autosave = input("AutoSave? (yes/no): ").upper()
        if Autosave == "Y" or Autosave == "YES":
            print("Enabling Autosave!")
            for playername, table in Players.items():
                table["SaveGame"] = True
            time.sleep(1)
        else:
            print("Okay it will not Auto Save!")
            time.sleep(1)
        clear()
        MonopolyMan()
        if not int(NumberOfPlayers) == 1:
            print("Now we have to decide who goes first!")
            time.sleep(1)
            print(
                "Every player will roll the dice and the person with the highest roll goes first."
            )
            Rolls = {}
            for Index, Player in Players.items():
                print("Its " + Player["Name"] + "'s Roll!")
                input("Press Enter to Roll!")
                PlayerRoll = Roll(Player["Name"])
                Rolls[Player["Name"]] = PlayerRoll[0]
            HighestRoll = max(Rolls.keys(), key=(lambda k: Rolls[k]))
            print(str(HighestRoll) + " got the Highest Roll!")
            Players[HighestRoll]["Order"] = 0
            Count = 0
            for Index, Player in Players.items():
                if not Player["Name"] == HighestRoll:
                    Count = Count + 1
                    Player["Order"] = int(Count)
            input("Press Enter to Start the Game!")
            while Ended == False:
                for Order in range(Count + 1):
                    for Index, Player in Players.items():
                        if Player["Order"] == Order:
                            Turn(Player["Name"])
        else:
            print(
                "Because you are the only player we don't need to roll to see who go's first!"
            )
            print("The game will just end when you get every deed!")
            input("Press Enter to Start the Game!")
            while Ended == False:
                for Index, Player in Players.items():
                    Turn(Player["Name"])
    else:
        clear()
        MonopolyMan()
        if not int(NumberOfPlayers) == 1:
            input("Press Enter to Start the Game!")
            Count = 0
            for Index, Player in Players.items():
                Count = Count + 1
            while Ended == False:
                for Order in range(Count):
                    for Index, Player in Players.items():
                        if Player["Order"] == Order:
                            Turn(Player["Name"])
        else:
            print(
                "Because you are the only player we don't need to roll to see who go's first!"
            )
            print("The game will just end when you get every deed!")
            input("Press Enter to Start the Game!")
            while Ended == False:
                for Index, Player in Players.items():
                    Turn(Player["Name"])


def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


clear()
Start()
