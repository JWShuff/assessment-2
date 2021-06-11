from modules.interface import Interface

blockbuster = Interface()
blockbuster.run()

"""
Dev Notes:
Adjusted customers.csv so that current_video_rentals has a leading "/" on
every video. Assists in determining rental counts, and will aid in an
eventual refactor to have video objects move between inventory and attached
to customer objects in an upcoming development cycle.
"""