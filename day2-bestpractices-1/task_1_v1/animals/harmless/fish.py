class Fish:
    def __init__(self):
        """Constructor for this class"""
        # Create some member fish
        self.members = ['Salmon', 'Barb','Catfish']

    def printMembers(self):
        print('Printing members of the fish class')
        for member in self.members:
            print('\t%s' % member)
