import dateutil.parser as parser


def validate_date(date_to_validate: str) -> str:
    try:
        return str(parser.parse(date_to_validate, yearfirst=True).date())
    except ValueError:
        print("Invalid date format; Date will be set ad default 2001-01-01")
        return "2001-01-01"
