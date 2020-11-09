from flask import Flask
from flask import render_template
from localsettings import DEBUG

app = Flask(__name__)


# filters
# -----------------------------------------------------------------------------

def children_are_same_orientation(row):
    return len({item['orientation'] for item in row}) == 1


@app.template_filter('get_row_class')
def get_row_class(row):
    if children_are_same_orientation(row):
        return 'layout-' + str(len(row)) + '-column'

    # if there are two images, we know they aren't the same orientation, so we
    # can just give it one class
    if len(row) == 2:
        return 'layout-two-photo-mix'

    if len(row) == 3:
        portraits = [pic for pic in row if pic['orientation'] == 'portrait']

        if len(portraits) == 1:
            return 'layout-two-landscape-one-portrait'
        else:
            return 'layout-two-portrait-one-landscape'

    # anything that makes it down here doesn't have a style defined yet.
    return 'layout-butts'  # TODO


# routes
# -----------------------------------------------------------------------------

@app.route('/')
def index_route(params={}):
    rows = [
        # overall setting
        [
            {'id': '6', 'orientation': 'landscape'},
        ], [
            {'id': '10', 'orientation': 'portrait'},
            {'id': '12', 'orientation': 'portrait'},
        ], [
            {'id': '21', 'orientation': 'portrait'},
            {'id': '18', 'orientation': 'portrait'},
            {'id': '23', 'orientation': 'portrait'},
        ], [
            {'id': '27', 'orientation': 'landscape'},
        ], [
            {'id': '31', 'orientation': 'portrait'},
            {'id': '37', 'orientation': 'portrait'},
        ], [
            {'id': '39', 'orientation': 'landscape'},
        ],

        # pepper denim phase
        [
            {'id': '41', 'orientation': 'landscape'},  # amy bow
        ], [
            {'id': '44', 'orientation': 'portrait'},  # makeup bag
            {'id': '48', 'orientation': 'portrait'},  # fussing
        ], [
            {'id': '51', 'orientation': 'landscape'},  # brushing
        ], [
            {'id': '53', 'orientation': 'portrait'},  # liz
            {'id': '70', 'orientation': 'portrait'},  # amy hair
        ], [
            {'id': '59', 'orientation': 'landscape'},  # rings
        ], [
            {'id': '56', 'orientation': 'portrait'},  # dress
            {'id': '62', 'orientation': 'portrait'},  # headband and dog
        ], [
            {'id': '63', 'orientation': 'landscape'},  # headband
        ], [
            {'id': '65', 'orientation': 'portrait'},  # hair before
            {'id': '73', 'orientation': 'portrait'},  # hair after
        ], [
            {'id': '81', 'orientation': 'landscape'},  # makeup mirror
        ],

        # indoor and outdoor prep
        [
            {'id': '67', 'orientation': 'landscape'},  # kitchen
        ], [
            {'id': '83', 'orientation': 'portrait'},  # van
            {'id': '86', 'orientation': 'portrait'},  # trash cans
        ], [
            {'id': '234', 'orientation': 'portrait'},  # dave
            {'id': '87', 'orientation': 'landscape'},  # wind tables
        ], [
            {'id': '149', 'orientation': 'portrait'},  # carry flowers
            {'id': '323', 'orientation': 'portrait'},  # liz smile
        ],

        # ben tie and shoes
        [
            {'id': '111', 'orientation': 'portrait'},
            {'id': '110', 'orientation': 'portrait'},
        ], [
            {'id': '289', 'orientation': 'landscape'},
        ],

        # bubba and baby
        [
            {'id': '122', 'orientation': 'portrait'},
            {'id': '124', 'orientation': 'portrait'},
        ],

        # pepper in dress
        [
            {'id': '167', 'orientation': 'landscape'},
        ], [
            {'id': '173', 'orientation': 'portrait'},
            {'id': '175', 'orientation': 'portrait'},
        ], [
            {'id': '176', 'orientation': 'portrait'},
            {'id': '177', 'orientation': 'portrait'},
        ], [
            {'id': '184', 'orientation': 'landscape'},  # bouquet handing
        ], [
            {'id': '180', 'orientation': 'portrait'},  # bouquet holding
            {'id': '191', 'orientation': 'portrait'},  # amy reaction
        ], [
            {'id': '181', 'orientation': 'portrait'},  # bouquet closeup
            {'id': '220', 'orientation': 'portrait'},  # shoes on
        ], [
            {'id': '196', 'orientation': 'landscape'},  # mike bouquet
        ],

        # ben nervous
        [
            {'id': '129', 'orientation': 'portrait'},
            {'id': '135', 'orientation': 'portrait'},
        ], [
            {'id': '138', 'orientation': 'portrait'},
            {'id': '158', 'orientation': 'portrait'},
        ],

        # ceremony setting
        [
            {'id': '320', 'orientation': 'landscape'},  # deb's dog
        ], [
            {'id': '102', 'orientation': 'portrait'},  # chairs
            {'id': '153', 'orientation': 'portrait'},  # flowers still
        ], [
            {'id': '334', 'orientation': 'landscape'},  # cello still
        ],

        # pepper champagne / dad
        [
            {'id': '238', 'orientation': 'portrait'},
            {'id': '251', 'orientation': 'landscape'},
        ], [
            {'id': '262', 'orientation': 'portrait'},
            {'id': '270', 'orientation': 'portrait'},
        ], [
            {'id': '276', 'orientation': 'landscape'},
        ],

        # ben waiting TODO
        [
            {'id': '288', 'orientation': 'portrait'},
            {'id': '295', 'orientation': 'landscape'},
        ],

        # pinning flowers TODO
        [
            {'id': '345', 'orientation': 'landscape'},
            {'id': '340', 'orientation': 'portrait'},
        ], [
            {'id': '351', 'orientation': 'portrait'},
            {'id': '356', 'orientation': 'portrait'},
        ], [
            {'id': '361', 'orientation': 'portrait'},
            {'id': '366', 'orientation': 'landscape'},
        ], [
            {'id': '374', 'orientation': 'landscape'},  # family gang
        ],

        # audience waiting
        [
            {'id': '339', 'orientation': 'landscape'},  # audience waiting
        ], [
            {'id': '388', 'orientation': 'landscape'},  # audient waiting
        ], [
            {'id': '393', 'orientation': 'landscape'},  # pitbull waiting
        ],

        # procession
        [
            {'id': '401', 'orientation': 'landscape'},  # pepper 1st leg
        ], [
            {'id': '407', 'orientation': 'landscape'},
            {'id': '412', 'orientation': 'portrait'},
        ], [
            {'id': '418', 'orientation': 'landscape'},  # family processing
        ], [
            {'id': '442', 'orientation': 'landscape'},  # dogs processing
        ], [
            {'id': '423', 'orientation': 'portrait'},  # family sitting
            {'id': '424', 'orientation': 'portrait'},
            {'id': '425', 'orientation': 'portrait'},
        ], [
            {'id': '436', 'orientation': 'portrait'},  # ben on stage
            {'id': '432', 'orientation': 'portrait'},  # pepper 2nd leg
        ],

        # ceremony - start
        [
            {'id': '447', 'orientation': 'portrait'},  # dad delivery
            {'id': '451', 'orientation': 'portrait'},  # premature kiss
            {'id': '452', 'orientation': 'portrait'},  # mike's reaction
        ],

        # ceremony - amy
        [
            {'id': '475', 'orientation': 'portrait'},
            {'id': '483', 'orientation': 'landscape'},
        ],

        # ceremony - liz
        [
            {'id': '491', 'orientation': 'landscape'},
            {'id': '328', 'orientation': 'landscape'},  # liz playing (trick!)
        ],

        # ceremony - mom
        [
            {'id': '490', 'orientation': 'portrait'},  # watching liz
            {'id': '506', 'orientation': 'landscape'},
        ], [
            {'id': '520', 'orientation': 'portrait'},
            {'id': '524', 'orientation': 'portrait'},
        ],

        # ceremony - mike
        [
            {'id': '560', 'orientation': 'landscape'},
        ], [
            {'id': '540', 'orientation': 'portrait'},
            {'id': '567', 'orientation': 'landscape'},
        ],

        # ceremony - audience
        [
            {'id': '576', 'orientation': 'landscape'},
        ], [
            {'id': '577', 'orientation': 'landscape'},
        ], [
            {'id': '579', 'orientation': 'landscape'},
        ], [
            {'id': '580', 'orientation': 'landscape'},
        ],

        # ceremony - vows
        [
            {'id': '586', 'orientation': 'landscape'},
        ], [
            {'id': '589', 'orientation': 'portrait'},
            {'id': '605', 'orientation': 'portrait'},
        ],

        # ceremony - dogs
        [
            {'id': '459', 'orientation': 'portrait'},
            {'id': '514', 'orientation': 'portrait'},
            {'id': '555', 'orientation': 'portrait'},
        ], [
            {'id': '612', 'orientation': 'landscape'},  # ass
            {'id': '630', 'orientation': 'portrait'},  # petals
        ], [
            {'id': '622', 'orientation': 'landscape'},  # baby
        ], [
            {'id': '641', 'orientation': 'landscape'},  # bubba
        ],

        # ceremony - rings TODO
        [
            {'id': '659', 'orientation': 'portrait'},
            {'id': '665', 'orientation': 'landscape'},
            {'id': '682', 'orientation': 'portrait'},
        ],

        # ceremony - kiss and exit TODO
        [
            {'id': '702', 'orientation': 'landscape'},  # kiss
        ], [
            {'id': '706', 'orientation': 'portrait'},  # hug
            {'id': '732', 'orientation': 'portrait'},  # walk
        ], [
            {'id': '744', 'orientation': 'portrait'},  # hands
            {'id': '748', 'orientation': 'portrait'},  # waist
            {'id': '765', 'orientation': 'portrait'},  # basket interlude
        ], [
            {'id': '754', 'orientation': 'landscape'},  # distant
        ],

        # reception setting
        [
            {'id': '90', 'orientation': 'landscape'},  # lawn living room
        ], [
            {'id': '97', 'orientation': 'portrait'},  # plates
            {'id': '1074', 'orientation': 'portrait'},  # cake
        ], [
            {'id': '1173', 'orientation': 'portrait'},  # lemonade
            {'id': '787', 'orientation': 'portrait'},  # solo chair
        ], [
            {'id': '1209', 'orientation': 'landscape'},  # flowers
        ],

        # reception part one - mingling and drinking phase
        [
            {'id': '789', 'orientation': 'landscape'},  # A+K carrying
        ], [
            {'id': '785', 'orientation': 'portrait'},  # ben mingling
            {'id': '791', 'orientation': 'portrait'},  # bar scene
        ], [
            {'id': '795', 'orientation': 'landscape'},  # folks mingling
        ], [
            {'id': '800', 'orientation': 'portrait'},  # bar still
            {'id': '803', 'orientation': 'portrait'},  # ben mingling
        ], [
            {'id': '806', 'orientation': 'landscape'},  # overall
        ], [
            {'id': '1003', 'orientation': 'portrait'},  # overall - afar
            {'id': '1012', 'orientation': 'portrait'},  # amy being cute
        ],

        # formals
        [
            {'id': '848', 'orientation': 'landscape'},  # ben dad & stepmom
        ], [
            {'id': '961', 'orientation': 'landscape'},  # ben dad extended 1
            {'id': '966', 'orientation': 'landscape'},  # ben dad extended 2
        ], [
            {'id': '839', 'orientation': 'landscape'},  # greens
        ], [
            {'id': '886', 'orientation': 'portrait'},  # ben mom
            {'id': '860', 'orientation': 'landscape'},  # ben mom extended
        ], [
            {'id': '889', 'orientation': 'portrait'},
            {'id': '890', 'orientation': 'portrait'},
        ], [
            {'id': '911', 'orientation': 'portrait'},
            {'id': '917', 'orientation': 'portrait'},
        ], [
            {'id': '923', 'orientation': 'landscape'},
        ], [
            {'id': '927', 'orientation': 'landscape'},
        ],

        # couple situations
        [
            {'id': '934', 'orientation': 'portrait'},
            {'id': '939', 'orientation': 'landscape'},
        ], [
            {'id': '948', 'orientation': 'landscape'},
            {'id': '977', 'orientation': 'portrait'},
        ], [
            {'id': '994', 'orientation': 'landscape'},
            {'id': '1018', 'orientation': 'portrait'},  # first dance
            {'id': '995', 'orientation': 'landscape'},
        ],

        # friend formals (greenhouse)
        [
            {'id': '1054', 'orientation': 'landscape'},
        ], [
            {'id': '1062', 'orientation': 'landscape'},
        ], [
            {'id': '1078', 'orientation': 'landscape'},
        ],

        # the rings are found
        [
            {'id': '1091', 'orientation': 'portrait'},
            {'id': '1097', 'orientation': 'portrait'},
        ], [
            {'id': '1111', 'orientation': 'portrait'},
            {'id': '1118', 'orientation': 'portrait'},
        ],

        # cake cutting
        [
            {'id': '1126', 'orientation': 'portrait'},
            {'id': '1143', 'orientation': 'landscape'},
        ], [
            {'id': '1146', 'orientation': 'landscape'},
            {'id': '1150', 'orientation': 'portrait'},
        ], [
            {'id': '1154', 'orientation': 'landscape'},  # audience reaction
        ],

        # reception part two - cake phase
        [
            {'id': '1167', 'orientation': 'portrait'},  # kids eating cake
            {'id': '1177', 'orientation': 'portrait'},  # dave and ann cake
        ], [
            {'id': '1170', 'orientation': 'landscape'},  # overall - closer
        ], [
            {'id': '1103', 'orientation': 'landscape'},  # pepper mingling
            {'id': '1165', 'orientation': 'portrait'},  # cooler sitter
        ], [
            {'id': '1226', 'orientation': 'portrait'},  # jenga
            {'id': '1207', 'orientation': 'portrait'},  # deb & greens cake
        ], [
            {'id': '1172', 'orientation': 'landscape'},  # overall - greenhouse
        ],

        # kubb
        [
            {'id': '1089', 'orientation': 'portrait'},  # setting
            {'id': '1212', 'orientation': 'portrait'},  # katur
        ], [
            {'id': '1192', 'orientation': 'portrait'},  # action A
            {'id': '1189', 'orientation': 'portrait'},  # action pepper
            {'id': '1230', 'orientation': 'portrait'},  # action B
        ],

        # frisbee / playing
        [
            {'id': '1204', 'orientation': 'landscape'},  # amy throwing
        ], [
            {'id': '1228', 'orientation': 'landscape'},  # guy throwing
        ], [
            {'id': '1235', 'orientation': 'portrait'},  # dad throwing
            {'id': '1248', 'orientation': 'portrait'},  # amy and kids
        ], [
            {'id': '1241', 'orientation': 'landscape'},  # action shot
        ],

        # reception part three - wind down
        [
            {'id': '1319', 'orientation': 'portrait'},  # suit jacket on shed
            {'id': '1240', 'orientation': 'portrait'},  # bros
        ], [
            {'id': '1221', 'orientation': 'landscape'},  # overall scene - late
        ], [
            {'id': '1243', 'orientation': 'portrait'},  # cute couple #1
            {'id': '1391', 'orientation': 'portrait'},  # maggie and kurt
        ],

        # epic couple - shed & solar
        [
            {'id': '1401', 'orientation': 'landscape'},  # tractor
            {'id': '1259', 'orientation': 'portrait'},
        ], [
            {'id': '1285', 'orientation': 'landscape'},
        ], [
            {'id': '1369', 'orientation': 'landscape'},
        ],

        # goodnight
        [
            {'id': '1393', 'orientation': 'portrait'},  # pepper and ben
            {'id': '1403', 'orientation': 'portrait'},  # with deb
        ], [
            {'id': '1364', 'orientation': 'landscape'},  # sunset
        ],
    ]

    return render_template('index.html', rows=rows, debug=DEBUG)


# init
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0')
