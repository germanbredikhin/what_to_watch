import csv

import click

from . import app, db
from .models import Opinion


@app.cli.command('load_opinions')
def load_opinions_command():
    """Функция загрузки мнений в базу данных."""
    with open('opinions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            click.echo(row)
            if Opinion.query.filter_by(text=row.get('text')).first():
                click.echo('This opininon already exists')
            else:
                opinion = Opinion(**row)
                db.session.add(opinion)
                db.session.commit()
                counter += 1
    click.echo(f'Loaded {counter} opinion(s)')
