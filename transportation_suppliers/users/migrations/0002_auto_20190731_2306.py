# Generated by Django 2.2.3 on 2019-07-31 23:06

import django.core.validators
from django.db import migrations, models
import transportation_suppliers.users.utils


class Migration(migrations.Migration):

    dependencies = [("users", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "address1",
                    models.CharField(
                        help_text="Input address location.",
                        max_length=255,
                        verbose_name="address1",
                    ),
                ),
                (
                    "address2",
                    models.CharField(
                        blank=True,
                        help_text="Input address location if another exists here.",
                        max_length=255,
                        verbose_name="address2",
                    ),
                ),
                (
                    "area",
                    models.CharField(
                        blank=True,
                        help_text="Input area.",
                        max_length=255,
                        verbose_name="area",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        help_text="Input city.",
                        max_length=255,
                        verbose_name="city",
                    ),
                ),
                (
                    "county",
                    models.CharField(
                        blank=True,
                        help_text="Input county.",
                        max_length=255,
                        verbose_name="county",
                    ),
                ),
                (
                    "postcode",
                    models.CharField(
                        help_text="Input postcode.",
                        max_length=255,
                        verbose_name="postcode",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("GB", "United Kingdom"),
                            ("AF", "Afghanistan"),
                            ("AX", "Aland Islands"),
                            ("AL", "Albania"),
                            ("DZ", "Algeria"),
                            ("AS", "American Samoa"),
                            ("AD", "Andorra"),
                            ("AO", "Angola"),
                            ("AI", "Anguilla"),
                            ("AQ", "Antarctica"),
                            ("AG", "Antigua and Barbuda"),
                            ("AR", "Argentina"),
                            ("AM", "Armenia"),
                            ("AW", "Aruba"),
                            ("AU", "Australia"),
                            ("AT", "Austria"),
                            ("AZ", "Azerbaijan"),
                            ("BS", "Bahamas"),
                            ("BH", "Bahrain"),
                            ("BD", "Bangladesh"),
                            ("BB", "Barbados"),
                            ("BY", "Belarus"),
                            ("BE", "Belgium"),
                            ("BZ", "Belize"),
                            ("BJ", "Benin"),
                            ("BM", "Bermuda"),
                            ("BT", "Bhutan"),
                            ("BO", "Bolivia"),
                            ("BA", "Bosnia and Herzegovina"),
                            ("BW", "Botswana"),
                            ("BV", "Bouvet Island"),
                            ("BR", "Brazil"),
                            ("IO", "British Indian Ocean Territory"),
                            ("BN", "Brunei Darussalam"),
                            ("BG", "Bulgaria"),
                            ("BF", "Burkina Faso"),
                            ("BI", "Burundi"),
                            ("KH", "Cambodia"),
                            ("CM", "Cameroon"),
                            ("CA", "Canada"),
                            ("CV", "Cape Verde"),
                            ("KY", "Cayman Islands"),
                            ("CF", "Central African Republic"),
                            ("TD", "Chad"),
                            ("CL", "Chile"),
                            ("CN", "China"),
                            ("CX", "Christmas Island"),
                            ("CC", "Cocos (Keeling) Islands"),
                            ("CO", "Colombia"),
                            ("KM", "Comoros"),
                            ("CG", "Congo"),
                            ("CD", "Congo, The Democratic Republic of the"),
                            ("CK", "Cook Islands"),
                            ("CR", "Costa Rica"),
                            ("CI", "Cote d'Ivoire"),
                            ("HR", "Croatia"),
                            ("CU", "Cuba"),
                            ("CY", "Cyprus"),
                            ("CZ", "Czech Republic"),
                            ("DK", "Denmark"),
                            ("DJ", "Djibouti"),
                            ("DM", "Dominica"),
                            ("DO", "Dominican Republic"),
                            ("EC", "Ecuador"),
                            ("EG", "Egypt"),
                            ("SV", "El Salvador"),
                            ("GQ", "Equatorial Guinea"),
                            ("ER", "Eritrea"),
                            ("EE", "Estonia"),
                            ("ET", "Ethiopia"),
                            ("FK", "Falkland Islands (Malvinas)"),
                            ("FO", "Faroe Islands"),
                            ("FJ", "Fiji"),
                            ("FI", "Finland"),
                            ("FR", "France"),
                            ("GF", "French Guiana"),
                            ("PF", "French Polynesia"),
                            ("TF", "French Southern Territories"),
                            ("GA", "Gabon"),
                            ("GM", "Gambia"),
                            ("GE", "Georgia"),
                            ("DE", "Germany"),
                            ("GH", "Ghana"),
                            ("GI", "Gibraltar"),
                            ("GR", "Greece"),
                            ("GL", "Greenland"),
                            ("GD", "Grenada"),
                            ("GP", "Guadeloupe"),
                            ("GU", "Guam"),
                            ("GT", "Guatemala"),
                            ("GG", "Guernsey"),
                            ("GN", "Guinea"),
                            ("GW", "Guinea-Bissau"),
                            ("GY", "Guyana"),
                            ("HT", "Haiti"),
                            ("HM", "Heard Island and McDonald Islands"),
                            ("VA", "Holy See (Vatican City State)"),
                            ("HN", "Honduras"),
                            ("HK", "Hong Kong"),
                            ("HU", "Hungary"),
                            ("IS", "Iceland"),
                            ("IN", "India"),
                            ("ID", "Indonesia"),
                            ("IR", "Iran, Islamic Republic of"),
                            ("IQ", "Iraq"),
                            ("IE", "Ireland"),
                            ("IM", "Isle of Man"),
                            ("IL", "Israel"),
                            ("IT", "Italy"),
                            ("JM", "Jamaica"),
                            ("JP", "Japan"),
                            ("JE", "Jersey"),
                            ("JO", "Jordan"),
                            ("KZ", "Kazakhstan"),
                            ("KE", "Kenya"),
                            ("KI", "Kiribati"),
                            ("KP", "Korea, Democratic People's Republic of"),
                            ("KR", "Korea, Republic of"),
                            ("KW", "Kuwait"),
                            ("KG", "Kyrgyzstan"),
                            ("LA", "Lao People's Democratic Republic"),
                            ("LV", "Latvia"),
                            ("LB", "Lebanon"),
                            ("LS", "Lesotho"),
                            ("LR", "Liberia"),
                            ("LY", "Libyan Arab Jamahiriya"),
                            ("LI", "Liechtenstein"),
                            ("LT", "Lithuania"),
                            ("LU", "Luxembourg"),
                            ("MO", "Macao"),
                            (
                                "MK",
                                "Macedonia, The Former Yugoslav Republic of",
                            ),
                            ("MG", "Madagascar"),
                            ("MW", "Malawi"),
                            ("MY", "Malaysia"),
                            ("MV", "Maldives"),
                            ("ML", "Mali"),
                            ("MT", "Malta"),
                            ("MH", "Marshall Islands"),
                            ("MQ", "Martinique"),
                            ("MR", "Mauritania"),
                            ("MU", "Mauritius"),
                            ("YT", "Mayotte"),
                            ("MX", "Mexico"),
                            ("FM", "Micronesia, Federated States of"),
                            ("MD", "Moldova"),
                            ("MC", "Monaco"),
                            ("MN", "Mongolia"),
                            ("ME", "Montenegro"),
                            ("MS", "Montserrat"),
                            ("MA", "Morocco"),
                            ("MZ", "Mozambique"),
                            ("MM", "Myanmar"),
                            ("NA", "Namibia"),
                            ("NR", "Nauru"),
                            ("NP", "Nepal"),
                            ("NL", "Netherlands"),
                            ("AN", "Netherlands Antilles"),
                            ("NC", "New Caledonia"),
                            ("NZ", "New Zealand"),
                            ("NI", "Nicaragua"),
                            ("NE", "Niger"),
                            ("NG", "Nigeria"),
                            ("NU", "Niue"),
                            ("NF", "Norfolk Island"),
                            ("MP", "Northern Mariana Islands"),
                            ("NO", "Norway"),
                            ("OM", "Oman"),
                            ("PK", "Pakistan"),
                            ("PW", "Palau"),
                            ("PS", "Palestinian Territory, Occupied"),
                            ("PA", "Panama"),
                            ("PG", "Papua New Guinea"),
                            ("PY", "Paraguay"),
                            ("PE", "Peru"),
                            ("PH", "Philippines"),
                            ("PN", "Pitcairn"),
                            ("PL", "Poland"),
                            ("PT", "Portugal"),
                            ("PR", "Puerto Rico"),
                            ("QA", "Qatar"),
                            ("RE", "Reunion"),
                            ("RO", "Romania"),
                            ("RU", "Russian Federation"),
                            ("RW", "Rwanda"),
                            ("BL", "Saint Barthelemy"),
                            ("SH", "Saint Helena"),
                            ("KN", "Saint Kitts and Nevis"),
                            ("LC", "Saint Lucia"),
                            ("MF", "Saint Martin"),
                            ("PM", "Saint Pierre and Miquelon"),
                            ("VC", "Saint Vincent and the Grenadines"),
                            ("WS", "Samoa"),
                            ("SM", "San Marino"),
                            ("ST", "Sao Tome and Principe"),
                            ("SA", "Saudi Arabia"),
                            ("SN", "Senegal"),
                            ("RS", "Serbia"),
                            ("SC", "Seychelles"),
                            ("SL", "Sierra Leone"),
                            ("SG", "Singapore"),
                            ("SK", "Slovakia"),
                            ("SI", "Slovenia"),
                            ("SB", "Solomon Islands"),
                            ("SO", "Somalia"),
                            ("ZA", "South Africa"),
                            (
                                "GS",
                                "South Georgia and the South Sandwich Islands",
                            ),
                            ("ES", "Spain"),
                            ("LK", "Sri Lanka"),
                            ("SD", "Sudan"),
                            ("SR", "Suriname"),
                            ("SJ", "Svalbard and Jan Mayen"),
                            ("SZ", "Swaziland"),
                            ("SE", "Sweden"),
                            ("CH", "Switzerland"),
                            ("SY", "Syrian Arab Republic"),
                            ("TW", "Taiwan, Province of China"),
                            ("TJ", "Tajikistan"),
                            ("TZ", "Tanzania, United Republic of"),
                            ("TH", "Thailand"),
                            ("TL", "Timor-Leste"),
                            ("TG", "Togo"),
                            ("TK", "Tokelau"),
                            ("TO", "Tonga"),
                            ("TT", "Trinidad and Tobago"),
                            ("TN", "Tunisia"),
                            ("TR", "Turkey"),
                            ("TM", "Turkmenistan"),
                            ("TC", "Turks and Caicos Islands"),
                            ("TV", "Tuvalu"),
                            ("UG", "Uganda"),
                            ("UA", "Ukraine"),
                            ("AE", "United Arab Emirates"),
                            ("US", "United States"),
                            ("UM", "United States Minor Outlying Islands"),
                            ("UY", "Uruguay"),
                            ("UZ", "Uzbekistan"),
                            ("VU", "Vanuatu"),
                            ("VE", "Venezuela"),
                            ("VN", "Viet Nam"),
                            ("VG", "Virgin Islands, British"),
                            ("VI", "Virgin Islands, U.S."),
                            ("WF", "Wallis and Futuna"),
                            ("EH", "Western Sahara"),
                            ("YE", "Yemen"),
                            ("ZM", "Zambia"),
                            ("ZW", "Zimbabwe"),
                        ],
                        help_text="Input country.",
                        max_length=255,
                        verbose_name="country",
                    ),
                ),
            ],
            options={
                "verbose_name": "address",
                "verbose_name_plural": "addresses",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Upload user avatar here.",
                upload_to=transportation_suppliers.users.utils.user_avatar_path,
                verbose_name="avatar",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.CharField(
                blank=True,
                help_text="Enter user description here (Min 500 characters).",
                max_length=500,
                verbose_name="bio",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="date_of_birth",
            field=models.DateField(
                blank=True,
                help_text="Enter date of birth here.",
                null=True,
                verbose_name="date of birth",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[
                    ("male", "Male"),
                    ("female", "Female"),
                    ("other", "Other"),
                ],
                help_text="Enter gender of user here.",
                max_length=10,
                verbose_name="gender",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="mobile",
            field=models.CharField(
                blank=True,
                help_text="Enter mobile phone details here.",
                max_length=12,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone Number must be entered in the format: '9999999999' or '999-999-9999'.",
                        regex="(\\d{3})\\D*(\\d{4}|\\d{3})\\D*(\\d{4}|\\d{3})$",
                    )
                ],
                verbose_name="mobile phone number",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_home",
            field=models.CharField(
                blank=True,
                help_text="Enter home phone details here.",
                max_length=12,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone Number must be entered in the format: '9999999999' or '999-999-9999'.",
                        regex="(\\d{3})\\D*(\\d{4}|\\d{3})\\D*(\\d{4}|\\d{3})$",
                    )
                ],
                verbose_name="home phone",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_work",
            field=models.CharField(
                blank=True,
                help_text="Enter work phone details here.",
                max_length=12,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone Number must be entered in the format: '9999999999' or '999-999-9999'.",
                        regex="(\\d{3})\\D*(\\d{4}|\\d{3})\\D*(\\d{4}|\\d{3})$",
                    )
                ],
                verbose_name="work phone",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="salutation",
            field=models.CharField(
                blank=True,
                choices=[
                    ("mr", "MR"),
                    ("mrs", "MRS"),
                    ("miss", "MISS"),
                    ("dr", "DR"),
                    ("prof", "PROF"),
                ],
                help_text="Enter user title here.",
                max_length=10,
                verbose_name="salutation",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Enter full name of user.",
                max_length=255,
                verbose_name="Name of User",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="addresses",
            field=models.ManyToManyField(
                help_text="Select addresses of the user.",
                related_name="address_users",
                to="users.Address",
                verbose_name="addresses",
            ),
        ),
    ]
