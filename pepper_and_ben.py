from flask import Flask
from flask import render_template
from localsettings import DEBUG

app = Flask(__name__)


# routes
# -----------------------------------------------------------------------------

@app.route('/')
def index_route(params={}):
    images = [
        # overall setting
        {'id': '6', 'orientation': 'landscape'},
        {'id': '10', 'orientation': 'portrait'},
        {'id': '12', 'orientation': 'portrait'},
        {'id': '18', 'orientation': 'portrait'},
        {'id': '21', 'orientation': 'portrait'},
        {'id': '23', 'orientation': 'portrait'},
        {'id': '27', 'orientation': 'landscape'},
        {'id': '31', 'orientation': 'portrait'},
        {'id': '37', 'orientation': 'portrait'},
        {'id': '39', 'orientation': 'landscape'},
        {'id': '311', 'orientation': 'landscape'},

        # pepper prep pre-dress
        {'id': '41', 'orientation': 'landscape'},
        {'id': '44', 'orientation': 'portrait'},
        {'id': '48', 'orientation': 'portrait'},
        {'id': '51', 'orientation': 'landscape'},
        {'id': '53', 'orientation': 'portrait'},
        {'id': '56', 'orientation': 'portrait'},
        {'id': '59', 'orientation': 'landscape'},
        {'id': '62', 'orientation': 'portrait'},
        {'id': '63', 'orientation': 'landscape'},
        {'id': '65', 'orientation': 'portrait'},
        {'id': '70', 'orientation': 'portrait'},
        {'id': '73', 'orientation': 'portrait'},
        {'id': '81', 'orientation': 'landscape'},

        # indoor prep
        {'id': '67', 'orientation': 'landscape'},
        {'id': '234', 'orientation': 'portrait'},

        # outdoor prep
        {'id': '83', 'orientation': 'portrait'},
        {'id': '86', 'orientation': 'portrait'},
        {'id': '87', 'orientation': 'landscape'},
        {'id': '149', 'orientation': 'portrait'},  # carrying flowers
        {'id': '323', 'orientation': 'portrait'},  # liz smiling

        # ben tie prep, and shoes
        {'id': '111', 'orientation': 'portrait'},
        {'id': '110', 'orientation': 'portrait'},
        {'id': '289', 'orientation': 'landscape'},

        # bubba and baby prep
        {'id': '122', 'orientation': 'portrait'},
        {'id': '124', 'orientation': 'portrait'},

        # pepper prep post-dress
        {'id': '167', 'orientation': 'landscape'},
        {'id': '173', 'orientation': 'portrait'},
        {'id': '175', 'orientation': 'portrait'},
        {'id': '176', 'orientation': 'portrait'},
        {'id': '177', 'orientation': 'portrait'},
        {'id': '180', 'orientation': 'portrait'},
        {'id': '181', 'orientation': 'portrait'},
        {'id': '184', 'orientation': 'landscape'},
        {'id': '191', 'orientation': 'portrait'},
        {'id': '196', 'orientation': 'landscape'},
        {'id': '220', 'orientation': 'portrait'},

        # ben reading prep
        {'id': '129', 'orientation': 'portrait'},
        {'id': '135', 'orientation': 'portrait'},
        {'id': '138', 'orientation': 'portrait'},
        {'id': '158', 'orientation': 'portrait'},

        # ceremony setting
        {'id': '102', 'orientation': 'portrait'},  # chairs
        {'id': '320', 'orientation': 'landscape'},  # old dog option A
        {'id': '153', 'orientation': 'portrait'},  # flowers still
        {'id': '334', 'orientation': 'landscape'},  # cello still

        # pepper champagne / dad
        {'id': '238', 'orientation': 'portrait'},
        {'id': '251', 'orientation': 'landscape'},
        {'id': '262', 'orientation': 'portrait'},
        {'id': '270', 'orientation': 'portrait'},
        {'id': '276', 'orientation': 'landscape'},

        # ben waiting
        {'id': '288', 'orientation': 'portrait'},
        {'id': '295', 'orientation': 'landscape'},

        # pinning flowers
        {'id': '340', 'orientation': 'portrait'},
        {'id': '345', 'orientation': 'landscape'},
        {'id': '351', 'orientation': 'portrait'},
        {'id': '356', 'orientation': 'portrait'},
        {'id': '361', 'orientation': 'portrait'},
        {'id': '366', 'orientation': 'landscape'},
        {'id': '374', 'orientation': 'landscape'},  # family pre-procession

        # audience waiting
        {'id': '339', 'orientation': 'landscape'},  # audience waiting
        {'id': '388', 'orientation': 'landscape'},  # audient waiting
        {'id': '393', 'orientation': 'landscape'},  # pitbull waiting

        # procession
        {'id': '397', 'orientation': 'portrait'},  # pepper first leg
        {'id': '401', 'orientation': 'landscape'},
        {'id': '407', 'orientation': 'landscape'},
        {'id': '412', 'orientation': 'portrait'},

        {'id': '418', 'orientation': 'landscape'},  # family processing
        {'id': '442', 'orientation': 'landscape'},  # dogs processing

        {'id': '423', 'orientation': 'portrait'},  # family sitting
        {'id': '424', 'orientation': 'portrait'},  # family sitting
        {'id': '425', 'orientation': 'portrait'},  # family sitting

        {'id': '436', 'orientation': 'portrait'},  # ben on stage
        {'id': '432', 'orientation': 'portrait'},  # pepper second leg
        {'id': '447', 'orientation': 'portrait'},  # dad delivery

        # ceremony - start
        {'id': '451', 'orientation': 'portrait'},
        {'id': '452', 'orientation': 'portrait'},
        {'id': '463', 'orientation': 'landscape'},

        # ceremony - amy
        {'id': '469', 'orientation': 'landscape'},
        {'id': '475', 'orientation': 'portrait'},
        {'id': '483', 'orientation': 'landscape'},

        # ceremony - liz
        {'id': '491', 'orientation': 'landscape'},
        {'id': '328', 'orientation': 'landscape'},  # liz playing (trick!)
        {'id': '490', 'orientation': 'portrait'},

        # ceremony - mom
        {'id': '506', 'orientation': 'landscape'},
        {'id': '520', 'orientation': 'portrait'},
        {'id': '524', 'orientation': 'portrait'},

        # ceremony - mike
        {'id': '540', 'orientation': 'portrait'},
        {'id': '560', 'orientation': 'landscape'},
        {'id': '567', 'orientation': 'landscape'},

        # ceremony - audience
        {'id': '576', 'orientation': 'landscape'},
        {'id': '577', 'orientation': 'landscape'},
        {'id': '579', 'orientation': 'landscape'},
        {'id': '580', 'orientation': 'landscape'},

        # ceremony - vows
        {'id': '586', 'orientation': 'landscape'},
        {'id': '589', 'orientation': 'portrait'},
        {'id': '605', 'orientation': 'portrait'},

        # ceremony - dogs
        {'id': '459', 'orientation': 'portrait'},
        {'id': '514', 'orientation': 'portrait'},
        {'id': '555', 'orientation': 'portrait'},
        {'id': '612', 'orientation': 'landscape'},
        {'id': '630', 'orientation': 'portrait'},
        {'id': '622', 'orientation': 'landscape'},

        # ceremony - rings
        {'id': '641', 'orientation': 'landscape'},
        {'id': '659', 'orientation': 'portrait'},
        {'id': '665', 'orientation': 'landscape'},

        # ceremony - kiss and exit
        {'id': '682', 'orientation': 'portrait'},
        {'id': '702', 'orientation': 'landscape'},
        {'id': '706', 'orientation': 'portrait'},
        {'id': '732', 'orientation': 'portrait'},
        {'id': '744', 'orientation': 'portrait'},
        {'id': '748', 'orientation': 'portrait'},
        {'id': '754', 'orientation': 'landscape'},
        {'id': '765', 'orientation': 'portrait'},

        # reception setting
        {'id': '90', 'orientation': 'landscape'},  # living room still
        {'id': '97', 'orientation': 'portrait'},  # plates
        {'id': '787', 'orientation': 'portrait'},  # solo chair
        {'id': '1074', 'orientation': 'portrait'},  # cake
        {'id': '1173', 'orientation': 'portrait'},  # lemonade
        {'id': '1209', 'orientation': 'landscape'},  # flowers
        {'id': '1319', 'orientation': 'portrait'},  # suit on shed

        # reception
        {'id': '789', 'orientation': 'landscape'},
        {'id': '785', 'orientation': 'portrait'},
        {'id': '791', 'orientation': 'portrait'},
        {'id': '795', 'orientation': 'landscape'},
        {'id': '800', 'orientation': 'portrait'},
        {'id': '803', 'orientation': 'portrait'},
        {'id': '806', 'orientation': 'landscape'},

        # formals
        {'id': '839', 'orientation': 'landscape'},
        {'id': '848', 'orientation': 'landscape'},
        {'id': '886', 'orientation': 'landscape'},
        {'id': '860', 'orientation': 'landscape'},
        {'id': '961', 'orientation': 'landscape'},
        {'id': '966', 'orientation': 'landscape'},
        {'id': '889', 'orientation': 'portrait'},
        {'id': '890', 'orientation': 'portrait'},
        {'id': '911', 'orientation': 'portrait'},
        {'id': '917', 'orientation': 'portrait'},
        {'id': '923', 'orientation': 'landscape'},
        {'id': '927', 'orientation': 'landscape'},

        # couple situations
        {'id': '934', 'orientation': 'portrait'},
        {'id': '939', 'orientation': 'landscape'},
        {'id': '948', 'orientation': 'landscape'},
        {'id': '977', 'orientation': 'portrait'},
        {'id': '994', 'orientation': 'landscape'},
        {'id': '995', 'orientation': 'landscape'},

        # reception
        {'id': '790', 'orientation': 'landscape'},  # overall scene, angled
        {'id': '1003', 'orientation': 'portrait'},  # overall scene, straight
        {'id': '1012', 'orientation': 'portrait'},
        {'id': '1018', 'orientation': 'portrait'},  # dancing

        # friend formals (greenhouse)
        {'id': '1054', 'orientation': 'landscape'},
        {'id': '1062', 'orientation': 'landscape'},
        {'id': '1078', 'orientation': 'landscape'},

        # reception
        {'id': '1088', 'orientation': 'landscape'},
        {'id': '1103', 'orientation': 'landscape'},

        # the actual rings
        {'id': '1091', 'orientation': 'portrait'},
        {'id': '1097', 'orientation': 'portrait'},
        {'id': '1111', 'orientation': 'portrait'},
        {'id': '1118', 'orientation': 'portrait'},

        # cake
        {'id': '1126', 'orientation': 'portrait'},
        {'id': '1143', 'orientation': 'landscape'},
        {'id': '1146', 'orientation': 'landscape'},
        {'id': '1150', 'orientation': 'portrait'},
        {'id': '1154', 'orientation': 'landscape'},
        {'id': '1167', 'orientation': 'portrait'},

        # reception
        {'id': '1165', 'orientation': 'portrait'},
        {'id': '1170', 'orientation': 'landscape'},
        {'id': '1172', 'orientation': 'landscape'},
        {'id': '1177', 'orientation': 'portrait'},

        # kubb
        {'id': '1089', 'orientation': 'portrait'},
        {'id': '1185', 'orientation': 'portrait'},
        {'id': '1189', 'orientation': 'portrait'},
        {'id': '1192', 'orientation': 'portrait'},
        {'id': '1212', 'orientation': 'portrait'},
        {'id': '1215', 'orientation': 'portrait'},
        {'id': '1219', 'orientation': 'portrait'},
        {'id': '1230', 'orientation': 'portrait'},

        {'id': '1226', 'orientation': 'portrait'},  # jenga

        # frisbee
        {'id': '1204', 'orientation': 'landscape'},
        {'id': '1228', 'orientation': 'landscape'},
        {'id': '1235', 'orientation': 'portrait'},
        {'id': '1241', 'orientation': 'landscape'},

        # reception
        {'id': '1248', 'orientation': 'portrait'},
        {'id': '1207', 'orientation': 'portrait'},
        {'id': '1211', 'orientation': 'landscape'},
        {'id': '1221', 'orientation': 'landscape'},
        {'id': '1240', 'orientation': 'portrait'},
        {'id': '1243', 'orientation': 'portrait'},
        {'id': '1391', 'orientation': 'portrait'},

        # shed & solar
        {'id': '1259', 'orientation': 'portrait'},
        {'id': '1285', 'orientation': 'landscape'},
        {'id': '1369', 'orientation': 'landscape'},

        {'id': '1401', 'orientation': 'landscape'},  # tractor
        {'id': '1393', 'orientation': 'portrait'},  # pepper and ben
        {'id': '1403', 'orientation': 'portrait'},  # with deb
        {'id': '1364', 'orientation': 'landscape'},  # sunset
    ]

    return render_template('index.html', images=images, debug=DEBUG)


# init
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0')
