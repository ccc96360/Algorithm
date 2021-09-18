from bisect import bisect_left

languages = ["cpp", "java", "python"]
groups = ["backend", "frontend"]
careers = ["junior", "senior"]
foods = ["chicken", "pizza"]
def execQurey(lang, group, career, food, score, info, size):
    ret = 0
    for l in lang:
        for g in group:
            for c in career:
                for f in food:
                    # print(l,g,c,f,score, size[l][g][c][f], bisect_left(info[l][g][c][f], score))
                    ret += size[l][g][c][f] - bisect_left(info[l][g][c][f], score)
    return ret

def sort(lang, group, career, food, info):
    for l in lang:
        for g in group:
            for c in career:
                for f in food:
                    info[l][g][c][f].sort()
def solution(info, query):
    answer = []
    information = {lang : {g : {c : {f : [] for f in foods} for c in careers} for g in groups} for lang in languages}
    size = {lang : {g : {c : {f : 0 for f in foods} for c in careers} for g in groups} for lang in languages}
    for v in info:
        lang, group, career, food, score = v.split()
        information[lang][group][career][food].append(int(score))
        size[lang][group][career][food] += 1
    sort(languages, groups, careers, foods, information)
    for q in query:
        # print("====={0}=====".format(q))
        li = list(map(lambda x: str(x).strip(), q.split("and")))
        li.extend(li.pop().split())

        lang, group, career, food, score = li
        lang = [lang] if lang != "-" else languages
        group = [group] if group != "-" else groups
        career = [career] if career != "-" else careers
        food = [food] if food != "-" else foods

        answer.append(execQurey(lang, group, career, food, int(score), information, size))
    return answer
def main():
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))
if __name__ == '__main__':
    main()