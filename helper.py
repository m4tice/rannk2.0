def export_to_txt(data):
    """
    export data to text file
    """

    with open('./generated-output.txt', 'w') as f:
        for idx, item in enumerate(data.items(), start=1):
            name, point, rank = item[0], item[1]['point'], item[1]['rank']

            # Decision for 'pts' or 'pt'
            pt = 'pt' if point == 1 else 'pts'

            # Forming line's content
            line = ("{}. {}, {} {}".format(rank, name, point, pt))
            f.write(line + '\n')
