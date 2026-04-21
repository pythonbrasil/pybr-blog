"""
Plugin para filtrar artigos com data futura
Apenas artigos com data <= data atual serão exportados para HTML
"""

from pelican import signals
from datetime import datetime
import pytz


def filter_future_articles(generator):
    """Remove artigos com data no futuro da lista de artigos a serem publicados"""
    
    # Define a timezone
    tz = pytz.timezone('America/Sao_Paulo')
    now = datetime.now(tz)
    
    # Filtra artigos
    published_articles = []
    for article in generator.articles:
        # Se o artigo tem data e é no futuro, pula
        if hasattr(article, 'date') and article.date:
            article_date = article.date
            # Se a data do artigo é naive, adiciona timezone
            if article_date.tzinfo is None:
                article_date = tz.localize(article_date)
            
            if article_date > now:
                print(f"⏭️  Artigo futuro ignorado: {article.title} (data: {article_date})")
                continue
        
        published_articles.append(article)
    
    # Atualiza a lista de artigos
    generator.articles = published_articles
    
    # Atualiza o índice de artigos
    if hasattr(generator, 'articles_list'):
        generator.articles_list = published_articles


def register():
    """Registra o plugin"""
    signals.article_generator_finalized.connect(filter_future_articles)
