import os

def get_records(path):
    files = os.listdir(path)

    records = {}

    for file in files:
        tokens = file.split('.')

        if len(tokens) < 2 or not tokens[0]:
            continue

        if tokens[1] == 'wav':
            records[tokens[0]] = ''
        else:
            continue

        try:
            with open(os.path.join(path, tokens[0]+'.txt'), 'r', encoding='utf8') as cf:
                records[tokens[0]] = cf.read()
        except Exception:
            continue

    return dict(sorted(records.items(), key=lambda x: _name_to_float(x[0])))

def post_records(path, records):
    for record in records:
        if os.path.isfile(os.path.join(path, record['id']+'.wav')):
            txt = record['text'].strip()
            content_file = os.path.join(path, record['id']+'.txt')

            if (not txt):
                if os.path.isfile(content_file):
                    os.unlink(content_file)
            else:
                with open(content_file, 'w', encoding='utf8') as frc:
                    frc.write(txt.strip())

def _name_to_float(val):

    res = val.split('-')

    if int(res[1]) < 100:
        res[1] = '0' + res[1]

    return '-'.join(res)