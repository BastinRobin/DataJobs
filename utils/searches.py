
from BeautifulSoup import BeautifulSoup
from os.path import join
from logging import info, debug
from codecs import open

ENCODING='utf-8'

class Search(object):

    def __init__(self, page, job, job_types, commands):
        self.page = page
        self.job = job
        self.job_types = job_types
        self.commands = commands
        self.next_page = None
        self.completed = []

    def queries(self, queries):
        for query in queries:
            debug("Selecting: %s", query[0])
            self.query(query)

    def query(self, query):
        self.links = []
        q = query[0]
        u = query[1]
        self.page.open_page(u)
        commands = self.commands['search']

        # send the job title
        txt = self.page.find_xpath(commands['text'])
        self.page.send(txt, self.job + '\n')

        # get results from first page, all remaining pages
        # will be collected
        self.c = 1
        self.q = q
        self.get_results()
        self.find_next_pages()

        #sometimes you only get one page
        if len(self.links) == 0:
            return False
        self.c, url = self.links.pop(0)
        while True:
            self.page.open_page(url)
            # collect some results
            self.get_results()
            # find all next pages on page
            self.find_next_pages()
            if self.c > 100:
                print self.links
                break
            if len(self.links) == 0:
                break
            self.c, url = self.links.pop(0)

        # reset c
        self.c = 1

    def get_results(self):
        page_name = "{job}-{type}-{0:03d}".format(
            self.c,
            job=self.job.replace(' ','_'),
            type=self.q
            )
        self.completed.append(self.c)
        info("%s:: Reaping data: %s", page_name,  self.page.current_url)
        write(page_name + '.html', self.page.source)

    def find_next_pages(self):
        ele = self.page.find_xpath('//*[@id="FooterPageNav"]/div[1]/ul')
        elements = ele.find_elements_by_tag_name('li')
        elements = [ele for ele in elements if ele.get_attribute('class') == 'notranslate']
        for e in elements:
            link = e.find_elements_by_tag_name('a')
            for l in link:
                c = int(l.text)
                h = l.get_attribute('href')
                if c in self.completed: continue
                if c in [l[0] for l in self.links]: continue
                self.links.append((c, h))

    @classmethod
    def run(cls, page, jobs, job_types, commands, queries):
        for job in jobs:
            search = cls(page, job, job_types, commands)
            search.queries(queries)
        return search


def write(page_name, html, dir_name='pages'):
    page_name = join(dir_name, page_name)
    debug("Writing Page:: %s", page_name)
    with open(page_name, 'w', encoding=ENCODING) as f:
        f.write(html)