import urllib
import urllib.parse
import urllib.request, urllib.error
from xml.dom.minidom import parse as parseXML
import re

URL = 'http://ja.wikipedia.org/w/api.php?'
BASIC_PARAMETERS = {'action': 'query',
                    'format': 'xml'}

class WikiHandler(object):
    def __init__(self, parameters, titles=None, url=URL):
        self._url = url if url.endswith('?') else url + '?'

        self._parameters = {}
        self._parameters.update(BASIC_PARAMETERS)
        self._parameters.update(parameters)

        if titles:
            self._parameters['titles'] = titles

        self.rawdata = self._urlfetch(self._parameters)

        if self._parameters['format'] == 'xml':
            self.dom = parseXML(self.rawdata)
           # print('DOM ready.')

    def _urlfetch(self, parameters):
        parameters_list = []

        for key, val in parameters.items():
            if isinstance(val, str):
                val = val.encode('utf-8')
            else:
                val = str(val)

            val = urllib.parse.quote(val)
            parameters_list.append('='.join([key, val]))

        url = self._url + '&'.join(parameters_list)

        #print('Accessing...\n', url)
        return urllib.request.urlopen(url, timeout=20)

    def reCall(self, categorys):
        tmp_list = []
        for category in categorys:

            parameters = {'list': 'categorymembers',
                    'cmlimit': 2100,
                    'cmtitle': u'Category:' + category}

            page = WikiHandler(parameters)
 
            elelist = page.dom.getElementsByTagName('cm')
            for ele in elelist:
                ele = ele.getAttribute('title')
                if 'Template:' in ele:
                    continue
                elif 'ファイル:' in ele:
                    continue
                elif 'Category:' in ele:
                    ele = ele.replace("Category:", "")
                    tmp_list.append(ele)
                elif 'プロジェクト:' in ele:
                    continue
                elif 'Portal:' in ele:
                    continue
                elif 'ノート:' in ele:
                    continue
                elif 'Otkksinmsk/sandbox' in ele:
                    continue
                else:
                    with open('traffic.txt', 'a') as f:
                        print(ele, file = f)
        return tmp_list

def main():
    parameters = {'list': 'categorymembers',
                  'cmlimit': 2100,
                  'cmtitle': u'Category:交通'}
    main_list = []
    page = WikiHandler(parameters)

    elelist = page.dom.getElementsByTagName('cm')

    #print(elelist.length) # 要素数

    for ele in elelist:
        ele = ele.getAttribute('title') # 日本の観光地 (自然)始発
        if 'Template:' in ele:
            continue
        elif 'Portal:' in ele:
            continue
        elif 'プロジェクト:' in ele:
            continue
        elif 'ノート:' in ele:
            continue
        elif 'Category:' in ele: #TemplateとCategoryを含んでいたら関数reCallで再帰呼び出し!
            ele = ele.replace("Category:", "")
            main_list.append(ele)
            continue
        else:
            with open('traffic.txt', 'a') as f:
                print(ele, file = f)
    if(len(main_list) != 0):
        for i in range(2):
            call = page.reCall(main_list)
            del main_list
            main_list = call
            del call
            if(len(main_list) == 0):
                break
if __name__ == '__main__':
    main()
