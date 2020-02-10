from rest_framework.validators import ValidationError
import datetime
import dateutil.parser


def format_date(date_):
    try:
        dateutil.parser.parse(date_).date()
        try:
            datetime.datetime.strptime(date_, '%d/%m/%Y')
        except ValueError:
            raise ValidationError(
                'Invalid date. Date must be of the format DD/MM/YYYY')
    except ValueError:
        raise ValidationError(
            'Invalid date. Date must be of the format DD/MM/YYYY')

    date = date_.split("/")[::-1]
    date = datetime.date(int(date[0]), int(date[1]), int(date[2]))

    return date
