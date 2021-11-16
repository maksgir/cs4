class WithoutLibs:
    def __init__(self, n):
        self.YAML = "data/tt.yaml"
        self.XML_f = f"out/1{n}.xml"
        self.a = []

    def yaml_reader(self, f):
        with open(f) as f:
            data = f.read().splitlines()
            return data

    def count_spaces(self, s):
        c = 0
        for x in list(s):
            if x == ' ':
                c += 1
            else:
                break
        return c

    def search_key(self, s):
        s = s.replace(' ', '')
        s = s.replace('-', '')
        return s.split(':')[0], s.split(':')[1]

    def find_max_space(self, data):
        m = -1
        for s in data:
            c = self.count_spaces(s)
            if c > m:
                m = c
        return m

    def into_xml(self, data, file):
        f = open(file, 'w')
        for i in data:
            f.write(i + '\n')
        f.close()

    def go(self):
        data = self.yaml_reader(self.YAML)

        count = int(self.find_max_space(data) / 4)

        for i in range(count + 2):
            self.a.append([])

        history_of_keys = ''
        sp = 0
        flag = False
        for i, s in enumerate(data):
            if ":" in s:
                cur_key, ans = self.search_key(s)

                group = history_of_keys.count('---')
                # print(group)
                if history_of_keys != '':
                    history_of_keys += f'---{cur_key}'
                else:
                    history_of_keys = cur_key
                c_sp = self.count_spaces(s)

                g = int(c_sp / 4)
                self.a[g].append(history_of_keys)
                if ans != '':
                    history_of_keys += f'---{ans}'
                    self.a[g + 1].append(history_of_keys)
                    answer_was = True
                next_s_exist = False
                for j, st in enumerate(data[i + 1:]):
                    if st != '':
                        next_sp = self.count_spaces(st)
                        next_s_exist = True
                        break
                if next_s_exist:
                    hell = history_of_keys.split('---')
                    if c_sp == next_sp:
                        if answer_was:
                            hell = hell[:-2]
                        else:
                            hell = hell[:-1]
                    elif c_sp > next_sp:
                        r = int((c_sp - next_sp) / 4)
                        if answer_was:
                            new = 2
                        else:
                            new = 1
                        new += r
                        hell = hell[:-new]

                    history_of_keys = '---'.join(hell)

        # pprint(a)

        last = self.a[-1]
        ost = self.a[-2]
        needed = []
        for i in ost:
            flag = True
            for j in last:
                if j.startswith(i):
                    flag = False
            if flag:
                needed.append(i)
        ways = []

        for i in range(0, len(last), 6):
            ways += last[i:i + len(needed)]
            ways.append(needed[int(i / 6)])

        xml = []

        for j, s in enumerate(ways):
            keys = s.split('---')
            open_s = ''
            close_s = ''
            m = ''
            for i, st in enumerate(keys):

                if i != len(keys) - 1:
                    open_s += f'<{st}>888'
                    close_s = f'888</{st}>' + close_s
                else:
                    m = st
            point = open_s + m + close_s
            # print(point.replace('888', ''))
            if j != 0:
                pr = ways[j - 1].split('---')
                cur = ways[j].split('---')

                k = 0
                for z in range(min(len(pr), len(cur))):
                    if pr[z] == cur[z]:
                        k += 1

                if pr[:k] == cur[:k] and k > 0:
                    point_prev = xml[-1]

                    p = '888'.join(point.split('888')[k - 1:-k + 1]) + '888'

                    xml[-1] = ('888'.join(point_prev.split('888')[:-k + 1]) + p + '888'.join(
                        point_prev.split('888')[-k + 1:]))
                    n = ('888'.join(point_prev.split('888')[:-k + 1]) + p + '888'.join(
                        point_prev.split('888')[-k + 1:]))

                else:
                    xml.append(point)
            else:
                xml.append(point)
        for i, s in enumerate(xml):
            xml[i] = s.replace('888', "")

        self.into_xml(xml, self.XML_f)


prog = WithoutLibs('')
prog.go()
