'''Web crawler básico'''

##### Copyright (c) 2021, Carlos Mandele K.
#### Attribution-NonCommercial 4.0 International


from urllib.parse import urljoin
from html.parser import HTMLParser
from urllib.request import Request, urlopen


class Collector(HTMLParser):
    '''coleta URLs de hyperklink em uma lista'''
    def __init__(self, url):
        '''inicializa analisador, o URL e uma lista'''
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        '''coleta URLs de hyperlink em sua forma absoluta'''
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # URL absoluto
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http': # coleta URLs HTTP
                        self.links.append(absolute)

    def getLinks(self):
        '''retorna URLs de hyperlink em seu formato absoluto'''
        return self.links

def analyze(url):
    '''retorna a lista de links http, em formato absoluto,
        na pÃ¡gina Web com URL url'''
    print('Visitando', url) # para teste
    # obtendo links na pagina Web
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    content = urlopen(req).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()
    # Análise do conteúdo da pagina Web ainda a ser feita
    return urls
visited = set()
def crawl(url):
    '''crawler Web recursiva que chama analyze() em cada pagina Web'''
    # inclui url para conjunto de paginas visitadas
    # embora não necessário, avisa ao programador
    global visited       
    visited.add(url)
    if (len(visited)>=maxlinks):
        return
    # analyze() exibe uma lista de URLs de hyperlink no URL da pagina Web
    links = analyze(url)
    # continua recursivamente a verificação de cada link em links
    for link in links:
        if (externalLink):
            follow = externalLink
        else: follow = str(link).find(uri)>=0
        if (link not in visited) and follow:
            try: # bloco try porque o link pode não ser um arquivo HTML valido
                crawl(link)
            except:            # se uma exceÃ§Ã£o for lanÃ§ada
                pass           # ignora e prossegue.

maxlinks= 30 # Limita o crawler para uma quantidade maxima
externalLink=False # Flag para permitir seguir links fora do site
uri='https://db-engines.com/en/'
crawl(uri)
