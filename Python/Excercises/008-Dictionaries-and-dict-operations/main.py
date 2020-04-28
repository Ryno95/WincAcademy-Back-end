from datetime import date

all_countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "American Samoa",
    "Andorra",
    "Angola",
    "Anguilla",
    "Antarctica",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Aruba",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bermuda",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Bouvet Island",
    "Brazil",
    "British Indian Ocean Territory",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Cayman Islands",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Christmas Island",
    "Cocos (Keeling) Islands",
    "Colombia",
    "Comoros",
    "Congo",
    "The Democratic Republic of Congo",
    "Cook Islands",
    "Costa Rica",
    "Ivory Coast",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor",
    "Ecuador",
    "Egypt",
    "England",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Falkland Islands",
    "Faroe Islands",
    "Fiji Islands",
    "Finland",
    "France",
    "French Guiana",
    "French Polynesia",
    "French Southern territories",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Gibraltar",
    "Greece",
    "Greenland",
    "Grenada",
    "Guadeloupe",
    "Guam",
    "Guatemala",
    "Guernsey",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Heard Island and McDonald Islands",
    "Holy See (Vatican City State)",
    "Honduras",
    "Hong Kong",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Isle of Man",
    "Italy",
    "Jamaica",
    "Japan",
    "Jersey",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libyan Arab Jamahiriya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macao",
    "North Macedonia",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Martinique",
    "Mauritania",
    "Mauritius",
    "Mayotte",
    "Mexico",
    "Micronesia, Federated States of",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montserrat",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "Netherlands Antilles",
    "New Caledonia",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Niue",
    "Norfolk Island",
    "North Korea",
    "Northern Ireland",
    "Northern Mariana Islands",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Pitcairn",
    "Poland",
    "Portugal",
    "Puerto Rico",
    "Qatar",
    "Reunion",
    "Romania",
    "Russian Federation",
    "Rwanda",
    "Saint Helena",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Pierre and Miquelon",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Scotland",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Georgia and the South Sandwich Islands",
    "South Korea",
    "South Sudan",
    "Spain",
    "SriLanka",
    "Sudan",
    "Suriname",
    "Svalbard and Jan Mayen",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Timor-Leste",
    "Togo",
    "Tokelau",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Turks and Caicos Islands",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "United States Minor Outlying Islands",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Venezuela",
    "Vietnam",
    "Virgin Islands, British",
    "Virgin Islands, U.S.",
    "Wales",
    "Wallis and Futuna",
    "Western Sahara",
    "Yemen",
    "Yugoslavia",
    "Zambia",
    "Zimbabwe",
]

commonwealth_states = [
    "Antigua and Barbuda",
    "Australia",
    "Bahamas",
    "Bangladesh",
    "Barbados",
    "Belize",
    "Botswana",
    "Brunei",
    "Cameroon",
    "Canada",
    "Cyprus",
    "Dominica",
    "Eswatini",
    "Fiji",
    "Gambia",
    "Ghana",
    "Grenada",
    "Guyana",
    "India",
    "Jamaica",
    "Kenya",
    "Kiribati",
    "Lesotho",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Malta",
    "Mauritius",
    "Mozambique",
    "Namibia",
    "Nauru",
    "New Zealand",
    "Nigeria",
    "Pakistan",
    "Papua New Guinea",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Solomon Islands",
    "South Africa",
    "Sri Lanka",
    "Tanzania",
    "Tonga",
    "Trinidad and Tobago",
    "Tuvalu",
    "Uganda",
    "United Kingdom",
    "Vanuatu",
    "Zambia",
]
# 1

myPassport = {
    "Photo": "passportphoto.png",
    "Name": "Janus",
    "Surname": "Adrianus",
    "Birthdate": date(1980, 2, 4),
    "Birthplace": "Verwoerdburg",
    "Sex": "Male",
    "Length": 1.81,
    "Signature": "signature.png",
    "Passportnumber": 9402826493,
    "Nationality": "South Africa",
    "Fingerprint": ["fingerprint_001.png", "fingerprint_002.png"],
}

birthDate = myPassport["Birthdate"]
length = myPassport["Length"]
birthPlace = myPassport["Birthplace"]
print("birthDate: ", birthDate, "length: ", length, "birthPlace: ", birthPlace)


# 2
indexOfChina = all_countries.index("China")
# print(indexOfChina)
yourPassport = {}
yourPassport["Photo"] = "yourpassportphoto.png"
yourPassport["Name"] = "Wuhanna"
yourPassport["Surname"] = "Johnson"
yourPassport["Birthdate"] = date(2019, 12, 28)
yourPassport["Birthplace"] = "China"
yourPassport["Sex"] = "Female"
yourPassport["Length"] = 1.69
yourPassport["Signature"] = "yoursignature.png"
yourPassport["Passportnumber"] = 7385627482
yourPassport["Nationality"] = all_countries[indexOfChina]
yourPassport["Fingerprint"] = ["yourfingerprint_001.png", "yourfingerprint_002.png"]
# print(yourPassport)


# 3
randomPassport = {
    "Photo": "randompassportphoto.png",
    "Name": "Janus",
    "Surname": "Adrianus",
    "Birthdate": date(1990, 2, 4),
    "Birthplace": "Verwoerdburg",
    "Sex": "Male",
    "Length": 1.81,
    "Signature": "randomsignature.png",
    "Passportnumber": 9402826493,
    "Nationality": "South Africa",
    "Fingerprint": ["randomfingerprint_001.png", "randomfingerprint_002.png"],
}

today = date.today()
ageRestriction = "You are not older than 18"
countryRestriction = "You are not part of the common wealth"
errorMessage = "You cannot edit you passport because: "

if (
    today.year - randomPassport["Birthdate"].year >= 18
    and randomPassport["Nationality"] in commonwealth_states
):
    print("You can edit your passport: ")
    randomPassport["Nationality"] = "Canada"
    randomPassport["Photo"] = input("Please add your new photo here: ")
    randomPassport["Fingerprint"] = randomPassport["Fingerprint"] * 5
    # print(randomPassport)
elif today.year - randomPassport["Birthdate"].year <= 18:
    print(errorMessage + ageRestriction)
else:
    print(errorMessage + countryRestriction)