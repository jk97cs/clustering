while len(set(random_med) & set(tmp_med)) < num_medoids:
    tmp_med = random_med[:]

    m = 0
    clusters = [[] for i in range(num_medoids)]
    for j in tmp_med:
        clusters[m].append(j)
        m += 1

    for j in data.keys():
        if j not in tmp_med:
            tmp_dist = sys.maxsize
            tmp_k = 0
            for k in range(num_medoids):
                dist = distances[clusters[k][0], j]
                if dist < tmp_dist:
                    tmp_dist = dist
                    tmp_k = k
            clusters[tmp_k].append(j)

    for j in range(len(clusters)):
        tmp_dist = sys.maxsize
        tmp_m = 0
        for m in range(len(clusters[j])):
            dist = 0
            for n in range(len(clusters[j])):
                if m != n:
                    dist += distances[clusters[j][m], clusters[j][n]]
            if dist < tmp_dist:
                tmp_dist = dist
                tmp_m = m
        random_med[j] = clusters[j][tmp_m]