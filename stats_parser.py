from datetime import datetime
import glob, os
import time


def parse_file(filename):
    lines = dict()
    with open(filename, 'r') as f:
        i = 0
        for line in f:
            if i < 2:
                i += 1
                continue
            args = line[:-1].split()
            day = int(args[0])
            lines[day] = args[1:]
            i += 1
    return lines


def get_order(names, stats):
    places = len(names) + 1
    local_points = {name: 0 for name in names}
    for day in range(1, 26):
        day_scores_a = []
        day_scores_b = []
        for key in names:
            if day in stats[key]:
                r1 = int(stats[key][day][1])
                day_scores_a.append((key, r1))
                if stats[key][day][4] != '-':
                    r2 = int(stats[key][day][4])
                    day_scores_b.append((key, r2))
        day_scores_a = sorted(day_scores_a, key=lambda tup: tup[1])
        day_scores_b = sorted(day_scores_b, key=lambda tup: tup[1])
        day_ranks_a = dict()
        day_ranks_b = dict()

        rank = 1
        for key, score in day_scores_a:
            day_ranks_a[key] = rank
            local_points[key] += places - rank
            rank += 1
        rank = 1
        for key, score in day_scores_b:
            day_ranks_b[key] = rank
            local_points[key] += places - rank
            rank += 1

    order = sorted(local_points, key=local_points.get, reverse=True)
    return order


def gen_global_ranks(order, stats, filename):
    header = "Name"
    for day in range(1, 26):
        header = "{},{}{},{}{}".format(header, day, "a", day, "b")
    header = "{}\n".format(header)
    lines = [header]
    for key in order:
        line = key
        for day in range(1, 26):
            r1 = "NA"
            r2 = "NA"
            if day in stats[key]:
                r1 = int(stats[key][day][1])
                if stats[key][day][4] != '-':
                    r2 = int(stats[key][day][4])
            line = "{},{},{}".format(line, r1, r2)
        line = "{}\n".format(line)
        lines.append(line)

    with open(filename, 'w') as f:
        f.writelines(lines)


def gen_local_ranks(order, stats, filename):
    lines = ["{}".format(key) for key in order]
    for day in range(1, 26):
        day_scores_a = []
        day_scores_b = []
        for key in order:
            if day in stats[key]:
                r1 = int(stats[key][day][1])
                day_scores_a.append((key, r1))
                if stats[key][day][4] != '-':
                    r2 = int(stats[key][day][4])
                    day_scores_b.append((key, r2))
        day_scores_a = sorted(day_scores_a, key=lambda tup: tup[1])
        day_scores_b = sorted(day_scores_b, key=lambda tup: tup[1])
        day_ranks_a = dict()
        day_ranks_b = dict()

        rank = 1
        for key, score in day_scores_a:
            day_ranks_a[key] = rank
            rank += 1
        rank = 1
        for key, score in day_scores_b:
            day_ranks_b[key] = rank
            rank += 1

        for i in range(len(lines)):
            name = order[i]
            s1 = "NA"
            s2 = "NA"
            if name in day_ranks_a:
                s1 = day_ranks_a[name]
            if name in day_ranks_b:
                s2 = day_ranks_b[name]
            lines[i] = "{},{},{}".format(lines[i], s1, s2)

    for i in range(len(lines)):
        lines[i] = "{}\n".format(lines[i])

    header = "Name"
    for day in range(1, 26):
        header = "{},{}{},{}{}".format(header, day, "a", day, "b")
    header = "{}\n".format(header)
    lines.insert(0, header)

    with open(filename, 'w') as f:
        f.writelines(lines)


def gen_times(order, stats, filename):
    header = "Name"
    for day in range(1, 26):
        header = "{},{}{},{}{}".format(header, day, "a", day, "b")
    header = "{}\n".format(header)
    lines = [header]
    for key in order:
        line = key
        for day in range(1, 26):
            r1 = "NA"
            r2 = "NA"
            if day in stats[key]:
                r1 = stats[key][day][0]
                if r1[0] != '>':
                    dt = datetime.strptime(r1, "%H:%M:%S")
                    r1 = int(dt.hour * 3600 + dt.minute * 60 + dt.second)
                else:
                    r1 = "NA"
                if stats[key][day][3] != '-':
                    r2 = stats[key][day][3]
                    if r2[0] != '>':
                        dt = datetime.strptime(r2, "%H:%M:%S")
                        r2 = int(dt.hour * 3600 + dt.minute * 60 + dt.second) - r1
                    else:
                        r2 = "NA"
            line = "{},{},{}".format(line, r1, r2)
        line = "{}\n".format(line)
        lines.append(line)

    with open(filename, 'w') as f:
        f.writelines(lines)


if __name__ == "__main__":
    stats = dict()
    names = []
    os.chdir("./friend_stats")
    for file in glob.glob("*.txt"):
        name = file[:-4]
        names.append(name)
        lines = parse_file(file)
        stats[name] = lines

    order = get_order(names, stats)

    gen_global_ranks(order, stats, "global_ranks.csv")
    gen_local_ranks(order, stats, "local_ranks.csv")
    gen_times(order, stats, "times.csv")
