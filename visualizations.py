import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib import patches


def parse_csv(filename):
    mat = []
    header = []
    names = []
    with open(filename, 'r') as f:
        i = 0
        for line in f:
            if i == 0:
                header = line[:-1].split(',')
            else:
                row = []
                args = line[:-1].split(',')
                names.append(args[0])
                for x in args[1:]:
                    if x == "NA":
                        row.append(x)
                    else:
                        row.append(int(x))
                mat.append(row)
            i += 1
    return mat, names, header


def bracket(data, brackets):
    brackets = sorted(brackets)
    new_data = []
    for row in data:
        new_row = []
        for x in row:
            if x == "NA":
                new_row.append(-1)
            else:
                b = 0
                done = False
                val = brackets[0]
                while not done and x > brackets[b]:
                    b += 1
                    if b == len(brackets):
                        val = brackets[len(brackets) - 1] + 1
                        done = True
                    else:
                        val = brackets[b]
                new_row.append(val)
        new_data.append(new_row)

    return new_data


def medals_chart(loc_ranks, names, header, display_values=False):
    data = np.array(bracket(loc_ranks, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

    # create discrete colormap
    cmap = colors.ListedColormap([(0.0, 0.0, 0.0), (1.0, 0.8, 0.0), (0.8, 0.8, 0.9), (0.8, 0.4, 0.0), (1.0, 1.0, 1.0)])
    bounds = [-2, 0, 1.5, 2.5, 3.5, 13]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap, norm=norm)

    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
    ax.set_xticks(np.arange(-0.5, len(header) - 0.5))
    ax.set_xticklabels(header[1:] + [""])
    ax.set_yticks(np.arange(-0.5, len(names) + 0.5))
    ax.set_yticklabels(names + [""])

    plt.setp(ax.xaxis.get_majorticklabels(), rotation=-45, ha="left")
    plt.setp(ax.yaxis.get_majorticklabels(), va="top")

    if display_values:
        for (i, j), z in np.ndenumerate(data):
            ax.text(j, i, '{}'.format(int(z)), ha='center', va='center')

    plt.title("Daily Local Leaderboard")

    plt.show()
    plt.close()


def globals_chart(glob_ranks, names, header):
    data = np.array(bracket(glob_ranks, [100, 200, 450, 1000, 2000, 4500, 10000]))

    # create discrete colormap
    color_list = [(0.0, 0.0, 0.0), (1.0, 1.0, 0.0),
                  (1.0, 0.4, 0.4), (1.0, 0.6, 0.6), (1.0, 0.8, 0.8),
                  (0.8, 0.8, 1.0), (0.6, 0.6, 1.0), (0.4, 0.4, 1.0),
                  (0.0, 0.0, 0.0)]
    cmap = colors.ListedColormap(color_list)
    bounds = [-2, 0, 101, 201, 451, 1001, 2001, 4501, 10001, 10002]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap, norm=norm)

    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
    ax.set_xticks(np.arange(-0.5, len(header) - 0.5))
    ax.set_xticklabels(header[1:] + [""])
    ax.set_yticks(np.arange(-0.5, len(names) + 0.5))
    ax.set_yticklabels(names + [""])

    plt.setp(ax.xaxis.get_majorticklabels(), rotation=-45, ha="left")
    plt.setp(ax.yaxis.get_majorticklabels(), va="top")

    patch_labels = ["1-100", "101-200", "201-450", "451-1000", "1001-2000", "2001-4500", "4501-10000"]
    patch_list = [patches.Patch(color=color_list[i], label=patch_labels[i - 1]) for i in range(1, len(color_list) - 1)]
    ax.legend(handles=patch_list, loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=len(patch_list))

    plt.title("Global Leaderboard Ranks")

    plt.show()
    plt.close()


def times_chart(time_ranks, names, header):
    data = np.array(bracket(time_ranks, [60, 150, 480, 1200, 3600, 9000, 28800]))

    # create discrete colormap
    color_list = [(0.0, 0.0, 0.0), (0.95, 0.95, 1.0),
                  (0.75, 0.75, 1.0), (0.6, 0.6, 0.95), (0.45, 0.45, 0.9),
                  (0.3, 0.3, 0.85), (0.15, 0.15, 0.75), (0.0, 0.0, 0.6),
                  (0.0, 0.0, 0.0)]
    cmap = colors.ListedColormap(color_list)
    bounds = [-2, 0, 61, 151, 481, 1201, 3601, 9001, 28801, 28802]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap, norm=norm)

    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
    ax.set_xticks(np.arange(-0.5, len(header) - 0.5))
    ax.set_xticklabels(header[1:] + [""])
    ax.set_yticks(np.arange(-0.5, len(names) + 0.5))
    ax.set_yticklabels(names + [""])

    plt.setp(ax.xaxis.get_majorticklabels(), rotation=-45, ha="left")
    plt.setp(ax.yaxis.get_majorticklabels(), va="top")

    patch_labels = ["<1m", "1m-2.5m", "2.5m-8m", "8m-20m", "20m-1h", "1h-2.5h", "2.5h-8h"]
    patch_list = [patches.Patch(color=color_list[i], label=patch_labels[i - 1]) for i in range(1, len(color_list) - 1)]
    ax.legend(handles=patch_list, loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=len(patch_list))

    plt.title("Time Taken Per Problem")

    plt.show()
    plt.close()


def cumul_score(loc_ranks, names, header, num_lead=-1):
    if num_lead == -1:
        num_lead = len(names)
    cumul_points = [[0, 0, 0] for _ in range(len(names))]
    for day in range(2, 50):
        for i in range(len(names)):
            new_points = 0
            if loc_ranks[i][day] != "NA":
                new_points = num_lead + 1 - loc_ranks[i][day]
            cumul_points[i].append(cumul_points[i][day] + new_points)

    lines = [[] for _ in range(len(names))]
    for day in range(len(cumul_points[0])):
        day_scores = []
        for i in range(len(cumul_points)):
            day_scores.append((i, cumul_points[i][day]))
        day_scores = sorted(day_scores, key=lambda tup: tup[1], reverse=True)
        day_ranks = dict()

        rank = 1
        for key, score in day_scores:
            day_ranks[key] = rank
            rank += 1

        for i in range(len(lines)):
            lines[i].append(day_ranks[i])

    cumul_ranks = np.array(lines).T
    handles = plt.plot(cumul_ranks[3:,])

    plt.legend(handles=handles, labels=names)
    plt.gca().invert_yaxis()

    plt.xlabel("Problem")
    plt.ylabel("Placing")

    plt.title("Private Leaderboard Placings Per Day")

    plt.show()
    plt.close()


if __name__ == "__main__":
    glob_ranks, names, header = parse_csv("./friend_stats/global_ranks.csv")
    loc_ranks, _, _ = parse_csv("./friend_stats/local_ranks.csv")
    time_ranks, _, _ = parse_csv("./friend_stats/times.csv")

    medals = bracket(loc_ranks, [1, 2, 3])

    medals_chart(loc_ranks, names, header)
    medals_chart(loc_ranks, names, header, display_values=True)
    globals_chart(glob_ranks, names, header)
    times_chart(time_ranks, names, header)
    cumul_score(loc_ranks, names, header, 15)

