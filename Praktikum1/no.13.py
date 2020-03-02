import inflect
def katakan(x):
    z = {"zero" : "nol", "one" : "satu", "two" : "dua", "three" : "tiga", "four" : "empat", "five" : "lima", "six" : "enam", "seven" : "tujuh", "eight" : "delapan", "nine" : "sembilan","ten" : "sepuluh",
         "eleven" : "sebelas", "twelve" : "dua belas", "thirteen" : "tiga belas", "fourteen" : "empat belas", "fifteen" : "lima belas", "sixteen" : "enam belas", "seventeen" : "tujuh belas",
         "eighteen" : "delapan belas", "nineteen" : "sembilan belas", "twenty" : "dua puluh", "thirty" : "tiga puluh", "forty" : "empat puluh", "fifty" : "lima puluh", "sixty" : "enam puluh",
         "seventy" : "tujuh puluh", "eighty" : "delapan puluh", "ninety" : "sembilan puluh", "hundred" : "ratus", "thousand" : "ribu", "million" : "juta", "billion" : "miliar", "trillion" : "triliun"}
    if len(str(x)) > 15 :
        print("tidak boleh melebihi 15 digit")
    else:
        y = inflect.engine().number_to_words(x)
        w = list(y)
        for i in w:
            if i == "-":
                w.insert(w.index("-"), " ")
                w.remove("-")
            if i == ",":
                w.remove(",")
        v = ""
        for i in w:
            v += i
        u = v.splitlines()
        t = ""
        for i in u:
            t += i
        s = t.split(" and")
        r = ""
        for i in s:
            r += i
        q = r.split(" ")
        p = []
        p.append(q[0:2])
        k = []
        k.append(q[2:4])
        i = []
        i.append(q[4:6])
        h = []
        h.append(q[6:8])
        g = []
        g.append(q[8:10])
        f = []
        f.append(q[10:12])
        e = []
        e.append(q[12:14])
        d = []
        d.append(q[14:16])
        c = []
        c.append(q[16:18])
        b = []
        b.append(q[18:20])
        a = []
        a.append(q[20:22])
        aa = []
        aa.append(q[22:24])
        ab = []
        ab.append(q[24:26])
        ac = []
        ac.append(p)
        ac.append(k)
        ac.append(i)
        ac.append(h)
        ac.append(g)
        ac.append(f)
        ac.append(e)
        ac.append(d)
        ac.append(c)
        ac.append(b)
        ac.append(a)
        ac.append(aa)
        ac.append(ab)
    n = [['one', 'hundred']]
    m = [['one', 'thousand']]
    for i in ac:
        if i == n:
            print("seratus", end = " ")
        elif i == m:
            print("seribu", end = " ")
        else:
            for ae in i:
                for af in ae:
                    print(z[af], end = " ")
    
 


