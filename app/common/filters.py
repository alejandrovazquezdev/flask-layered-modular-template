"""
Custom Jinja2 filters for formatting datetime objects
"""


def format_datetime(value, format='short'):
    """
    Format a datetime object to string with specified format.
    
    Args:
        value: datetime object to format
        format: 'short' (dd/mm/yyyy) or 'full' (dd de mm de yyyy)
    
    Returns:
        Formatted datetime string
    """
    value_str = None
    if not value:
        value_str = ''
    elif format == 'short':
        value_str = value.strftime('%d/%m/%Y')
    elif format == 'full':
        value_str = value.strftime('%d de %m de %Y')
    else:
        value_str = ''
    return value_str
