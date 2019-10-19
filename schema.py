# Keep all sample schema in one place

# This is the dress collection
sample_dress = {
    'dressnumber': 1,
    'type': 'jeans',
    'color': 'green',
    'fabric': 'denims',
    'store': 'macys',              
    'datebought': '10/19/2019',      # Date on which it was bought
    'pictures': ['a', 'b']           # These will be image URL
}

# These are the comments
comments = {
    'dressnumber': 1,
    'date': '10/10/2019',
    'userid': 'rina',
    'comment': 'whatever'
    'pictures':
}

# Transaction keeps track of history - who borrowed/worn the dress
transactions = {
    'userid':
    'date':
    'action':
    'action':  It can be borrowed/returned/retired
    'counterparty':  who is the other userid 
}