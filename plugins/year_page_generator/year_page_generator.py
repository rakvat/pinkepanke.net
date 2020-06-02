# -*- coding: utf-8 -*-
from pathlib import Path

from logging import info
from codecs import open

from pelican import signals
from pelican.generators import Generator

class YearPageGenerator(Generator):

    def __init__(self, context, settings, path, theme, output_path, *null):
        self.output_path = output_path
        self.context = context
        self.siteurl = settings.get('SITEURL')
        self.settings = settings
        self.aktuelles_path = f'{self.output_path}/aktuelles'
        super().__init__(context, settings, path, theme, output_path)

    def _get_years(self):
        years = set()
        for article in self.context['articles']:
            if not hasattr(article, 'type') or article.type != 'news':
                continue
            years.add(article.date.year)
        return sorted(list(years), reverse=True)

    def generate_context(self):
        self.context['year'] = None
        self.context['years'] = []

    def generate_output(self, writer):
        years = self._get_years()
        for year in years:
            path = Path(f'{self.aktuelles_path}/{year}')
            path.mkdir(parents=True, exist_ok=True)
            path = path / 'index.html'
            info(f'writing {path}')
            template = self.get_template('year')
            writer.write_file(path, template, self.context, year=year, years=years)


def get_generators(generators):
    return YearPageGenerator


def register():
    signals.get_generators.connect(get_generators)
